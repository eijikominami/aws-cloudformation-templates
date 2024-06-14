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
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-dynamodb(ja)

cloudwatch-alarm-about-dynamodb は、Amazon DynamoDB に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Operation | 閾値 |
| --- | --- | --- | --- |
| AWS/DynamoDB | **UserErrors** | GetRecords | 1分間に1回以上 | 
| AWS/DynamoDB | **SystemErrors** | GetRecords | 1分間に2回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |