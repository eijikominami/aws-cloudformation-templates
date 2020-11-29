import boto3
import json
import logging
import os
import sys
# Lambda Powertools
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer

from base64 import b64decode
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
        ALERT_HOOK_URL = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ALERT_HOOK_URL))['Plaintext'].decode('utf-8')
        DEPLOYMENT_HOOK_URL = boto3.client('kms').decrypt(CiphertextBlob=b64decode(DEPLOYMENT_HOOK_URL))['Plaintext'].decode('utf-8')
    # Variable declaration
    hook_url = None
    slack_message = None
    try:
        message = json.loads(event['Records'][0]['Sns']['Message'])
        logger.structure_logs(append=True, sns_message_body=str(message))
        logger.structure_logs(append=True, sns_message_type=type(message).__name__)
        logger.structure_logs(append=True, sns_message_length=str(len(message)))
        logger.info("Analyzing the received message.")                          
    except json.decoder.JSONDecodeError:
        logger.info("Message is NOT a JSON format.")
        return
    # Sends Slack
    sendMessage(hook_url, slack_message)

def createUnauthorizedApiCallsAlarmMessage(message):

    resources = ''
    title = ":x: 警告イベント | CloudWatch Alarm | " + message['Region'] + " | Account: " + message['AWSAccountId']
    title_link = "https://console.aws.amazon.com/cloudwatch/home?region=" + message['region'] + "#logsV2:log-groups"
    
    for resource in message['resources']:
        resources = resources + ' ' + resource
    return {
        'attachments': [{
            'color': '#dc4f7e',
            'title': "%s" % title,
            'title_link': "%s" % title_link,
            'text': "CloudTrail が 不正なAPIコールを検知 しました。CloudTrail および CloudWatch Logs で当該イベントを特定し、IAMロールなどの 権限設定に問題が無いかを確認してください 。",
            'fields': [
                    {
                        'title': "Resources",
                        'value': "%s" % resources
                    }
                ]
        }]
    }

def sendMessage(hook_url, message):
    if hook_url is None or message is None:
        logger.warning("Hook url or message is empty.")
        return False
    else:
        req = Request(hook_url, json.dumps(message).encode('utf-8'))
        try:
            logger.structure_logs(append=True, slack_hook_url=hook_url)
            logger.info("Posted a message to the Slack.")
            response = urlopen(req)
            response.read()
            return True
        except HTTPError:
            logger.exception("Received an exception in %s.", sys._getframe().f_code.co_name)
            return False
        except URLError:
            logger.exception("Received an exception in %s.", sys._getframe().f_code.co_name)
            return False   