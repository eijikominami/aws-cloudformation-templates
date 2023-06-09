Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-mediaconnect-source(en)

cloudwatch-alarm-about-mediaconnect-source creates Amazon CloudWatch Alarm about AWS Elemental MediaConnect source.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | SourceARN | Threshold |
| --- | --- | --- | --- |
| AWS/MediaConnect | **SourcePTSError** | `SourceARN` | At least once a minute |
| AWS/MediaConnect | **SourcePCRAccuracyError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceCRCError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourcePIDError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceCATError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceTSByteError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourcePCRError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourcePMTError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceTSSyncLoss** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourcePATError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceTransportError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceDroppedPackets** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourcePacketLossPercent** | `SourceARN` | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom alram name |
| `SourceName` | String |  | ○ | The source name |
| `SourceARN` | String |  | ○ | The source ARN |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

---------------------------------------

# cloudwatch-alarm-about-mediaconnect-source(ja)

cloudwatch-alarm-about-mediaconnect-source は、 AWS Elemental MediaConnect source に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | SourceARN | 閾値 |
| --- | --- | --- | --- |
| AWS/MediaConnect | **SourcePTSError** | `SourceARN` | 1分間に1回以上 |
| AWS/MediaConnect | **SourcePCRAccuracyError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceCRCError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourcePIDError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceCATError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceTSByteError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourcePCRError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourcePMTError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceTSSyncLoss** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourcePATError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceTransportError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceDroppedPackets** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourcePacketLossPercent** | `SourceARN` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ChannelId` | String |  | ○ | チャンネルID |
| `SourceName` | String |  | ○ | ソース名 |
| `SourceARN` | String |  | ○ | ソース ARN |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |