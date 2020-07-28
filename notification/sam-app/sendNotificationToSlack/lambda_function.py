import boto3
import json
import logging
import os
import sys
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# X-Ray
xray_recorder.configure()
patch_all()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):

    logger.info("Event: " + str(event))
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
        logger.info("Message: " + str(message) + " Type:" + type(message).__name__ + " Length:" + str(len(message)))
        if isinstance(message, dict):
            # CloudWatch Alarm
            if 'AlarmName' in message:
                hook_url = "https://" + ALERT_HOOK_URL
                slack_message = createCloudWatchAlarmMessage(message)
            # Scheduled Event
            elif 'source' in message and 'aws.events' in message['source']:  
                hook_url = "https://" + ALERT_HOOK_URL
                slack_message = createScheduledEventMessage(message)    
            # EC2
            # EBS  
            elif 'source' in message and 'aws.ec2' in message['source']:  
                hook_url = "https://" + ALERT_HOOK_URL
                slack_message = createEC2Message(message)  
            # AutoScaling   
            elif 'source' in message and 'aws.autoscaling' in message['source']:  
                hook_url = "https://" + ALERT_HOOK_URL
                slack_message = createAutoScalingMessage(message)   
            # KMS
            elif 'source' in message and 'aws.kms' in message['source']:  
                hook_url = "https://" + ALERT_HOOK_URL
                slack_message = createKMSMessage(message) 
            # Sign-in
            elif 'source' in message and 'aws.signin' in message['source']:  
                hook_url = "https://" + ALERT_HOOK_URL
                slack_message = createManagementConsoleMessage(message)     
            # Tag
            elif 'source' in message and 'aws.tag' in message['source']:  
                hook_url = "https://" + ALERT_HOOK_URL
                slack_message = createTagMessage(message)          
            # TrustedAdvisor
            elif 'source' in message and 'aws.trustedadvisor' in message['source']:  
                hook_url = "https://" + ALERT_HOOK_URL
                slack_message = createTrustedAdvisorMessage(message)      
            # IAM Access Analyzer
            elif 'source' in message and 'aws.access-analyzer' in message['source']:  
                hook_url = "https://" + ALERT_HOOK_URL
                slack_message = createIAMAccessAnalyzer(message)
            # Amplify Console
            elif 'source' in message and 'aws.amplify' in message['source']:  
                hook_url = "https://" + DEPLOYMENT_HOOK_URL
                slack_message = createAmplifyMessage(message)
            else:
                hook_url = None
                slack_message = None                           
    except json.decoder.JSONDecodeError as e:
        logger.error("JSON decode error: %s at %s.", e.msg, sys._getframe().f_code.co_name)
    # Sends Slack
    sendMessage(hook_url, slack_message)

@xray_recorder.capture('createCloudWatchAlarmMessage')
def createCloudWatchAlarmMessage(message):

    alarm_name = message['AlarmName']
    new_state = message['NewStateValue']
    title_suffix = "CloudWatch Alarm | " + message['Region'] + " | Account: " + message['AWSAccountId']

    # OK
    if new_state == "OK":
        alarm_description = "エラーから *回復* しました。"
        reason = "なし"
        title_prefix = ":white_check_mark: 正常復帰イベント"
        color = "#49C39E"
    # NG
    else: 
        alarm_description = message['AlarmDescription']
        reason = message['NewStateReason']
        if alarm_name.startswith('Warning'):
            title_prefix = ":x: 警告イベント"
            color = "#961D13"
        elif alarm_name.startswith('Notice'):
            title_prefix = ":x: 注意イベント"
            color = "#EBB424"
        else:
            title_prefix = ":japanese_ogre: 不明なイベント"
            color = "#EBB424"
    return {
        'attachments': [{
            'color': color,
            'title': "%s | %s" % (title_prefix, title_suffix),
            'text': "%s" % (alarm_description),
            'fields': [
                    {
                        'title': "Alarm Name",
                        'value': "%s" % (alarm_name)
                    },
                    {
                        'title': "Cause",
                        'value': "%s" % (reason)
                    }
                ]
        }]
    }

@xray_recorder.capture('createScheduledEventMessage')
def createScheduledEventMessage(message):

    resources = ''
    
    for resource in message['resources']:
        resources = resources + ' ' + resource
    return {
        'attachments': [{
            'color': '#ca792d',
            'title': ':alarm_clock: Amazon EventBridge Scheduled Events | %s | Account: %s' % (message['region'], message['account']),
            'title_link': 'https://console.aws.amazon.com/cloudwatch/home?region=%s#rules:' % message['region'],
            'text': '*スケジュールされたイベント* が *実行* されました。',
            'fields': [
                    {
                        'title': "Resources",
                        'value': "%s" % resources
                    }
                ]
        }]
    }

@xray_recorder.capture('createEC2Message')
def createEC2Message(message):

    color = "#e38b33"
    title = "Amazon EC2/EBS Events | " + message['region'] + " | Account: " + message['account']
    title_link = "https://console.aws.amazon.com/ec2/home?region=" + message['region'] + "#Home:"
    detail = "なし"
    resources = ''    
    
    for resource in message['resources']:
        resources = resources + ' ' + resource
    # EBS Volume Notification
    if message['detail-type'] == 'EBS Volume Notification':
        if message['detail']['result'] == "failed":
            icon = ':x:'
            text = '*EBSボリューム* で *' + message['detail']['event'] + "* が失敗しました。"
            color = "#961D13"
            detail = message['detail']['cause']
        else:
            icon = ':floppy_disk:'
            text = '*EBSボリューム* で *' + message['detail']['event'] + "* が成功しました。"
    # EBS Snapshot Notification
    # EBS Multi-Volume Snapshots Completion Status
    elif message['detail-type'] == 'EBS Snapshot Notification' or message['detail-type'] == 'EBS Multi-Volume Snapshots Completion Status':
        if message['detail']['result'] == "failed":
            icon = ':x:'
            text = '*EBSスナップショット* で *' + message['detail']['event'] + "* が失敗しました。"
            color = "#961D13"
            detail = message['detail']['cause']
        else:
            icon = ':floppy_disk:'
            text = '*EBSスナップショット* で *' + message['detail']['event'] + "* が成功しました。"
    # EBS Fast Snapshot Restore State-change Notification
    elif message['detail-type'] == 'EBS Fast Snapshot Restore State-change Notification':
        icon = ':floppy_disk:'
        text = '*EBS高速スナップショット復元イベント* の状態が *' + message['detail']['state'] + '* になりました。'
        detail = message['detail']['message']
    # EC2 Instance State-change Notification
    elif message['detail-type'] == 'EC2 Instance State-change Notification':
        icon = ':computer:'
        text = '*EC2インスタンス* の *状態変更* を検知しました。'
        detail = message['detail']['state']
    return {
        'attachments': [{
            'color': "%s" % color,
            'title': "%s %s" % (icon, title),
            'title_link': "%s" % title_link,
            'text': "%s" % text,
            'fields': [
                    {
                        'title': "Resources",
                        'value': "%s" % resources
                    },
                    {
                        'title': "Message",
                        'value': "%s" % detail
                    }
                ]
        }]
    }

