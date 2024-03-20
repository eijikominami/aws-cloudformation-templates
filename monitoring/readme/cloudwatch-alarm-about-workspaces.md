Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-workspaces(en)

cloudwatch-alarm-about-workspaces creates Amazon CloudWatch Alarm about Amazon Workspaces.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | DirectoryId | Threshold |
| --- | --- | --- |
| AWS/WorkSpaces | **Unhealthy** | `DirectoryId` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `DirectoryId` | String | | ○ | The id of the Workspaces directory |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

---------------------------------------

# cloudwatch-alarm-about-workspaces(ja)

cloudwatch-alarm-about-workspaces は、Amazon Workspaces アタッチメントに関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ディレクトリ ID | 閾値 |
| --- | --- | --- |
| AWS/WorkSpaces | **Unhealthy** | `DirectoryId` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `DirectoryId` | String | | ○ | Workspaces ディレクトリ ID |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |