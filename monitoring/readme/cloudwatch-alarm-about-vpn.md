Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-vpn(en)

cloudwatch-alarm-about-vpn creates Amazon CloudWatch Alarm about AWS Site-to-Site VPN.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | VPNId | Threshold |
| --- | --- | --- |
| AWS/VPN | **TunnelState** | `VpnId` | 0 |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `VpnId` | String | | ○ | The VPN ID |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-vpn(ja)

cloudwatch-alarm-about-vpn は、Amazon Site-to-Site VPN に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | VPN ID | 閾値 |
| --- | --- | --- |
| AWS/VPN | **TunnelState** | `VpnId` | 0 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `VpnId` | String | | ○ | VPN ID |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |