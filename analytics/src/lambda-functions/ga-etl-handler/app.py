"""
Visual ETL Custom Resource Lambda Handler

This Lambda function manages AWS Glue Visual ETL Jobs through CloudFormation custom resources.
It handles CREATE, UPDATE, and DELETE operations for Visual ETL jobs that process Google Analytics 4 data.
"""

import json
import logging
import time
import boto3
from botocore.exceptions import ClientError
import cfnresponse

# Configure structured logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
glue_client = boto3.client('glue')

def lambda_handler(event, context):
    """
    Main Lambda handler for Visual ETL Custom Resource operations.
    
    Args:
        event: CloudFormation event containing request details
        context: Lambda context object
    
    Returns:
        CloudFormation response via cfnresponse
    """
    
    # Log the incoming event (structured logging)
    logger.info(json.dumps({
        "message": "Received CloudFormation event",
        "request_type": event.get('RequestType'),
        "logical_resource_id": event.get('LogicalResourceId'),
        "stack_id": event.get('StackId')
    }))
    
    try:
        request_type = event['RequestType']
        properties = event['ResourceProperties']
        
        # Extract required properties
        job_name = properties['JobName']
        connection_name = properties['ConnectionName']
        iceberg_data_bucket = properties['IcebergDataBucket']
        database_name = properties['DatabaseName']
        scripts_bucket = properties['ScriptsBucket']
        logical_name = properties['LogicalName']
        iam_role_arn = properties['IAMRoleArn']
        
        
        # Handle different request types
        if request_type == 'Create':
            response_data = handle_create(job_name, connection_name, iceberg_data_bucket, database_name, scripts_bucket, logical_name,
                                        iam_role_arn)
        elif request_type == 'Update':
            response_data = handle_update(job_name, connection_name, iceberg_data_bucket, database_name, scripts_bucket, logical_name,
                                        iam_role_arn)
        elif request_type == 'Delete':
            response_data = handle_delete(job_name)
        else:
            raise ValueError(f"Unknown request type: {request_type}")
        
        # Send success response with consistent PhysicalResourceId
        cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data, job_name)
        
    except Exception as e:
        logger.error(json.dumps({
            "message": "Error processing CloudFormation request",
            "error": str(e),
            "request_type": event.get('RequestType'),
            "logical_resource_id": event.get('LogicalResourceId')
        }))
        
        # Extract job_name for PhysicalResourceId, fallback to LogicalResourceId if not available
        try:
            job_name = event['ResourceProperties']['JobName']
        except (KeyError, TypeError):
            job_name = event.get('LogicalResourceId', 'unknown-job')
        
        # Send failure response with consistent PhysicalResourceId
        cfnresponse.send(event, context, cfnresponse.FAILED, {
            "Error": str(e)
        }, job_name, reason=str(e))

def handle_create(job_name, connection_name, iceberg_data_bucket, database_name, scripts_bucket, logical_name, iam_role_arn):
    """
    Handle CREATE operation for Visual ETL Job.
    
    Args:
        job_name: Name of the Glue job to create
        connection_name: Name of the Google Analytics 4 connection
        iceberg_data_bucket: S3 bucket for Iceberg data output
        database_name: Glue Data Catalog database name
        scripts_bucket: S3 bucket for Glue scripts
        logical_name: Logical name for resource naming
        iam_role_arn: IAM role ARN for job execution
        property_id: Google Analytics Property ID
    
    Returns:
        dict: Response data with job details
    """
    
    logger.info(json.dumps({
        "message": "Creating Visual ETL Job",
        "job_name": job_name,
        "connection_name": connection_name
    }))
    
    try:
        # Prepare job creation parameters
        job_params = {
            'Name': job_name,
            'Role': iam_role_arn,
            'JobMode': 'VISUAL',  # Specify Visual ETL mode
            'Command': {
                'Name': 'glueetl',
                'ScriptLocation': f's3://{scripts_bucket}/glue-jobs/{logical_name}-ga4-to-iceberg.py',
                'PythonVersion': '3'
            },
            'DefaultArguments': {
                '--enable-metrics': 'true',
                '--enable-spark-ui': 'true',
                '--spark-event-logs-path': f's3://{iceberg_data_bucket}/spark-logs/',
                '--enable-job-insights': 'true',
                '--enable-observability-metrics': 'true',
                '--job-language': 'python',
                '--conf': (
                    'spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions'
                    ' --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog'
                    ' --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog'
                    f' --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO'
                    f' --conf spark.sql.catalog.glue_catalog.warehouse=s3://{iceberg_data_bucket}/iceberg-warehouse/'
                ),
                '--datalake-formats': 'iceberg'
            },
            'Connections': {
                'Connections': [connection_name]
            },
            'MaxRetries': 0,
            'Timeout': 480,  # 8 hours
            'GlueVersion': '5.0',
            'NumberOfWorkers': 10,
            'WorkerType': 'G.1X',
            'ExecutionClass': 'STANDARD',
            'Tags': {
                'Environment': 'production',
                'Project': 'analytics-platform',
                'Component': 'ga4-to-iceberg'
            }
        }
        

        # Create the Glue Visual ETL Job
        response = glue_client.create_job(**job_params)
        
        # Wait for job creation to complete
        job_arn = wait_for_job_ready(job_name)
        
        logger.info(json.dumps({
            "message": "Visual ETL Job created successfully",
            "job_name": job_name,
            "job_arn": job_arn
        }))
        
        return {
            "JobName": job_name,
            "JobArn": job_arn,
            "Status": "CREATED"
        }
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        
        logger.error(json.dumps({
            "message": "AWS Glue API error during job creation",
            "error_code": error_code,
            "error_message": error_message,
            "job_name": job_name
        }))
        
        if error_code == 'AlreadyExistsException':
            raise Exception(f"Glue job '{job_name}' already exists")
        elif error_code == 'InvalidInputException':
            raise Exception(f"Invalid input for Glue job creation: {error_message}")
        elif error_code == 'InternalServiceException':
            raise Exception(f"Internal Glue service error: {error_message}")
        else:
            raise Exception(f"Glue API error ({error_code}): {error_message}")

def handle_update(job_name, connection_name, iceberg_data_bucket, database_name, scripts_bucket, logical_name, iam_role_arn):
    """
    Handle UPDATE operation for Visual ETL Job.
    
    Args:
        job_name: Name of the Glue job to update
        connection_name: Name of the Google Analytics 4 connection
        iceberg_data_bucket: S3 bucket for Iceberg data output
        database_name: Glue Data Catalog database name
        scripts_bucket: S3 bucket for Glue scripts
        logical_name: Logical name for resource naming
        iam_role_arn: IAM role ARN for job execution
        property_id: Google Analytics Property ID
    
    Returns:
        dict: Response data with updated job details
    """
    
    logger.info(json.dumps({
        "message": "Updating Visual ETL Job",
        "job_name": job_name
    }))
    
    try:
        # Get current job configuration
        current_job = glue_client.get_job(JobName=job_name)
        
        # CodeGenConfigurationNodes is left out so a deployment cannot overwrite the flow
        job_update = {
            'JobMode': 'VISUAL',  # Ensure Visual ETL mode
            'Role': iam_role_arn,
            'Command': current_job['Job']['Command'],
            'DefaultArguments': {
                **current_job['Job']['DefaultArguments'],
                '--conf': (
                    'spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions'
                    ' --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog'
                    ' --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog'
                    ' --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO'
                    f' --conf spark.sql.catalog.glue_catalog.warehouse=s3://{iceberg_data_bucket}/iceberg-warehouse/'
                ),
                '--datalake-formats': 'iceberg',
                '--enable-job-insights': 'true',
                '--job-language': 'python'
            },
            'Connections': {
                'Connections': [connection_name]
            },
            'MaxRetries': 0,
            'Timeout': 480,
            'GlueVersion': '5.0',
            'NumberOfWorkers': 10,
            'WorkerType': 'G.1X',
            'ExecutionClass': 'STANDARD'
        }
        

        response = glue_client.update_job(
            JobName=job_name,
            JobUpdate=job_update
        )
        
        # Wait for job update to complete
        job_arn = wait_for_job_ready(job_name)
        
        logger.info(json.dumps({
            "message": "Visual ETL Job updated successfully",
            "job_name": job_name,
            "job_arn": job_arn
        }))
        
        return {
            "JobName": job_name,
            "JobArn": job_arn,
            "Status": "UPDATED"
        }
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        
        logger.error(json.dumps({
            "message": "AWS Glue API error during job update",
            "error_code": error_code,
            "error_message": error_message,
            "job_name": job_name
        }))
        
        if error_code == 'EntityNotFoundException':
            # Job doesn't exist yet, create it
            return handle_create(job_name, connection_name, iceberg_data_bucket, database_name, scripts_bucket, logical_name,
                                iam_role_arn)
        elif error_code == 'InvalidInputException':
            raise Exception(f"Invalid input for Glue job update: {error_message}")
        else:
            raise Exception(f"Glue API error ({error_code}): {error_message}")

def handle_delete(job_name):
    """
    Handle DELETE operation for Visual ETL Job.
    Deletes the Glue job. Called only when the CFn stack itself is deleted.
    """
    logger.info(json.dumps({"message": "Deleting Visual ETL Job", "job_name": job_name}))

    try:
        glue_client.delete_job(JobName=job_name)
        return {"JobName": job_name, "Status": "DELETED"}
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityNotFoundException':
            return {"JobName": job_name, "Status": "ALREADY_DELETED"}
        raise


def wait_for_job_ready(job_name, max_wait_time=300, poll_interval=10):
    """
    Wait for Glue job to be in READY state after creation/update.
    
    Args:
        job_name: Name of the Glue job
        max_wait_time: Maximum time to wait in seconds (default: 5 minutes)
        poll_interval: Polling interval in seconds (default: 10 seconds)
    
    Returns:
        str: Job ARN when ready
    
    Raises:
        Exception: If job doesn't become ready within max_wait_time
    """
    
    start_time = time.time()
    
    while time.time() - start_time < max_wait_time:
        try:
            response = glue_client.get_job(JobName=job_name)
            job = response['Job']
            
            # Job is ready when it exists and can be retrieved successfully
            job_arn = job['Name']  # Use job name as identifier since ARN format varies
            
            logger.info(json.dumps({
                "message": "Job is ready",
                "job_name": job_name,
                "elapsed_time": time.time() - start_time
            }))
            
            return f"arn:aws:glue:*:*:job/{job_name}"
            
        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityNotFoundException':
                logger.info(json.dumps({
                    "message": "Waiting for job to be created",
                    "job_name": job_name,
                    "elapsed_time": time.time() - start_time
                }))
            else:
                raise
        
        time.sleep(poll_interval)
    
    raise Exception(f"Job '{job_name}' did not become ready within {max_wait_time} seconds")

def wait_for_job_deleted(job_name, max_wait_time=300, poll_interval=10):
    """
    Wait for Glue job to be completely deleted.
    
    Args:
        job_name: Name of the Glue job
        max_wait_time: Maximum time to wait in seconds (default: 5 minutes)
        poll_interval: Polling interval in seconds (default: 10 seconds)
    
    Raises:
        Exception: If job is not deleted within max_wait_time
    """
    
    start_time = time.time()
    
    while time.time() - start_time < max_wait_time:
        try:
            glue_client.get_job(JobName=job_name)
            
            logger.info(json.dumps({
                "message": "Waiting for job deletion to complete",
                "job_name": job_name,
                "elapsed_time": time.time() - start_time
            }))
            
            time.sleep(poll_interval)
            
        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityNotFoundException':
                logger.info(json.dumps({
                    "message": "Job deletion completed",
                    "job_name": job_name,
                    "elapsed_time": time.time() - start_time
                }))
                return
            else:
                raise
    
    raise Exception(f"Job '{job_name}' was not deleted within {max_wait_time} seconds")
