[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/cicd
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/cicd`` は、`CodePipeline` を用いて このリポジトリにある CloudFormation テンプレートを一括デプロイします。

## TL;DR

以下のいずれかのボタンをクリックすることで、 この **CloudFormationをデプロイ** することが可能です。

[codepipeline-default-settings - AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~codepipeline-default-settings)

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CICD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cicd/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CICD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cicd/template.yaml) |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture.png)

このテンプレートは、以下のダイアグラムを作成します。

![](../images/cicd_codepipeline.png)

### 準備

### S3 アーティファクトバケットの作成 (オプション)

``Global Settings Template`` を実行する際には、バージニアリージョン（`us-east-1`）に Amazon S3 アーティファクトバケットを作成してください。
 
```bash
aws s3api create-bucket --bucket my-bucket --region us-east-1
```

### テンプレート設定ファイルの作成 (オプション)

[テンプレート設定ファイル](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html#w2ab1c13c17c13) を使用する場合は、GitHubリポジトリに以下に示す命名規則で Configuration File をアップロードした上で、CloudFormationを実行する際に `GitHubOwnerNameForTemplateConfiguration` パラメータ、`GitHubOwnerNameForTemplateConfiguration` パラメータと `GitHubRepoNameForTemplateConfiguration` パラメータを指定してください。

| スタック名 | Template Configuration File 名 | 
| --- | --- |
| CICD Template | CICD.json |
| [CloudOps Template](../cloudops/README_JP.md) | CloudOps.json |
| [Global Settings Template](../global/README_JP.md) | GlobalSettings.json |
| [Network Template](../network/README.md) | Network.json |
| [Notification Template](../notification/README_JP.md) | Notification.json |
| [Shared Service Template](../shared/README_JP.md) | SharedServices.json |
| [Security Template](../security/README_JP.md) | DefaultSecuritySettings.json |
| [Security Template with Config Rule](../security-config-rules/README_JP.md) | DefaultSecuritySettings-ConfigRules.json |
| [Static Website Hosting Template](../static-website-hosting/README_JP.md) | StaticWebsiteHosting.json |
| [EC2-based Web Servers Template](../web-servers/README_JP.md) | WebServers.json |

## デプロイ

`ArtifactBucketInVirginia` パラメータ、`GitHubOwnerNameForTemplateConfiguration` パラメータと `GitHubRepoNameForTemplateConfiguration` パラメータを指定して、デプロイを実行してください。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name StaticWebsiteHosting --parameter-overrides ArtifactBucketInVirginia=xxxxx GitHubOwnerNameForTemplateConfiguration=xxxxx GitHubRepoNameForTemplateConfiguration=xxxxx
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| ArtifactBucketInVirginia | String | | | Amazon S3 アーティファクトバケット（us-east-1） |
| CentralizedLogBucketName | String | | | 集約ログバケット名 |
| **CloudOps** | ENABLED / INCIDENT_MANAGER_DISABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`CloudOps` スタックがデプロイされます。 |
| CodeBuildImageName | String | aws/codebuild/amazonlinux2-x86_64-standard:3.0 | ○ | |
| **DefaultSecuritySettings** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`DefaultSecuritySettings` スタックがデプロイされます。 |
| **GitHubOwnerNameForTemplateConfiguration** | String | | | TemplateConfigurationファイルが置かれている **GitHubリポジトリの所有者名** |
| **GitHubRepoNameForTemplateConfiguration** | String | | | TemplateConfigurationファイルが置かれている **GitHubリポジトリ名** |
| GitHubBranchName | String | master | ○ | CloudFormationテンプレートが置かれているリポジトリのステージ名 |
| **GlobalSettings** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`GlobalSettings` スタックがデプロイされます。 |
| ManagementAccountId | String | | | 管理アカウントの AWS ID |
| **Network** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`Network` スタックがデプロイされます。 |
| **Notification** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`Notification` スタックがデプロイされます。 |
| OrganizationsRootId | String | | | AWS Organizations のルート ID |
| **SharedServices** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`SharedServices` スタックがデプロイされます。 |
| **StaticWebsiteHosting** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`StaticWebsiteHosting` スタックがデプロイされます。 |
| TemplateConfigurationBasePath | String | | | 設定プロパティのあるディレクトリのパス |
| **UploadArtifacts** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`UploadArtifacts` スタックがデプロイされます。 |
| **WebServers** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`WebServers` スタックがデプロイされます。 |