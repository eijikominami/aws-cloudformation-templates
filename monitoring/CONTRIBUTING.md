# Contributing to Monitoring Templates

## 概要

このプロジェクトでは、Amazon CloudWatch Alarm などの監視リソースを **AWS Serverless Application Repository** で管理しています。個別に CloudFormation テンプレートを作成するのではなく、再利用可能なアプリケーションとして公開し、他のテンプレートから参照する方式を採用しています。

## 基本方針

### 管理対象

- CloudWatch Alarm（Lambda、Glue、その他 AWS サービス用）
- SNS Topic（アラート通知用）

## ディレクトリ構造

```
aws-cloudformation-templates/
├── monitoring/
│   ├── sam-app/              # SAM テンプレート（Serverless Application Repository 用）
│   │   ├── lambda.yaml       # Lambda 用 CloudWatch Alarm
│   │   ├── glue.yaml         # Glue 用 CloudWatch Alarm
│   │   └── [service].yaml    # その他サービス用
│   ├── readme/               # 各テンプレートの README
│   │   ├── cloudwatch-alarm-about-lambda.md
│   │   ├── cloudwatch-alarm-about-glue.md
│   │   └── [service].md
│   ├── templates/            # 親テンプレート（実際にデプロイするもの）
│   │   └── [project].yaml
│   ├── README.md             # プロジェクト概要
│   └── CONTRIBUTING.md       # このファイル
├── cicd/
│   └── codebuild/
│       └── buildspec-upload-artifacts-serverlessrepo.yml  # 自動デプロイ設定
└── LICENSE                   # ライセンスファイル
```

## テンプレートの追加・更新手順

### 1. テンプレートファイルの作成・編集

`sam-app/[service].yaml` を作成・編集

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: CloudWatch Alarms for [Service Name]

Metadata:
  AWS::ServerlessRepo::Application:
    Name: cloudwatch-alarm-about-[service]
    Description: CloudWatch Alarms for [Service Name]
    Author: Eiji KOMINAMI
    SpdxLicenseId: MIT
    LicenseUrl: s3://eijikominami-test/LICENSE
    ReadmeUrl: s3://eijikominami-test/readme/cloudwatch-alarm-about-[service].md
    Labels: []
    HomePageUrl: https://github.com/eijikominami/aws-cloudformation-templates
    SourceCodeUrl: https://github.com/eijikominami/aws-cloudformation-templates

Parameters:
  ResourceName:
    Type: String
    Description: Name of the [Service] resource to monitor

Resources:
  ErrorAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmName: !Sub '${ResourceName}-errors'
      # その他のプロパティ...

Outputs:
  ErrorAlarmArn:
    Description: ARN of the error alarm
    Value: !GetAtt ErrorAlarm.Arn
```

**重要**: 
- `Metadata` セクションは必須（`sam publish` で使用）
- `SemanticVersion` は含めない（`--semantic-version` オプションで渡すため）

### 2. CFN Lint 実行

```bash
cd aws-cloudformation-templates/monitoring
cfn-lint sam-app/[service].yaml
```

**exit code 0 であることを確認**

### 3. README の作成・更新

`readme/cloudwatch-alarm-about-[service].md` を作成・更新

```markdown
# CloudWatch Alarms for [Service Name]

## Overview
This application creates CloudWatch Alarms for monitoring [Service Name] resources.

## Parameters
- **ResourceName**: Name of the [Service] resource to monitor
- **AlarmEmail**: Email address for alarm notifications

## Alarms Created
1. **Error Alarm**: Triggers when errors exceed threshold
2. **Duration Alarm**: Triggers when execution time exceeds threshold

## Usage
\`\`\`yaml
Resources:
  MonitoringStack:
    Type: AWS::Serverless::Application
    Properties:
      Location:
        ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-[service]
        SemanticVersion: 1.0.0
      Parameters:
        ResourceName: my-resource
        AlarmEmail: alerts@example.com
\`\`\`
```

### 4. buildspec を更新（新規追加の場合のみ）

`cicd/codebuild/buildspec-upload-artifacts-serverlessrepo.yml` を編集：

**build フェーズの `for` ループに追加：**
```yaml
monitoring/sam-app/[service].yaml \
```

**post_build フェーズの `for` ループに追加：**
```yaml
cloudwatch-alarm-about-[service] \
```

### 5. 変更をコミットしてタグをプッシュ

```bash
# 新規追加の場合
git add aws-cloudformation-templates/monitoring/sam-app/[service].yaml
git add aws-cloudformation-templates/monitoring/readme/cloudwatch-alarm-about-[service].md
git add cicd/codebuild/buildspec-upload-artifacts-serverlessrepo.yml
git commit -m "Add CloudWatch Alarm template for [Service]"

# 更新の場合
git add aws-cloudformation-templates/monitoring/sam-app/[service].yaml
git commit -m "Update [Service] alarm template"

# 共通
git push origin develop
git tag v2.2.15-rc
git push origin v2.2.15-rc
```

**タグプッシュ後、CodeBuild が自動的に以下を実行：**
- LICENSE と README を S3 にアップロード
- `sam publish` でアプリケーションを作成・更新
- パブリック公開ポリシーを設定

### 6. 親テンプレートで参照（新規追加の場合のみ）

ApplicationId は `arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-[service]` の形式です。

```yaml
Resources:
  CloudWatchAlarm[Service]:
    Type: AWS::Serverless::Application
    Properties:
      Location:
        ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/cloudwatch-alarm-about-[service]
        SemanticVersion: 2.2.15
      Parameters:
        ResourceName: !Ref MyResource
        AlarmEmail: !Ref AlarmEmail
```

## 参考リンク

- [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/)
- [SAM CLI Reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)
- [CloudFormation Linter](https://github.com/aws-cloudformation/cfn-lint)
- [CodeBuild Webhook Filters](https://docs.aws.amazon.com/codebuild/latest/userguide/github-webhook.html)
