Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-elementallink(en)

cloudwatch-alarm-about-elementallink creates Amazon CloudWatch Alarm about AWS Elemental Elemental Link.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | InputDeviceId | DeviceType | Threshold |
| --- | --- | --- | --- | --- |
| AWS/MediaLive | **Temperature** | `InputDeviceId` | HD / UHD | < 40 | 
| AWS/MediaLive | **NotRecoveredPackets** | `InputDeviceId` | HD / UHD | At least once a minute |
| AWS/MediaLive | **ErrorSeconds** | `InputDeviceId` | `Pipeline` | HD / UHD | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `InputDeviceId` | String |  | ○ | Input device Id |
| `DeviceType` | HD / UHD | | | The device type |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-elementallink(ja)

cloudwatch-alarm-about-elementallink は、 AWS Elemental Link に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | InputDeviceId | DeviceType | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/MediaLive | **Temperature** | `InputDeviceId` | HD / UHD | 40度以上 | 
| AWS/MediaLive | **NotRecoveredPackets** | `InputDeviceId` | HD / UHD | 1分間に1回以上 |
| AWS/MediaLive | **ErrorSeconds** | `InputDeviceId` | `Pipeline` | HD / UHD | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `InputDeviceId` | String |  | ○ | インプットデバイスID |
| `DeviceType` | HD / UHD | | | デバイスID |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |