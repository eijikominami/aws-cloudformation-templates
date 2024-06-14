Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-lambda(en)

cloudwatch-alarm-about-lambda creates Amazon CloudWatch Alarm about AWS Lambda.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Resource | FunctionName | Threshold |
| --- | --- | --- | --- | --- |
| AWS/Lambda | **Errors** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |
| AWS/Lambda | **Duration** | `FunctionResouceName` | `FunctionResouceName` | `TimeoutMilliseconds` | 
| AWS/Lambda | **Throttles** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |  

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `FunctionResouceName` | String | | ○ | The resource name of the Lambda function |
| `MetricFilterPattern` | String | ?Error ?Exception | ○ | Metric filter pattern | 
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `TimeoutMilliseconds` | Integer | 24000 | ○ | The threshold of Duration |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-lambda(ja)

cloudwatch-alarm-about-lambda は、AWS Lambda に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Resource | FunctionName | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/Lambda | **Errors** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |
| AWS/Lambda | **Duration** | `FunctionResouceName` | `FunctionResouceName` | `TimeoutMilliseconds` | 
| AWS/Lambda | **Throttles** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |  

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `FunctionResouceName` | String | | ○ | Lambda のリソース名 |
| `MetricFilterPattern` | String | ?Error ?Exception | ○ | メトリックフィルタパターン | 
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `TimeoutMilliseconds` | Integer | 24000 | ○ | 実行時間の閾値 |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |