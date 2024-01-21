import json
import logging
import cf_response
import boto3
import os
import sys

logger = logging.getLogger(os.getenv("LOGGER", default="aws-blue-green-deploymentgrp"))
logger.setLevel(os.getenv("LOG_LEVEL", default=logging.DEBUG))
stdout_logger = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_logger)

cd_client = boto3.client('codedeploy')
def lambda_handler(event, context):
  logger.info('Event received:')
  logger.info(json.dumps(event, indent=2))
  responseData = {}
  applicationName = event['ResourceProperties']['applicationName']
  deploymentGroupName = event['ResourceProperties']['deploymentGroupName']
  deploymentConfigName = event['ResourceProperties']['deploymentConfigName']
  newdeploymentGroupName = event['ResourceProperties']['deploymentGroupName']
  TerminationTimeInMinutes = int(event['ResourceProperties']['TerminationTimeInMinutes'])
  serviceRoleArn = event['ResourceProperties']['serviceRoleArn']

  if event['RequestType'] == 'Delete':
    try:
      response = cd_client.delete_deployment_group(
        applicationName = event['ResourceProperties']["applicationName"],   
        deploymentGroupName = event['ResourceProperties']["deploymentGroupName"]
      )
      logger.info('SUCCESS: Deleted CodeDeploy DeploymentGroup')
      responseData['Data'] = 'Success'
      responseData['applicationName'] = applicationName
      print("CodeDeploy Deployment Application Name: %s" %(responseData['applicationName']))
      responseData['CodeDeployDeploymentGroupName'] = deploymentGroupName
      print("CodeDeploy Deployment Group Name: %s" %(responseData['CodeDeployDeploymentGroupName']))
      cf_response.send(event, context, cf_response.SUCCESS, responseData, 'CustomResourcePhysicalId')
    except Exception as e:
      logger.error(f'Error deleting CodeDeploy DeploymentGroup: {e}')
      responseData['Data'] = 'Failed'
      cf_response.send(event, context, cf_response.FAILED, responseData, 'CustomResourcePhysicalId')
  elif event['RequestType'] == 'Create':
    try:
      response = cd_client.create_deployment_group(
        applicationName = event['ResourceProperties']['applicationName'],   
        deploymentGroupName = event['ResourceProperties']['deploymentGroupName'],  
        deploymentConfigName = event['ResourceProperties']['deploymentConfigName'],
        serviceRoleArn = event['ResourceProperties']['serviceRoleArn'],
        triggerConfigurations = [
          {
            'triggerName': event['ResourceProperties']['CDtriggerName'],
            'triggerTargetArn': event['ResourceProperties']['CDtriggerTargetArn'],
            'triggerEvents': [
              "DeploymentStart",
              "DeploymentSuccess",
              "DeploymentFailure",
              "DeploymentStop",
              "DeploymentRollback",
              "DeploymentReady"
            ]
          },
        ],
        autoRollbackConfiguration = {
          'enabled': True,
          'events': [
            'DEPLOYMENT_FAILURE', 
            'DEPLOYMENT_STOP_ON_ALARM', 
            'DEPLOYMENT_STOP_ON_REQUEST',
          ]
        },
        deploymentStyle = {
          'deploymentType': 'BLUE_GREEN',
          'deploymentOption': 'WITH_TRAFFIC_CONTROL'
        },
        blueGreenDeploymentConfiguration = {
          'terminateBlueInstancesOnDeploymentSuccess': {
            'action': 'TERMINATE',
            'terminationWaitTimeInMinutes': TerminationTimeInMinutes
        },
          'deploymentReadyOption': {
            'actionOnTimeout': 'CONTINUE_DEPLOYMENT',
            'waitTimeInMinutes': 0
          }
        },
        loadBalancerInfo = {
          'targetGroupPairInfoList':[{
            'targetGroups': [
              {
                'name': event['ResourceProperties']['ECSalbTargetGroupBlue']
              },
              {
                'name': event['ResourceProperties']['ECSalbTargetGroupGreen']
              }
            ],
            'prodTrafficRoute': {
              'listenerArns': [
                event['ResourceProperties']['ECSprodTrafficRoute']
              ]
              },
            'testTrafficRoute': {
              'listenerArns': [
                event['ResourceProperties']['ECStestTrafficRoute']
              ]
              }
            }
          ]
        },
        ecsServices = [
          {
            'serviceName': event['ResourceProperties']['ECSFargateBGService'],
            'clusterName': event['ResourceProperties']['ECSFargateBGCluster'] 
          }
          ]
      )
      logger.info('SUCCESS: Created CodeDeploy DeploymentGroup')
      responseData['Data'] = 'Success'
      responseData['applicationName'] = applicationName
      print("CodeDeploy Deployment Application Name: %s" %(responseData['applicationName']))              
      responseData['CodeDeployDeploymentGroupName'] = deploymentGroupName
      print("CodeDeploy Deployment Group Name: %s" %(responseData['CodeDeployDeploymentGroupName']))
      responseData['BGNotificationsTriggerName'] = event['ResourceProperties']['CDtriggerName']
      print("Blue/Green Deployment Notifications Trigger Name: %s" %(responseData['BGNotificationsTriggerName']))       
      cf_response.send(event, context, cf_response.SUCCESS, responseData, 'CustomResourcePhysicalId')
    except Exception as e:
      logger.error(f'Error creating CodeDeploy DeploymentGroup: {e}')
      responseData['Data'] = 'Failed'
      cf_response.send(event, context, cf_response.FAILED, responseData, 'CustomResourcePhysicalId')
  elif event['RequestType'] == 'Update':
    try:
      response = cd_client.update_deployment_group(
        applicationName = event['ResourceProperties']['applicationName'],   
        newdeploymentGroupName = event['ResourceProperties']['deploymentGroupName'],  
        deploymentConfigName = event['ResourceProperties']['deploymentConfigName'], 
        currentdeploymentGroupName = event['OldResourceProperties']['deploymentGroupName'], 
        serviceRoleArn = event['ResourceProperties']['serviceRoleArn'],
        triggerConfigurations = [
          {
            'triggerName': event['ResourceProperties']['CDtriggerName'],
            'triggerTargetArn': event['ResourceProperties']['CDtriggerTargetArn'],
            'triggerEvents': [
              "DeploymentStart",
              "DeploymentSuccess",
              "DeploymentFailure",
              "DeploymentStop",
              "DeploymentRollback",
              "DeploymentReady"
            ]
          },
        ],
        autoRollbackConfiguration = {
          'enabled': True,
          'events': [
            'DEPLOYMENT_FAILURE', 
            'DEPLOYMENT_STOP_ON_ALARM', 
            'DEPLOYMENT_STOP_ON_REQUEST',
          ]
        },
        deploymentStyle = {
          'deploymentType': 'BLUE_GREEN',
          'deploymentOption': 'WITH_TRAFFIC_CONTROL'
        },
        blueGreenDeploymentConfiguration = {
          'terminateBlueInstancesOnDeploymentSuccess': {
            'action': 'TERMINATE',
            'terminationWaitTimeInMinutes': TerminationTimeInMinutes
        },
          'deploymentReadyOption': {
            'actionOnTimeout': 'CONTINUE_DEPLOYMENT',
            'waitTimeInMinutes': 0
          }
        },
        loadBalancerInfo = {
          'targetGroupPairInfoList':[{
            'targetGroups': [
              {
                'name': event['ResourceProperties']['ECSalbTargetGroupBlue']
              },
              {
                'name': event['ResourceProperties']['ECSalbTargetGroupGreen']
              }
            ],
            'prodTrafficRoute': {
              'listenerArns': [
                event['ResourceProperties']['ECSprodTrafficRoute']
              ]
              },
            'testTrafficRoute': {
              'listenerArns': [
                event['ResourceProperties']['ECStestTrafficRoute']
              ]
              }
            }
          ]
        },
        ecsServices = [
          {
            'serviceName': event['ResourceProperties']['ECSFargateBGService'],
            'clusterName': event['ResourceProperties']['ECSFargateBGCluster'] 
          }
          ]
      )
      logger.info('SUCCESS: Updated CodeDeploy DeploymentGroup')
      responseData['Data'] = 'Success' 
      responseData['applicationName'] = applicationName
      print("CodeDeploy Deployment Application Name: %s" %(responseData['applicationName']))
      responseData['CodeDeployDeploymentGroupName'] = newdeploymentGroupName
      print("CodeDeploy Deployment Group Name: %s" %(responseData['CodeDeployDeploymentGroupName']))
      responseData['BGNotificationsTriggerName'] = event['ResourceProperties']['CDtriggerName']
      print("Blue/Green Deployment Notifications Trigger Name: %s" %(responseData['BGNotificationsTriggerName']))               
      cf_response.send(event, context, cf_response.SUCCESS, responseData, 'CustomResourcePhysicalId')
    except Exception as e:
      logger.error(f'Error updating CodeDeploy DeploymentGroup: {e}')
      responseData['Data'] = 'Failed'
      cf_response.send(event, context, cf_response.FAILED, responseData, 'CustomResourcePhysicalId')      
  else:
    print("Did not recieve a create deploy event, skipping.. ")
    logger.error('Error: unsupported event type')
    responseData['Data'] = 'Failed'
    cf_response.send(event, context, cf_response.FAILED, responseData, 'CustomResourcePhysicalId')
