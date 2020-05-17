Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# eventbridge-rules (en)

``eventbridge-rules`` creates **Amazon EventBridge Events rules** for [supported AWS Services](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-types.html). This template covers the following events.

| Events | Source | Detail Type |
| --- | --- | --- |
| Amazon EventBridge Scheduled Events | aws.events | Scheduled Event |
| Amazon EBS Events | aws.ec2 | EBS Volume Notification |
| Amazon EBS Events | aws.ec2 | EBS Snapshot Notification |
| Amazon EBS Events | aws.ec2 | EBS Multi-Volume Snapshots Completion Status |
| Amazon EBS Events | aws.ec2 | EBS Fast Snapshot Restore State-change Notification |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance-launch Lifecycle Action  |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance Launch Successful  |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance Launch Unsuccessful  |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance-terminate Lifecycle Action |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance Terminate Successful  |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance Terminate Unsuccessful |
| Amazon EC2 State Change Events | aws.ec2 | EC2 Instance State-change Notification |
| AWS KMS Events | aws.kms | KMS CMK Rotations |
| AWS KMS Events | aws.kms | KMS Imported Key Material Expiration |
| AWS KMS Events | aws.kms | KMS CMK Deletion |
| AWS Management Console Sign-in Events | aws.signin | AWS Console Sign In via CloudTrail |
| Tag Change Events on AWS Resources | aws.tag | Tag Change on Resource |
| AWS Trusted Advisor Events | aws.trustedadvisor | Trusted Advisor Check Item Refresh Notification |

These events are transfered to the **Amazon SNS topic** set by the ``SNSForAlertArn`` input parameter.

---------------------------------------

# eventbridge-rules (ja)

``eventbridge-rules`` は [サポート対象のAWS サービス](https://docs.aws.amazon.com/ja_jp/eventbridge/latest/userguide/event-types.html) に関する **EventBridge イベントルール** を作成します。このテンプレートは、以下のイベントに対応しています。

| イベント | ソース | 詳細タイプ |
| --- | --- | --- |
| Amazon EventBridge Scheduled Events | aws.events | Scheduled Event |
| Amazon EBS Events | aws.ec2 | EBS Volume Notification |
| Amazon EBS Events | aws.ec2 | EBS Snapshot Notification |
| Amazon EBS Events | aws.ec2 | EBS Multi-Volume Snapshots Completion Status |
| Amazon EBS Events | aws.ec2 | EBS Fast Snapshot Restore State-change Notification |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance-launch Lifecycle Action  |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance Launch Successful  |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance Launch Unsuccessful  |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance-terminate Lifecycle Action |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance Terminate Successful  |
| Amazon EC2 Auto Scaling Events | aws.autoscaling | EC2 Instance Terminate Unsuccessful |
| Amazon EC2 State Change Events | aws.ec2 | EC2 Instance State-change Notification |
| AWS KMS Events | aws.kms | KMS CMK Rotations |
| AWS KMS Events | aws.kms | KMS Imported Key Material Expiration |
| AWS KMS Events | aws.kms | KMS CMK Deletion |
| AWS Management Console Sign-in Events | aws.signin | AWS Console Sign In via CloudTrail |
| Tag Change Events on AWS Resources | aws.tag | Tag Change on Resource |
| AWS Trusted Advisor Events | aws.trustedadvisor | Trusted Advisor Check Item Refresh Notification |

これらのイベントは、入力パラメータ ``SNSForAlertArn`` で指定した **Amazon SNS トピック** に転送されます。