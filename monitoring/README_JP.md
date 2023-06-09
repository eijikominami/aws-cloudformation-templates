[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/monitoring
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/monitoring`` は 主要なAWSサービスに関する ``CloudWatch アラーム`` を作成します。

## API Gateway

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ApiName | Stage | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/ApiGateway | **4XXError** | `ApiName` | `ApiStageName` | 1分間に1回以上 | 
| AWS/ApiGateway | **5XXError** | `ApiName` | `ApiStageName` | 1分間に1回以上 |
| AWS/ApiGateway | **Count** | `ApiName` | `ApiStageName` | `ApiCount` | 
| AWS/ApiGateway | **Latency** | `ApiName` | `ApiStageName` | `LatencyThreshold` | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ApiMethodName` | GET / POST / DELETE / OPTIONS |  | ○ | |
| `ApiName` | String |  | ○ | |
| `ApiStageName` | String | | ○ | |
| `CustomAlarmName` | String | | | |
| `ApiCount` | Number | 0 | ○ | |
| `LatencyThreshold` | Number | 2000 | ○ | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    ApiMethodName : String
    ApiName : String
    ApiStageName : String
    CustomAlarmName : String
    ApiCount : Integer
    LatencyThreshold : Integer
    ApiMethodName : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/apigateway.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-apigateway
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    ApiMethodName : String
    ApiName : String
    ApiResourcePath : String
    ApiStageName : String
    CustomAlarmName : String
    ApiCount : Integer
    LatencyThreshold : Integer
    ApiMethodName : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## CodeBuild

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ProjectName | 閾値 |
| --- | --- | --- | --- |
| AWS/CodeBuild | **FailedBuilds** | `ProjectName` | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `ProjectName` | String |  | ○ | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ProjectName : String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/codebuild.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-codebuild
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ProjectName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Directory Service

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ディレクトリ ID | ドメインコントローラ IP | メトリックカテゴリ | 閾値 |
| --- | --- | --- | --- | --- | --- |
| AWS/DirectoryService | **Recursive Query Failure/sec** | `DirectoryId` | `DomainControllerIp` | DNS | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `DirectoryId` | String | | ○ | ディレクトリの ID |
| `DomainControllerIp` | String | | ○ | ドメインコントローラの IP |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DirectoryId: String
    DomainControllerIp: String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/directoryservice.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-directoryservice
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DirectoryId: String
    DomainControllerIp: String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## DynamoDB throttle

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TableName | 閾値 |
| --- | --- | --- | --- |
| AWS/DynamoDB | **WriteThrottleEvents** | `TableName` | 1分間に1回以上 | 
| AWS/DynamoDB | **ReadThrottleEvents** | `TableName` | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `TableName` | String |  | ○ | |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ProjectName : String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/dynamodb-throttle.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-dynamodb-throttle
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ProjectName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## DynamoDB

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Operation | 閾値 |
| --- | --- | --- | --- |
| AWS/DynamoDB | **UserErrors** | GetRecords | 1分間に1回以上 | 
| AWS/DynamoDB | **SystemErrors** | GetRecords | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/dynamodb.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-dynamodb
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## EC2

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/EC2 | **StatusCheckFailed** | 1分間に1回以上 | 
| AWS/EC2 | **CPUUtilization** | `CPUUtilizationThreshold` | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CPUUtilizationThreshold` | Number | 100 | ○ | |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CPUUtilizationThreshold: Integer
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/ec2.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-ec2
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CPUUtilizationThreshold: Integer
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## EC2 CloudWatch Agent

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/EC2 | **StatusCheckFailed** | 1分間に1回以上 | 
| AWS/EC2 | **CPUUtilization** | `CPUUtilizationThreshold` | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CPUUtilizationThreshold` | Number | 100 | ○ | CPU使用率の閾値 |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters:
    CPUUtilizationThreshold: Integer
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/ec2-cwagent.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-ec2-cwagent
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CPUUtilizationThreshold: Integer
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## OpenSearch Service

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

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters:
    CustomAlarmName : String
    DomainName: String
    FreeStorageSpaceThreshold: Integer
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/elasticsearch.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-ec2-elasticsearch
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DomainName: String
    FreeStorageSpaceThreshold: Integer
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

# Elemental Link

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

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DeviceType: String
    InputDeviceId: String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/elementallink.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-elementallink
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DeviceType: String
    InputDeviceId: String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## EventBridge

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | RuleName | 閾値 |
| --- | --- | --- | --- |
| AWS/Events | **StatusCheckFailed** | `FailedInvocations` | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `EventsRuleName` | String | | ○ | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    EventsRuleName: String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/events.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-events
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    EventsRuleName: String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Kinesis Streams

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | StreamName | 閾値 |
| --- | --- | --- | --- |
| AWS/Kinesis | **GetRecords.IteratorAgeMilliseconds** | `KinesisStreamName` | `IteratorAgeMillisecondsThreshold` |
| AWS/Kinesis | **PutRecord.Success** | `KinesisStreamName` | `NumberOfPutRecordThreshold` |  
| AWS/Kinesis | **WriteProvisionedThroughputExceeded** | `KinesisStreamName` | 1分間に1回以上 |  

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `IteratorAgeMillisecondsThreshold` | Integer | 30000 | ○ | |
| `KinesisStreamName` | String | | ○ | |
| `NumberOfPutRecordThreshold` | Integer | 1000 | ○ | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    IteratorAgeMillisecondsThreshold: Integer
    KinesisStreamName : String
    NumberOfPutRecordThreshold : Integer
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/kinesis.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-kinesis
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    IteratorAgeMillisecondsThreshold: Integer
    KinesisStreamName : String
    NumberOfPutRecordThreshold : Integer
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Kinesis Firehose

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | StreamName | 閾値 |
| --- | --- | --- | --- |
| AWS/Kinesis | **GetRecords.IteratorAgeMilliseconds** | `KinesisStreamName` | `IteratorAgeMillisecondsThreshold` |
| AWS/Kinesis | **PutRecord.Success** | `KinesisStreamName` | `NumberOfPutRecordThreshold` |  
| AWS/Kinesis | **WriteProvisionedThroughputExceeded** | `KinesisStreamName` | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `IteratorAgeMillisecondsThreshold` | Integer | 30000 | ○ | IteratorAgeMilliseconds の閾値 |
| `KinesisStreamName` | String | | ○ | ストリーム名 |
| `NumberOfPutRecordThreshold` | Integer | 1000 | ○ | 分間の PutRecord 数の閾値 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    IteratorAgeMillisecondsThreshold: Integer
    KinesisStreamName: String
    NumberOfPutRecordThreshold: Integer
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/kinesis-data-firehose.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-kinesis-data-firehose
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    IteratorAgeMillisecondsThreshold: Integer
    KinesisStreamName: String
    NumberOfPutRecordThreshold: Integer
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Lambda

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Resource | FunctionName | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/Lambda | **Errors** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |
| AWS/Lambda | **ClientError** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |  
| AWS/Lambda | **TypeError** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |  
| AWS/Lambda | **Duration** | `FunctionResouceName` | `FunctionResouceName` | `TimeoutMilliseconds` | 
| AWS/Lambda | **Throttles** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |  

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `FunctionResouceName` | String | | ○ | |
| `MetricFilterPattern` | String | ?Error ?Exception | ○ | メトリックフィルタパターン | 
| `SNSTopicArn` | String | | ○ | |
| `TimeoutMilliseconds` | Integer | 24000 | ○ | |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    FunctionResouceName: String
    SNSTopicArn : String
    TimeoutMilliseconds: Integer
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/lambda.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-lambda
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    FunctionResouceName: String
    SNSTopicArn : String
    TimeoutMilliseconds: Integer
  Tags: Map
  TimeoutInMinutes: Integer
```

## MediaConnect

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
| AWS/MediaConnect | **SourcePacketLossPercent** | `SourceARN` | > 0 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ChannelId` | String |  | ○ | チャンネルID |
| `SourceName` | String |  | ○ | ソース名 |
| `SourceARN` | String |  | ○ | ソース ARN |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SourceName: String
    SourceARN: String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/mediaconnect-source.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-mediaconnect-source
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SourceName: String
    SourceARN: String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## MediaLive

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | OutputGroupName | ChannelId | Pipeline | 閾値 |
| --- | --- | --- | --- | --- | --- |
| AWS/MediaLive | **Output4xxErrors** | `OutputGroupName` | `ChannelId` | `Pipeline` | 1分間に1回以上 | 
| AWS/MediaLive | **Output5xxErrors** | `OutputGroupName` | `ChannelId` | `Pipeline` | 1分間に1回以上 |
| AWS/MediaLive | **ActiveAlerts** | | `ChannelId` | `Pipeline` | 1分間に1回以上 | 
| AWS/MediaLive | **PrimaryInputActive** | | `ChannelId` | `Pipeline` | <1 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ChannelId` | String |  | ○ | チャンネルID |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `OutputGroupName` | String |  | ○ | Output Group 名 |
| `PipelineId` | String |  | ○ | パイプラインID |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    ChannelId: String
    CustomAlarmName : String
    OutputGroupName: String
    PipelineId: String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/medialive.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-medialive
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    ChannelId: String
    CustomAlarmName : String
    OutputGroupName: String
    PipelineId: String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## MediaStore

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ContainerName | RequestType | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | PutRequests | 1分間に1回以上 | 
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | ListRequests | 1分間に1回以上 | 
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | PutRequests | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `ContainerName` | String |  | ○ | コンテナ名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ContainerName: String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/mediastore.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-mediastore
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ContainerName: String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## NAT Gateway

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/NATGateway | **PacketsDropCount** | 1分間に1回以上 |
| AWS/NATGateway | **ErrorPortAllocation** | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/natgateway.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-natgateway
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## SNS

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TopicName | 閾値 |
| --- | --- | --- | --- |
| AWS/SNS | **NumberOfNotificationsFailed** | `SNSTopicName` | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `SNSTopicName` | String | | ○ | |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    SNSTopicName: String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/sns.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-sns
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    SNSTopicName: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Transit Gateway

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TopicName | 閾値 |
| --- | --- | --- |
| AWS/TransitGateway | **PacketDropCountNoRoute** | `TransitGateway` | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `TransitGatewayId` | String | | ○ | Transit Gateway の ID |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    TransitGatewayId: String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/transitgateway.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-transitgateway
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    TransitGatewayId: String
  Tags: Map
  TimeoutInMinutes: Integer
```

# Transit Gateway アタッチメント

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TransitGateway | TransitGateway アタッチメント | 閾値 |
| --- | --- | --- |
| AWS/TransitGateway | **PacketDropCountNoRoute** | `TransitGatewayId` | `TransitGatewayAttachmentId` | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `TransitGatewayId` | String | | ○ | Transit Gateway の ID |
| `TransitGatewayAttachmentId` | String | | ○ | Transit Gateway アタッチメントの ID |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    TransitGatewayId: String
    TransitGatewayAttachmentId: String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/transitgateway-attachment.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-transitgateway-attachment
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    TransitGatewayId: String
    TransitGatewayAttachmentId: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## VPC エンドポイント

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | VPC ID | VPC エンドポイント ID | エンドポイントタイプ | サービス名 | 閾値 |
| --- | --- | --- | --- | --- | --- | --- |
| AWS/PrivateLinkEndpoints | **PacketsDropped** | `VPCId` | `VPCEndpointId` | `EndpointType` | `ServiceName`  | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `EndpointType` | String | | ○ | エンドポイントタイプ | 
| `ServiceName` | String | | ○ | サービス名 | 
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `VPCEndpointId` | String | | ○ | エンドポイント ID | 
| `VPCId` | String | | ○ | VPC ID | 

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    EndpointType: String
    ServiceName: String
    SNSTopicArn : String
    VPCEndpointId: String
    VPCId: String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/privateendpoint.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-privateendpoint
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    EndpointType: String
    ServiceName: String
    SNSTopicArn : String
    VPCEndpointId: String
    VPCId: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Workspaces

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ディレクトリ ID | 閾値 |
| --- | --- | --- |
| AWS/WorkSpaces | **PacketDropCountNoRoute** | `DirectoryId` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `DirectoryId` | String | | ○ | The id of the Workspaces directory |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DirectoryId: String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: !If
        - Development
        - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/workspaces.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-workspaces
    SemanticVersion: 2.1.4
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DirectoryId: String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```