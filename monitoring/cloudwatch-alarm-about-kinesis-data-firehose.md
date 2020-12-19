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
| `CustomAlarmName` | String | | | |
| `FirehoseStreamName` | String | | ○ | |
| `OldestRecordAge` | Number | 120 | ○ | |
| `SNSTopicArn` | String | | ○ | |

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
| `CustomAlarmName` | String | | | |
| `FirehoseStreamName` | String | | ○ | |
| `OldestRecordAge` | Number | 120 | ○ | |
| `SNSTopicArn` | String | | ○ | |