Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-kinesis-data-streams(en)

cloudwatch-alarm-about-kinesis-data-streams creates Amazon CloudWatch Alarm about Amazon Kinesis Data Streams.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | StreamName | Threshold |
| --- | --- | --- | --- |
| AWS/Kinesis | **GetRecords.IteratorAgeMilliseconds** | `KinesisStreamName` | `IteratorAgeMillisecondsThreshold` |
| AWS/Kinesis | **PutRecord.Success** | `KinesisStreamName` | `NumberOfPutRecordThreshold` |  
| AWS/Kinesis | **WriteProvisionedThroughputExceeded** | `KinesisStreamName` | At least once a minute |  

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `IteratorAgeMillisecondsThreshold` | Integer | 30000 | ○ | |
| `KinesisStreamName` | String | | ○ | |
| `NumberOfPutRecordThreshold` | Integer | 1000 | ○ | |
| `SNSTopicArn` | String | | ○ | |

---------------------------------------

# cloudwatch-alarm-about-kinesis-data-streams(ja)

cloudwatch-alarm-about-apigateway は、Amazon Kinesis Data Streams に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | StreamName | 閾値 |
| --- | --- | --- | --- |
| AWS/Kinesis | **GetRecords.IteratorAgeMilliseconds** | `KinesisStreamName` | `IteratorAgeMillisecondsThreshold` |
| AWS/Kinesis | **PutRecord.Success** | `KinesisStreamName` | `NumberOfPutRecordThreshold` |  
| AWS/Kinesis | **WriteProvisionedThroughputExceeded** | `KinesisStreamName` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `IteratorAgeMillisecondsThreshold` | Integer | 30000 | ○ | |
| `KinesisStreamName` | String | | ○ | |
| `NumberOfPutRecordThreshold` | Integer | 1000 | ○ | |
| `SNSTopicArn` | String | | ○ | |