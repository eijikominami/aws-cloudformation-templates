Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-ec2(en)

cloudwatch-alarm-about-ec2 creates Amazon CloudWatch Alarm about Amazon EC2.

## CloudWatch Alarm

The template provide the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/EC2 | **StatusCheckFailed** | At least once a minute | 
| AWS/EC2 | **CPUUtilization** | `CPUUtilizationThreshold` | 

## Parameters

You can give optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CPUUtilizationThreshold` | Number | 100 | ○ | |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |

---------------------------------------

# cloudwatch-alarm-about-ec2(ja)

cloudwatch-alarm-about-apigateway は、Amazon EC2 に関する Amazon CloudWatch アラームを作成します。

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
| `CPUUtilizationThreshold` | Number | 100 | ○ | |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |