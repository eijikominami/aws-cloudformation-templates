English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/analytics
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates) 

``AWSCloudFormationTemplates/analytics`` builds a data analytics platform with ``Amazon AppFlow``, ``AWS Glue`` , and related resources.

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) | 

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-analytics.png)

## Deployment

When you connect to Google Analytics, [Set up a new OAuth client](https://aws.amazon.com/jp/blogs/big-data/analyzing-google-analytics-data-with-amazon-appflow-and-amazon-athena/) and get the authorization code via Google API.

```bash
https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=GOOGLE_ANALYTICS_CLIENT_ID&redirect_uri=https://AWS_REGION.console.aws.amazon.com/appflow/oauth&scope=https://www.googleapis.com/auth/analytics.readonly&access_type=offline
```

Then execute the command to deploy.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name Analytics --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows:

| Name | Type | Default | Requied | Details | 
| --- | --- | --- | --- | --- |
| AppFlowConnectorProfileName | String |  |  | The profile name of AppFlow Connector for Google Analytics |
| AppFlowGoogleAnalyticsObject | String |  |  | The object of Google Analytics |
| AppFlowScheduleRate | Number | 24 | ◯ | The rate at which the scheduled flow will run |
| CloudFrontLogPrefix | String |  |  | The S3 prefix that is used in the configuration of your Amazon CloudFront distribution for log storage |
| SourceAccountIAMRoleArn | String |  |  | The role arn of account id source bucket is contained |
| GlueDatabaseName | String | datalake | ◯ | Prefix that is used for the created resources (20 chars, a-z, 0-9 and _ only) |
| S3AccessLogPrefix | String |  |  | The S3 prefix that is used in the configuration of your Amazon S3 distribution for log storage |