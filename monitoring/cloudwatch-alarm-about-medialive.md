Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-medialive(en)

cloudwatch-alarm-about-medialive creates Amazon CloudWatch Alarm about AWS Elemental MediaLive.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | OutputGroupName | ChannelId | Pipeline | Threshold |
| --- | --- | --- | --- | --- | --- |
| AWS/MediaLive | **Output4xxErrors** | `OutputGroupName` | `ChannelId` | `Pipeline` | At least once a minute | 
| AWS/MediaLive | **Output5xxErrors** | `OutputGroupName` | `ChannelId` | `Pipeline` | At least once a minute |
| AWS/MediaLive | **ActiveAlerts** | | `ChannelId` | `Pipeline` | At least once a minute | 
| AWS/MediaLive | **PrimaryInputActive** | | `ChannelId` | `Pipeline` | <1 | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `ChannelId` | String |  | ○ | |
| `CustomAlarmName` | String | | | |
| `OutputGroupName` | String |  | ○ | |
| `PipelineId` | String |  | ○ | |
| `SNSTopicArn` | String | | ○ | |

---------------------------------------

# cloudwatch-alarm-about-medialive(ja)

cloudwatch-alarm-about-medialive は、 AWS Elemental MediaLive に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | OutputGroupName | ChannelId | Pipeline | 閾値 |
| --- | --- | --- | --- | --- | --- |
| AWS/MediaLive | **Output4xxErrors** | `OutputGroupName` | `ChannelId` | `Pipeline` | 1分間に1回以上 | 
| AWS/MediaLive | **Output5xxErrors** | `OutputGroupName` | `ChannelId` | `Pipeline` | 1分間に1回以上 |
| AWS/MediaLive | **ActiveAlerts** | | `ChannelId` | `Pipeline` | 1分間に1回以上 | 
| AWS/MediaLive | **PrimaryInputActive** | | `ChannelId` | `Pipeline` | <1 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ChannelId` | String |  | ○ | |
| `CustomAlarmName` | String | | | |
| `OutputGroupName` | String |  | ○ | |
| `PipelineId` | String |  | ○ | |
| `SNSTopicArn` | String | | ○ | |