Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-ec2(en)

cloudwatch-alarm-about-ec2 creates Amazon CloudWatch Alarm about Amazon EC2.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/EC2 | **StatusCheckFailed** | At least once a minute | 
| AWS/EC2 | **CPUUtilization** | `CPUUtilizationThreshold` | 

## Parameters

You can give optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CPUUtilizationThreshold` | Number | 100 | ○ | The threshold of CPU Utilization |
| `CustomAlarmName` | String | | | The custom alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-ec2(ja)

cloudwatch-alarm-about-ec2 は、Amazon EC2 に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/EC2 | **StatusCheckFailed** | 1分間に1回以上 | 
| AWS/EC2 | **CPUUtilization** | `CPUUtilizationThreshold` | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CPUUtilizationThreshold` | Number | 100 | ○ | CPU使用率の閾値 |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |