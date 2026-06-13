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

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) |

If you want to deploy each service individually, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| CloudFront Logs | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Analytics-CloudFrontLogs&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/cloudfront-logs.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Analytics-CloudFrontLogs&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/cloudfront-logs.yaml) |

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
| **CloudFrontLogPrefix** | String | | | S3 prefix where CloudFront access logs are stored |
| **CloudFrontLogSourceAccountId** | String | | | Source account ID for cross-account replication |
| **CloudFrontLogSourceRoleName** | String | | | IAM role name in source account for replication |
| **GoogleAnalyticsPropertyId** | String | | | Google Analytics 4 Property ID |
| **GoogleAnalyticsAccountId** | String | | | Google Analytics 4 Account ID |
| **GoogleAnalyticsClientSecret** | String | | | Google Analytics 4 OAuth2 Client Secret |
| **GlueJobTimeout** | Number | 60 | | Glue Job timeout in minutes |
| **GlueWorkerCount** | Number | 5 | | Number of Glue workers |
| **LogicalName** | String | analytics | ○ | Custom prefix name for resources |

### CloudFront Logs

``AWSCloudFormationTemplates/analytics/cloudfront-logs`` creates resources for analyzing CloudFront standard access logs using AWS Glue and Amazon Athena.

This template creates:
- Glue table for CloudFront standard log format (33 fields, LazySimpleSerDe)
- Glue Crawler for schema detection (on-demand)
- Athena WorkGroup with dedicated query result location
- Athena Named Queries for common analysis patterns (daily requests, status codes, real user access)
- IAM role with least-privilege access for the Crawler

| Name | Type | Default | Required | Details |
| --- | --- | --- | --- | --- |
| **AccessLogPrefix** | String | | ○ | S3 prefix where CloudFront access logs are stored |
| **DomainName** | String | | ○ | Domain name of the CloudFront distribution |
| **GlueDatabaseName** | String | | ○ | Name of the Glue Data Catalog database |
| **LogicalName** | String | | ○ | Logical name for resource naming |
| **QueryResultsBucketName** | String | | ○ | Name of the S3 bucket for Athena query results |
| **RawDataBucketName** | String | | ○ | Name of the S3 bucket for raw data |
| **SourceAccountId** | String | | | Source account ID for cross-account replication |
| **SourceRoleName** | String | | | IAM role name in source account for replication |

### Google Analytics

``AWSCloudFormationTemplates/analytics/google-analytics`` creates Google Analytics 4 data processing resources using AWS Glue Visual ETL.
