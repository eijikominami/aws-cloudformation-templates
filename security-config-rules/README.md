English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/security-config-rules
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/security-config-rules`` deletes AWS resources without required tags. This template covers the following resources.

## Prerequisites

Before deploying this template, ensure you have:

- AWS Config service enabled and configured
- S3 bucket for SAM deployment artifacts
- Understanding of resource tagging strategy and policies
- Appropriate IAM permissions for Config rules and Lambda functions

+ Amazon S3 - Bucket
+ Amazon DynamoDB - Table
+ Amazon API Gateway - API
+ AWS Lambda - Function

```bash
.
├── README.md                       <-- Instructions file (Japanese)
├── README_EN.md                    <-- This instructions file
└── sam-app
    ├── checkRequiredTags           <-- Source code for a lambda function（AWS Config Custom Rules）
    │   ├── lambda_function.py      <-- Lambda function code
    │   └── requirements.txt        <-- List of items to be installed using pip install
    ├── deleteUnapplicableResources <-- Source code for a lambda function
    │   ├── lambda_function.py      <-- Lambda function code
    │   └── requirements.txt        <-- List of items to be installed using pip install
    └── template.yaml               <-- SAM Template
```

## TL;DR

1. Before running this Cloudformation template, run  ``Security`` template in this project.

+ [Security Template](../security/README.md)

2. Click one of the two buttons below.

+ [delete-resources-without-required-tags - AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~delete-resources-without-required-tags)
+ [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings-ConfigRules&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security-config-rules/packaged.yaml)

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-delete-resources-without-required-tags.png)

## Deployment

Execute the command to deploy.

```bash
cd sam-app
sam build
sam package --output-template-file packaged.yaml --s3-bucket S3_BUCKET_NAME
aws cloudformation deploy --template-file packaged.yaml --stack-name DefaultSecuritySettings-ConfigRules --s3-bucket S3_BUCKET_NAME --capabilities CAPABILITY_NAMED_IAM
```

You can provide optional parameters as follows.

| Name | Type | Default | Requied | Details | 
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| AWSConfigAutoRemediation | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, **AWSConfigAutoRemediation** by SSM Automation and Lambda are enabled |
| RequiredTagKey | String | createdby | ○ | AWS Config removes AWSnresouces without this tag |
| RequiredTagValue | String | aws-cloudformation-templates | ○ | AWS Config removes AWS resources without this tag |

## Troubleshooting

### Config Rule Issues

If Config rules are not evaluating resources correctly:

1. Verify that AWS Config is enabled and recording the resource types you want to monitor
2. Check that the Lambda function for custom Config rules has the correct permissions
3. Ensure that the Config rule parameters match your tagging requirements
4. Monitor CloudWatch Logs for the Config rule Lambda function for any errors

### Resource Deletion Issues

If resources are not being deleted as expected:

1. Verify that the auto-remediation Lambda function has the necessary permissions to delete resources
2. Check that the resources are actually non-compliant according to your tagging rules
3. Ensure that the deletion Lambda function is being triggered by Config rule compliance changes
4. Review CloudWatch Logs for the deletion Lambda function to identify any errors

### False Positive Deletions

If resources are being deleted incorrectly:

1. Review your tag key and value requirements to ensure they're not too restrictive
2. Check that the Config rule evaluation logic correctly identifies compliant resources
3. Consider implementing a grace period or notification before deletion
4. Test the Config rules in a non-production environment first

### Permission Issues

If Lambda functions are failing due to permissions:

1. Verify that the Lambda execution role has the necessary permissions for Config and resource deletion
2. Check that cross-account permissions are configured if resources span multiple accounts
3. Ensure that service-linked roles are created for AWS Config
4. Review IAM policies to ensure they allow the required actions on target resources