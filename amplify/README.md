English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/amplify
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates) 

``AWSCloudFormationTemplates/amplify`` builds a CI/CD environment with ``AWS Amplify Console``, ``AWS CodeCommit``, and related resources.

## Prerequisites

- Custom domain name registered and accessible
- Route 53 hosted zone for domain management (recommended)
- Appropriate IAM permissions for Amplify, CodeCommit, and SNS services

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Amplify&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/amplify/templates/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Amplify&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/amplify/templates/template.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-amplify.png)

## Deployment

Execute the command to deploy with `DomainName` and `RepositoryName` parameter.

```bash
aws cloudformation deploy --template-file templates/template.yaml --stack-name Amplify --parameter-overrides DomainName=xxxxx RepositoryName=xxxxx --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide parameters as follows:

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| **AlarmLevel** | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| AmplifyConsoleAppId | String |  | | **You can provide this parameter after your first deployment** |
| **DomainName** | String | | ○ | The custom domain name for your Amplify Console application |
| **RepositoryName** | String | | ○ | The repository name on CodeCommit |
| SNSForAlertArn | String | | | The Amazon SNS topic ARN for alert |
| SNSForDeploymentArn | String | | | The Amazon SNS topic ARN for deployment information |
| Environment | production / test / development | production | ○ | The environment type |
| **TagKey** | String | createdby | ○ | Tag key for resource tagging |
| **TagValue** | String | aws-cloudformation-templates | ○ | Tag value for resource tagging |

