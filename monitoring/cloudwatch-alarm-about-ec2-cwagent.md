Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-ec2-cwagent(en)

cloudwatch-alarm-about-ec2-cwagent creates Amazon CloudWatch Alarm about Amazon EC2.

## CloudWatch Alarm

The template provide the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| CWAgent | **disk_used_percent** | `DiskUsedPercentThreshold` | 
| CWAgent | **mem_used_percent** | `MemUsedPercentThreshold` | 

## Parameters

You can give optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `DiskUsedPercentThreshold` | Number | 100 | ○ | The threshold of disk used percent |
| `MemUsedPercentThreshold` | Number | 100 | ○ | The threshold of memory used percent |
| `ImageId` | String | | | The image id |
| `InstanceId` | String | | | The instance id |
| `CustomAlarmName` | String | | | The custom alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

---------------------------------------

# cloudwatch-alarm-about-ec2-cwagent(ja)

cloudwatch-alarm-about-ec2-cwagent は、Amazon EC2 に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| CWAgent | **disk_used_percent** | `DiskUsedPercentThreshold` | 
| CWAgent | **mem_used_percent** | `MemUsedPercentThreshold` | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `DiskUsedPercentThreshold` | Number | 100 | ○ | ディスク使用率の閾値 |
| `MemUsedPercentThreshold` | Number | 100 | ○ | メモリ使用率の閾値 |
| `ImageId` | String | | | AMI の ID |
| `InstanceId` | String | | | インスタンスID |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |