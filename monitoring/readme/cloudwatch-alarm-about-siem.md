Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-siem(en)

cloudwatch-alarm-about-siem creates Amazon CloudWatch Alarm about SIEM on Amazon OpenSearch Service.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Dimensions | Threshold |
| --- | --- | --- | --- |
| SIEM | **ErrorLogLoadCount** | Summed over every `logtype` | `ErrorLogLoadCountThreshold` |
| SIEM | **SuccessLogLoadCount** | Summed over every `logtype` | <1 |
| AWS/Lambda | **Throttles** | `EsLoaderFunctionName` | At least once an hour |

**ErrorLogLoadCount** catches logs that es-loader read but OpenSearch Service rejected, which a Lambda error metric never reports. The usual causes are the index field limit, a mapping mismatch, and a missing S3 read permission.

**SuccessLogLoadCount** is the silence detector, so it treats missing data as breaching. Leave it `DISABLED` where log delivery is intermittent by nature.

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `EsLoaderFunctionName` | String | aes-siem-es-loader | ○ | The name of the es-loader function |
| `ErrorLogLoadCountPeriod` | Number | 3600 | ○ | The number of seconds over which failed log loads are summed |
| `ErrorLogLoadCountThreshold` | Number | 1 | ○ | The number of failed log loads that is treated as a failure |
| `NoLogLoadAlarm` | ENABLED/DISABLED | DISABLED | | Whether an alarm is raised while no log reaches OpenSearch Service |
| `NoLogLoadPeriod` | Number | 10800 | ○ | The number of seconds without any loaded log that is treated as a failure |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-siem(ja)

cloudwatch-alarm-about-siem は、 SIEM on Amazon OpenSearch Service に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ディメンション | 閾値 |
| --- | --- | --- | --- |
| SIEM | **ErrorLogLoadCount** | すべての `logtype` の合計 | `ErrorLogLoadCountThreshold` |
| SIEM | **SuccessLogLoadCount** | すべての `logtype` の合計 | <1 |
| AWS/Lambda | **Throttles** | `EsLoaderFunctionName` | 1時間に1回以上 |

**ErrorLogLoadCount** は、es-loader が読み込んだものの OpenSearch Service が拒否したログを検知します。Lambda のエラーメトリクスには現れません。インデックスのフィールド数上限、マッピングの不一致、S3 からの読み取り権限不足が主な原因です。

**SuccessLogLoadCount** は無音検知のため、データなしを異常として扱います。ログの到着が本質的に断続的な環境では `DISABLED` のままにしてください。

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `EsLoaderFunctionName` | String | aes-siem-es-loader | ○ | es-loader 関数の名前 |
| `ErrorLogLoadCountPeriod` | Number | 3600 | ○ | 取り込み失敗を合計する秒数 |
| `ErrorLogLoadCountThreshold` | Number | 1 | ○ | 異常と判定する取り込み失敗件数 |
| `NoLogLoadAlarm` | ENABLED/DISABLED | DISABLED | | ログが取り込まれていないときにアラームを発報するか |
| `NoLogLoadPeriod` | Number | 10800 | ○ | 異常と判定する無音の秒数 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグのキー |
| `TagValue` | String | aws-cloudformation-templates | | タグの値 |
