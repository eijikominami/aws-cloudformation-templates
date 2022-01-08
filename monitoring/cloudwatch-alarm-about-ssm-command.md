Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-ssm(en)

cloudwatch-alarm-about-ssm creates Amazon AWS Systems Manager Run Command.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- | --- | --- |
| AWS/SSM-RunCommand | `CommandsDeliveryTimedOut` | At least once a minute | 
| AWS/SSM-RunCommand | `CommandsFailed` | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |

---------------------------------------

# cloudwatch-alarm-about-ssm(ja)

cloudwatch-alarm-about-ssm は、 Amazon AWS Systems Manager Run Command に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/SSM-RunCommand | `CommandsDeliveryTimedOut` | 1分間に1回以上 | 
| AWS/SSM-RunCommand | `CommandsFailed` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |