Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-apigateway(en)

cloudwatch-alarm-about-apigateway creates Amazon CloudWatch Alarm about Amazon API Gateway.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | ApiName | Stage | Threshold |
| --- | --- | --- | --- | --- |
| AWS/ApiGateway | **4XXError** | `ApiName` | `ApiStageName` | At least once a minute | 
| AWS/ApiGateway | **5XXError** | `ApiName` | `ApiStageName` | At least once a minute |
| AWS/ApiGateway | **Count** | `ApiName` | `ApiStageName` | `ApiCount` | 
| AWS/ApiGateway | **Latency** | `ApiName` | `ApiStageName` | `LatencyThreshold` | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `ApiCount` | Number | 0 | ○ | The threshold of ApiCount per minute |
| `ApiMethodName` | GET / POST / DELETE / OPTIONS |  | ○ | |
| `ApiName` | String |  | ○ | The API Gateway api name |
| `ApiStageName` | String | | ○ | The API Gateway stage name |
| `CustomAlarmName` | String | | | The custom alram name |
| `LatencyThreshold` | Number | 2000 | ○ | The threshold of Latency |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

---------------------------------------

# cloudwatch-alarm-about-apigateway(ja)

cloudwatch-alarm-about-apigateway は、 Amazon API Gateway に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ApiName | Stage | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/ApiGateway | **4XXError** | `ApiName` | `ApiStageName` | 1分間に1回以上 | 
| AWS/ApiGateway | **5XXError** | `ApiName` | `ApiStageName` | 1分間に1回以上 |
| AWS/ApiGateway | **Count** | `ApiName` | `ApiStageName` | `ApiCount` | 
| AWS/ApiGateway | **Latency** | `ApiName` | `ApiStageName` | `LatencyThreshold` | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ApiCount` | Number | 0 | ○ | リクエストの合計数 |
| `ApiMethodName` | GET / POST / DELETE / OPTIONS |  | ○ | メソッド名 |
| `ApiName` | String |  | ○ | API名 |
| `ApiStageName` | String | | ○ | ステージ名 |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `LatencyThreshold` | Number | 2000 | ○ | Latency の閾値 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |