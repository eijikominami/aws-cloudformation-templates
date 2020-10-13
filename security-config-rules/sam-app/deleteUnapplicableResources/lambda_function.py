import logging
import json
import boto3
# Lambda Powertools
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer

# Lambda Powertools
logger = Logger()
tracer = Tracer()

@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    if 'detail' in event:
        detail = event['detail']
        if 'configRuleName' in detail:
            if detail['configRuleName'] == 'required-tags':
                logger.debug(str(detail))
                # S3
                if detail['resourceType'] == 'AWS::S3::Bucket': 
                    s3 = boto3.resource('s3') 
                    bucket = s3.Bucket(detail['resourceId'])
                    # Deletes all objects
                    for o in bucket.objects.all(): 
                        bucket.delete_objects(
                            Delete={
                            "Objects": [
                                {"Key": o.key}
                                ]
                            }
                        )
                    # Deletes a bucket    
                    bucket.delete()
                # DynamoDB
                if detail['resourceType'] == 'AWS::DynamoDB::Table':
                    client = boto3.client('dynamodb')
                    client.delete_table(
                        TableName=detail['resourceId']
                    )

            if detail['configRuleName'] == 'required-tags-expanded':
                # API Gateway
                if detail['resourceType'] == 'AWS::ApiGateway::RestApi':
                    client = boto3.client('apigateway')
                    client.delete_rest_api(
                        restApiId=detail["resourceId"][-10:]
                    )
                # Lambda
                if detail['resourceType'] == 'AWS::Lambda::Function':
                    client = boto3.client('lambda')
                    client.delete_function(
                        FunctionName=detail['resourceId']
                    )
