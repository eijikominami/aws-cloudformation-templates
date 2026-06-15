"""
Synthetics ETL Custom Resource Lambda Handler

This Lambda function manages AWS Glue Script ETL Jobs through CloudFormation custom resources.
It handles CREATE, UPDATE, and DELETE operations for Glue jobs that process CloudWatch Synthetics data.
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
    """Main Lambda handler for Synthetics ETL Custom Resource operations."""
    logger.info(json.dumps({
        "message": "Received CloudFormation event",
        "request_type": event.get('RequestType'),
        "logical_resource_id": event.get('LogicalResourceId'),
        "stack_id": event.get('StackId')
    }))

    try:
        request_type = event['RequestType']
        properties = event['ResourceProperties']

        job_name = properties['JobName']
        script_location = properties['ScriptLocation']
        iceberg_data_bucket = properties['IcebergDataBucket']
        database_name = properties['DatabaseName']
        table_name = properties['TableName']
        source_path = properties['SourcePath']
        iam_role_arn = properties['IAMRoleArn']

        git_repository = properties.get('GitRepository', '')
        git_owner = properties.get('GitOwner', '')
        git_branch = properties.get('GitBranch', 'main')
        git_folder = properties.get('GitFolder', 'glue-jobs')
        git_token = properties.get('GitToken', '')

        if request_type == 'Create':
            response_data = handle_create(
                job_name, script_location, iceberg_data_bucket, database_name,
                table_name, source_path, iam_role_arn,
                git_repository, git_owner, git_branch, git_folder, git_token)
        elif request_type == 'Update':
            response_data = handle_update(
                job_name, script_location, iceberg_data_bucket, database_name,
                table_name, source_path, iam_role_arn,
                git_repository, git_owner, git_branch, git_folder, git_token)
        elif request_type == 'Delete':
            response_data = handle_delete(job_name)
        else:
            raise ValueError(f"Unknown request type: {request_type}")

        cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data, job_name)

    except Exception as e:
        logger.error(json.dumps({
            "message": "Error processing CloudFormation request",
            "error": str(e),
            "request_type": event.get('RequestType'),
            "logical_resource_id": event.get('LogicalResourceId')
        }))
        try:
            job_name = event['ResourceProperties']['JobName']
        except (KeyError, TypeError):
            job_name = event.get('LogicalResourceId', 'unknown-job')

        cfnresponse.send(event, context, cfnresponse.FAILED, {
            "Error": str(e)
        }, job_name, reason=str(e))


def build_default_arguments(iceberg_data_bucket, database_name, table_name, source_path):
    """Build DefaultArguments for the Synthetics Glue Job with glue_catalog full config."""
    return {
        '--SOURCE_PATH': source_path,
        '--DATABASE_NAME': database_name,
        '--TABLE_NAME': table_name,
        '--conf': (
            'spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions'
            ' --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog'
            ' --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog'
            ' --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO'
            f' --conf spark.sql.catalog.glue_catalog.warehouse=s3://{iceberg_data_bucket}/iceberg-warehouse/'
        ),
        '--datalake-formats': 'iceberg',
        '--enable-job-insights': 'true',
        '--enable-metrics': 'true',
        '--enable-observability-metrics': 'true',
        '--enable-spark-ui': 'true',
        '--job-language': 'python',
        '--spark-event-logs-path': f's3://{iceberg_data_bucket}/spark-logs/',
    }


def handle_create(job_name, script_location, iceberg_data_bucket, database_name,
                  table_name, source_path, iam_role_arn,
                  git_repository, git_owner, git_branch, git_folder, git_token):
    """Handle CREATE operation for Synthetics Glue Job."""
    logger.info(json.dumps({"message": "Creating Synthetics ETL Job", "job_name": job_name}))

    job_params = {
        'Name': job_name,
        'Role': iam_role_arn,
        'Command': {
            'Name': 'glueetl',
            'ScriptLocation': script_location,
            'PythonVersion': '3'
        },
        'DefaultArguments': build_default_arguments(
            iceberg_data_bucket, database_name, table_name, source_path
        ),
        'Description': 'ETL job to convert Synthetics reports to Iceberg format',
        'ExecutionClass': 'STANDARD',
        'GlueVersion': '5.0',
        'MaxRetries': 0,
        'NumberOfWorkers': 2,
        'Timeout': 60,
        'WorkerType': 'G.1X',
        'Tags': {
            'Environment': 'production',
            'Project': 'analytics-platform',
            'Component': 'synthetics-to-iceberg'
        }
    }

    if is_git_integration_enabled(git_repository, git_owner, git_token):
        source_control_details = build_source_control_details(
            git_repository, git_owner, git_branch, git_folder, git_token
        )
        job_params['SourceControlDetails'] = source_control_details
        logger.info(json.dumps({
            "message": "Git integration enabled",
            "job_name": job_name,
            "git_repository": git_repository
        }))

    try:
        glue_client.create_job(**job_params)
    except ClientError as e:
        if e.response['Error']['Code'] in ('AlreadyExistsException', 'IdempotentParameterMismatchException'):
            logger.info(json.dumps({"message": "Job already exists, falling back to update", "job_name": job_name}))
            return handle_update(
                job_name, script_location, iceberg_data_bucket, database_name,
                table_name, source_path, iam_role_arn,
                git_repository, git_owner, git_branch, git_folder, git_token)
        raise
    job_arn = wait_for_job_ready(job_name)

    if is_git_integration_enabled(git_repository, git_owner, git_token):
        glue_client.update_source_control_from_job(
            JobName=job_name,
            Provider='GITHUB',
            RepositoryName=git_repository,
            RepositoryOwner=git_owner,
            BranchName=git_branch,
            Folder=git_folder,
            AuthStrategy='PERSONAL_ACCESS_TOKEN',
            AuthToken=git_token
        )
        logger.info(json.dumps({"message": "Pushed job to Git repository", "job_name": job_name}))

    return {"JobName": job_name, "JobArn": job_arn, "Status": "CREATED"}


def handle_update(job_name, script_location, iceberg_data_bucket, database_name,
                  table_name, source_path, iam_role_arn,
                  git_repository, git_owner, git_branch, git_folder, git_token):
    """Handle UPDATE operation for Synthetics Glue Job."""
    logger.info(json.dumps({"message": "Updating Synthetics ETL Job", "job_name": job_name}))

    try:
        job_update = {
            'Role': iam_role_arn,
            'Command': {
                'Name': 'glueetl',
                'ScriptLocation': script_location,
                'PythonVersion': '3'
            },
            'DefaultArguments': build_default_arguments(
                iceberg_data_bucket, database_name, table_name, source_path
            ),
            'ExecutionClass': 'STANDARD',
            'GlueVersion': '5.0',
            'MaxRetries': 0,
            'NumberOfWorkers': 2,
            'Timeout': 60,
            'WorkerType': 'G.1X',
        }

        if is_git_integration_enabled(git_repository, git_owner, git_token):
            source_control_details = build_source_control_details(
                git_repository, git_owner, git_branch, git_folder, git_token
            )
            job_update['SourceControlDetails'] = source_control_details

        glue_client.update_job(JobName=job_name, JobUpdate=job_update)
        job_arn = wait_for_job_ready(job_name)

        if is_git_integration_enabled(git_repository, git_owner, git_token):
            glue_client.update_source_control_from_job(
                JobName=job_name,
                Provider='GITHUB',
                RepositoryName=git_repository,
                RepositoryOwner=git_owner,
                BranchName=git_branch,
                Folder=git_folder,
                AuthStrategy='PERSONAL_ACCESS_TOKEN',
                AuthToken=git_token
            )
            logger.info(json.dumps({"message": "Pushed job to Git repository", "job_name": job_name}))

        return {"JobName": job_name, "JobArn": job_arn, "Status": "UPDATED"}

    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityNotFoundException':
            return handle_create(
                job_name, script_location, iceberg_data_bucket, database_name,
                table_name, source_path, iam_role_arn,
                git_repository, git_owner, git_branch, git_folder, git_token)
        raise


def handle_delete(job_name):
    """Handle DELETE operation for Synthetics Glue Job."""
    logger.info(json.dumps({"message": "Deleting Synthetics ETL Job", "job_name": job_name}))

    try:
        glue_client.delete_job(JobName=job_name)
        return {"JobName": job_name, "Status": "DELETED"}
    except ClientError as e:
        if e.response['Error']['Code'] == 'EntityNotFoundException':
            return {"JobName": job_name, "Status": "ALREADY_DELETED"}
        raise


def wait_for_job_ready(job_name, max_wait_time=300, poll_interval=10):
    """Wait for Glue job to be in READY state after creation/update."""
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
    """Check if Git integration should be enabled based on provided parameters."""
    return all(param and param.strip() for param in [git_repository, git_owner, git_token])


def build_source_control_details(git_repository, git_owner, git_branch, git_folder, git_token):
    """Build SourceControlDetails configuration for Git integration."""
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
