Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-amplify(en)

cloudwatch-alarm-about-amplify creates Amazon CloudWatch Alarm about Amplify.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | AppId | Threshold |
| --- | --- | --- | --- |
| AWS/AmplifyHosting | **5xxErrors** | `AppId` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AppId` | String | | ○ | The app id |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-amplify(ja)

cloudwatch-alarm-about-amplify は、Amplify に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | AppID | 閾値 |
| --- | --- | --- | --- |
| AWS/AmplifyHosting | **5xxErrors** | `AppId` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AppId` | String | | ○ | アプリ ID |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |