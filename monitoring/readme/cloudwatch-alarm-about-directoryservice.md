Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-directoryservice(en)

cloudwatch-alarm-about-directoryservice creates Amazon CloudWatch Alarm about AWS Directory Service.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Directory Id | Domain Controller IP | Metric Category | Threshold |
| --- | --- | --- | --- | --- | --- |
| AWS/DirectoryService | **Recursive Query Failure/sec** | `DirectoryId` | `DomainControllerIp` | DNS | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `DirectoryId` | String | | ○ | The id of the directory |
| `DomainControllerIp` | String | | ○ | The IP of the domain controller |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-directoryservice(ja)

cloudwatch-alarm-about-directoryservice は、AWS Directory Service に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ディレクトリ ID | ドメインコントローラ IP | メトリックカテゴリ | 閾値 |
| --- | --- | --- | --- | --- | --- |
| AWS/DirectoryService | **Recursive Query Failure/sec** | `DirectoryId` | `DomainControllerIp` | DNS | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `DirectoryId` | String | | ○ | ディレクトリの ID |
| `DomainControllerIp` | String | | ○ | ドメインコントローラの IP |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |