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
    SemanticVersion: 2.0.6
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
| `CustomAlarmName` | String | | | |
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
    SemanticVersion: 2.0.6
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ProjectName : String
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
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |
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
    SemanticVersion: 2.0.6
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
    SemanticVersion: 2.0.6
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
    SemanticVersion: 2.0.6
  NotificationARNs: 
    - String
  Parameters: 
    CPUUtilizationThreshold: Integer
    CustomAlarmName : String
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
| `CustomAlarmName` | String | | | |
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
    SemanticVersion: 2.0.6
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
| `CustomAlarmName` | String | | | |
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
    SemanticVersion: 2.0.6
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
| `CustomAlarmName` | String | | | |
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
    SemanticVersion: 2.0.6
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

## NAT Gateway

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/NATGateway | **PacketsDropCount** | 1分間に1回以上 |
| AWS/NATGateway | **ErrorPortAllocation** | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
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
    SemanticVersion: 2.0.6
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
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |
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
    SemanticVersion: 2.0.6
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    SNSTopicName: String
  Tags: Map
  TimeoutInMinutes: Integer
```