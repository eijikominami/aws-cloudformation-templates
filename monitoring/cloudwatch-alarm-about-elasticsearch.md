Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-elasticsearch(en)

cloudwatch-alarm-about-elasticsearch creates Amazon CloudWatch Alarm about Amazon Elasticsearch Service.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | DomainName | ClientId | Threshold |
| --- | --- | --- | --- | --- |
| AWS/ES | **ClusterStatus.green** | `DomainName` | `AWS::AccountId` | <1 | 
| AWS/ES | **ClusterIndexWritesBlocked** | `DomainName` | `AWS::AccountId` | At least once a minute | 
| AWS/ES | **MasterReachableFromNode** | `DomainName` | `AWS::AccountId` | <1 | 
| AWS/ES | **AutomatedSnapshotFailure** | `DomainName` | `AWS::AccountId` | At least once a minute | 
| AWS/ES | **KibanaHealthyNodes** | `DomainName` | `AWS::AccountId` | <1 | 
| AWS/ES | **FreeStorageSpace** | `DomainName` | `AWS::AccountId` | `FreeStorageSpaceThreshold` | 
| AWS/ES | **MasterCPUUtilization** | `DomainName` | `AWS::AccountId` | >50 | 
| AWS/ES | **MasterJVMMemoryPressure** | `DomainName` | `AWS::AccountId` | >80 | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `DomainName` | String | | ○ | |
| `FreeStorageSpaceThreshold` | Number | | ○ | |
| `SNSTopicArn` | String | | ○ | |

---------------------------------------

# cloudwatch-alarm-about-elasticsearch(ja)

cloudwatch-alarm-about-elasticsearch は、 Amazon Elasticsearch Service に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | DomainName | ClientId | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/ES | **ClusterStatus.green** | `DomainName` | `AWS::AccountId` | <1 | 
| AWS/ES | **ClusterIndexWritesBlocked** | `DomainName` | `AWS::AccountId` | 1分間に1回以上 | 
| AWS/ES | **MasterReachableFromNode** | `DomainName` | `AWS::AccountId` | <1 | 
| AWS/ES | **AutomatedSnapshotFailure** | `DomainName` | `AWS::AccountId` | 1分間に1回以上 | 
| AWS/ES | **KibanaHealthyNodes** | `DomainName` | `AWS::AccountId` | <1 | 
| AWS/ES | **FreeStorageSpace** | `DomainName` | `AWS::AccountId` | `FreeStorageSpaceThreshold` | 
| AWS/ES | **MasterCPUUtilization** | `DomainName` | `AWS::AccountId` | >50 | 
| AWS/ES | **MasterJVMMemoryPressure** | `DomainName` | `AWS::AccountId` | >80 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `DomainName` | String | | ○ | |
| `FreeStorageSpaceThreshold` | Number | | ○ | |
| `SNSTopicArn` | String | | ○ | |