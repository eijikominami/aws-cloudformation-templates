Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-codebuild(en)

cloudwatch-alarm-about-codebuild creates Amazon CloudWatch Alarm about AWS CodeBuild.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | ProjectName | Threshold |
| --- | --- | --- | --- |
| AWS/CodeBuild | **FailedBuilds** | `ProjectName` | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `ProjectName` | String |  | ○ | |
| `SNSTopicArn` | String | | ○ | |

---------------------------------------

# cloudwatch-alarm-about-codebuild(ja)

cloudwatch-alarm-about-apigateway は、AWS CodeBuild に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ProjectName | 閾値 |
| --- | --- | --- | --- |
| AWS/CodeBuild | **FailedBuilds** | `ProjectName` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `ProjectName` | String |  | ○ | |
| `SNSTopicArn` | String | | ○ | |