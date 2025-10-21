#!/usr/bin/env python3
"""
Google Analytics 4 Data Processing Job for AWS Glue

This script extracts data from Google Analytics 4, processes it, and saves it
in Apache Iceberg format to S3 with metadata registered in Glue Data Catalog.

Requirements:
- AWS Glue 5.0 with Apache Iceberg support
- Google Analytics 4 connection configured in AWS Glue
- Secrets Manager secret with Google Analytics credentials
- S3 buckets for raw data and Iceberg data storage

Author: AWS CloudFormation Templates
"""

import sys
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

import boto3
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GoogleAnalyticsProcessor:
    """Google Analytics 4 data processor for AWS Glue"""
    
    def __init__(self, args: Dict[str, Any]):
        """Initialize the processor with job arguments"""
        self.args = args
        self.sc = SparkContext()
        self.glue_context = GlueContext(self.sc)
        self.spark = self.glue_context.spark_session
        self.job = Job(self.glue_context)
        self.job.init(args['JOB_NAME'], args)
        
        # Initialize AWS clients
        self.secrets_client = boto3.client('secretsmanager')
        
        # Job parameters
        self.raw_data_bucket = args['raw_data_bucket']
        self.iceberg_data_bucket = args['iceberg_data_bucket']
        self.secrets_manager_secret_name = args['secrets_manager_secret_name']
        self.database_name = args['database_name']
        self.table_name = args['table_name']
        
        logger.info(f"Initialized GoogleAnalyticsProcessor with database: {self.database_name}, table: {self.table_name}")
    
    def get_google_analytics_credentials(self) -> Dict[str, str]:
        """Retrieve Google Analytics credentials from Secrets Manager"""
        try:
            response = self.secrets_client.get_secret_value(
                SecretId=self.secrets_manager_secret_name
            )
            credentials = json.loads(response['SecretString'])
            logger.info("Successfully retrieved Google Analytics credentials from Secrets Manager")
            return credentials
        except Exception as e:
            logger.error(f"Failed to retrieve credentials from Secrets Manager: {str(e)}")
            raise
    
    def extract_google_analytics_data(self, credentials: Dict[str, str]) -> DynamicFrame:
        """Extract data from Google Analytics 4 using Glue Connection"""
        try:
            # Calculate date range (yesterday's data)
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=1)
            
            logger.info(f"Extracting Google Analytics data for date range: {start_date} to {end_date}")
            
            # Connection options for Google Analytics 4
            connection_options = {
                "connectionName": f"{self.args.get('database_name', 'analytics')}-google-analytics-connection",
                "ENTITY_NAME": "reports",
                "API_VERSION": "v1beta",
                "SELECTED_FIELDS": [
                    "date",
                    "pagePath",
                    "pageTitle", 
                    "sessions",
                    "users",
                    "pageviews",
                    "bounceRate",
                    "averageSessionDuration",
                    "conversions",
                    "totalRevenue",
                    "source",
                    "medium",
                    "campaign",
                    "deviceCategory",
                    "country"
                ],
                "FILTER_PREDICATE": f"date >= '{start_date}' AND date <= '{end_date}'"
            }
            
            # Create DynamicFrame from Google Analytics connection
            dynamic_frame = self.glue_context.create_dynamic_frame.from_options(
                connection_type="custom.googleanalytics4",
                connection_options=connection_options,
                transformation_ctx="google_analytics_source"
            )
            
            logger.info(f"Successfully extracted {dynamic_frame.count()} records from Google Analytics")
            return dynamic_frame
            
        except Exception as e:
            logger.error(f"Failed to extract data from Google Analytics: {str(e)}")
            raise
    
    def save_raw_data(self, dynamic_frame: DynamicFrame, date_partition: str) -> str:
        """Save raw data to S3 for staging purposes"""
        try:
            raw_data_path = f"s3://{self.raw_data_bucket}/google-analytics/year={date_partition[:4]}/month={date_partition[5:7]}/day={date_partition[8:10]}/"
            
            # Convert to DataFrame and save as Parquet
            df = dynamic_frame.toDF()
            df.write.mode("overwrite").parquet(raw_data_path)
            
            logger.info(f"Successfully saved raw data to: {raw_data_path}")
            return raw_data_path
            
        except Exception as e:
            logger.error(f"Failed to save raw data: {str(e)}")
            raise
    
    def transform_data(self, dynamic_frame: DynamicFrame) -> DynamicFrame:
        """Transform and clean Google Analytics data"""
        try:
            logger.info("Starting data transformation")
            
            # Convert to DataFrame for easier manipulation
            df = dynamic_frame.toDF()
            
            # Data cleaning and transformation
            df_transformed = df.select(
                col("date").cast("date").alias("date"),
                col("pagePath").alias("page_path"),
                col("pageTitle").alias("page_title"),
                col("sessions").cast("integer").alias("sessions"),
                col("users").cast("integer").alias("users"),
                col("pageviews").cast("integer").alias("page_views"),
                col("bounceRate").cast("double").alias("bounce_rate"),
                col("averageSessionDuration").cast("double").alias("avg_session_duration"),
                col("conversions").cast("integer").alias("goal_completions"),
                col("totalRevenue").cast("double").alias("revenue"),
                struct(
                    col("source").alias("source"),
                    col("medium").alias("medium"), 
                    col("campaign").alias("campaign"),
                    col("deviceCategory").alias("device_category"),
                    col("country").alias("country")
                ).alias("dimensions")
            ).filter(
                col("date").isNotNull() & 
                col("page_path").isNotNull()
            ).withColumn(
                "processing_timestamp", 
                current_timestamp()
            ).withColumn(
                "ga_property_id",
                lit("PLACEHOLDER_PROPERTY_ID")  # Will be replaced with actual property ID from credentials
            )
            
            # Remove duplicates based on date and page_path
            df_deduplicated = df_transformed.dropDuplicates(["date", "page_path"])
            
            # Convert back to DynamicFrame
            transformed_dynamic_frame = DynamicFrame.fromDF(
                df_deduplicated, 
                self.glue_context, 
                "transformed_data"
            )
            
            logger.info(f"Successfully transformed data. Record count: {transformed_dynamic_frame.count()}")
            return transformed_dynamic_frame
            
        except Exception as e:
            logger.error(f"Failed to transform data: {str(e)}")
            raise
    
    def validate_data_quality(self, dynamic_frame: DynamicFrame) -> DynamicFrame:
        """Validate data quality and flag problematic records"""
        try:
            logger.info("Starting data quality validation")
            
            df = dynamic_frame.toDF()
            
            # Data quality checks
            df_with_quality_flags = df.withColumn(
                "data_quality_issues",
                array()
            ).withColumn(
                "data_quality_issues",
                when(col("sessions") < 0, array_union(col("data_quality_issues"), array(lit("negative_sessions"))))
                .otherwise(col("data_quality_issues"))
            ).withColumn(
                "data_quality_issues",
                when(col("users") < 0, array_union(col("data_quality_issues"), array(lit("negative_users"))))
                .otherwise(col("data_quality_issues"))
            ).withColumn(
                "data_quality_issues", 
                when(col("bounce_rate") < 0 | col("bounce_rate") > 1, 
                     array_union(col("data_quality_issues"), array(lit("invalid_bounce_rate"))))
                .otherwise(col("data_quality_issues"))
            ).withColumn(
                "is_quality_issue",
                size(col("data_quality_issues")) > 0
            )
            
            # Log quality statistics
            total_records = df_with_quality_flags.count()
            quality_issues = df_with_quality_flags.filter(col("is_quality_issue") == True).count()
            
            logger.info(f"Data quality validation completed. Total records: {total_records}, Quality issues: {quality_issues}")
            
            # For now, we'll keep all records but flag them
            # In production, you might want to isolate problematic records
            validated_dynamic_frame = DynamicFrame.fromDF(
                df_with_quality_flags,
                self.glue_context,
                "validated_data"
            )
            
            return validated_dynamic_frame
            
        except Exception as e:
            logger.error(f"Failed to validate data quality: {str(e)}")
            raise
    
    def save_to_iceberg(self, dynamic_frame: DynamicFrame) -> None:
        """Save processed data to Apache Iceberg format"""
        try:
            logger.info("Starting save to Apache Iceberg format")
            
            # Convert to DataFrame
            df = dynamic_frame.toDF()
            
            # Create database if it doesn't exist
            self.spark.sql(f"CREATE DATABASE IF NOT EXISTS {self.database_name}")
            
            # Define the full table name
            full_table_name = f"{self.database_name}.{self.table_name}"
            
            # Check if table exists
            table_exists = self.spark.catalog.tableExists(full_table_name)
            
            if not table_exists:
                logger.info(f"Creating new Iceberg table: {full_table_name}")
                
                # Create Iceberg table with partitioning
                df.writeTo(full_table_name) \
                  .using("iceberg") \
                  .partitionedBy("date") \
                  .tableProperty("write.format.default", "parquet") \
                  .tableProperty("write.parquet.compression-codec", "snappy") \
                  .create()
                  
                logger.info(f"Successfully created Iceberg table: {full_table_name}")
            else:
                logger.info(f"Appending to existing Iceberg table: {full_table_name}")
                
                # Append to existing table
                df.writeTo(full_table_name) \
                  .using("iceberg") \
                  .append()
                  
                logger.info(f"Successfully appended data to Iceberg table: {full_table_name}")
            
            # Update table statistics
            self.spark.sql(f"ANALYZE TABLE {full_table_name} COMPUTE STATISTICS")
            
            logger.info("Successfully saved data to Apache Iceberg format")
            
        except Exception as e:
            logger.error(f"Failed to save data to Iceberg: {str(e)}")
            raise
    
    def run(self) -> None:
        """Main execution method"""
        try:
            logger.info("Starting Google Analytics data processing job")
            
            # Step 1: Get credentials
            credentials = self.get_google_analytics_credentials()
            
            # Step 2: Extract data from Google Analytics
            raw_dynamic_frame = self.extract_google_analytics_data(credentials)
            
            # Step 3: Save raw data for staging
            date_partition = datetime.now().strftime("%Y-%m-%d")
            self.save_raw_data(raw_dynamic_frame, date_partition)
            
            # Step 4: Transform data
            transformed_dynamic_frame = self.transform_data(raw_dynamic_frame)
            
            # Step 5: Validate data quality
            validated_dynamic_frame = self.validate_data_quality(transformed_dynamic_frame)
            
            # Step 6: Save to Apache Iceberg
            self.save_to_iceberg(validated_dynamic_frame)
            
            logger.info("Google Analytics data processing job completed successfully")
            
        except Exception as e:
            logger.error(f"Job failed with error: {str(e)}")
            raise
        finally:
            self.job.commit()

def main():
    """Main entry point"""
    # Get job arguments
    args = getResolvedOptions(sys.argv, [
        'JOB_NAME',
        'raw_data_bucket',
        'iceberg_data_bucket', 
        'secrets_manager_secret_name',
        'database_name',
        'table_name'
    ])
    
    # Initialize and run processor
    processor = GoogleAnalyticsProcessor(args)
    processor.run()

if __name__ == "__main__":
    main()