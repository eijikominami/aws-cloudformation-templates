Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-transitgateway(en)

cloudwatch-alarm-about-transitgateway creates Amazon CloudWatch Alarm about AWS Transit Gateway.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | TopicName | Threshold |
| --- | --- | --- |
| AWS/TransitGateway | **PacketDropCountNoRoute** | `TransitGateway` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `TransitGateway` | String | | ○ | The id of the Transit Gateway |

---------------------------------------

# cloudwatch-alarm-about-transitgateway(ja)

cloudwatch-alarm-about-transitgateway は、AWS Transit Gateway に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TopicName | 閾値 |
| --- | --- | --- |
| AWS/TransitGateway | **PacketDropCountNoRoute** | `TransitGateway` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `TransitGateway` | String | | ○ | Transit Gateway の ID |