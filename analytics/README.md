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
| **GlueJobTimeout** | Number | 60 | | Glue Job timeout in minutes (1–2880) |
| **GlueWorkerCount** | Number | 5 | | Number of Glue workers (2–100) |
| **CloudFrontLogDomainName** | String | | | Domain name of the CloudFront distribution. Setting this enables the CloudFront Logs feature |
| **CloudFrontLogPrefix** | String | | | S3 prefix where CloudFront access logs are stored |
| **CloudFrontLogSourceAccountId** | String | | | Source account ID for cross-account log replication |
| **CloudFrontLogSourceRoleName** | String | | | IAM role name in the source account for replication |
| **SyntheticsResultsBucketName** | String | | | S3 bucket where CloudWatch Synthetics stores results. Setting this enables the Synthetics feature |
| **SyntheticsResultsPrefix** | String | canary/ | | S3 prefix for Synthetics results |
| **GoogleAnalyticsPropertyId** | String | | | Google Analytics 4 Property ID |
| **GoogleAnalyticsAccountId** | String | | | Google Analytics 4 Account ID |
| **GoogleAnalyticsClientId** | String | | | Google OAuth2 Client Application ID (from Google Cloud Console) |
| **GoogleAnalyticsClientSecret** | String | | | Google Analytics 4 OAuth2 Client Secret |
| **GoogleAnalyticsRefreshToken** | String | | | Google Analytics 4 OAuth2 Refresh Token |
| **GoogleAnalyticsAccessToken** | String | | | Google Analytics 4 OAuth2 Access Token |
| **GitRepository** | String | | | Git repository URL for Visual ETL job source control |
| **GitOwner** | String | | | Git repository owner/organization name |
| **GitBranch** | String | main | | Git branch for Visual ETL job source control |
| **GitFolder** | String | glue-jobs | | Folder path in Git repository for job storage |
| **GitToken** | String | | | GitHub/GitLab personal access token for authentication |
| **ScheduleEnabled** | String | false | | Enable daily scheduled execution of ETL jobs (4:00 AM JST) |
| **AlarmLevel** | String | NOTICE | | CloudWatch alarm level (NOTICE or WARNING) |
| **SNSForAlertArn** | String | | | Existing SNS topic ARN for alerts. A topic is created automatically when empty |
| **SNSForDeploymentArn** | String | | | Existing SNS topic ARN for deployment notifications. A topic is created automatically when empty |
| **LogicalName** | String | analytics | ○ | Custom prefix name for resources |
| **Environment** | String | development | | Deployment environment (production / test / development) |
| **TagKey** | String | createdby | | Tag key for resource tagging |
| **TagValue** | String | aws-cloudformation-templates | | Tag value for resource tagging |

Feature activation: the CloudFront Logs resources are created when `CloudFrontLogDomainName` is set; the Synthetics resources when `SyntheticsResultsBucketName` is set; the Google Analytics resources when `GoogleAnalyticsPropertyId`, `GoogleAnalyticsAccountId`, and `GoogleAnalyticsClientSecret` are all set.

### CloudFront Logs

``AWSCloudFormationTemplates/analytics/cloudfront-logs`` creates resources for analyzing CloudFront standard access logs using AWS Glue and Amazon Athena.

This template creates:
- Glue table for the CloudFront standard log format (33 fields, LazySimpleSerDe) for the raw access logs
- Glue Crawler for schema detection of the raw logs (on-demand)
- Iceberg Glue table (`cloudfront_access_logs_iceberg`) for the transformed data
- Glue Visual ETL Job that converts the raw logs to Apache Iceberg (managed via Custom Resource)
- Lambda function for Visual ETL Job lifecycle management
- Athena WorkGroup with dedicated query result location
- Athena Named Queries for common analysis patterns (daily requests, status codes, real user access)
- IAM roles with least-privilege access for the Crawler, ETL Job, and Lambda
- Glue Trigger for daily scheduled execution of the ETL job (optional, 4:00 AM JST)

### Google Analytics

``AWSCloudFormationTemplates/analytics/google-analytics`` creates Google Analytics 4 data processing resources using AWS Glue Visual ETL.

This template creates:
- Glue Visual ETL Job for GA4 to S3 data ingestion (managed via Custom Resource)
- Glue Connection for Google Analytics 4 (OAuth2 authentication)
- Glue Table for GA4 core reports (Apache Iceberg format)
- Secrets Manager secret for OAuth2 client credentials
- Lambda function for Visual ETL Job lifecycle management
- CloudWatch Alarms for Lambda errors, Glue job failures, and estimated charges
- Glue Trigger for daily scheduled execution of the GA4 ingestion job (optional, 4:00 AM JST)

### CloudWatch Synthetics

``AWSCloudFormationTemplates/analytics/synthetics`` creates resources for analyzing CloudWatch Synthetics canary results using AWS Glue and Amazon Athena.

This template creates:
- Glue ETL Job (script-based) that reads `SyntheticsReport-*.json` and writes Apache Iceberg (managed via Custom Resource)
- Lambda function for Glue Job lifecycle management
- Athena WorkGroup with dedicated query result location
- Athena Named Queries for common analysis (recent results with duration, failure details, daily availability)
- IAM roles with least-privilege access for the ETL Job and Lambda
- Glue Trigger for daily scheduled execution of the ETL job (optional, 4:00 AM JST)

The Iceberg table `synthetics_canary_iceberg` is created and owned by the Glue job script (`createOrReplace`), not by CloudFormation.

**Design: Reading mixed file types with a Spark path filter**

CloudWatch Synthetics stores multiple file types in the same S3 prefix per run (JSON reports, PNG screenshots, HTML HAR files, log files, and Chromium crash dumps). The Glue ETL job reads only the report files by applying Spark read options:

1. `pathGlobFilter: "SyntheticsReport-*.json"` — selects only the report JSON files, excluding binary and log artifacts at read time.
2. `recursiveFileLookup: "true"` — traverses the per-run prefix structure.
3. `multiline: "true"` — each report is a single pretty-printed JSON object spanning multiple lines, so multiline parsing is required to avoid `_corrupt_record`.

The job writes the result to the Iceberg table with `createOrReplace`, and self-heals a stale catalog entry (drops the registration via the Glue API and recreates the table) when the registered Iceberg metadata file is missing in S3.

## Architecture Notes

### Visual ETL Job Management via Custom Resource

Glue Visual ETL Jobs cannot be created natively through CloudFormation. This template uses a Lambda-backed Custom Resource to manage their lifecycle (Create/Update/Delete). The Google Analytics and CloudFront Logs jobs are Visual ETL jobs (`CodeGenConfigurationNodes`); the Synthetics job is a script-based Glue job (`synthetics-to-iceberg.py`) managed through the same Custom Resource pattern.

**Key design decisions for Visual ETL creation:**

| Parameter | Required | Reason |
| --- | --- | --- |
| `JobMode: VISUAL` | ○ | Declares the job as Visual ETL |
| `CodeGenConfigurationNodes` | ○ | **Must be provided** — without this, the Glue console does not render the Visual editor |
| `Connections` | | Can be passed in `create_job`; the connection is also referenced inside `CodeGenConfigurationNodes.connectionName` |
| `SourceControlDetails` | | Sets Git integration metadata; actual push requires calling `update_source_control_from_job` separately |

> **Important**: If you delete and recreate a Visual ETL Job with the same name, the Glue console may cache the old state and not display the Visual editor. Use a new job name when recreating.

**Git integration**: The `create_job` API stores `SourceControlDetails` metadata, but **does not persist** `Owner` and `AuthToken` in `get_job` responses. To push the job to Git, the Custom Resource calls `update_source_control_from_job` after creation, which requires `RepositoryOwner` and `AuthToken` to be passed explicitly every time.

### Iceberg Table Management

The CloudFront Logs and GA4 Iceberg tables are created by CloudFormation with:
- `DeletionPolicy: Retain` — Table is preserved when the stack is deleted
- `UpdateReplacePolicy: Retain` — Table is not replaced on stack updates
- `MetadataOperation: CREATE` — Table is only created if it doesn't exist

This ensures that schema changes made manually (e.g., via Visual ETL's `EnableUpdateCatalog`) or through job execution are **never overwritten** by subsequent CloudFormation deployments.

The Synthetics Iceberg table (`synthetics_canary_iceberg`) is intentionally **not** managed by CloudFormation — it is created and owned by the Glue job script. A CFn-managed table was removed because it pre-registered a `metadata_location` whose physical metadata file did not exist in S3, causing "Location does not exist" failures.

### Custom Resource Lifecycle

| Event | Behavior |
| --- | --- |
| **Create** | Creates the Glue Visual ETL Job with `CodeGenConfigurationNodes`, then pushes to Git |
| **Update** | Updates the job with full configuration including `CodeGenConfigurationNodes`, `--conf` (Spark/Iceberg settings), and infrastructure settings (Role, Timeout, Workers) |
| **Delete** | Deletes the Glue Job |
