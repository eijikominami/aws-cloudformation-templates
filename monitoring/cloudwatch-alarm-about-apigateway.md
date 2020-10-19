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
| `ApiMethodName` | GET / POST / DELETE / OPTIONS |  | ○ | |
| `ApiName` | String |  | ○ | |
| `ApiResourcePath` | String | | ○ | |
| `ApiStageName` | String | | ○ | |
| `CustomAlarmName` | String | | | |
| `ApiCount` | Number | 0 | ○ | |
| `LatencyThreshold` | Number | 2000 | ○ | |
| `SNSTopicArn` | String | | ○ | |

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
| `ApiMethodName` | GET / POST / DELETE / OPTIONS |  | ○ | |
| `ApiName` | String |  | ○ | |
| `ApiStageName` | String | | ○ | |
| `CustomAlarmName` | String | | | |
| `ApiCount` | Number | 0 | ○ | |
| `LatencyThreshold` | Number | 2000 | ○ | |
| `SNSTopicArn` | String | | ○ | |