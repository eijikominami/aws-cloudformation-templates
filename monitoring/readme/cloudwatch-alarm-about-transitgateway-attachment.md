Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-transitgateway-attachment(en)

cloudwatch-alarm-about-transitgateway creates Amazon CloudWatch Alarm about AWS Transit Gateway attachements.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | TransitGateway | TransitGateway attachment | Threshold |
| --- | --- | --- |
| AWS/TransitGateway | **PacketDropCountNoRoute** | `TransitGatewayId` | `TransitGatewayAttachmentId` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `TransitGatewayId` | String | | ○ | The id of the Transit Gateway |
| `TransitGatewayAttachmentId` | String | | ○ | The id of the Transit Gateway attachment |

---------------------------------------

# cloudwatch-alarm-about-transitgateway-attachment(ja)

cloudwatch-alarm-about-transitgateway は、AWS Transit Gateway アタッチメントに関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TransitGateway | TransitGateway アタッチメント | 閾値 |
| --- | --- | --- |
| AWS/TransitGateway | **PacketDropCountNoRoute** | `TransitGatewayId` | `TransitGatewayAttachmentId` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `TransitGatewayId` | String | | ○ | Transit Gateway の ID |
| `TransitGatewayAttachmentId` | String | | ○ | Transit Gateway アタッチメントの ID |