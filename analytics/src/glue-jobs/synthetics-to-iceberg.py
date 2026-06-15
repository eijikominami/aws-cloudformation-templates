import sys
import boto3
from botocore.exceptions import ClientError
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME", "SOURCE_PATH", "DATABASE_NAME", "TABLE_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Read SyntheticsReport JSON files recursively.
# CloudWatch Synthetics writes each report as a single pretty-printed (multi-line)
# JSON object per file, so multiline must be enabled; otherwise Spark parses each
# physical line independently and yields only the _corrupt_record column.
df = spark.read.option("recursiveFileLookup", "true") \
    .option("pathGlobFilter", "SyntheticsReport-*.json") \
    .option("multiline", "true") \
    .json(args["SOURCE_PATH"])

# Write to Iceberg table
table_name = f"glue_catalog.{args['DATABASE_NAME']}.{args['TABLE_NAME']}"
try:
    df.writeTo(table_name).using("iceberg").createOrReplace()
except Exception as e:
    if "does not exist" in str(e) or "metadata" in str(e).lower():
        # Self-heal a stale catalog entry whose Iceberg metadata file is missing in S3.
        # Drop the catalog registration directly via the Glue API (catalog-only; this
        # avoids reading the broken metadata_location that causes
        # "Location does not exist ...metadata.json"), then recreate the table fresh
        # from the inferred schema. Idempotent: EntityNotFoundException is ignored.
        glue = boto3.client("glue")
        try:
            glue.delete_table(DatabaseName=args["DATABASE_NAME"], Name=args["TABLE_NAME"])
        except ClientError as ce:
            if ce.response["Error"]["Code"] != "EntityNotFoundException":
                raise
        df.writeTo(table_name).using("iceberg").create()
    else:
        raise

job.commit()
