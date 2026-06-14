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
        raw_data_bucket = properties['RawDataBucketName']
        access_log_prefix = properties['AccessLogPrefix']
        iceberg_data_bucket = properties['IcebergDataBucketName']
        database_name = properties['DatabaseName']
        scripts_bucket = properties['ScriptsBucketName']
        logical_name = properties['LogicalName']
        iam_role_arn = properties['IAMRoleArn']

        git_repository = properties.get('GitRepository', '')
        git_owner = properties.get('GitOwner', '')
        git_branch = properties.get('GitBranch', 'main')
        git_folder = properties.get('GitFolder', 'glue-jobs')
        git_token = properties.get('GitToken', '')

        if request_type == 'Create':
            response_data = handle_create(
                job_name, raw_data_bucket, access_log_prefix, iceberg_data_bucket,
                database_name, scripts_bucket, logical_name, iam_role_arn,
                git_repository, git_owner, git_branch, git_folder, git_token)
        elif request_type == 'Update':
            response_data = handle_update(
                job_name, raw_data_bucket, access_log_prefix, iceberg_data_bucket,
                database_name, scripts_bucket, logical_name, iam_role_arn,
                git_repository, git_owner, git_branch, git_folder, git_token)
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


def handle_create(job_name, raw_data_bucket, access_log_prefix, iceberg_data_bucket,
                  database_name, scripts_bucket, logical_name, iam_role_arn,
                  git_repository, git_owner, git_branch, git_folder, git_token):
    logger.info(json.dumps({"message": "Creating Visual ETL Job", "job_name": job_name}))

    code_gen_nodes = generate_visual_etl_nodes(
        raw_data_bucket, access_log_prefix, iceberg_data_bucket, database_name)

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
            '--conf': 'spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions',
            '--datalake-formats': 'iceberg'
        },
        'MaxRetries': 0,
        'Timeout': 60,
        'GlueVersion': '5.0',
        'NumberOfWorkers': 2,
        'WorkerType': 'G.1X',
        'ExecutionClass': 'STANDARD',
        'CodeGenConfigurationNodes': code_gen_nodes,
        'Tags': {
            'environment': 'production',
            'createdby': 'aws-cloudformation-templates'
        }
    }

    if is_git_integration_enabled(git_repository, git_owner, git_token):
        job_params['SourceControlDetails'] = build_source_control_details(
            git_repository, git_owner, git_branch, git_folder, git_token)

    glue_client.create_job(**job_params)
    job_arn = wait_for_job_ready(job_name)

    return {"JobName": job_name, "JobArn": job_arn, "Status": "CREATED"}


def handle_update(job_name, raw_data_bucket, access_log_prefix, iceberg_data_bucket,
                  database_name, scripts_bucket, logical_name, iam_role_arn,
                  git_repository, git_owner, git_branch, git_folder, git_token):
    logger.info(json.dumps({"message": "Updating Visual ETL Job", "job_name": job_name}))

    try:
        current_job = glue_client.get_job(JobName=job_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityNotFoundException':
            return handle_create(
                job_name, raw_data_bucket, access_log_prefix, iceberg_data_bucket,
                database_name, scripts_bucket, logical_name, iam_role_arn,
                git_repository, git_owner, git_branch, git_folder, git_token)
        raise

    job_update = {
        'JobMode': 'VISUAL',
        'Role': iam_role_arn,
        'Command': current_job['Job']['Command'],
        'DefaultArguments': current_job['Job']['DefaultArguments'],
        'MaxRetries': 0,
        'Timeout': 60,
        'GlueVersion': '5.0',
        'NumberOfWorkers': 2,
        'WorkerType': 'G.1X',
        'ExecutionClass': 'STANDARD'
    }

    if is_git_integration_enabled(git_repository, git_owner, git_token):
        job_update['SourceControlDetails'] = build_source_control_details(
            git_repository, git_owner, git_branch, git_folder, git_token)

    glue_client.update_job(JobName=job_name, JobUpdate=job_update)
    job_arn = wait_for_job_ready(job_name)

    return {"JobName": job_name, "JobArn": job_arn, "Status": "UPDATED"}


def handle_delete(job_name):
    logger.info(json.dumps({
        "message": "DELETE called - retaining job",
        "job_name": job_name
    }))
    return {"JobName": job_name, "Status": "RETAINED"}


def generate_visual_etl_nodes(raw_data_bucket, access_log_prefix, iceberg_data_bucket, database_name):
    return {
        "node-source": {
            "S3CsvSource": {
                "Name": "CloudFront Logs",
                "Paths": [f"s3://{raw_data_bucket}/{access_log_prefix}"],
                "Separator": "tab",
                "QuoteChar": "quote",
                "WithHeader": False,
                "Recurse": True
            }
        },
        "node-target": {
            "S3IcebergCatalogTarget": {
                "Name": "Iceberg Table",
                "Inputs": ["node-source"],
                "Table": "cloudfront_access_logs_iceberg",
                "Database": database_name,
                "PartitionKeys": [["date"]]
            }
        }
    }


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


def is_git_integration_enabled(git_repository, git_owner, git_token):
    return all(p and p.strip() for p in [git_repository, git_owner, git_token])


def build_source_control_details(git_repository, git_owner, git_branch, git_folder, git_token):
    provider = 'GITHUB'
    if 'gitlab' in git_repository.lower():
        provider = 'GITLAB'
    elif 'codecommit' in git_repository.lower():
        provider = 'AWS_CODE_COMMIT'
    elif 'bitbucket' in git_repository.lower():
        provider = 'BITBUCKET'

    details = {
        'Provider': provider,
        'Repository': git_repository,
        'Branch': git_branch,
        'Folder': git_folder,
        'AuthStrategy': 'PERSONAL_ACCESS_TOKEN',
        'AuthToken': git_token
    }

    if provider != 'AWS_CODE_COMMIT' and git_owner:
        details['Owner'] = git_owner

    return details
