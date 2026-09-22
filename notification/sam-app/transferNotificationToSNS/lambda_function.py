import boto3
import json
import logging
import os
import sys
# Lambda Powertools
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer

import base64
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# Lambda Powertools
logger = Logger()
tracer = Tracer()

# AWS Chatbot custom notification schema
# https://docs.aws.amazon.com/chatbot/latest/adminguide/custom-notifs.html
TITLE_MAX_LENGTH = 250
DESCRIPTION_MAX_LENGTH = 8000

def createCustomNotification(subject, text):
    return {
        'version': '1.0',
        'source': 'custom',
        'content': {
            'textType': 'client-markdown',
            'title': (subject if subject else 'AWS Notification')[:TITLE_MAX_LENGTH],
            'description': text[:DESCRIPTION_MAX_LENGTH]
        }
    }

@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):

    sns = boto3.client('sns')
    for record in event['Records']:

        raw_message = record['Sns']['Message']
        subject = record['Sns']['Subject']
        logger.structure_logs(append=True, sns_message_length=str(len(raw_message)))
        logger.info("Analyzing the received message.")

        try:
            decoded_message = json.loads(raw_message)
        except json.decoder.JSONDecodeError:
            decoded_message = None
        logger.structure_logs(append=True, sns_message_type=type(decoded_message).__name__)

        if isinstance(decoded_message, dict):
            # CloudWatch Alarm
            if 'AlarmName' in decoded_message:
                new_state = decoded_message['NewStateValue']
                # OK
                if new_state == "OK":
                    decoded_message['NewStateReason'] = '*正常* になりました。'
                # NG
                else:
                    decoded_message['NewStateReason'] = decoded_message['AlarmDescription']
            payload = decoded_message
        else:
            # AWS Budgets sends a plain text notification, which Chatbot cannot render.
            payload = createCustomNotification(subject, raw_message)

        request = {
            'TopicArn': os.environ['SNS_TOPIC_ARN'],
            'Message': json.dumps(payload)
        }
        if subject is not None:
            request['Subject'] = subject
        logger.structure_logs(append=True, sns_message_body=payload)
        logger.info("Transfered a message to a SNS topic.")
        sns.publish(**request)
