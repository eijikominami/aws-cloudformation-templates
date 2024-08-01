English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates
![GitHub Stars](https://img.shields.io/github/stars/eijikominami/aws-cloudformation-templates.svg?style=social&label=Stars)
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
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
| [Media](/media/README.md) | | |
| [**Network**](/network/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/template.yaml) |
| [**Security**](/security/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml) |
| [Send Notification to Slack](/notification/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Notification&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/notification/packaged.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Notification&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/notification/packaged.yaml) |
| [Shared Servivces](/shared/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) |
| [**Static Website Hosting**](/static-website-hosting-with-ssl/README.md) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting-with-ssl/template.yaml) | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting-with-ssl/template.yaml) |

## Environment

This project uses the following modules.

| Service | Resource | Version |
| --- | --- | --- |
| Amazon CloudWatch Synthetics | [Runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html) | syn-nodejs-puppeteer-9.0 |
| AWS CodeBuild | [Image](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) | aws/codebuild/amazonlinux2-aarch64-standard:2.0 (Python 3.9) |
| Amazon EBS | Volume Type | gp3 |
| Amazon EC2 | Amazon Linux 2 Default AMI Id | ami-03dceaabddff8067e |
| Amazon EC2 | Microsoft Windows Server 2022 Default AMI Id | ami-0659e3a420d8a74ea |
| AWS Glue | [GlueVersion](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html) | 4.0 |
| AWS Glue | PythonVersion | 3 |
| AWS Lambda | [CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/python-lambda-layers.html) | AWSCodeGuruProfilerPythonAgentLambdaLayer:11 (Python 3.9) |
| AWS Lambda | [Lambda Insights](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/Lambda-Insights-extension-versionsARM.html) | LambdaInsightsExtension-Arm64:11 |
| AWS Lambda | Python | 3.9 |
| AWS Serverless Repository | aws-usage-queries | 0.1.5+19.38c7b8 |
| AWS Systems Manager | [SSM Document Schema (Automation)](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-schemas-features.html) | 0.3 |
| AWS Systems Manager | [SSM Document Schema (Command)](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-schemas-features.html) | 2.2 |
| Amazon OpenSearch Service | [OpenSearch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/release-notes.html) | OpenSearch_2.13 |
| Elastic Load Balancer | [SSL Policy](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) | ELBSecurityPolicy-TLS13-1-2-2021-06 |

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