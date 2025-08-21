English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/analytics
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/analytics`` creates AWS Glue resources for data analytics and ETL processing with Google Analytics 4 integration.

## Prerequisites

- Google Analytics 4 property with API access enabled
- Google Cloud Console project with Analytics Reporting API enabled
- OAuth 2.0 credentials (Client ID and Client Secret) configured for your application
- Appropriate IAM permissions for AWS Glue, Secrets Manager, and S3 services

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/sam-app/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/sam-app/template.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-analytics.png)

## Deployment

Execute the command to deploy with SAM CLI.

```bash
cd sam-app
sam build
sam deploy --guided
```

You can provide parameters as follows.

| Name | Type | Default | Required | Details |
| --- | --- | --- | --- | --- |
| **LogicalName** | String | GoogleAnalytics | ○ | The custom prefix name for resources |
| **GoogleAnalyticsPropertyId** | String | | ○ | The Google Analytics 4 Client ID |
| **GoogleAnalyticsClientSecret** | String | | ○ | The client secret for Google Analytics 4 OAuth application |
| **GoogleAnalyticsAccountId** | String | | ○ | The Google Analytics 4 Account ID |
| **GoogleAnalyticsPropertyNumber** | String | | ○ | The Google Analytics 4 Property Number |
| **TagKey** | String | createdby | ○ | Tag key for resource tagging |
| **TagValue** | String | aws-cloudformation-templates | ○ | Tag value for resource tagging |

## Troubleshooting

### Visual ETL Editor Not Showing Job

If the Glue job doesn't appear in AWS Glue Studio Visual ETL editor:

1. Verify that the job has `CodeGenConfigurationNodes` in its definition
2. Use AWS CLI to add Visual ETL metadata:
   ```bash
   aws glue get-job --job-name {LogicalName}-GA4-ETL-Job
   ```
3. If `CodeGenConfigurationNodes` is missing, update the job using AWS CLI

### OAuth Authentication Issues

If you encounter OAuth authentication errors:

1. Verify that the Google Analytics Reporting API is enabled in Google Cloud Console
2. Check that the OAuth 2.0 credentials are correctly configured
3. Ensure the client secret is properly stored in AWS Secrets Manager
4. Verify that the Google Analytics account has appropriate permissions

### Glue Job Execution Failures

If the Glue job fails to execute:

1. Check CloudWatch logs for detailed error messages
2. Verify that the Google Analytics connection is properly configured
3. Ensure the specified Google Analytics account and property exist and are accessible
4. Check IAM permissions for the Glue service role

![](../images/architecture-analytics.png)