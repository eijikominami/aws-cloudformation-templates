English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/cicd
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/cicd`` deploys CloudFormation templates in this repository using `CodePipeline`.

## TL;DR

If you just want to deploy the stack, click one of the two buttons below.

[codepipeline-default-settings - AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~codepipeline-default-settings)

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=CICD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cicd/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CICD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cicd/template.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture.png)

This template creates the following diagram.

![](../images/cicd_codepipeline.png)

## Preparation

### Create S3 artifact bucket in us-east-1 (Optional)

If you deploy ``Global Settings Template``, create an ``S3 artifact bucket`` in N.Verginia (`us-east-1`) region.
 
```bash
aws s3api create-bucket --bucket my-bucket --region us-east-1
```
### Set up template configuration files (Optional)

If you use [Template Configuration File](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html#w2ab1c13c17c13), upload your configuration files to your GitHub repository with the following file names and specify `GitHubOwnerNameForTemplateConfiguration`, `GitHubOwnerNameForTemplateConfiguration` and `GitHubRepoNameForTemplateConfiguration` in your deployment.

| Stack Name | Template Configuration File Name | 
| --- | --- |
| CICD Template | CICD.json |
| [CloudOps Template](../cloudops/README_JP.md) | CloudOps.json |
| [Global Settings Template](../global/README.md) | GlobalSettings.json |
| [Network Template](../network/README.md) | Network.json |
| [Notification Template](../notification/README.md) | Notification.json |
| [Shared Service Template](../shared/README_JP.md) | SharedServices.json |
| [Security Template](../security/README.md) | DefaultSecuritySettings.json |
| [Security Template with Config Rule](../security-config-rules/README.md) | DefaultSecuritySettings-ConfigRules.json |
| [Static Website Hosting Template](../static-website-hosting/README.md) | StaticWebsiteHosting.json |
| [EC2-based Web Servers Template](../web-servers/README.md) | WebServers.json |

## Deployment

Execute the command to deploy with `ArtifactBucketInVirginia`, `GitHubOwnerNameForTemplateConfiguration` and `GitHubRepoNameForTemplateConfiguration` parameter.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name StaticWebsiteHosting --parameter-overrides ArtifactBucketInVirginia=xxxxx GitHubOwnerNameForTemplateConfiguration=xxxxx GitHubRepoNameForTemplateConfiguration=xxxxx
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| ArtifactBucketInVirginia | String | | | The S3 artifact bucket name in N.Verginia region |
| CentralizedLogBucketName | String | | | The centralize S3 bucket name for logging |
| **CloudOps** | ENABLED / INCIDENT_MANAGER_DISABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `GlobalSettings` stack is deployed |
| CodeBuildImageName | String | aws/codebuild/amazonlinux2-x86_64-standard:3.0 | ○ | The Docker image name for CodeBuild |
| **DefaultSecuritySettings** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `DefaultSecuritySettings` stack is deployed |
| **GitHubOwnerNameForTemplateConfiguration** | String | | | The **GitHub owner name** for CloudFormation Template Configuration files |
| **GitHubRepoNameForTemplateConfiguration** | String | | | The **GitHub repository name** for CloudFormation Template Configuration files |
| GitHubBranchName | String | master | ○ | The Branch name of GitHub |
| **GlobalSettings** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `GlobalSettings` stack is deployed |
| ManagementAccountId | String | | | The management account ID |
| **Network** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `Network` stack is deployed |
| **Notification** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `Notification` stack is deployed |
| OrganizationsRootId | String | | | The root id of AWS Organizations |
| **SharedServices** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `SharedServices` stack is deployed |
| **StaticWebsiteHosting** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `StaticWebsiteHosting` stack is deployed |
| TemplateConfigurationBasePath | String | | | The base path of template configration files |
| **UploadArtifacts** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `UploadArtifacts` stack is deployed |
| **WebServers** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `WebServers` stack is deployed |