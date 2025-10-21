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
        account_id = properties['AccountId']
        
        # Extract Git integration properties (optional)
        git_repository = properties.get('GitRepository', '')
        git_owner = properties.get('GitOwner', '')
        git_branch = properties.get('GitBranch', 'main')
        git_folder = properties.get('GitFolder', 'glue-jobs')
        git_token = properties.get('GitToken', '')
        
        # Handle different request types
        if request_type == 'Create':
            response_data = handle_create(job_name, connection_name, iceberg_data_bucket, database_name, scripts_bucket, logical_name,
                                        iam_role_arn, account_id,
                                        git_repository, git_owner, git_branch, git_folder, git_token)
        elif request_type == 'Update':
            response_data = handle_update(job_name, connection_name, iceberg_data_bucket, database_name, scripts_bucket, logical_name,
                                        iam_role_arn, account_id,
                                        git_repository, git_owner, git_branch, git_folder, git_token)
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
        }, job_name)

def handle_create(job_name, connection_name, iceberg_data_bucket, database_name, scripts_bucket, logical_name, iam_role_arn, account_id,
                 git_repository, git_owner, git_branch, git_folder, git_token):
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
        account_id: Google Analytics Account ID
        git_repository: Git repository URL (optional)
        git_owner: Git repository owner (optional)
        git_branch: Git branch name
        git_folder: Git folder path
        git_token: Git authentication token (optional)
    
    Returns:
        dict: Response data with job details
    """
    
    logger.info(json.dumps({
        "message": "Creating Visual ETL Job",
        "job_name": job_name,
        "connection_name": connection_name
    }))
    
    try:
        # Generate CodeGenConfigurationNodes for Visual ETL
        code_gen_nodes = generate_visual_etl_nodes(
            connection_name, iceberg_data_bucket, database_name, account_id
        )
        
        # Prepare job creation parameters
        job_params = {
            'Name': job_name,
            'Role': iam_role_arn,
            'JobMode': 'VISUAL',  # Specify Visual ETL mode
            'Command': {
                'Name': 'glueetl',
                'ScriptLocation': f's3://{scripts_bucket}/glue-jobs/{logical_name}-ga4-to-s3-ingestion-job.py',
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
                '--conf spark.sql.catalog.glue_catalog': 'org.apache.iceberg.spark.SparkCatalog',
                '--conf spark.sql.catalog.glue_catalog.catalog-impl': 'org.apache.iceberg.aws.glue.GlueCatalog',
                '--conf spark.sql.catalog.glue_catalog.io-impl': 'org.apache.iceberg.aws.s3.S3FileIO',
                '--conf spark.sql.catalog.glue_catalog.warehouse': f's3://{scripts_bucket}/iceberg-warehouse/',
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
            'CodeGenConfigurationNodes': code_gen_nodes,
            'Tags': {
                'Environment': 'production',
                'Project': 'analytics-platform',
                'Component': 'ga4-to-s3-ingestion'
            }
        }
        
        # Add Git integration if all required parameters are provided
        if is_git_integration_enabled(git_repository, git_owner, git_token):
            source_control_details = build_source_control_details(
                git_repository, git_owner, git_branch, git_folder, git_token
            )
            job_params['SourceControlDetails'] = source_control_details
            
            logger.info(json.dumps({
                "message": "Git integration enabled for Visual ETL Job",
                "job_name": job_name,
                "git_repository": git_repository,
                "git_branch": git_branch,
                "git_folder": git_folder
            }))
        else:
            logger.info(json.dumps({
                "message": "Git integration disabled - required parameters not provided",
                "job_name": job_name,
                "has_repository": bool(git_repository),
                "has_owner": bool(git_owner),
                "has_token": bool(git_token)
            }))
        
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

def handle_update(job_name, connection_name, iceberg_data_bucket, database_name, scripts_bucket, logical_name, iam_role_arn, account_id,
                 git_repository, git_owner, git_branch, git_folder, git_token):
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
        account_id: Google Analytics Account ID
        git_repository: Git repository URL (optional)
        git_owner: Git repository owner (optional)
        git_branch: Git branch name
        git_folder: Git folder path
        git_token: Git authentication token (optional)
    
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
        
        # Generate updated CodeGenConfigurationNodes
        code_gen_nodes = generate_visual_etl_nodes(
            connection_name, iceberg_data_bucket, database_name, account_id
        )
        
        # Update the job with new configuration
        job_update = {
            'JobMode': 'VISUAL',  # Ensure Visual ETL mode
            'Role': iam_role_arn,
            'Command': current_job['Job']['Command'],
            'DefaultArguments': current_job['Job']['DefaultArguments'],
            'Connections': {
                'Connections': [connection_name]
            },
            'MaxRetries': 0,
            'Timeout': 480,
            'GlueVersion': '5.0',
            'NumberOfWorkers': 10,
            'WorkerType': 'G.1X',
            'ExecutionClass': 'STANDARD',
            'CodeGenConfigurationNodes': code_gen_nodes
        }
        
        # Add or update Git integration if all required parameters are provided
        if is_git_integration_enabled(git_repository, git_owner, git_token):
            source_control_details = build_source_control_details(
                git_repository, git_owner, git_branch, git_folder, git_token
            )
            job_update['SourceControlDetails'] = source_control_details
            
            logger.info(json.dumps({
                "message": "Git integration updated for Visual ETL Job",
                "job_name": job_name,
                "git_repository": git_repository,
                "git_branch": git_branch,
                "git_folder": git_folder
            }))
        else:
            logger.info(json.dumps({
                "message": "Git integration disabled - required parameters not provided",
                "job_name": job_name,
                "has_repository": bool(git_repository),
                "has_owner": bool(git_owner),
                "has_token": bool(git_token)
            }))
        
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
            raise Exception(f"Glue job '{job_name}' not found for update")
        elif error_code == 'InvalidInputException':
            raise Exception(f"Invalid input for Glue job update: {error_message}")
        else:
            raise Exception(f"Glue API error ({error_code}): {error_message}")

def handle_delete(job_name):
    """
    Handle DELETE operation for Visual ETL Job.
    
    Note: Due to DeletionPolicy: Retain on the Custom Resource,
    this function should not actually delete the job to prevent
    accidental deletion during CloudFormation updates.
    
    Args:
        job_name: Name of the Glue job to delete
    
    Returns:
        dict: Response data confirming deletion (without actual deletion)
    """
    
    logger.info(json.dumps({
        "message": "DELETE operation called for Visual ETL Job",
        "job_name": job_name,
        "action": "SKIPPED - DeletionPolicy: Retain protects this resource"
    }))
    
    try:
        # Check if job exists
        try:
            job = glue_client.get_job(JobName=job_name)
            logger.info(json.dumps({
                "message": "Visual ETL Job exists but will be retained",
                "job_name": job_name,
                "job_status": "RETAINED"
            }))
            
            return {
                "JobName": job_name,
                "Status": "RETAINED",
                "Message": "Job preserved due to DeletionPolicy: Retain"
            }
            
        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityNotFoundException':
                logger.info(json.dumps({
                    "message": "Job already deleted or does not exist",
                    "job_name": job_name
                }))
                return {
                    "JobName": job_name,
                    "Status": "ALREADY_DELETED"
                }
            raise
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        
        logger.error(json.dumps({
            "message": "AWS Glue API error during job deletion check",
            "error_code": error_code,
            "error_message": error_message,
            "job_name": job_name
        }))
        
        if error_code == 'EntityNotFoundException':
            return {
                "JobName": job_name,
                "Status": "ALREADY_DELETED"
            }
        else:
            # Even on error, don't fail the CloudFormation operation
            return {
                "JobName": job_name,
                "Status": "RETAINED",
                "Message": f"Job preserved due to error: {error_message}"
            }

def generate_visual_etl_nodes(connection_name, iceberg_data_bucket, database_name, account_id):
    """
    Generate CodeGenConfigurationNodes for Visual ETL Job.
    
    This creates a Visual ETL flow with:
    1. Google Analytics 4 data source
    2. Schema transformation (Apply Mapping)
    3. S3 Parquet target
    
    Args:
        connection_name: Name of the Google Analytics 4 connection
        iceberg_data_bucket: S3 bucket for Iceberg output
        database_name: Glue Data Catalog database name
        account_id: Google Analytics Account ID
    
    Returns:
        dict: CodeGenConfigurationNodes configuration
    """
    
    return {
        "node-source": {
            "ConnectorDataSource": {
                "Name": "Google Analytics 4",
                "ConnectionType": "googleanalytics4",
                "Data": {
                    "connectionName": connection_name,
                    "ENTITY_NAME": f"core-reports/accounts/{account_id}",
                    "SELECTED_FIELDS": "date,activeusers",
                    "API_VERSION": "v1beta"
                },
                "OutputSchemas": [{
                    "Columns": [
                        {"Name": "date", "Type": "date"},
                        {"Name": "activeusers", "Type": "string"}
                    ]
                }]
            }
        },
        "node-transform": {
            "ApplyMapping": {
                "Name": "Change Schema",
                "Inputs": ["node-source"],
                "Mapping": [
                    {
                        "ToKey": "date",
                        "FromPath": ["date"],
                        "FromType": "date",
                        "ToType": "date",
                        "Dropped": False
                    },
                    {
                        "ToKey": "activeusers", 
                        "FromPath": ["activeusers"],
                        "FromType": "string",
                        "ToType": "string",
                        "Dropped": False
                    }
                ]
            }
        },
        "node-target": {
            "S3IcebergCatalogTarget": {
                "Name": "Amazon S3 (Iceberg)",
                "Inputs": ["node-transform"],
                "Table": "ga4_core_reports",
                "Database": database_name,
                "PartitionKeys": [],
                "SchemaChangePolicy": {
                    "EnableUpdateCatalog": True
                }
            }
        }
    }

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

def is_git_integration_enabled(git_repository, git_owner, git_token):
    """
    Check if Git integration should be enabled based on provided parameters.
    
    Args:
        git_repository: Git repository URL
        git_owner: Git repository owner
        git_token: Git authentication token
    
    Returns:
        bool: True if all required Git parameters are provided, False otherwise
    """
    
    # All required parameters must be non-empty strings
    required_params = [git_repository, git_owner, git_token]
    
    # Check if all required parameters are provided and non-empty
    git_enabled = all(param and param.strip() for param in required_params)
    
    logger.info(json.dumps({
        "message": "Git integration eligibility check",
        "git_enabled": git_enabled,
        "has_repository": bool(git_repository and git_repository.strip()),
        "has_owner": bool(git_owner and git_owner.strip()),
        "has_token": bool(git_token and git_token.strip())
    }))
    
    return git_enabled

def build_source_control_details(git_repository, git_owner, git_branch, git_folder, git_token):
    """
    Build SourceControlDetails configuration for Git integration.
    
    Args:
        git_repository: Git repository URL
        git_owner: Git repository owner
        git_branch: Git branch name
        git_folder: Git folder path
        git_token: Git authentication token
    
    Returns:
        dict: SourceControlDetails configuration
    """
    
    # Determine provider based on repository URL
    provider = 'GITHUB'  # Default to GitHub
    if 'gitlab' in git_repository.lower():
        provider = 'GITLAB'
    elif 'codecommit' in git_repository.lower():
        provider = 'AWS_CODE_COMMIT'
    elif 'bitbucket' in git_repository.lower():
        provider = 'BITBUCKET'
    
    source_control_details = {
        'Provider': provider,
        'Repository': git_repository,
        'Branch': git_branch,
        'Folder': git_folder,
        'AuthStrategy': 'PERSONAL_ACCESS_TOKEN',
        'AuthToken': git_token
    }
    
    # Add owner for non-CodeCommit providers
    if provider != 'AWS_CODE_COMMIT' and git_owner:
        source_control_details['Owner'] = git_owner
    
    logger.info(json.dumps({
        "message": "Built SourceControlDetails configuration",
        "provider": provider,
        "repository": git_repository,
        "branch": git_branch,
        "folder": git_folder,
        "has_owner": bool(git_owner),
        "has_token": bool(git_token)
    }))
    
    return source_control_details