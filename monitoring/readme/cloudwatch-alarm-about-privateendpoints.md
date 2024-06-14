Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-privateendpoints(en)

cloudwatch-alarm-about-privateendpoints creates Amazon CloudWatch Alarm about VPC endpoint.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | VPCId | VPCEndpointId | EndpointType | ServiceName | Threshold |
| --- | --- | --- | --- | --- | --- | --- |
| AWS/PrivateLinkEndpoints | **PacketsDropped** | `VPCId` | `VPCEndpointId` | `EndpointType` | `ServiceName` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `EndpointType` | String | | ○ | The type of endpoint | 
| `ServiceName` | String | | ○ | The service name | 
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `VPCEndpointId` | String | | ○ | The id of the endpoint | 
| `VPCId` | String | | ○ | The VPC id | 
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-privateendpoints(ja)

cloudwatch-alarm-about-privateendpoints は、VPC エンドポイントに関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | VPC ID | VPC エンドポイント ID | エンドポイントタイプ | サービス名 | 閾値 |
| --- | --- | --- | --- | --- | --- | --- |
| AWS/PrivateLinkEndpoints | **PacketsDropped** | `VPCId` | `VPCEndpointId` | `EndpointType` | `ServiceName`  | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `EndpointType` | String | | ○ | エンドポイントタイプ | 
| `ServiceName` | String | | ○ | サービス名 | 
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `VPCEndpointId` | String | | ○ | エンドポイント ID | 
| `VPCId` | String | | ○ | VPC ID | 
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |