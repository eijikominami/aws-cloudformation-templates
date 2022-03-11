Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-mediastore(en)

cloudwatch-alarm-about-mediastore creates Amazon CloudWatch Alarm about AWS Elemental MediaStore.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | ContainerName | RequestType | Threshold |
| --- | --- | --- | --- | --- |
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | PutRequests | At least once a minute | 
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | ListRequests | At least once a minute | 
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | PutRequests | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `ContainerName` | String |  | ○ | |
| `SNSTopicArn` | String | | ○ | |

---------------------------------------

# cloudwatch-alarm-about-mediastore(ja)

cloudwatch-alarm-about-mediastore は、 AWS Elemental MediaStore に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ContainerName | RequestType | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | PutRequests | 1分間に1回以上 | 
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | ListRequests | 1分間に1回以上 | 
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | PutRequests | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ContainerName` | String |  | ○ | |
| `SNSTopicArn` | String | | ○ | |