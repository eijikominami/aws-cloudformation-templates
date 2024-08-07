Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-mediaconnect-source(en)

cloudwatch-alarm-about-mediaconnect-source creates Amazon CloudWatch Alarm about AWS Elemental MediaConnect source.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | SourceARN | Threshold |
| --- | --- | --- | --- |
| AWS/MediaConnect | **SourcePTSError** | `SourceARN` | At least once a minute |
| AWS/MediaConnect | **SourceCRCError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourcePIDError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceCATError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceTSByteError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourcePMTError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceTSSyncLoss** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourcePATError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceTransportError** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourceDroppedPackets** | `SourceARN` | At least once a minute | 
| AWS/MediaConnect | **SourcePacketLossPercent** | `SourceARN` | > 0 | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom alram name |
| `SourceName` | String |  | ○ | The source name |
| `SourceARN` | String |  | ○ | The source ARN |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-mediaconnect-source(ja)

cloudwatch-alarm-about-mediaconnect-source は、 AWS Elemental MediaConnect source に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | SourceARN | 閾値 |
| --- | --- | --- | --- |
| AWS/MediaConnect | **SourcePTSError** | `SourceARN` | 1分間に1回以上 |
| AWS/MediaConnect | **SourceCRCError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourcePIDError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceCATError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceTSByteError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourcePMTError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceTSSyncLoss** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourcePATError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceTransportError** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourceDroppedPackets** | `SourceARN` | 1分間に1回以上 | 
| AWS/MediaConnect | **SourcePacketLossPercent** | `SourceARN` | > 0 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String |  | ○ | カスタムアラーム名 |
| `SourceName` | String |  | ○ | ソース名 |
| `SourceARN` | String |  | ○ | ソース ARN |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |