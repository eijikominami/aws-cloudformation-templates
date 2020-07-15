English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates`` contains basic Cloudformation templates.

## AWS SAM–based Serverless Applications

This project contains **AWS SAM–based serverless applications** and they are published on the ``AWS Serverless Application Repository``.

| Application Name | Link |
| --- | --- |
| [codepipeline-default-settings](cicd/codepipeline-default-settings.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~codepipeline-default-settings) |
| [cloudwatch-alarm-about-apigateway](monitoring/cloudwatch-alarm-about-apigateway.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-apigateway) |
| [cloudwatch-alarm-about-codebuild](monitoring/cloudwatch-alarm-about-codebuild.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-codebuild) |
| [cloudwatch-alarm-about-dynamodb-throttle](monitoring/cloudwatch-alarm-about-dynamodb-throttle.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-dynamodb-throttle) |
| [cloudwatch-alarm-about-dynamodb](monitorining/cloudwatch-alarm-about-dynamodb.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-dynamodb) |
| [cloudwatch-alarm-about-ec2](monitoring/cloudwatch-alarm-about-ec2.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-ec2) |
| [cloudwatch-alarm-about-events](monitoring/cloudwatch-alarm-about-events.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-events) |
| [cloudwatch-alarm-about-kinesis-data-streams](monitoring/cloudwatch-alarm-about-kinesis-data-streams.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-kinesis-data-streams) |
| [cloudwatch-alarm-about-lambda](monitoring/cloudwatch-alarm-about-lambda.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-lambda) |
| [cloudwatch-alarm-about-natgateway](monitoring/cloudwatch-alarm-about-natgateway.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-natgateway) |
| [cloudwatch-alarm-about-sns](monitoring/cloudwatch-alarm-about-sns.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-sns) |
| [sns-topic](notification/sns-topic.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~sns-topic) |
| [eventbridge-rules](eventbridge-rules.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~eventbridge-rules) |
| [delete-resources-without-required-tags](security-config-rules/delete-resources-without-required-tags.md) | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~delete-resources-without-required-tags) |

## Templates

This project contains **Cloudformation templates** as follows.

| Template Name | AWS Region Code | Launch |
| --- | --- | --- |
| [All-in-One Template](/cicd/README.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CICD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cicd/template.yaml) |
| [**Security Template**](/security/README.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml) |
| [Delete Resources without Required Tags](/security-config-rules/README.md) | | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings-ConfigRules&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security-config-rules/packaged.yaml) |
| [Global Settings Template](/global/README.md) | us-east-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=GlobalSettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/global/template.yaml) |
| [Static Website Hosting Template](/static-website-hosting-with-ssl/README.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting-with-ssl/template.yaml)  |
| [EC2-based Web Servers Template](/web-servers/README.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WebServers&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/template.yaml)  |
| [Systems Manager Template](/web-servers/README.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/ssm.yaml&param_LogicalNamePrefix=SystemsManager) |
| [Send Notification to Slack](/notification/README.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Notification&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/notification/packaged.yaml) |
| [Amplify Template](/amplify/README.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Amplify&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/amplify/template.yaml) |
| [CloudWatch Alarm Template](/monitoring/README.md) | | |

## Architecture

The following section describes the individual components of the architecture.

![](images/architecture.png)

### Security Template

![](images/architecture-default-security-settings.png)

### Delete Resources without Required Tags

![](images/architecture-delete-resources-without-required-tags.png)

### Static Website Hosting Template

![](images/architecture-static-website-hosting.png)

### Global Settings Template

![](images/architecture-global.png)

### EC2-based Web Servers Template

![](images/architecture-web-servers.png)

### Amplify Template

![](images/architecture-amplify.png)

### Send Notification to Slack

![](images/architecture-notification.png)