Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-route53-resolver(en)

cloudwatch-alarm-about-route53-resolver creates Amazon CloudWatch Alarm about Route 53 Resolver.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | EndpointId | Threshold |
| --- | --- | --- | --- |
| AWS/Route53Resolver | **EndpointUnhealthyENICount** | `EndpointId` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `EndpointId` | String | | ○ | The endpoint ID |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-route53-resolver(ja)

cloudwatch-alarm-about-route53-resolver は、Route 53 Resolver に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | エンドポイント ID | 閾値 |
| --- | --- | --- | --- |
| AWS/Route53Resolver | **EndpointUnhealthyENICount** | `EndpointId` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `EndpointId` | String | | ○ | エンドポイント ID |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |