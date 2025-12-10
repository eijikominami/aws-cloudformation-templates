# Transfer SNS Topic

This AWS Serverless Application Repository (SAR) application creates resources for cross-region SNS topic message forwarding using Lambda.

## Overview

This application enables forwarding of SNS messages from a source topic to a destination topic across regions, solving cross-region messaging requirements.

## Resources Created

- **Lambda Function**: Forwards messages from source to destination SNS topic
- **IAM Role**: Provides necessary permissions for Lambda execution
- **CloudWatch Log Group**: Stores Lambda execution logs
- **SNS Subscription**: Connects source topic to Lambda function
- **Lambda Permission**: Allows SNS to invoke the Lambda function
- **CloudWatch Alarm**: Monitors Lambda function performance

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| AlarmLevel | String | NOTICE | The alarm level of CloudWatch alarms (NOTICE/WARNING) |
| SourceSNSArn | String | - | The ARN of the source SNS topic that messages will be forwarded from |
| DestinationSNSArn | String | - | The ARN of the destination SNS topic that messages will be forwarded to |
| LogicalName | String | TransferSNS | The custom prefix name |
| Environment | String | production | Environment name (production/test/development) |
| TagKey | String | createdby | Custom tag key |
| TagValue | String | aws-cloudformation-templates | Custom tag value |

## Usage

Deploy this application through the AWS Serverless Application Repository or use the CloudFormation template directly.

### Example

```yaml
Resources:
  TransferSNSApplication:
    Type: AWS::Serverless::Application
    Properties:
      Location:
        ApplicationId: arn:aws:serverlessrepo:us-east-1:172664222583:applications/transfer-sns-topic
        SemanticVersion: 1.0.0
      Parameters:
        SourceSNSArn: arn:aws:sns:us-east-1:123456789012:source-topic
        DestinationSNSArn: arn:aws:sns:us-west-2:123456789012:destination-topic
        LogicalName: MyTransfer
        Environment: production
```

## Features

- **Cross-Region Support**: Forward messages between SNS topics in different regions
- **Message Preservation**: Maintains original message content and subject
- **Monitoring**: Built-in CloudWatch alarms for Lambda monitoring
- **Tagging**: Comprehensive resource tagging for management
- **Security**: Least-privilege IAM permissions

## License

MIT License - see LICENSE file for details.
