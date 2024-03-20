Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-appstream(en)

cloudwatch-alarm-about-appstream creates Amazon CloudWatch Alarm about Amazon AppStream.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Fleet | Threshold |
| --- | --- | --- |
| AWS/AppStream | **InsufficientConcurrencyLimitError** | `Fleet` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `Fleet` | String | | ○ | The name of the AppStream Fleet |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

---------------------------------------

# cloudwatch-alarm-about-appstream(ja)

cloudwatch-alarm-about-appstream は、Amazon AppStream アタッチメントに関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Fleet 名 | 閾値 |
| --- | --- | --- |
| AWS/AppStream | **InsufficientConcurrencyLimitError** | `Fleet` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `Fleet` | String | | ○ | AppSream Fleet 名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |