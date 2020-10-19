Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-dynamodb-throttole(en)

cloudwatch-alarm-about-dynamodb-throttole creates Amazon CloudWatch Alarm about Amazon DynamoDB Throttole metrics.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | TableName | Threshold |
| --- | --- | --- | --- |
| AWS/DynamoDB | **WriteThrottleEvents** | `TableName` | At least once a minute | 
| AWS/DynamoDB | **ReadThrottleEvents** | `TableName` | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |
| `TableName` | String |  | ○ | |

---------------------------------------

# cloudwatch-alarm-about-dynamodb-throttole(ja)

cloudwatch-alarm-about-apigateway は、Amazon DynamoDB の スロットルメトリクス に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TableName | 閾値 |
| --- | --- | --- | --- |
| AWS/DynamoDB | **WriteThrottleEvents** | `TableName` | 1分間に1回以上 | 
| AWS/DynamoDB | **ReadThrottleEvents** | `TableName` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |
| `TableName` | String |  | ○ | |