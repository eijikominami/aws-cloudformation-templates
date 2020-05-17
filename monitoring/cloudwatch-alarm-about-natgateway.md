Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-natgateway(en)

cloudwatch-alarm-about-natgateway creates Amazon CloudWatch Alarm about NAT Gateway.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/NATGateway | **PacketsDropCount** | At least once a minute |
| AWS/NATGateway | **ErrorPortAllocation** | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |

# cloudwatch-alarm-about-natgateway(ja)

cloudwatch-alarm-about-apigateway は、NAT Gateway に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/NATGateway | **PacketsDropCount** | 1分間に1回以上 |
| AWS/NATGateway | **ErrorPortAllocation** | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |