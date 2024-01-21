Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-ecs(en)

cloudwatch-alarm-about-ecs creates Amazon CloudWatch Alarm about Amazon ECS.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/ECS | **CPUUtilization** | `UtilizationThreshold` | 
| AWS/ECS | **MemoryUtilization** | `UtilizationThreshold` | 

## Parameters

You can give optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `ClusterName` | String | | ○ | The ECS Cluster name |
| `CustomAlarmName` | String | | | The custom alram name |
| `ServiceName` | String | | ○ | The ECS Service name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `UtilizationThreshold` | Number | 100 | ○ | The threshold of utilization |

---------------------------------------

# cloudwatch-alarm-about-ecs(ja)

cloudwatch-alarm-about-ecs は、Amazon ECS に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/ECS | **CPUUtilization** | `UtilizationThreshold` | 
| AWS/ECS | **MemoryUtilization** | `UtilizationThreshold` | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ClusterName` | String | | ○ | The ECS クラスター名 |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `ServiceName` | String | | ○ | The ECS サービス名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `UtilizationThreshold` | Number | 100 | ○ | 使用率の閾値 |