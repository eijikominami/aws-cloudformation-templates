English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/cicd
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/cicd`` deploys CloudFormation templates in this repository using `CodePipeline`.

## TL;DR

If you just want to deploy the stack, click one of the two buttons below.

+ [codepipeline-default-settings - AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~codepipeline-default-settings)

+ [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CICD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cicd/template.yaml) 

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture.png)

This template creates the following diagram.

![](../images/cicd_codepipeline.png)

## Preparation

### Generate a GitHub personal access token

Generate a GitHub [personal access token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) and copy it.

![](../images/generate_your_access_token.png)

### Create S3 artifact bucket in us-east-1 (Optional)

If you deploy ``Global Settings Template``, create an ``S3 artifact bucket`` in N.Verginia (`us-east-1`) region.
 
```bash
aws s3api create-bucket --bucket my-bucket --region us-east-1
```
### Set up template configuration files (Optional)

If you use [Template Configuration File](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html#w2ab1c13c17c13), upload your configuration files to your GitHub repository with the following file names and specify `GitHubOwnerNameForTemplateConfiguration` and `GitHubRepoNameForTemplateConfiguration` in your deployment.

| Stack Name | Template Configuration File Name | 
| --- | --- |
| CICD Template | CICD.json |
| [Global Settings Template](../global/README.md) | GlobalSettings.json |
| [Notification Template](../notification/README.md) | Notification.json |
| [Security Template](../security/README.md) | DefaultSecuritySettings.json |
| [Security Template with Config Rule](../security-config-rules/README.md) | DefaultSecuritySettings-ConfigRules.json |
| [Static Website Hosting Template](../static-website-hosting-with-ssl/README.md) | StaticWebsiteHosting.json |
| [EC2-based Web Servers Template](../web-servers/README.md) | WebServers.json |

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