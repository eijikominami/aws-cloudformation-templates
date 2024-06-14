Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-elasticsearch(en)

cloudwatch-alarm-about-elasticsearch creates Amazon CloudWatch Alarm about Amazon OpenSearch Service.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | DomainName | ClientId | Threshold |
| --- | --- | --- | --- | --- |
| AWS/ES | **ClusterStatus.green** | `DomainName` | `AWS::AccountId` | 0 | 
| AWS/ES | **ClusterIndexWritesBlocked** | `DomainName` | `AWS::AccountId` | At least once a minute | 
| AWS/ES | **MasterReachableFromNode** | `DomainName` | `AWS::AccountId` | 0 | 
| AWS/ES | **AutomatedSnapshotFailure** | `DomainName` | `AWS::AccountId` | At least once a minute | 
| AWS/ES | **KibanaHealthyNodes** | `DomainName` | `AWS::AccountId` | 0 | 
| AWS/ES | **FreeStorageSpace** | `DomainName` | `AWS::AccountId` | `FreeStorageSpaceThreshold` | 
| AWS/ES | **MasterCPUUtilization** | `DomainName` | `AWS::AccountId` | >50 | 
| AWS/ES | **MasterJVMMemoryPressure** | `DomainName` | `AWS::AccountId` | >80 |
| AWS/ES | **CPUUtilization** | `DomainName` | `AWS::AccountId` | >50 | 
| AWS/ES | **JVMMemoryPressure** | `DomainName` | `AWS::AccountId` | >80 | 
| AWS/ES | **SysMemoryUtilization** | `DomainName` | `AWS::AccountId` | >80 | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `DomainName` | String | | ○ | The domain name |
| `FreeStorageSpaceThreshold` | Number | | ○ | The threshold of the free storage space (MB) |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-elasticsearch(ja)

cloudwatch-alarm-about-elasticsearch は、 Amazon OpenSearch Service に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | DomainName | ClientId | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/ES | **ClusterStatus.green** | `DomainName` | `AWS::AccountId` | 0 | 
| AWS/ES | **ClusterIndexWritesBlocked** | `DomainName` | `AWS::AccountId` | 1分間に1回以上 | 
| AWS/ES | **MasterReachableFromNode** | `DomainName` | `AWS::AccountId` | 0 | 
| AWS/ES | **AutomatedSnapshotFailure** | `DomainName` | `AWS::AccountId` | 1分間に1回以上 | 
| AWS/ES | **KibanaHealthyNodes** | `DomainName` | `AWS::AccountId` | 0 | 
| AWS/ES | **FreeStorageSpace** | `DomainName` | `AWS::AccountId` | `FreeStorageSpaceThreshold` | 
| AWS/ES | **MasterCPUUtilization** | `DomainName` | `AWS::AccountId` | >50 | 
| AWS/ES | **MasterJVMMemoryPressure** | `DomainName` | `AWS::AccountId` | >80 | 
| AWS/ES | **CPUUtilization** | `DomainName` | `AWS::AccountId` | >50 | 
| AWS/ES | **JVMMemoryPressure** | `DomainName` | `AWS::AccountId` | >80 | 
| AWS/ES | **SysMemoryUtilization** | `DomainName` | `AWS::AccountId` | >80 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `DomainName` | String | | ○ | ドメイン名 |
| `FreeStorageSpaceThreshold` | Number | | ○ | ストレージの空き容量の閾値（MB） |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |