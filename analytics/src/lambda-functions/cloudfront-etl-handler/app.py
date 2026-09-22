"""
CloudFront ETL Custom Resource Lambda Handler

Creates and manages a Glue Visual ETL Job for converting CloudFront
standard access logs (TSV) to Iceberg (Parquet) format.
"""

import json
import logging
import time
import boto3
from botocore.exceptions import ClientError
import cfnresponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

glue_client = boto3.client('glue')


def lambda_handler(event, context):
    logger.info(json.dumps({
        "message": "Received CloudFormation event",
        "request_type": event.get('RequestType'),
        "logical_resource_id": event.get('LogicalResourceId')
    }))

    try:
        request_type = event['RequestType']
        properties = event['ResourceProperties']

        job_name = properties['JobName']
        iceberg_data_bucket = properties['IcebergDataBucketName']
        scripts_bucket = properties['ScriptsBucketName']
        logical_name = properties['LogicalName']
        iam_role_arn = properties['IAMRoleArn']


        if request_type == 'Create':
            response_data = handle_create(
                job_name, iceberg_data_bucket,
                scripts_bucket, logical_name, iam_role_arn)
        elif request_type == 'Update':
            response_data = handle_update(
                job_name, iceberg_data_bucket,
                scripts_bucket, logical_name, iam_role_arn)
        elif request_type == 'Delete':
            response_data = handle_delete(job_name)
        else:
            raise ValueError(f"Unknown request type: {request_type}")

        cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data, job_name)

    except Exception as e:
        logger.error(json.dumps({"message": "Error", "error": str(e)}), exc_info=True)
        try:
            job_name = event['ResourceProperties']['JobName']
        except (KeyError, TypeError):
            job_name = event.get('LogicalResourceId', 'unknown-job')
        cfnresponse.send(event, context, cfnresponse.FAILED, {"Error": str(e)}, job_name, reason=str(e))


def handle_create(job_name, iceberg_data_bucket,
                  scripts_bucket, logical_name, iam_role_arn):
    logger.info(json.dumps({"message": "Creating Visual ETL Job", "job_name": job_name}))

    job_params = {
        'Name': job_name,
        'Role': iam_role_arn,
        'JobMode': 'VISUAL',
        'Command': {
            'Name': 'glueetl',
            'ScriptLocation': f's3://{scripts_bucket}/glue-jobs/{job_name}.py',
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
                ' --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO'
                f' --conf spark.sql.catalog.glue_catalog.warehouse=s3://{iceberg_data_bucket}/iceberg-warehouse/'
            ),
            '--datalake-formats': 'iceberg'
        },
        'MaxRetries': 0,
        'Timeout': 60,
        'GlueVersion': '5.0',
        'NumberOfWorkers': 2,
        'WorkerType': 'G.1X',
        'ExecutionClass': 'STANDARD',
        'Tags': {
            'environment': 'production',
            'createdby': 'aws-cloudformation-templates'
        }
    }

    glue_client.create_job(**job_params)
    job_arn = wait_for_job_ready(job_name)

    return {"JobName": job_name, "JobArn": job_arn, "Status": "CREATED"}


def handle_update(job_name, iceberg_data_bucket,
                  scripts_bucket, logical_name, iam_role_arn):
    logger.info(json.dumps({"message": "Updating Visual ETL Job", "job_name": job_name}))

    try:
        current_job = glue_client.get_job(JobName=job_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityNotFoundException':
            return handle_create(
                job_name, iceberg_data_bucket,
                scripts_bucket, logical_name, iam_role_arn)
        raise

    # CodeGenConfigurationNodes is left out so a deployment cannot overwrite the flow
    job_update = {
        'JobMode': 'VISUAL',
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
        'MaxRetries': 0,
        'Timeout': 60,
        'GlueVersion': '5.0',
        'NumberOfWorkers': 2,
        'WorkerType': 'G.1X',
        'ExecutionClass': 'STANDARD'
    }

    glue_client.update_job(JobName=job_name, JobUpdate=job_update)
    job_arn = wait_for_job_ready(job_name)

    return {"JobName": job_name, "JobArn": job_arn, "Status": "UPDATED"}


def handle_delete(job_name):
    logger.info(json.dumps({"message": "Deleting Visual ETL Job", "job_name": job_name}))
    try:
        glue_client.delete_job(JobName=job_name)
        return {"JobName": job_name, "Status": "DELETED"}
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityNotFoundException':
            return {"JobName": job_name, "Status": "ALREADY_DELETED"}
        raise


def wait_for_job_ready(job_name, max_wait_time=120, poll_interval=5):
    start_time = time.time()
    while time.time() - start_time < max_wait_time:
        try:
            glue_client.get_job(JobName=job_name)
            return f"arn:aws:glue:*:*:job/{job_name}"
        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityNotFoundException':
                time.sleep(poll_interval)
            else:
                raise
    raise Exception(f"Job '{job_name}' did not become ready within {max_wait_time} seconds")
