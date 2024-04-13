English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates
![GitHub Stars](https://img.shields.io/github/stars/eijikominami/aws-cloudformation-templates.svg?style=social&label=Stars)
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates`` contains basic Cloudformation templates.

> [!NOTE]
> You can also get useful sample templates at [**eijikominami/aws-cloudformation-samples**](https://github.com/eijikominami/aws-cloudformation-samples).

## Templates

This project contains **Cloudformation templates** as follows.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| [All-in-One](/cicd/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=CICD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cicd/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CICD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cicd/template.yaml) |
| [Amplify Console](/amplify/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Amplify&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/amplify/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Amplify&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/amplify/template.yaml) |
| [Analytics](/analytics/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Anlytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Anlytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) |
| [**CloudOps**](/cloudops/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=CloudOps&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudOps&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/template.yaml) |
| [CloudWatch alarm](/monitoring/README.md) | | |
| [Delete Resources without Required Tags](/security-config-rules/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DefaultSecuritySettings-ConfigRules&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security-config-rules/packaged.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings-ConfigRules&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security-config-rules/packaged.yaml) |
| [EC2-based Web Servers](/web-servers/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=WebServers&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WebServers&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/template.yaml) |
| [Global Settings](/global/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=GlobalSettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/global/template.yaml) | |
| [Identity](/identity/README.md) | | |
| [Media](/media/README.md) | | [Sample templates](https://github.com/eijikominami/aws-cloudformation-samples/tree/master/media) |
| [**Network**](/network/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/template.yaml) |
| [**Security**](/security/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml) |
| [Send Notification to Slack](/notification/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Notification&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/notification/packaged.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Notification&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/notification/packaged.yaml) |
| [Shared Servivces](/shared/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) |
| [**Static Website Hosting**](/static-website-hosting-with-ssl/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting-with-ssl/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting-with-ssl/template.yaml) |

## Environment

This project uses the following modules.

| Service | Resource | Version |
| --- | --- | --- |
| Amazon CloudWatch Synthetics | Runtime | syn-nodejs-puppeteer-6.2 |
| AWS CodeBuild | Image | aws/codebuild/amazonlinux2-aarch64-standard:2.0 (Python 3.9) |
| Amazon EBS | Volume Type | gp3 |
| Amazon EC2 | Amazon Linux 2 Default AMI Id | ami-03dceaabddff8067e |
| Amazon EC2 | Microsoft Windows Server 2022 Default AMI Id | ami-0659e3a420d8a74ea |
| AWS Glue | GlueVersion | 4.0 |
| AWS Glue | PythonVersion | 3 |
| AWS Lambda | CodeGuru Profiler | [AWSCodeGuruProfilerPythonAgentLambdaLayer:11 (Python 3.9)](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-lambda-layers.html) |
| AWS Lambda | Lambda Insights | [LambdaInsightsExtension-Arm64:11](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/Lambda-Insights-extension-versionsARM.html) |
| AWS Lambda | Python | 3.9 |
| AWS Serverless Repository | aws-usage-queries | 0.1.5+19.38c7b8 |
| AWS Systems Manager | SSM Document Schema (Automation) | 0.3 |
| AWS Systems Manager | SSM Document Schema (Command) | 2.2 |
| Amazon OpenSearch Service | OpenSearch | OpenSearch_2.11 |
| Elastic Load Balancer | SSL Policy | ELBSecurityPolicy-TLS13-1-2-2021-06 |

## Architecture

The following section describes the individual components of the architecture.

![](images/architecture.png)

### Security Template

![](images/architecture-default-security-settings.png)

### Delete Resources without Required Tags

![](images/architecture-delete-resources-without-required-tags.png)

### Global Settings Template

![](images/architecture-global.png)

### Static Website Hosting Template

![](images/architecture-static-website-hosting.png)

### Network Template

![](images/architecture-network.png)

### EC2-based Web Servers Template

![](images/architecture-web-servers.png)

### Synthetics Monitoring Template

![](images/architecture-cloudops.png)

### Shared Services

![](images/architecture-shared.png)

### CloudOps Template

![](images/architecture-cloudops.png)

### Send Notification to Slack

![](images/architecture-notification.png)

### Amplify Console Template

![](images/architecture-amplify.png)