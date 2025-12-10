Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-glue(en)

cloudwatch-alarm-about-glue creates Amazon CloudWatch Alarm about AWS Glue.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | JobName | JobRunId | Type | Threshold |
| --- | --- | --- | --- | --- | --- |
| Glue | **glue.driver.aggregate.numFailedTasks** | `JobName` | ALL | count | At least once in 5 minutes |
| Glue | **glue.driver.aggregate.elapsedTime** | `JobName` | ALL | gauge | `TimeoutMilliseconds` |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom alarm name |
| `JobName` | String | | ○ | The name of the Glue job |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `TimeoutMilliseconds` | Integer | 3300000 | ○ | The threshold of job execution time in milliseconds |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-glue(ja)

cloudwatch-alarm-about-glue は、AWS Glue に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | JobName | JobRunId | Type | 閾値 |
| --- | --- | --- | --- | --- | --- |
| Glue | **glue.driver.aggregate.numFailedTasks** | `JobName` | ALL | count | 5分間に1回以上 |
| Glue | **glue.driver.aggregate.elapsedTime** | `JobName` | ALL | gauge | `TimeoutMilliseconds` |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `JobName` | String | | ○ | Glue ジョブの名前 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `TimeoutMilliseconds` | Integer | 3300000 | ○ | ジョブ実行時間の閾値（ミリ秒） |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |
