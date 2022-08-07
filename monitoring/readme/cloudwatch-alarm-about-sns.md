Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-sns(en)

cloudwatch-alarm-about-sns creates Amazon CloudWatch Alarm about Amazon SNS.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | TopicName | Threshold |
| --- | --- | --- |
| AWS/SNS | **NumberOfNotificationsFailed** | `SNSTopicName` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `SNSTopicName` | String | | ○ | The SNS topic name |

---------------------------------------

# cloudwatch-alarm-about-sns(ja)

cloudwatch-alarm-about-sns は、Amazon SNS に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TopicName | 閾値 |
| --- | --- | --- |
| AWS/SNS | **NumberOfNotificationsFailed** | `SNSTopicName` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `SNSTopicName` | String | | ○ | SNSトピック名 |