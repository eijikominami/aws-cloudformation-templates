English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/monitoring
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/monitoring`` provides ``CloudWatch alarm`` for major AWS services.

## Prerequisites

Before deploying these monitoring templates, ensure you have:

- SNS topics configured for alarm notifications
- Understanding of CloudWatch metrics and alarm thresholds for your specific use case
- Appropriate IAM permissions for CloudWatch and SNS services

## TL;DR

If you want to deploy monitoring templates quickly, you can use the AWS Serverless Application Repository. Each monitoring template is available as a serverless application that you can deploy directly from the console.

| Service | Application Repository Link |
| --- | --- |
| ACM | [cloudwatch-alarm-about-acm](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-acm) |
| Amplify | [cloudwatch-alarm-about-amplify](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-amplify) |
| API Gateway | [cloudwatch-alarm-about-apigateway](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-apigateway) |
| Application ELB | [cloudwatch-alarm-about-application-elb](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-application-elb) |
| EC2 | [cloudwatch-alarm-about-ec2](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-ec2) |
| Lambda | [cloudwatch-alarm-about-lambda](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-lambda) |

## AWS Certificate Manager

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/CertificateManager | **DaysToExpiry** | =<30 |
| AWS/CertificateManager | **DaysToExpiry** | =<7 |
| AWS/CertificateManager | **DaysToExpiry** | =<1 |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CertificateArn` | String | | ○ | The Certificate ARN |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel : String
    CertificateArn : String
    CustomAlarmName : String
    CustomAlarmName : String
    SNSTopicArn : Integer
    Environment : Integer
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/acm.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-acm
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel : String
    CertificateArn : String
    CustomAlarmName : String
    CustomAlarmName : String
    SNSTopicArn : Integer
    Environment : Integer
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Amplify

The template creates the following alarms.

| Namespace | MetricName | AppId | Threshold |
| --- | --- | --- | --- |
| AWS/AmplifyHosting | **5xxErrors** | `AppId` | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AppId` | String | | ○ | The app id |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AppId: String
    CustomAlarmName: String
    SNSTopicArn: String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/amplify.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-amplifys
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    AppId: String
    CustomAlarmName: String
    SNSTopicArn: String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

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
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `ApiMethodName` | GET / POST / DELETE / OPTIONS |  | ○ | |
| `ApiName` | String |  | ○ | The API Gateway api name |
| `ApiStageName` | String | | ○ | The API Gateway stage name |
| `CustomAlarmName` | String | | | |
| `ApiCount` | Number | 0 | ○ | The threshold of ApiCount per minute |
| `LatencyThreshold` | Number | 2000 | ○ | The threshold of Latency |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: String
    ApiMethodName : String
    ApiName : String
    ApiStageName : String
    CustomAlarmName : String
    ApiCount : Integer
    LatencyThreshold : Integer
    ApiMethodName : String
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters:
    AlarmLevel: String
    ApiMethodName : String
    ApiName : String
    ApiResourcePath : String
    ApiStageName : String
    CustomAlarmName : String
    ApiCount : Integer
    LatencyThreshold : Integer
    ApiMethodName : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## AppFlow

The template creates the following alarms.

| Namespace | MetricName | FlowName | Threshold |
| --- | --- | --- | --- |
| AWS/AppFlow | **FlowExecutionsFailed** | `FlowName` | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `FlowName` | String | | ○ | The AppFlow flow name |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    FlowName : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/appflow.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-appflow
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    FlowName : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Application Load Balancer

The template creates the following alarms.

| Namespace | MetricName | TargetGroup | LoadBalancer | Threshold |
| --- | --- | --- | --- | --- |
| AWS/ApplicationELB | **UnHealthyHostCount** | `TargetGroup` | `LoadBalancer` | At least once a minute | 
| AWS/ApplicationELB | **HTTPCode_Target_5XX_Count** | `TargetGroup` | `LoadBalancer` | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `TargetGroup` | String | | ○ | The target group id |
| `LoadBalancer` | String | | ○ | The load balancer name |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel : String
    CustomAlarmName : String
    TargetGroup: String
    LoadBalancer: String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/application-elb.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-application-elb
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel : String
    CustomAlarmName : String
    TargetGroup: String
    LoadBalancer: String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## AppStream

The template creates the following alarms.

| Namespace | MetricName | Fleet | Threshold |
| --- | --- | --- |
| AWS/AppStream | **InsufficientConcurrencyLimitError** | `Fleet` | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `Fleet` | String | | ○ | The name of the AppStream Fleet |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: String
    CustomAlarmName : String
    Fleet : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/appstream.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-appstream
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: String
    CustomAlarmName : String
    Fleet : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `ProjectName` | String |  | ○ | The CodeBuild project name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ProjectName : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Config

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/Config | **ChangeNotificationsDeliveryFailed** | At least once a minute |
| AWS/Config | **ConfigHistoryExportFailed** | At least once a minute |
| AWS/Config | **ConfigSnapshotExportFailed** | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName: String
    SNSTopicArn: String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/cofig.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-cofig
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName: String
    SNSTopicArn: String
    Environment: String
    TagKey: String
    TagValue: String
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
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DirectoryId: String
    DomainControllerIp: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `TableName` | String |  | ○ | The DynamoDB table name |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ProjectName : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `CPUUtilizationThreshold` | Number | 100 | ○ | The threshold of CPU Utilization |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CPUUtilizationThreshold: Integer
    CustomAlarmName : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CPUUtilizationThreshold: Integer
    CustomAlarmName : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## ECS

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- |
| AWS/ECS | **CPUUtilization** | `UtilizationThreshold` | 
| AWS/ECS | **MemoryUtilization** | `UtilizationThreshold` | 

You can give optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `ClusterName` | String | | ○ | The ECS Cluster name |
| `CustomAlarmName` | String | | | The custom alram name |
| `ServiceName` | String | | ○ | The ECS Service name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `UtilizationThreshold` | Number | 100 | ○ | The threshold of utilization |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters:
    ClusterName: String
    CustomAlarmName : String
    ServiceName: String
    SNSTopicArn : String
    UtilizationThreshold: Integer
    Environment: String
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/ecs.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-ecs
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    ClusterName: String
    CustomAlarmName : String
    ServiceName: String
    SNSTopicArn : String
    UtilizationThreshold: Integer
    Environment: String
    TagKey: String
    TagValue: String
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
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `DomainName` | String | | ○ | The domain name |
| `FreeStorageSpaceThreshold` | Number | | ○ | The threshold of the free storage space (MB) |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters:
    AlarmLevel: String
    CustomAlarmName : String
    DomainName: String
    FreeStorageSpaceThreshold: Integer
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: String
    CustomAlarmName : String
    DomainName: String
    FreeStorageSpaceThreshold: Integer
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

# Elemental Link

The template creates the following alarms.

| Namespace | MetricName | InputDeviceId | DeviceType | Threshold |
| --- | --- | --- | --- | --- |
| AWS/MediaLive | **Temperature** | `InputDeviceId` | HD / UHD | < 40 | 
| AWS/MediaLive | **NotRecoveredPackets** | `InputDeviceId` | HD / UHD | At least once a minute |
| AWS/MediaLive | **ErrorSeconds** | `InputDeviceId` | `Pipeline` | HD / UHD | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `InputDeviceId` | String |  | ○ | Input device Id |
| `DeviceType` | HD / UHD | | | The device type |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DeviceType: String
    InputDeviceId: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `EventsRuleName` | String | | ○ | The EventBridge rule name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: String
    CustomAlarmName : String
    EventsRuleName: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: String
    CustomAlarmName : String
    EventsRuleName: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `IteratorAgeMillisecondsThreshold` | Integer | 30000 | ○ | The threshold of IteratorAgeMilliseconds |
| `KinesisStreamName` | String | | ○ | The Kinesis stream name |
| `NumberOfPutRecordThreshold` | Integer | 1000 | ○ | The threshold of PutRecord per minute |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel : String
    CustomAlarmName : String
    IteratorAgeMillisecondsThreshold: Integer
    KinesisStreamName : String
    NumberOfPutRecordThreshold : Integer
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel : String
    CustomAlarmName : String
    IteratorAgeMillisecondsThreshold: Integer
    KinesisStreamName : String
    NumberOfPutRecordThreshold : Integer
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `IteratorAgeMillisecondsThreshold` | Integer | 30000 | ○ | The threshold of IteratorAgeMilliseconds |
| `KinesisStreamName` | String | | ○ | The Kinesis stream name |
| `NumberOfPutRecordThreshold` | Integer | 1000 | ○ | The threshold of PutRecord per minute |
| `SNSTopicArn` | String | | ○ | The custom Alram name |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: !Ref AlarmLevel
    CustomAlarmName : String
    IteratorAgeMillisecondsThreshold: Integer
    KinesisStreamName: String
    NumberOfPutRecordThreshold: Integer
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: !Ref AlarmLevel
    CustomAlarmName : String
    IteratorAgeMillisecondsThreshold: Integer
    KinesisStreamName: String
    NumberOfPutRecordThreshold: Integer
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Lambda

The template creates the following alarms.

| Namespace | MetricName | Resource | FunctionName | Threshold |
| --- | --- | --- | --- | --- |
| AWS/Lambda | **Errors** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |
| AWS/Lambda | **Duration** | `FunctionResouceName` | `FunctionResouceName` | `TimeoutMilliseconds` | 
| AWS/Lambda | **Throttles** | `FunctionResouceName` | `FunctionResouceName` | At least once a minute |  

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `FunctionResouceName` | String | | ○ | The resource name of the Lambda function |
| `MetricFilterPattern` | String | ?Error ?Exception | ○ | Metric filter pattern | 
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `TimeoutMilliseconds` | Integer | 24000 | ○ | The threshold of Duration |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    FunctionResouceName: String
    SNSTopicArn : String
    TimeoutMilliseconds: Integer
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## MediaConnect

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

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SourceName: String
    SourceARN: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## MediaConnect (Source)

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

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName: String
    SourceName : String
    SourceARN: String
    SNSTopicArn: String
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName: String
    SourceName : String
    SourceARN: String
    SNSTopicArn: String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## MediaConvert

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

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/mediaconvert.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-mediaconvert
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    ChannelId: String
    CustomAlarmName : String
    OutputGroupName: String
    PipelineId: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    ContainerName: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: String
    CustomAlarmName : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters:
    AlarmLevel: String 
    CustomAlarmName : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Route 53 Resolver

The template creates the following alarms.

| Namespace | MetricName | EndpointId | Threshold |
| --- | --- | --- | --- |
| AWS/Route53Resolver | **EndpointUnhealthyENICount** | `EndpointId` | At least once a minute |

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `EndpointId` | String | | ○ | The endpoint ID |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

### Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    EndpointId: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/route53-resolver.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-route53-resolver
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    EndpointId: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    SNSTopicName: String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## SSM Run Command

The template creates the following alarms.

| Namespace | MetricName | Threshold |
| --- | --- | --- | --- | --- |
| AWS/SSM-RunCommand | `CommandsDeliveryTimedOut` | At least once a minute | 
| AWS/SSM-RunCommand | `CommandsFailed` | At least once a minute | 

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
  Tags: 
    - Tag
  TemplateURL: !If
    - Development
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/ssm-command.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-transitgateway
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
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
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    TransitGatewayId: String
    Environment: String
    TagKey: String
    TagValue: String
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
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    SNSTopicArn : String
    TransitGatewayId: String
    TransitGatewayAttachmentId: String
    Environment: String
    TagKey: String
    TagValue: String
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
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    EndpointType: String
    ServiceName: String
    SNSTopicArn : String
    VPCEndpointId: String
    VPCId: String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```

## Workspaces

The template creates the following alarms.

| Namespace | MetricName | DirectoryId | Threshold |
| --- | --- | --- |
| AWS/WorkSpaces | **Unhealthy** | `DirectoryId` | At least once a minute |

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `DirectoryId` | String | | ○ | The id of the Workspaces directory |
| `SNSTopicArn` | String | | ○ | The SNS topic ARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
    Environment: String
    TagKey: String
    TagValue: String
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
    SemanticVersion: 2.2.13
  NotificationARNs: 
    - String
  Parameters: 
    CustomAlarmName : String
    DirectoryId: String
    SNSTopicArn : String
    Environment: String
    TagKey: String
    TagValue: String
  Tags: Map
  TimeoutInMinutes: Integer
```
## 
Troubleshooting

### CloudWatch Alarm Issues

If CloudWatch alarms are not triggering correctly:

1. Verify that the metric names and namespaces are correct for your AWS services
2. Check that the alarm thresholds are appropriate for your workload patterns
3. Ensure that the SNS topics have the correct permissions and subscribers
4. Verify that the alarm evaluation periods and datapoints are configured correctly

### SNS Notification Issues

If you're not receiving alarm notifications:

1. Check that SNS topic subscriptions are confirmed
2. Verify that email addresses or endpoints are correct and accessible
3. Ensure that SNS topic policies allow CloudWatch to publish messages
4. Check spam folders for email notifications

### Metric Data Issues

If metrics are not appearing or seem incorrect:

1. Verify that the AWS services are publishing metrics to CloudWatch
2. Check that custom metrics are being published with correct dimensions
3. Ensure that CloudWatch agent is properly configured (for EC2 custom metrics)
4. Verify that the metric retention period hasn't expired

### Permission Issues

If alarms cannot be created or modified:

1. Verify that IAM roles have the necessary CloudWatch permissions
2. Check that cross-account access is properly configured if applicable
3. Ensure that service-linked roles are created for AWS services
4. Verify that resource-based policies allow the required actions