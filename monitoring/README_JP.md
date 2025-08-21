[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/monitoring
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/monitoring`` は主要な AWS サービスに関する ``CloudWatch アラーム`` を作成します。

## 前提条件

デプロイの前に以下を準備してください。

- アラーム通知用に設定された SNS トピック
- 特定のユースケースに対する CloudWatch メトリクスとアラーム閾値の理解
- CloudWatch と SNS サービスに対する適切な IAM 権限

## TL;DR

監視テンプレートを素早くデプロイしたい場合は、AWS Serverless Application Repository を使用できます。各監視テンプレートは、コンソールから直接デプロイできるサーバーレスアプリケーションとして利用可能です。

| サービス | Application Repository リンク |
| --- | --- |
| ACM | [cloudwatch-alarm-about-acm](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-acm) |
| Amplify | [cloudwatch-alarm-about-amplify](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-amplify) |
| API Gateway | [cloudwatch-alarm-about-apigateway](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-apigateway) |
| Application ELB | [cloudwatch-alarm-about-application-elb](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-application-elb) |
| EC2 | [cloudwatch-alarm-about-ec2](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-ec2) |
| Lambda | [cloudwatch-alarm-about-lambda](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-lambda) |

## AWS Certificate Manager

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/CertificateManager | **DaysToExpiry** | =<30 |
| AWS/CertificateManager | **DaysToExpiry** | =<7 |
| AWS/CertificateManager | **DaysToExpiry** | =<1 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `CertificateArn` | String | | ○ | 証明書の ARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | AppID | 閾値 |
| --- | --- | --- | --- |
| AWS/AmplifyHosting | **5xxErrors** | `AppId` | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AppId` | String | | ○ | アプリ ID |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-amplify
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
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `ApiCount` | Number | 0 | ○ | リクエストの合計数 |
| `ApiMethodName` | GET / POST / DELETE / OPTIONS |  | ○ | メソッド名 |
| `ApiName` | String |  | ○ | API名 |
| `ApiStageName` | String | | ○ | ステージ名 |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `LatencyThreshold` | Number | 2000 | ○ | Latency の閾値 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | FlowName | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/AppFlow | **FlowExecutionsFailed** | `FlowName` | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `FlowName` | String | | ○ | フロー名 |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TargetGroup | LoadBalancer | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/ApplicationELB | **UnHealthyHostCount** | `TargetGroup` | `LoadBalancer` | 1分間に1回以上 | 
| AWS/ApplicationELB | **HTTPCode_Target_5XX_Count** | `TargetGroup` | `LoadBalancer` | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `TargetGroup` | String | | ○ | ターゲットグループID |
| `LoadBalancer` | String | | ○ | ロードバランサー名 |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Fleet 名 | 閾値 |
| --- | --- | --- |
| AWS/AppStream | **InsufficientConcurrencyLimitError** | `Fleet` | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `Fleet` | String | | ○ | AppSream Fleet 名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ProjectName | 閾値 |
| --- | --- | --- | --- |
| AWS/CodeBuild | **FailedBuilds** | `ProjectName` | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `ProjectName` | String |  | ○ | プロジェクト名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

```yaml
Type: AWS::CloudFormation::Stack
Properties: 
  NotificationARNs: 
    - String
  Parameters: 
    AlarmLevel: String
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
    AlarmLevel: String
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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/Config | **ChangeNotificationsDeliveryFailed** | 1分間に1回以上 |
| AWS/Config | **ConfigHistoryExportFailed** | 1分間に1回以上 |
| AWS/Config | **ConfigSnapshotExportFailed** | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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
    - https://s3.amazonaws.com/eijikominami-test/aws-cloudformation-templates/monitoring/config.yaml
  TimeoutInMinutes: Integer
```

```yaml
Type: AWS::Serverless::Application
Properties:
  Location:
    ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-config
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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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
| `TableName` | String |  | ○ | テーブル名 |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |
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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/ECS | **CPUUtilization** | `UtilizationThreshold` | 
| AWS/ECS | **MemoryUtilization** | `UtilizationThreshold` | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ClusterName` | String | | ○ | The ECS クラスター名 |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `ServiceName` | String | | ○ | The ECS サービス名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `UtilizationThreshold` | Number | 100 | ○ | 使用率の閾値 |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `DomainName` | String | | ○ | ドメイン名 |
| `FreeStorageSpaceThreshold` | Number | | ○ | ストレージの空き容量の閾値（MB） |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | RuleName | 閾値 |
| --- | --- | --- | --- |
| AWS/Events | **StatusCheckFailed** | `FailedInvocations` | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `EventsRuleName` | String | | ○ | EventBridge のルール名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | StreamName | 閾値 |
| --- | --- | --- | --- |
| AWS/Kinesis | **GetRecords.IteratorAgeMilliseconds** | `KinesisStreamName` | `IteratorAgeMillisecondsThreshold` |
| AWS/Kinesis | **PutRecord.Success** | `KinesisStreamName` | `NumberOfPutRecordThreshold` |  
| AWS/Kinesis | **WriteProvisionedThroughputExceeded** | `KinesisStreamName` | 1分間に1回以上 |  

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `IteratorAgeMillisecondsThreshold` | Integer | 30000 | ○ | IteratorAgeMilliseconds の閾値 |
| `KinesisStreamName` | String | | ○ | ストリーム名 |
| `NumberOfPutRecordThreshold` | Integer | 1000 | ○ | 分間の PutRecord 数の閾値 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | StreamName | 閾値 |
| --- | --- | --- | --- |
| AWS/Kinesis | **GetRecords.IteratorAgeMilliseconds** | `KinesisStreamName` | `IteratorAgeMillisecondsThreshold` |
| AWS/Kinesis | **PutRecord.Success** | `KinesisStreamName` | `NumberOfPutRecordThreshold` |  
| AWS/Kinesis | **WriteProvisionedThroughputExceeded** | `KinesisStreamName` | 1分間に1回以上 | 

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `FirehoseStreamName` | String | | ○ | ストリーム名 |
| `OldestRecordAge` | Number | 120 | ○ | 最も古いレコードの閾値 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | Resource | FunctionName | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/Lambda | **Errors** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |
| AWS/Lambda | **Duration** | `FunctionResouceName` | `FunctionResouceName` | `TimeoutMilliseconds` | 
| AWS/Lambda | **Throttles** | `FunctionResouceName` | `FunctionResouceName` | 1分間に1回以上 |  

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `FunctionResouceName` | String | | ○ | Lambda のリソース名 |
| `MetricFilterPattern` | String | ?Error ?Exception | ○ | メトリックフィルタパターン | 
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `TimeoutMilliseconds` | Integer | 24000 | ○ | 実行時間の閾値 |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `ChannelId` | String |  | ○ | チャンネルID |
| `SourceName` | String |  | ○ | ソース名 |
| `SourceARN` | String |  | ○ | ソース ARN |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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

## MediaConnect (ソース)

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

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- |
| AWS/NATGateway | **PacketsDropCount** | 1分間に1回以上 |
| AWS/NATGateway | **ErrorPortAllocation** | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AlarmLevel` | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | エンドポイント ID | 閾値 |
| --- | --- | --- | --- |
| AWS/Route53Resolver | **EndpointUnhealthyENICount** | `EndpointId` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `EndpointId` | String | | ○ | エンドポイント ID |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |

### Syntax

AWS CloudFormation テンプレートでこのエンティティを宣言するには、次の構文を使用します。

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TopicName | 閾値 |
| --- | --- | --- | --- |
| AWS/SNS | **NumberOfNotificationsFailed** | `SNSTopicName` | 1分間に1回以上 |

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `SNSTopicName` | String | | ○ | SNSトピック名 |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/SSM-RunCommand | `CommandsDeliveryTimedOut` | 1分間に1回以上 | 
| AWS/SSM-RunCommand | `CommandsFailed` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | ディレクトリ ID | 閾値 |
| --- | --- | --- |
| AWS/WorkSpaces | **Unhealthy** | `DirectoryId` | 1分間に1回以上 |

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `DirectoryId` | String | | ○ | The id of the Workspaces directory |
| `SNSTopicArn` | String | | ○ | SNSトピックのARN |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |

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
```## トラブルシュー
ティング

### CloudWatch アラームの問題

CloudWatch アラームが正しくトリガーされない場合：

1. AWS サービスのメトリクス名とネームスペースが正しいことを確認してください
2. アラーム閾値がワークロードパターンに適していることを確認してください
3. SNS トピックが正しい権限とサブスクライバーを持っていることを確認してください
4. アラーム評価期間とデータポイントが正しく設定されていることを確認してください

### SNS 通知の問題

アラーム通知を受信していない場合：

1. SNS トピックサブスクリプションが確認済みであることを確認してください
2. メールアドレスやエンドポイントが正しくアクセス可能であることを確認してください
3. SNS トピックポリシーが CloudWatch にメッセージの公開を許可していることを確認してください
4. メール通知についてはスパムフォルダーを確認してください

### メトリクスデータの問題

メトリクスが表示されない、または正しくない場合：

1. AWS サービスが CloudWatch にメトリクスを公開していることを確認してください
2. カスタムメトリクスが正しいディメンションで公開されていることを確認してください
3. CloudWatch エージェントが適切に設定されていることを確認してください（EC2 カスタムメトリクス用）
4. メトリクス保持期間が期限切れになっていないことを確認してください

### 権限の問題

アラームを作成または変更できない場合：

1. IAM ロールが必要な CloudWatch 権限を持っていることを確認してください
2. 該当する場合、クロスアカウントアクセスが適切に設定されていることを確認してください
3. AWS サービス用のサービスリンクロールが作成されていることを確認してください
4. リソースベースポリシーが必要なアクションを許可していることを確認してください