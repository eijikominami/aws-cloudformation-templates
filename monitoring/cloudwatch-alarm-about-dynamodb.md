Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-dynamodb(en)

cloudwatch-alarm-about-dynamodb creates  Amazon CloudWatch Alarm about Amazon DynamoDB.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Operation | Threshold |
| --- | --- | --- | --- |
| AWS/DynamoDB | **UserErrors** | GetRecords | At least once a minute | 
| AWS/DynamoDB | **SystemErrors** | GetRecords | At least once a minute | 

## Prameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |

# cloudwatch-alarm-about-dynamodb(ja)

cloudwatch-alarm-about-apigateway は、Amazon DynamoDB に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Operation | 閾値 |
| --- | --- | --- | --- |
| AWS/DynamoDB | **UserErrors** | GetRecords | 1分間に1回以上 | 
| AWS/DynamoDB | **SystemErrors** | GetRecords | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |