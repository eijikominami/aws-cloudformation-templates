import json
import cf_response
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
client = boto3.client('ecs')

def lambda_handler(event, context):
  logger.info('Event received:')
  logger.info(json.dumps(event, indent=2))
  responseData = {}
  physicalResourceId = ''
  try:
    request_type = event['RequestType']
    task_definition = event['ResourceProperties']['TaskDefinition']
    if request_type == 'Update':
        physicalResourceId = event['PhysicalResourceId']
        responseData['TaskDefinition'] = physicalResourceId
        print(responseData['TaskDefinition'])
    elif request_type == 'Create':
        responseData['TaskDefinition'] = task_definition
        physicalResourceId = task_definition
        print(responseData['TaskDefinition'])
    else:
      print("Did not recieve a create or update event, skipping.. ")
    
    cf_response.send(event, context, cf_response.SUCCESS, responseData, physicalResourceId)

  except Exception as e:
    print("ERROR creating the deployment, Error: %s" %(str(e)))
    cf_response.send(event, context, cf_response.FAILED, responseData, "CustomResourcePhysicalID")
