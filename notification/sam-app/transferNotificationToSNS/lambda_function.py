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

@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):

    sns = boto3.client('sns')
    for record in event['Records']:
        
        try:
            message = json.loads(record['Sns']['Message'])
            logger.structure_logs(append=True, sns_message_body=message)
            logger.structure_logs(append=True, sns_message_type=type(message).__name__)
            logger.structure_logs(append=True, sns_message_length=str(len(message)))
            logger.info("Analyzing the received message.")
            
            try:
                decoded_message = json.loads(record['Sns']['Message'])
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
                
                if record['Sns']['Subject'] is None:
                    request = {
                        'TopicArn': os.environ['SNS_TOPIC_ARN'],
                        'Message': json.dumps(decoded_message)
                    }
                else:
                    request = {
                        'TopicArn': os.environ['SNS_TOPIC_ARN'],
                        'Message': json.dumps(decoded_message),
                        'Subject': record['Sns']['Subject']
                    }
                logger.structure_logs(append=True, sns_message_body=decoded_message)
                logger.info("Transfered a message to a SNS topic.")          
                sns.publish(**request)
            except json.decoder.JSONDecodeError:
                logger.info("Message is NOT a JSON format.")
        except json.decoder.JSONDecodeError:
            logger.info("Message is NOT a JSON format.")