@xray_recorder.capture('createAutoScalingMessage')
def createAutoScalingMessage(message):

    color = "#e38b33"
    title = "Amazon EC2 Auto Scaling Events | " + message['region'] + " | Account: " + message['account']
    title_link = "https://console.aws.amazon.com/ec2/autoscaling/home?region=" + message['region'] + "#LaunchConfigurations:"
    detail = "なし"
    resources = ''

    for resource in message['resources']:
        resources = resources + ' ' + resource
    # EC2 Instance-launch Lifecycle Action
    if message['detail-type'] == 'EC2 Instance-launch Lifecycle Action':
        icon = ':arrow_up_down:'
        text = '*AutoScaling 起動アクション* を検知しました。'
        detail = message['detail']['LifecycleTransition']
    # EC2 Instance Launch Successful
    elif message['detail-type'] == 'EC2 Instance Launch Successful':
        icon = ':arrow_up_down:'
        text = '*EC2インスタンスの起動* に *成功* しました。'
    # EC2 Instance Launch Unsuccessful
    elif message['detail-type'] == 'EC2 Instance Launch Unsuccessful':
        icon = ':x:'
        text = '*EC2インスタンスの起動* に *失敗* しました。'
        detail = message['detail']['Cause']
        color = "#961D13"
    # EC2 Instance-terminate Lifecycle Action
    elif message['detail-type'] == 'EC2 Instance-terminate Lifecycle Action':
        icon = ':arrow_up_down:'
        text = '*AutoScaling 終了アクション* を検知しました。'
        detail = message['detail']['LifecycleTransition']
    # EC2 Instance Terminate Successful
    elif message['detail-type'] == 'EC2 Instance Terminate Successful':
        icon = ':arrow_up_down:'
        text = '*EC2インスタンスの削除* に *成功* しました。'
        detail = message['detail']['Cause']
    # EC2 Instance Terminate Unsuccessful
    elif message['detail-type'] == 'EC2 Instance Terminate Unsuccessful':
        icon = ':x:'
        text = '*EC2インスタンスの削除* に * 失敗* しました。'
        detail = message['detail']['Cause']
        color = "#961D13"
    return {
        'attachments': [{
            'color': "%s" % color,
            'title': "%s %s" % (icon, title),
            'title_link': "%s" % title_link,
            'text': "%s" % text,
            'fields': [
                    {
                        'title': "Resources",
                        'value': "%s" % resources
                    },
                    {
                        'title': "Message",
                        'value': "%s" % detail
                    }
                ]
        }]
    }

@xray_recorder.capture('createKMSMessage')
def createKMSMessage(message):

    color = "#dd4e4b"
    title = "AWS KMS Events | " + message['region'] + " | Account: " + message['account']
    title_link = "https://console.aws.amazon.com/kms/home?region=" + message['region'] + "#/kms/keys"
    detail = 'key-id: ' + message['detail']['key-id']
    resources = ''
    
    for resource in message['resources']:
        resources = resources + ' ' + resource
    # KMS CMK Rotation
    if message['detail-type'] == 'KMS CMK Rotation':
        text = '*KMS* で *CMK が ローテーション* されました。'
    # KMS Imported Key Material Expiration
    elif message['detail-type'] == 'KMS Imported Key Material Expiration':
        text = '*KMS* で *インポートされたキーが失効* しました。'
    # KMS Imported Key Material Expiration
    elif message['detail-type'] == 'KMS CMK Deletion':
        text = '*KMS* で *CMK が 削除* されました。'
    return {
        'attachments': [{
            'color': "%s" % color,
            'title': ":key: %s" % title,
            'title_link': "%s" % title_link,
            'text': "%s" % text,
            'fields': [
                    {
                        'title': "Resources",
                        'value': "%s" % resources
                    },
                    {
                        'title': "Message",
                        'value': "%s" % detail
                    }
                ]
        }]
    }

@xray_recorder.capture('createManagementConsoleMessage')
def createManagementConsoleMessage(message):

    resources = ''
    title = ":id: AWS Management Console Sign-in Events | " + message['region'] + " | Account: " + message['account']
    title_link = "https://console.aws.amazon.com/cloudtrail/home?region=" + message['region'] + "#/dashboard"
    if message['detail']['userIdentity']['type'] == 'IAMUser':
        user =  message['detail']['userIdentity']['userName']
    elif message['detail']['userIdentity']['type'] == 'AssumedRole':
        user = message['detail']['userIdentity']['principalId']
    elif message['detail']['userIdentity']['type'] == 'Root':
        user = 'ルートユーザ'
    else:
        user = '不明なユーザ'
    
    for resource in message['resources']:
        resources = resources + ' ' + resource
    return {
        'attachments': [{
            'color': '#dc4f7e',
            'title': "%s" % title,
            'title_link': "%s" % title_link,
            'text': "*ログインイベントを検知* しました。",
            'fields': [
                    {
                        'title': "Message",
                        'value': "%s が %s からログインしました。" % (user, message['detail']['sourceIPAddress'])
                    }
                ]
        }]
    }

@xray_recorder.capture('createTagMessage')
def createTagMessage(message):

    resources = ''
    title = ":pencil: Tag Change Events | " + message['region'] + " | Account: " + message['account']
    title_link = "https://console.aws.amazon.com/resource-groups/tag-editor/find-resources?region=" + message['region']
    
    for resource in message['resources']:
        resources = resources + ' ' + resource
    return {
        'attachments': [{
            'color': '#dc4f7e',
            'title': "%s" % title,
            'title_link': "%s" % title_link,
            'text': "*タグが変更* されました。",
            'fields': [
                    {
                        'title': "Resources",
                        'value': "%s" % resources
                    }
                ]
        }]
    }

@xray_recorder.capture('createTrustedAdvisorMessage')
def createTrustedAdvisorMessage(message):

    resources = ''
    title = ":heavy_check_mark: AWS Trusted Advisor Events | " + message['region'] + " | Account: " + message['account']
    title_link = "https://console.aws.amazon.com/trustedadvisor/home?region=" + message['region'] + "#/dashboard"
    
    for resource in message['resources']:
        resources = resources + ' ' + resource
    return {
        'attachments': [{
            'color': '#dc4f7e',
            'title': "%s" % title,
            'title_link': "%s" % title_link,
            'text': "*TrustedAdvisor* が項目を検知しました。",
            'fields': [
                    {
                        'title': "Item",
                        'value': "%s" % message['detail']['check-name']
                    },
                    {
                        'title': "Status",
                        'value': "%s" % message['detail']['status']
                    }
                ]
        }]
    }

@xray_recorder.capture('createIAMAccessAnalyzer')
def createIAMAccessAnalyzer(message):

    title = ":heavy_exclamation_mark: IAM Access Analyzer Findings | " + message['region'] + " | Account: " + message['account']
    title_link = "https://console.aws.amazon.com/resource-groups/access-analyzer/home?region=" + message['region']

    return {
        'attachments': [{
            'color': '#961D13',
            'title': "%s" % title,
            'title_link': "%s" % title_link,
            'text': "*IAM Access Analyzer* が %s に対する *%s* 権限を検知しました。 *意図していない権限の場合は、潜在的なセキュリティリスクが存在するため、この権限を許可するポリシーを変更または削除してください* 。ビジネスプロセスに必要なアクセスなど、アクセスが意図している場合は、結果をアーカイブできます。" % (message['detail']['resource'], str(message['detail']['action'])),
            'fields': [
                    {
                        'title': "Principal",
                        'value': "%s" % str(message['detail']['principal'])
                    },
                    {
                        'title': "Actions",
                        'value': "%s" % str(message['detail']['action'])
                    },
                    {
                        'title': "Resource",
                        'value': "%s" % message['detail']['resource']
                    },
                ]
        }]
    }

@xray_recorder.capture('createAmplifyMessages')
def createAmplifyMessage(message):
    if message['detail']['jobStatus'] == 'STARTED':
        text = ":information_source: Amplify Console のデプロイが開始されました 。"
        color = "#888888"
    elif message['detail']['jobStatus'] == 'FAILED':
        text = ":x: Amplify Console のデプロイが失敗しました 。"
        color = "#961D13"
    elif message['detail']['jobStatus'] == 'SUCCEED':
        text = ":white_check_mark: Amplify Console のデプロイが成功しました 。"
        color = "#49C39E"
    return {
        'attachments': [{
            'color': color,
            'title': text,
            'fields': [
                    {
                        'title': "AppId",
                        'value': "%s" % (message['detail']['appId'])
                    },
                    {
                        'title': "BranchName",
                        'value': "%s" % (message['detail']['branchName'])
                    },
                    {
                        'title': "JobId",
                        'value': "%s" % (message['detail']['jobId'])
                    }
                ]
        }]
    }

@xray_recorder.capture('sendMessage')
def sendMessage(hook_url, message):
    if hook_url is None or message is None:
        logger.warning("Hook url or message is empty at %s.", sys._getframe().f_code.co_name)
        return False
    else:
        req = Request(hook_url, json.dumps(message).encode('utf-8'))
        try:
            logger.info("Message posted to %s at %s.", hook_url, sys._getframe().f_code.co_name)
            response = urlopen(req)
            response.read()
            return True
        except HTTPError as e:
            logger.error("Request failed: %d %s at %s.", e.code, e.reason, sys._getframe().f_code.co_name)
            return False
        except URLError as e:
            logger.error("Server connection failed: %s at %s.", e.reason, sys._getframe().f_code.co_name)
            return False   