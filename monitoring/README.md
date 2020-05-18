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
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/apigateway.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-apigateway
    SemanticVersion: 1.0.8
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
| `CustomAlarmName` | String | | | |
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
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/codebuild.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-codebuild
    SemanticVersion: 1.0.8
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

The template creates the following alarms.

| Namespace | MetricName | TableName | Threshold |
| --- | --- | --- | --- |
| AWS/DynamoDB | **WriteThrottleEvents** | `TableName` | At least once a minute | 
| AWS/DynamoDB | **ReadThrottleEvents** | `TableName` | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |
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
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/dynamodb-throttle.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-dynamodb-throttle
    SemanticVersion: 1.0.8
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
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/dynamodb.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-dynamodb
    SemanticVersion: 1.0.8
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## EC2

The template provide the following alarms.

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
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/ec2.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-ec2
    SemanticVersion: 1.0.8
  NotificationARNs: 
    - String
  Parameters: 
    CPUUtilizationThreshold: Integer
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: Map
  TimeoutInMinutes: Integer
```

## CloudWatch Events

The template creates the following alarms.

| Namespace | MetricName | RuleName | Threshold |
| --- | --- | --- | --- |
| AWS/Events | **StatusCheckFailed** | `FailedInvocations` | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
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
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/events.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-events
    SemanticVersion: 1.0.8
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
| `CustomAlarmName` | String | | | |
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
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/kinesis.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-kinesis
    SemanticVersion: 1.0.8
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
| `CustomAlarmName` | String | | | |
| `FunctionResouceName` | String | | ○ | |
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
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/lambda.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-lambda
    SemanticVersion: 1.0.8
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

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/NATGateway | **PacketsDropCount** | At least once a minute |
| AWS/NATGateway | **ErrorPortAllocation** | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
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
    CustomAlarmName : String
    SNSTopicArn : String
  Tags: 
    - Tag
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/natgateway.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-natgateway
    SemanticVersion: 1.0.8
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
| --- | --- | --- |
| AWS/SNS | **NumberOfNotificationsFailed** | `SNSTopicName` | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | |
| `SNSTopicArn` | String | | ○ | |
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
  TemplateURL: https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/monitoring/sns.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: 'AWS::Serverless::Application'
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-sns
    SemanticVersion: 1.0.8
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    SNSTopicName: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture.png)