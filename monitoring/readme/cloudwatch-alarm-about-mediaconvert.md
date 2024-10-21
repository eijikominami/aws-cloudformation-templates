Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-mediaconvert(en)

cloudwatch-alarm-about-mediaconvert creates Amazon CloudWatch Alarm about AWS Elemental MediaConvert.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | Operation | Threshold |
| --- | --- | --- | --- |
| AWS/MediaConvert | **Errors** | CreateJob | At least once a minute | 
| AWS/MediaConvert | **Errors** | GetJob | At least once a minute | 
| AWS/MediaConvert | **Errors** | GetQueue | At least once a minute | 
| AWS/MediaConvert | **Errors** | ListJobs | At least once a minute | 
| AWS/MediaConvert | **Errors** | ListJobTemplates | At least once a minute | 
| AWS/MediaConvert | **Errors** | ListPresets | At least once a minute | 
| AWS/MediaConvert | **Errors** | ListQueues | At least once a minute | 
| AWS/MediaConvert | **Errors** | ListTagsForResource | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-mediaconvert(ja)

cloudwatch-alarm-about-mediaconvert は、 AWS Elemental MediaConvert に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Operation | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/MediaConvert | **Errors** | CreateJob | 1分間に1回以上 | 
| AWS/MediaConvert | **Errors** | GetJob | 1分間に1回以上 | 
| AWS/MediaConvert | **Errors** | GetQueue | 1分間に1回以上 | 
| AWS/MediaConvert | **Errors** | ListJobs | 1分間に1回以上 | 
| AWS/MediaConvert | **Errors** | ListJobTemplates | 1分間に1回以上 | 
| AWS/MediaConvert | **Errors** | ListPresets | 1分間に1回以上 | 
| AWS/MediaConvert | **Errors** | ListQueues | 1分間に1回以上 | 
| AWS/MediaConvert | **Errors** | ListTagsForResource | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |