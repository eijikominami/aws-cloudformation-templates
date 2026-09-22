English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/analytics
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/analytics`` creates analytics data processing infrastructure including Google Analytics 4 integration and CloudFront access log analysis.

## Prerequisites

Before deploying this template, ensure you have:

- An S3 bucket with CloudFront access logs (for CloudFront Logs feature)
- Google Analytics 4 property with API access enabled (for Google Analytics feature)
- OAuth 2.0 credentials configured in Google Cloud Console (for Google Analytics feature)
- An S3 bucket with CloudWatch Synthetics results (for Synthetics feature)

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) |

## Architecture

The three pipelines share one Glue database, one Athena WorkGroup and one S3 table bucket. Each raw source is read by its own Glue job and written as an Apache Iceberg table in that bucket, which the Glue Data Catalog exposes to Athena through a federated `s3tablescatalog`.

Table and column names must be lowercase. S3 Tables does not expose a table whose name or definition contains capital letters, and Athena rejects such a query with `Unsupported Federation Resource - Invalid table or column names` even when the bucket is integrated.

The CloudFront Logs and Google Analytics jobs are Visual ETL jobs. CloudFormation creates the job shell only, and the flow is built in the Glue console and kept in a separate job definitions repository. The Synthetics job is script-based and is declared as `AWS::Glue::Job`.
## Deployment

Execute the command to deploy with SAM CLI.

```bash
cd sam-app
sam build
sam deploy --guided
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details |
| --- | --- | --- | --- | --- |
| **CloudFrontLogDomainName** | String | | | Domain name of the CloudFront distribution |
| CloudFrontLogPrefix | String | | | S3 prefix where CloudFront access logs are stored |
| CloudFrontLogSourceAccountId | String | | | Source account ID for cross-account log replication |
| CloudFrontLogSourceRoleName | String | | | IAM role name in the source account for replication |
| **SyntheticsSourcePaths** | String | | ○ | Comma-separated S3 paths holding Synthetics reports, one per Canary artifact bucket |
| SyntheticsLookbackDays | Number | 3 | | Days of report folders each Synthetics run reads |
| GoogleAnalyticsClientId | String | | | Google OAuth2 Client Application ID (from Google Cloud Console) |
| **GoogleAnalyticsClientSecret** | String | | | Google Analytics 4 OAuth2 Client Secret |
| GoogleAnalyticsRefreshToken | String | | | Google Analytics 4 OAuth2 Refresh Token |
| GoogleAnalyticsAccessToken | String | | | Google Analytics 4 OAuth2 Access Token |
| QuickAccountId | String | | | AWS account ID of the Amazon Quick account allowed cross-account Athena access |
| LogicalName | String | analytics | ○ | Custom prefix name for resources |

Feature activation: the CloudFront Logs resources are created when `CloudFrontLogDomainName` is set; the Synthetics resources when `SyntheticsSourcePaths` is set; the Google Analytics resources when `GoogleAnalyticsClientSecret` is set.

Every ETL job runs at 19:00 UTC (4:00 AM JST).

### CloudFront Logs

``AWSCloudFormationTemplates/analytics/cloudfront-logs`` creates resources for analyzing CloudFront standard access logs using AWS Glue and Amazon Athena.

### Google Analytics

``AWSCloudFormationTemplates/analytics/google-analytics`` creates Google Analytics 4 data processing resources using AWS Glue Visual ETL.

### CloudWatch Synthetics

``AWSCloudFormationTemplates/analytics/synthetics`` creates resources for analyzing CloudWatch Synthetics canary results using AWS Glue and Amazon Athena.
