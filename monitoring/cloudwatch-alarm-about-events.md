Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-events(en)

cloudwatch-alarm-about-events creates Amazon CloudWatch Alarm about Amazon EventBridge.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | RuleName | Threshold |
| --- | --- | --- | --- |
| AWS/Events | **StatusCheckFailed** | `FailedInvocations` | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `EventsRuleName` | String | | ○ | |
| `SNSTopicArn` | String | | ○ | |

---------------------------------------

# cloudwatch-alarm-about-events(ja)

cloudwatch-alarm-about-apigateway は、Amazon EventBridge に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | RuleName | 閾値 |
| --- | --- | --- | --- |
| AWS/Events | **StatusCheckFailed** | `FailedInvocations` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `EventsRuleName` | String | | ○ | |
| `SNSTopicArn` | String | | ○ | |