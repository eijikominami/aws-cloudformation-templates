English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/monitoring
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/monitoring`` provides ``CloudWatch alarm`` for major AWS services.

## API Gateway

The template creates the following alarms.

| Namespace | MetricName | ApiName | Stage | Threshold |
| --- | --- | --- | --- | --- |
| AWS/ApiGateway | **4XXError** | `ApiName` | `ApiStageName` | At least once a minute | 
| AWS/ApiGateway | **5XXError** | `ApiName` | `ApiStageName` | At least once a minute |
| AWS/ApiGateway | **Count** | `ApiName` | `ApiStageName` | `ApiCount` | 
| AWS/ApiGateway | **Latency** | `ApiName` | `ApiStageName` | `LatencyThreshold` | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `ApiMethodName` | GET / POST / DELETE / OPTIONS |  | ○ | |
| `ApiName` | String |  | ○ | |
| `ApiResourcePath` | String | | ○ | |
| `ApiStageName` | String | | ○ | |
| `CustomAlarmName` | String | | | |
| `ApiCount` | Number | 0 | ○ | |
| `LatencyThreshold` | Number | 2000 | ○ | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | ProjectName | Threshold |
| --- | --- | --- | --- |
| AWS/CodeBuild | **FailedBuilds** | `ProjectName` | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `ProjectName` | String |  | ○ | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | Directory Id | Domain Controller IP | Metric Category | Threshold |
| --- | --- | --- | --- | --- | --- |
| AWS/DirectoryService | **Recursive Query Failure/sec** | `DirectoryId` | `DomainControllerIp` | DNS | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `DirectoryId` | String | | ○ | The id of the directory |
| `DomainControllerIp` | String | | ○ | The IP of the domain controller |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | TableName | Threshold |
| --- | --- | --- | --- |
| AWS/DynamoDB | **WriteThrottleEvents** | `TableName` | At least once a minute | 
| AWS/DynamoDB | **ReadThrottleEvents** | `TableName` | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `TableName` | String |  | ○ | |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | Operation | Threshold |
| --- | --- | --- | --- |
| AWS/DynamoDB | **UserErrors** | GetRecords | At least once a minute | 
| AWS/DynamoDB | **SystemErrors** | GetRecords | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## EC2

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/EC2 | **StatusCheckFailed** | At least once a minute | 
| AWS/EC2 | **CPUUtilization** | `CPUUtilizationThreshold` | 

You can give optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CPUUtilizationThreshold` | Number | 100 | ○ | |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/EC2 | **StatusCheckFailed** | At least once a minute | 
| AWS/EC2 | **CPUUtilization** | `CPUUtilizationThreshold` | 

You can give optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CPUUtilizationThreshold` | Number | 100 | ○ | The threshold of CPU Utilization |
| `CustomAlarmName` | String | | | The custom alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `DomainName` | String | | ○ | The domain name |
| `FreeStorageSpaceThreshold` | Number | | ○ | The threshold of the free storage space (MB) |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

## EventBridge

The template creates the following alarms.

| Namespace | MetricName | RuleName | Threshold |
| --- | --- | --- | --- |
| AWS/Events | **StatusCheckFailed** | `FailedInvocations` | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `EventsRuleName` | String | | ○ | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | StreamName | Threshold |
| --- | --- | --- | --- |
| AWS/Kinesis | **GetRecords.IteratorAgeMilliseconds** | `KinesisStreamName` | `IteratorAgeMillisecondsThreshold` |
| AWS/Kinesis | **PutRecord.Success** | `KinesisStreamName` | `NumberOfPutRecordThreshold` |  
| AWS/Kinesis | **WriteProvisionedThroughputExceeded** | `KinesisStreamName` | At least once a minute |  

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `IteratorAgeMillisecondsThreshold` | Integer | 30000 | ○ | |
| `KinesisStreamName` | String | | ○ | |
| `NumberOfPutRecordThreshold` | Integer | 1000 | ○ | |
| `SNSTopicArn` | String | | ○ | |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | StreamName | Threshold |
| --- | --- | --- | --- |
| AWS/Kinesis | **GetRecords.IteratorAgeMilliseconds** | `KinesisStreamName` | `IteratorAgeMillisecondsThreshold` |
| AWS/Kinesis | **PutRecord.Success** | `KinesisStreamName` | `NumberOfPutRecordThreshold` |  
| AWS/Kinesis | **WriteProvisionedThroughputExceeded** | `KinesisStreamName` | At least once a minute |  

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `IteratorAgeMillisecondsThreshold` | Integer | 30000 | ○ | The threshold of IteratorAgeMilliseconds |
| `KinesisStreamName` | String | | ○ | The Kinesis stream name |
| `NumberOfPutRecordThreshold` | Integer | 1000 | ○ | The threshold of PutRecord per minute |
| `SNSTopicArn` | String | | ○ | The custom Alram name |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | Resource | FunctionName | Threshold |
| --- | --- | --- | --- | --- |
| AWS/Lambda | **Errors** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |
| AWS/Lambda | **ClientError** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |  
| AWS/Lambda | **TypeError** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |  
| AWS/Lambda | **Duration** | `FunctionResouceName` | `FunctionResouceName` | `TimeoutMilliseconds` | 
| AWS/Lambda | **Throttles** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |  

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `FunctionResouceName` | String | | ○ | |
| `MetricFilterPattern` | String | ?Error ?Exception | ○ | Metric filter pattern | 
| `SNSTopicArn` | String | | ○ | |
| `TimeoutMilliseconds` | Integer | 24000 | ○ | |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

