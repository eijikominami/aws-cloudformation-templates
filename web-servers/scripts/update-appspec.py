import yaml
import argparse
import boto3

parser = argparse.ArgumentParser(description='Script usage')

parser.add_argument('--taskArn', type=str, required=True)
parser.add_argument('--hooksLambdaArn', type=str, required=True)
parser.add_argument('--inputAppSpecFile', type=str, required=True)
parser.add_argument('--outputAppSpecFile', type=str, required=True)
args = parser.parse_args()

ecs = boto3.client('ecs')

if args.inputAppSpecFile:
  inputAppSpecFile = args.inputAppSpecFile
if args.outputAppSpecFile:
  outputAppSpecFile = args.outputAppSpecFile
if args.taskArn:
  taskArn = args.taskArn
if args.hooksLambdaArn:
  hooksLambdaArn = args.hooksLambdaArn

with open(outputAppSpecFile, 'w') as outputFile:

  with open(inputAppSpecFile, 'r') as file:
    contents = yaml.safe_load(file)
    print(contents)
    response = ecs.describe_task_definition(taskDefinition=taskArn)
    contents['Hooks'][0]['AfterAllowTestTraffic'] = hooksLambdaArn
    contents['Resources'][0]['TargetService']['Properties']['LoadBalancerInfo']['ContainerName'] = response['taskDefinition']['containerDefinitions'][0]['name']
    contents['Resources'][0]['TargetService']['Properties']['LoadBalancerInfo']['ContainerPort'] = response['taskDefinition']['containerDefinitions'][0]['portMappings'][0]['containerPort']

    print('Updated appspec.yaml')
    print(contents)  

    yaml.dump(contents, outputFile)