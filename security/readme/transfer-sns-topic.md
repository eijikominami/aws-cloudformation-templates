# Transfer Alert Topic

This AWS Serverless Application Repository (SAR) application creates an Amazon SNS topic for transfer alerts with CloudWatch monitoring.

## Resources Created

- **SNS Topic**: Amazon SNS topic for transfer notifications
- **CloudWatch Alarm**: Monitors the number of messages published to the topic

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| TopicName | String | TransferAlertTopic | Name of the SNS topic |
| Environment | String | production | Environment name for tagging |
| TagKey | String | '' | Custom tag key |
| TagValue | String | '' | Custom tag value |

## Outputs

| Output | Description |
|--------|-------------|
| SNSTopicArn | ARN of the created SNS topic |

## Usage

Deploy this application through the AWS Serverless Application Repository or use the CloudFormation template directly.

## License

MIT License - see LICENSE file for details.
