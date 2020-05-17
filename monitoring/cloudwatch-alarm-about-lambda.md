Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-lambda(en)

cloudwatch-alarm-about-lambda creates Amazon CloudWatch Alarm about AWS Lambda.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Resource | FunctionName | Threshold |
| --- | --- | --- | --- | --- |
| AWS/Lambda | **Errors** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |
| AWS/Lambda | **ClientError** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |  
| AWS/Lambda | **TypeError** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |  
| AWS/Lambda | **Duration** | `FunctionResouceName` | `FunctionResouceName` | `TimeoutMilliseconds` | 
| AWS/Lambda | **Throttles** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |  

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `FunctionResouceName` | String | | ○ | |
| `SNSTopicArn` | String | | ○ | |
| `TimeoutMilliseconds` | Integer | 24000 | ○ | |

# cloudwatch-alarm-about-lambda(ja)

cloudwatch-alarm-about-apigateway は、AWS Lambda に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Resource | FunctionName | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/Lambda | **Errors** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |
| AWS/Lambda | **ClientError** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |  
| AWS/Lambda | **TypeError** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |  
| AWS/Lambda | **Duration** | `FunctionResouceName` | `FunctionResouceName` | `TimeoutMilliseconds` | 
| AWS/Lambda | **Throttles** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |  

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `FunctionResouceName` | String | | ○ | |
| `SNSTopicArn` | String | | ○ | |
| `TimeoutMilliseconds` | Integer | 24000 | ○ | |