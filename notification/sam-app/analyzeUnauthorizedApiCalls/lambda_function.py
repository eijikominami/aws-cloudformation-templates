import boto3
import json
import logging
import os
import sys
import datetime
# Lambda Powertools
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer

import base64
import gzip
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# Lambda Powertools
logger = Logger()
tracer = Tracer()

@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):

    ALERT_HOOK_URL = os.environ['ALERT_HOOK_URL']
    DEPLOYMENT_HOOK_URL = os.environ['DEPLOYMENT_HOOK_URL']
    if os.environ['ENCRYPT'] == 'true':
        # The base-64 encoded, encrypted key (CiphertextBlob) stored in the HOOK_URL and DEPLOYMENT_HOOK_URL environment variable
        ALERT_HOOK_URL = boto3.client('kms').decrypt(CiphertextBlob=base64.b64decode(ALERT_HOOK_URL))['Plaintext'].decode('utf-8')
        DEPLOYMENT_HOOK_URL = boto3.client('kms').decrypt(CiphertextBlob=base64.b64decode(DEPLOYMENT_HOOK_URL))['Plaintext'].decode('utf-8')
    # Variable declaration
    hook_url = None
    slack_message = None
    try:
        # Extracting the record data in bytes and base64 decoding it
        compressed_payload = base64.b64decode(event['awslogs']['data'])
        # Converting the bytes payload to string
        uncompressed_payload = gzip.decompress(compressed_payload)
        message = json.loads(uncompressed_payload)
        logger.structure_logs(append=True, log_message_body=message)
        logger.structure_logs(append=True, log_message_type=type(message).__name__)
        logger.structure_logs(append=True, log_message_length=str(len(message)))
        logger.info("Analyzing the received message.") 

        for logEvent in message['logEvents']:
            # Slack
            slack_message = createSlackMessage(message['owner'], json.loads(logEvent['message']))  
            sendSlackMessage(ALERT_HOOK_URL, slack_message)
            # SNS
            sendSNSMessage(json.loads(logEvent['message']))
    except json.decoder.JSONDecodeError:
        logger.info("Message is NOT a JSON format.")
        return

def createSlackMessage(account_id, message):

    resources = ''
    error = 'Unknown'
    user = 'Unknown'
    permissions = 'Unknown'
    title = ":heavy_exclamation_mark: 注意イベント | CloudWatch Alarm | " + message['awsRegion'] + " | Account: " + account_id
    title_link = "https://console.aws.amazon.com/cloudwatch/home?region=" + message['awsRegion'] + "#logsV2:log-groups"
    
    # Target Resources
    if 'resources' in message:
        for resource in message['resources']:
            if 'ARN' in resource:
                resources = resources + ' ' + resource['ARN']
            elif 'ARNPrefix' in resource:
                resources = resources + ' ' + resource['ARNPrefix']
    else:
        resources = 'Unknown'
    # User Id
    if 'arn' in message['userIdentity']:
        user = message['userIdentity']['arn']
    elif 'invokedBy' in message['userIdentity']:
        user = message['userIdentity']['invokedBy']
    elif 'accountId' in message['userIdentity']:
        user = message['userIdentity']['accountId']
    # Error Message
    if 'errorMessage' in message:
        error = message['errorMessage']
    # User Permissions
    if 'sessionContext' in message['userIdentity'] and 'sessionIssuer' in message['userIdentity']['sessionContext'] and 'arn' in message['userIdentity']['sessionContext']['sessionIssuer']:
        permissions = message['userIdentity']['sessionContext']['sessionIssuer']['arn']
    return {
        'attachments': [{
            'color': '#EBB424',
            'title': "%s" % title,
            'title_link': "%s" % title_link,
            'text': "*CloudTrail* が *不正なAPIコールを検知* しました。CloudTrail および CloudWatch Logs で当該イベントを特定し、IAMロールなどの *権限設定に問題が無いかを確認してください* 。",
            'fields': [
                    {
                        'title': "Target Service",
                        'value': "%s" % message['eventSource']
                    },
                    {
                        'title': "Target Resources",
                        'value': "%s" % resources
                    },
                    {
                        'title': "API Name",
                        'value': "%s" % message['eventName']
                    },
                    {
                        'title': "Error Message",
                        'value': "%s" % error
                    },
                    {
                        'title': "User Id",
                        'value': "%s" % user
                    },
                    {
                        'title': "User Permissions",
                        'value': "%s" % permissions
                    }
                ]
        }]
    }

def sendSlackMessage(hook_url, message):
    if not hook_url or not message:
        logger.warning("Hook url or message is empty.")
        return False
    else:
        hook_url = "https://" + hook_url
        req = Request(hook_url, json.dumps(message).encode('utf-8'))
        try:
            logger.structure_logs(append=True, slack_hook_url=hook_url)
            logger.info("Posted a message to Slack.")
            response = urlopen(req)
            response.read()
            return True
        except HTTPError:
            logger.exception("Received an exception in %s.", sys._getframe().f_code.co_name)
            return False
        except URLError:
            logger.exception("Received an exception in %s.", sys._getframe().f_code.co_name)
            return False

def sendSNSMessage(message):
    
    sns = boto3.client('sns')
    sts = boto3.client('sts')
    ssm = boto3.client('ssm')
    cloudwatch = boto3.client('cloudwatch')
    
    if os.environ['ALARM_NAME'] is None or os.environ['SNS_TOPIC_ARN'] is None:
        logger.warning("Hook url or message is empty.")
        return False
    else:    
        alarm = cloudwatch.describe_alarms(AlarmNames=[os.environ['ALARM_NAME']])['MetricAlarms'][0]
        now = datetime.datetime.now()
        
        resources = ''
        error = 'Unknown'
        user = 'Unknown'
        permissions = 'Unknown'
        # Target Resources
        if 'resources' in message:
            for resource in message['resources']:
                if 'ARN' in resource:
                    resources = resources + ' ' + resource['ARN']
                elif 'ARNPrefix' in resource:
                    resources = resources + ' ' + resource['ARNPrefix']
        else:
            resources = 'Unknown'
        # User Id
        if 'arn' in message['userIdentity']:
            user = message['userIdentity']['arn']
        elif 'invokedBy' in message['userIdentity']:
            user = message['userIdentity']['invokedBy']
        elif 'accountId' in message['userIdentity']:
            user = message['userIdentity']['accountId']
        # Error Message
        if 'errorMessage' in message:
            error = message['errorMessage']
        # User Permissions
        if 'sessionContext' in message['userIdentity'] and 'sessionIssuer' in message['userIdentity']['sessionContext'] and 'arn' in message['userIdentity']['sessionContext']['sessionIssuer']:
            permissions = message['userIdentity']['sessionContext']['sessionIssuer']['arn']
        # Region
        region = ssm.get_parameters(Names = ['/aws/service/global-infrastructure/regions/' + boto3.session.Session().region_name + '/longName'])['Parameters'][0]['Value']
        formatted_message = {
            'AlarmName': alarm['AlarmName'] if 'AlarmArn' in alarm else '',
            'AlarmDescription': '*CloudTrail* が *不正なAPIコールを検知* しました。詳細は以下の通りです。 User: *' + user + '* | Permission: *' + permissions + '* | Resource: *'+ resources + '* | Event Name: *' + message['eventName'] + '* | Error: *' + error + '*' ,
            'AWSAccountId': sts.get_caller_identity()['Account'],
            'AlarmConfigurationUpdatedTimestamp': now.strftime('%Y-%m-%dT%H:%M:%S.000+0000'),
            'NewStateValue': 'ALARM',
            'NewStateReason': '*CloudTrail* が *不正なAPIコールを検知* しました。詳細は以下の通りです。 User: *' + user + '* | Permission: *' + permissions + '* | Resource: *'+ resources + '* | Event Name: *' + message['eventName'] + '* | Error: *' + error + '*' ,
            'StateChangeTime': now.strftime('%Y-%m-%dT%H:%M:%S.000+0000'),
            'Region': region,
            'AlarmArn': alarm['AlarmArn'] if 'AlarmArn' in alarm else '',
            'OldStateValue': 'OK',
            'OKActions': alarm['OKActions'] if 'OKActions' in alarm else [],
            'AlarmActions': os.environ['SNS_TOPIC_ARN'],
            'InsufficientDataActions': alarm['InsufficientDataActions'] if 'InsufficientDataActions' in alarm else [],
            'Trigger': {
                'MetricName': alarm['MetricName'] if 'MetricName' in alarm else '',
                'Namespace': alarm['Namespace'] if 'Namespace' in alarm else '',
                'StatisticType': 'Statistic',
                'Statistic': alarm['Statistic'] if 'Statistic' in alarm else '',
                'Unit': alarm['Unit'] if 'Unit' in alarm else None,
                'Dimensions': alarm['Dimensions'] if 'Dimensions' in alarm else [],
                'Period': alarm['Period'] if 'Period' in alarm else 0,
                'EvaluationPeriods': alarm['EvaluationPeriods'] if 'EvaluationPeriods' in alarm else 0,
                'ComparisonOperator': alarm['ComparisonOperator'] if 'ComparisonOperator' in alarm else '',
                'Threshold': alarm['Threshold'] if 'Threshold' in alarm else 0,
                'TreatMissingData': alarm['TreatMissingData'] if '' in alarm else 'notBreaching',
                'EvaluateLowSampleCountPercentile': alarm['EvaluateLowSampleCountPercentile'] if 'EvaluateLowSampleCountPercentile' in alarm else ''
            }
        }
        request = {
            'TopicArn': os.environ['SNS_TOPIC_ARN'],
            'Subject': 'ALARM: "' + alarm['AlarmName'] + '" in ' + region,
            'Message': json.dumps(formatted_message)
        }
        logger.structure_logs(append=True, sns_message_body=formatted_message)
        logger.info("Transfered a message to a SNS topic.") 
        sns.publish(**request)