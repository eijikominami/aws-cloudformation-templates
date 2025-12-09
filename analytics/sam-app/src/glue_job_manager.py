import boto3
import cfnresponse
import json

def handler(event, context):
    request_type = event.get('RequestType')
    physical_resource_id = event.get('PhysicalResourceId', context.log_stream_name)
    
    print(f"Request type: {request_type}")
    print(f"Event: {json.dumps(event, default=str)}")
    
    try:
        resource_properties = event['ResourceProperties']
        glue = boto3.client("glue")
        job_name = resource_properties["JobName"]
        
        if request_type == "Delete":
            try:
                glue.delete_job(JobName=job_name)
            except glue.exceptions.EntityNotFoundException:
                pass  # Job already deleted
            
            cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, physical_resource_id)
            return
        
        # Parse job configuration
        default_args = json.loads(resource_properties.get("DefaultArguments", "{}"))
        tags = json.loads(resource_properties.get("Tags", "{}"))
        
        # Build job configuration for Visual ETL
        account_id = resource_properties.get('AccountId', context.invoked_function_arn.split(':')[4])
        region = resource_properties.get('Region', context.invoked_function_arn.split(':')[3])
        
        # For Visual ETL, we need CodeGenConfigurationNodes
        code_gen_nodes = resource_properties.get("CodeGenConfigurationNodes", "{}")
        
        # Check if this is a Visual ETL job
        is_visual_etl = code_gen_nodes and code_gen_nodes.strip() != "{}"
        
        job_config = {
            "Name": job_name,
            "Role": resource_properties["Role"],
            "Command": {
                "Name": "glueetl",
                "PythonVersion": "3"
            },
            "GlueVersion": resource_properties["GlueVersion"],
            "WorkerType": resource_properties["WorkerType"],
            "NumberOfWorkers": resource_properties["NumberOfWorkers"],
            "Description": resource_properties.get("Description", f"Glue job {job_name}"),
            "Tags": tags,
            "MaxRetries": resource_properties.get("MaxRetries", 0),
            "Timeout": resource_properties.get("Timeout", 60),
            "DefaultArguments": default_args
        }
        
        # Add Connections only if ConnectionName is provided
        if resource_properties.get("ConnectionName"):
            job_config["Connections"] = {
                "Connections": [resource_properties["ConnectionName"]]
            }
        
        # ScriptLocation is always required, even for Visual ETL jobs
        job_config["Command"]["ScriptLocation"] = f"s3://aws-glue-assets-{account_id}-{region}/scripts/{job_name}.py"
        
        if is_visual_etl:
            # Visual ETL job - add CodeGenConfigurationNodes
            job_config["CodeGenConfigurationNodes"] = json.loads(code_gen_nodes)
        

        
        if request_type == "Create":
            print(f"Creating job with config: {json.dumps(job_config, default=str)}")
            glue.create_job(**job_config)
            print("Job created successfully")
        
        elif request_type == "Update":
            job_update = {k: v for k, v in job_config.items() if k not in ["Name", "Tags"]}
            try:
                glue.update_job(JobName=job_name, JobUpdate=job_update)
            except glue.exceptions.EntityNotFoundException:
                glue.create_job(**job_config)
        
        # Get job details to retrieve ARN
        job_details = glue.get_job(JobName=job_name)
        job_arn = job_details['Job']['Name']  # Glue jobs don't have ARNs, use name as identifier
        
        # Construct ARN format for Glue job
        account_id = resource_properties.get('AccountId', context.invoked_function_arn.split(':')[4])
        region = resource_properties.get('Region', context.invoked_function_arn.split(':')[3])
        job_arn = f"arn:aws:glue:{region}:{account_id}:job/{job_name}"
        
        response_data = {
            "JobName": job_name,
            "JobArn": job_arn
        }
        
        cfnresponse.send(event, context, cfnresponse.SUCCESS, response_data, physical_resource_id)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        cfnresponse.send(event, context, cfnresponse.FAILED, {}, physical_resource_id, str(e))