## MediaLive

The template creates the following alarms.

| Namespace | MetricName | OutputGroupName | ChannelId | Pipeline | Threshold |
| --- | --- | --- | --- | --- | --- |
| AWS/MediaLive | **Output4xxErrors** | `OutputGroupName` | `ChannelId` | `Pipeline` | At least once a minute | 
| AWS/MediaLive | **Output5xxErrors** | `OutputGroupName` | `ChannelId` | `Pipeline` | At least once a minute |
| AWS/MediaLive | **ActiveAlerts** | | `ChannelId` | `Pipeline` | At least once a minute | 
| AWS/MediaLive | **PrimaryInputActive** | | `ChannelId` | `Pipeline` | <1 | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `ChannelId` | String |  | ○ | The channel Id |
| `CustomAlarmName` | String | | | The custom alram name |
| `OutputGroupName` | String |  | ○ | The output group name |
| `PipelineId` | String |  | ○ | The pipeline id |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | ContainerName | RequestType | Threshold |
| --- | --- | --- | --- | --- |
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | PutRequests | At least once a minute | 
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | ListRequests | At least once a minute | 
| AWS/MediaStore | **ThrottleCount** | `ContainerName` | PutRequests | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `ContainerName` | String |  | ○ | The container name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/NATGateway | **PacketsDropCount** | At least once a minute |
| AWS/NATGateway | **ErrorPortAllocation** | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## SNS

The template creates the following alarms.

| Namespace | MetricName | TopicName | Threshold |
| --- | --- | --- | --- |
| AWS/SNS | **NumberOfNotificationsFailed** | `SNSTopicName` | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `SNSTopicName` | String | | ○ | |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | TopicName | Threshold |
| --- | --- | --- |
| AWS/TransitGateway | **PacketDropCountNoRoute** | `TransitGateway` | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `TransitGatewayId` | String | | ○ | The id of the Transit Gateway |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    TransitGatewayId: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Transit Gateway　attachment

The template creates the following alarms.

| Namespace | MetricName | TransitGateway | TransitGateway attachment | Threshold |
| --- | --- | --- |
| AWS/TransitGateway | **PacketDropCountNoRoute** | `TransitGatewayId` | `TransitGatewayAttachmentId` | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `TransitGatewayId` | String | | ○ | The id of the Transit Gateway |
| `TransitGatewayAttachmentId` | String | | ○ | The id of the Transit Gateway attachment |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

## VPC Endpoint

The template creates the following alarms.

| Namespace | MetricName | VPCId | VPCEndpointId | EndpointType | ServiceName | Threshold |
| --- | --- | --- | --- | --- | --- | --- |
| AWS/PrivateLinkEndpoints | **PacketsDropped** | `VPCId` | `VPCEndpointId` | `EndpointType` | `ServiceName` | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `EndpointType` | String | | ○ | The type of endpoint | 
| `ServiceName` | String | | ○ | The service name | 
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `VPCEndpointId` | String | | ○ | The id of the endpoint | 
| `VPCId` | String | | ○ | The VPC id | 

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
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

The template creates the following alarms.

| Namespace | MetricName | DirectoryId | Threshold |
| --- | --- | --- |
| AWS/WorkSpaces | **PacketDropCountNoRoute** | `DirectoryId` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `DirectoryId` | String | | ○ | The id of the Workspaces directory |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    SemanticVersion: 2.1.2
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DirectoryId: String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```