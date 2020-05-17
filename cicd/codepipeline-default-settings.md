Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# codepipeline-default-settings (en)

codepipeline-default-settings deploys CloudFormation templates about security services, static website hosting and Slack notification using AWS CodePipeline.

## Architecture

The following sections describe the individual components of the architecture.

![](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/architecture.png)

This template creates the following diagram.

![](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cicd_codepipeline.png)

## Preparation

### Generate a GitHub personal access token

Generate a GitHub [personal access token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) and copy it.

![](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/generate_your_access_token.png)

### Create S3 artifact bucket in us-east-1 (Optional)

If you deploy ``Global Settings Template``, create an ``S3 artifact bucket`` in N.Verginia (`us-east-1`) region.
 
```bash
aws s3api create-bucket --bucket my-bucket --region us-east-1
```
### Set up template configuration files (Optional)

If you use [Template Configuration File](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html#w2ab1c13c17c13), upload your configuration files to your GitHub repository with the following file names and specify `GitHubOwnerNameForTemplateConfiguration` and `GitHubRepoNameForTemplateConfiguration` in your deployment.

| Stack Name | Template Configuration File Name | 
| --- | --- |
| [CICD Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/cicd/README.md) | CICD.json |
| [Global Settings Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/global/README.md) | GlobalSettings.json |
| [Notification Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/notification/README.md) | Notification.json |
| [Security Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/security/README.md) | DefaultSecuritySettings.json |
| [Security Template with Config Rule](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/security-config-rules/README.md) | DefaultSecuritySettings-ConfigRules.json |
| [Static Website Hosting Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/static-website-hosting-with-ssl/README.md) | StaticWebsiteHosting.json |
| [EC2-based Web Servers Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/web-servers/README.md) | Notification.json |

## Deployment

Execute the command to deploy with `ArtifactBacketInVirginia` and `GitHubOAuthToken` parameter.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name StaticWebsiteHosting --parameter-overrides ArtifactBacketInVirginia=my0bucket GitHubOAuthToken=XXXXX
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| ArtifactBacketInVirginia | String | | | S3 artifact bucket name in N.Verginia region. |
| CodeBuildImageName | String | aws/codebuild/amazonlinux2-x86_64-standard:3.0 | ○ | |
| **GitHubOAuthToken** | String | | | OAuth token to access GitHub |
| GitHubOwnerNameForTemplateConfiguration | String | | | GitHub owner name for CloudFormation Template Configuration files |
| GitHubRepoNameForTemplateConfiguration | String | | | GitHub repository name for CloudFormation Template Configuration files |
| GitHubStage | String | master | ○ | GitHub stage name of the repository CloudFormation templates are located |
| DefaultSecuritySettingsConfigRules | Enabled / Disabled | Disabled | ○ | If it is Enabled, `DefaultSecuritySettings-ConfigRules` stack is deployed. |
| GlobalSettings | Enabled / Disabled | Disabled | ○ | If it is Enabled, `GlobalSettings` stack is deployed. |
| Notification | Enabled / Disabled | Disabled | ○ | If it is Enabled, `Notification` stack is deployed. |
| StaticWebsiteHosting | Enabled / Disabled | Disabled | ○ | If it is Enabled, `StaticWebsiteHosting` stack is deployed. |
| WebServers | Enabled / SystemManager-Only / Disabled | Disabled | ○ | If it is Enabled, `WebServers` stack is deployed. |

---------------------------------------

# codepipeline-default-settings (ja)

codepipeline-default-settings は、`CodePipeline` を用いて AWSの **セキュリティサービスの有効化** や **Webサイトのホスティング機能** などをAWS上に一括デプロイします。

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/architecture.png)

このテンプレートは、以下のダイアグラムを作成します。

![](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cicd_codepipeline.png)

### 準備

### GitHub パーソナルアクセストークンの作成

GitHub [パーソナルアクセストークン](https://help.github.com/ja/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) を作成し、その値をコピーします。

![](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/generate_your_access_token.png)

### S3 アーティファクトバケットの作成 (オプション)

``Global Settings Template`` を実行する際には、バージニアリージョン（`us-east-1`）に Amazon S3 アーティファクトバケットを作成してください。
 
```bash
aws s3api create-bucket --bucket my-bucket --region us-east-1
```

### テンプレート設定ファイルの作成 (オプション)

[テンプレート設定ファイル](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html#w2ab1c13c17c13) を使用する場合は、GitHubリポジトリに以下に示す命名規則で Configuration File をアップロードした上で、CloudFormationを実行する際には、`GitHubOwnerNameForTemplateConfiguration` パラメータと `GitHubRepoNameForTemplateConfiguration` パラメータを指定してください。

| スタック名 | Template Configuration File 名 | 
| --- | --- |
| CICD Template | CICD.json |
| [Global Settings Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/global/README_JP.md) | GlobalSettings.json |
| [Notification Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/notification/README_JP.md) | Notification.json |
| [Security Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/security/README_JP.md) | DefaultSecuritySettings.json |
| [Security Template with Config Rule](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/security-config-rules/README_JP.md) | DefaultSecuritySettings-ConfigRules.json |
| [Static Website Hosting Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/static-website-hosting-with-ssl/README_JP.md) | StaticWebsiteHosting.json |
| [EC2-based Web Servers Template](https://github.com/eijikominami/aws-cloudformation-templates/tree/master/web-servers/README_JP.md) | Notification.json |

## デプロイ

`ArtifactBacketInVirginia` パラメータと `GitHubOAuthToken` パラメータを指定して、デプロイを実行してください。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name StaticWebsiteHosting --parameter-overrides ArtifactBacketInVirginia=my0bucket GitHubOAuthToken=XXXXX
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| ArtifactBacketInVirginia | String | | | Amazon S3 アーティファクトバケット（us-east-1） |
| CodeBuildImageName | String | aws/codebuild/amazonlinux2-x86_64-standard:3.0 | ○ | |
| **GitHubOAuthToken** | String | | | GitHubからコードを取得する際に用いるOAuthトークン |
| GitHubOwnerNameForTemplateConfiguration | String | | | TemplateConfigurationファイルが置かれているGitHubリポジトリの所有者名　|
| GitHubRepoNameForTemplateConfiguration | String | | | TemplateConfigurationファイルが置かれているGitHubリポジトリ名　|
| GitHubStage | String | master | ○ | CloudFormationテンプレートが置かれているリポジトリのステージ名 |
| DefaultSecuritySettingsConfigRules | Enabled / Disabled | Disabled | ○ | Enabledを指定した場合、`DefaultSecuritySettingsConfigRules` スタックがデプロイされます。 |
| GlobalSettings | Enabled / Disabled | Disabled | ○ | Enabledを指定した場合、`GlobalSettings` スタックがデプロイされます。 |
| Notification | Enabled / Disabled | Disabled | ○ | Enabledを指定した場合、`Notification` スタックがデプロイされます。 |
| StaticWebsiteHosting | Enabled / Disabled | Disabled | ○ | Enabledを指定した場合、`StaticWebsiteHosting` スタックがデプロイされます。 |
| WebServers | Enabled / SystemManager-Only / Disabled | Disabled | ○ | Enabledを指定した場合、`WebServers` スタックがデプロイされます。 |