Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-acm(en)

cloudwatch-alarm-about-acm creates Amazon CloudWatch Alarm about Certificate Manager.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/CertificateManager | **DaysToExpiry** | =<30 |
| AWS/CertificateManager | **DaysToExpiry** | =<7 |
| AWS/CertificateManager | **DaysToExpiry** | =<1 |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `CertificateArn` | String | | ○ | The Certificate ARN |

---------------------------------------

# cloudwatch-alarm-about-natgateway(ja)

cloudwatch-alarm-about-acm は、Certificate Manager に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/CertificateManager | **DaysToExpiry** | =<30 |
| AWS/CertificateManager | **DaysToExpiry** | =<7 |
| AWS/CertificateManager | **DaysToExpiry** | =<1 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `CertificateArn` | String | | ○ | 証明書の ARN |