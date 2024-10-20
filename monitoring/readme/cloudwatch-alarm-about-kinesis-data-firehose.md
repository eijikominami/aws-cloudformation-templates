Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-kinesis-data-firehose(en)

cloudwatch-alarm-about-kinesis-data-firehose creates Amazon CloudWatch Alarm about Amazon Kinesis Data Firehose.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | DeliveryStreamName | Threshold |
| --- | --- | --- | --- |
| AWS/Firehose | **DeliveryToElasticsearch.DataFreshness** | `FirehoseStreamName` | `OldestRecordAge` |
| AWS/Firehose | **ThrottledGetShardIterator** | `FirehoseStreamName` | At least once a minute | 
| AWS/Firehose | **ThrottledGetRecords** | `FirehoseStreamName` | At least once a minute | 
| AWS/Firehose | **DeliveryToElasticsearch.Success** | `FirehoseStreamName` | <1 | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `FirehoseStreamName` | String | | ○ | The Firehose stream name |
| `OldestRecordAge` | Number | 120 | ○ | The threshold of the age of the oldest record |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-kinesis-data-firehose(ja)

cloudwatch-alarm-about-kinesis-data-firehose は、 Amazon Kinesis Data Firehose に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | DeliveryStreamName | 閾値 |
| --- | --- | --- | --- |
| AWS/Firehose | **DeliveryToElasticsearch.DataFreshness** | `FirehoseStreamName` | `OldestRecordAge` |
| AWS/Firehose | **ThrottledGetShardIterator** | `FirehoseStreamName` | 1分間に1回以上 | 
| AWS/Firehose | **ThrottledGetRecords** | `FirehoseStreamName` | 1分間に1回以上 | 
| AWS/Firehose | **DeliveryToElasticsearch.Success** | `FirehoseStreamName` | <1 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `FirehoseStreamName` | String | | ○ | ストリーム名 |
| `OldestRecordAge` | Number | 120 | ○ | 最も古いレコードの閾値 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |