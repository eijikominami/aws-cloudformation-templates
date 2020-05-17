English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/security-config-rules
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiLzdYc1dVbmpHY1IvdnVCK2FrTS85dFhHMytNS2kzdEJ1YnE0MFhlc0ttanVIWWRhL1dBOTltSFZERGtZYWlmdlZnWElXWTBjcjdzSldHT0YyaGkxd01rPSIsIml2UGFyYW1ldGVyU3BlYyI6InF5RTZQQTBEYUNBVUJZU0kiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/security-config-rules`` deletes AWS resources without required tags. This template covers the following resources.

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
sam build
sam package --output-template-file packaged.yaml --s3-bucket S3_BUCKET_NAME
aws cloudformation deploy --template-file packaged.yaml --stack-name DefaultSecuritySettings-ConfigRules --s3-bucket S3_BUCKET_NAM --capabilities CAPABILITY_NAMED_IAM
```

You can provide optional parameters as follows.

| Name | Type | Default | Requied | Details | 
| --- | --- | --- | --- | --- |
| AutoRemediation | Enabled / Disabled | Disabled | ○ | If it is Enabled, **AutoRemediation** by SSM Automation and Lambda are enabled. |
| RequiredTagKey | String | createdby | ○ | AWS Config removes AWSnresouces without this tag. |
| RequiredTagValue | String | aws:cloudformation:stack | ○ | AWS Config removes AWSnresouces without this tag. |