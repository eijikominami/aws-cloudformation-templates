English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/static-website-hosting
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/static-website-hosting`` builds ``Amazon CloudFront``, ``Amazon S3`` and related resources for **static website hosting**.

## Prerequisites

Before deploying this template, ensure you have:

- Domain name registered and Route53 hosted zone configured
- SSL certificate created in AWS Certificate Manager (in us-east-1 for CloudFront)
- S3 bucket for storing website artifacts and logs
- Understanding of CloudFront distribution and caching behavior

## TL;DR

If you just want to deploy the stack follow these steps.

1. Before running this Cloudformation template, run both the ``Security`` template and ``Global Settings`` template in this project.

+ [Security Template](../security/README.md)
+ [Global Settings Template](../global/README.md)

2. Click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting/template.yaml) |

If you want to deploy each service individually, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| Synthetics | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Synthetics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/synthetics-heartbeat.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Synthetics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/synthetics-heartbeat.yaml) |
| Real-time Dashboard | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=RealtimeLogs&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/edge/realtime-dashboard.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=RealtimeLogs&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/edge/realtime-dashboard.yaml) |
| WAF | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/edge/waf.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/edge/waf.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-static-website-hosting.png)

### Amazon S3

#### Origin

This template create an S3 bucket as origin for web distributions.
S3 allows to be accessed from CloudFront using an ``origin access identity`` (``OAI``) , but denies direct access from anonimous users.

#### Log Bucket

Logs generated by S3 and CloudFront are stored in an S3 bucket created by this template.

### Amazon CloudFront

This template creates a CloudFront.
It supports ``Custom Domain Name with ACM``, ``Aliases``, ``Origin Access Identity``, ``Secondary Origin`` and ``Logging``.

### AWS WAF

This template can attach ``AWS WAF`` with Amazon CloudFront.
It enables [**AWS Managed Rules rule**](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html) as follows.

+ AWSManagedRulesCommonRuleSet
+ AWSManagedRulesAdminProtectionRuleSet
+ AWSManagedRulesKnownBadInputsRuleSet
+ AWSManagedRulesAmazonIpReputationList

### Synthetics Stack

This template creates a nested stack for monitoring.
See [here](../cloudops/README.md) for the detail on this stack.

### Real-time Dashboard Stack

This template creates a nested stack for real-time dashboard using CloudFront logs.
It contains the following resources.

#### Amazon Kinesis Data Streams

The real-time logs generated by Amazon CloudFront are integrated with ``Amazon Kinesis Data Streams`` to enable delivery of these logs to a generic HTTP endpoint using ``Amazon Kinesis Data Firehose``.

#### Amazon Kinesis Data Firehose and related resouces

``Amazon Kinesis Data Firehose`` delivers the logs to ``Amazon S3`` and ``Amazon OpenSearch Service``.
Kinesis Data Firehose invoke an ``AWS Lambda`` function to process logs, and update the log format.
Kinesis Data Firehose sends logs to ``Amazon S3`` bucket where it is unable to deliver the data to Elasticsearch. 

#### Amazon OpenSearch Service

you can create real-time dashboards, set up alerts, and investigate anomalies or respond to operational events quickly on ``Amazon OpenSearch Service``. 
Common data points that can be tracked include the number of viewer requests originating from different geographical regions and the number of unique viewers experiencing increased latency.

## Deployment

Execute the command to deploy with ``DomainName`` parameter.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name StaticWebsiteHosting --parameter-overrides DomainName=XXXXX CertificateManagerARN=XXXXX
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AccountIdForAnalysis | String | | | The AWS account id for log analysis |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| BucketNameForAnalysis | String | | | The Amazon S3 bucket name for log analysis |
| BucketNameForArtifact | String | | | The bucket name artifact art stored |
| CertificateManagerARN | String | | | If it's NOT empty, **SSL Certification** is associated with **CloudFront** |
| CloudFrontAdditionalMetrics | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, additional metrics is enabled |
| CloudFrontDefaultTTL | Number | 86400 | ○ | CloudFront Default TTL |
| CloudFrontMinimumTTL | Number | 0 | ○ | CloudFront Minimum TTL |
| CloudFrontMaximumTTL | Number | 31536000 | ○ | CloudFront Maximum TTL |
| CloudFrontViewerProtocolPolicy | allow-all / redirect-to-https / https-only | redirect-to-https | ○ | CloudFront Viewer Protocol Policy |
| CloudFrontAdditionalName | String | | | If it's NOT empty, **Alias name** is set on **CloudFront** |
| CloudFrontOriginShield | true or false | false | ○ | A flag that specifies whether Origin Shield is enabled |
| CloudFrontSecondaryOriginId | String | | | If it's NOT empty, **Secondary S3 bucket** is associated with **CloudFront** |
| CloudFrontRestrictViewerAccess | ENABLED / DISABLED | DISABLED | ○ | Enable or disable Restrict Viewer Access |
| CloudFront403ErrorResponsePagePath | String | | | The path to the 403 custom error page |
| CloudFront404ErrorResponsePagePath | String | | | The path to the 404 custom error page |
| CloudFront500ErrorResponsePagePath | String | | | The path to the 500 custom error page |
| CloudWatchAppicationSignals | ENABLED / DISABLED | ENABLED | | If it is ENABLED, Logging is enabled on **Internet Monitor** and **CloudWatch Synthetics**  |
| CodeStarConnectionArn | String | | | The Amazon Resource Name (ARN) of the CodeStar connection |
| **DomainName** | String | | ○ | The CNAME attached to CloudFront |
| GitHubOwnerNameForWebsite | String | | | The GitHub owner name of the contents repository |
| GitHubRepoNameForWebsite | String | | | The GitHub repository name of the contents repository |
| GitHubBranchNameForWebsite | String | | | The Branch name of GitHub for the contents repository |
| Logging | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, Logging is enabled on **CloudFront** and **S3** |
| RealtimeDashboardElasticSearchVolumeSize | Number | 10 | ○ | The volume size (GB) of ElasticSearch Service |
| RealtimeDashboardElasticSearchInstanceType | String | r5.large.elasticsearch | ○ | The instance type of OpenSearch Service |
| RealtimeDashboardElasticSearchMasterType | String | r5.large.elasticsearch | ○ | The master type of OpenSearch Service |
| RealtimeDashboardElasticSearchLifetime | Number | 1 | ○ | The lifetime (hour) of ElasticSearch Service |
| RealtimeDashboardElasticSearchMasterUserName | String | root | ○ | The user name of OpenSearch Service |
| RealtimeDashboardElasticSearchMasterUserPassword | String | Password1+ | ○ | The password of OpenSearch Service |
| RealtimeDashboardElasticsearchVersion | String | OpenSearch_2.13 | ○ | The version of OpenSearch Service |
| RealtimeDashboardState | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, Real-time Dashboard is enabled |
| RealtimeDashboardSamplingRate | Number | 100 | ○ | The sampling rate of logs sent by CloudFront |
| RealtimeDashboardKinesisShardCount | Number | 1 | ○ | The shard count of Kinesis |
| RealtimeDashboardKinesisNumberOfPutRecordThreshold | Number | 12000000 | ○ | The threshold of PutRecord API calls |
| Route53HostedZoneId | String | | | Route53 hosted zone id |
| S3DestinationBucketArnOfCrossRegionReplication | String | | | If it's NOT empty, Cross region replication is enabled on **S3** |
| SyntheticsCanaryName | String | | | If it's NOT empty, CloudWatch Synthetics is enabled |
| WebACLArn | String | | | The ARN of Web ACL |

### Manual Deployment

#### Origin failover

You can add ``secondary origin server`` in ``CloudFront`` by this CloudFormation Template, but it does **NOT suppport** creating ``Origin Group``.
Therefore create ``Origin Group`` and edit ``Default Cache Behavior Settings`` manually after comleting CloudFormation deployment.

1. Create ``Origin Group`` with ``Origins`` and ``Failover criteria`` .
2. Change ``Origin or Origin Group`` at ``Default Cache Behavior Settings`` to ``Origin Group`` you created.
## Troubleshooting

### CloudFront Issues

If CloudFront distribution is not serving content correctly:

1. Verify that the origin S3 bucket exists and contains the website files
2. Check that the Origin Access Identity (OAI) has proper permissions to access the S3 bucket
3. Ensure that the SSL certificate is valid and issued for the correct domain
4. Verify that the Route53 hosted zone is properly configured with the correct DNS records

### SSL Certificate Issues

If SSL certificate is not working with CloudFront:

1. Ensure that the certificate is created in the us-east-1 region (required for CloudFront)
2. Verify that the certificate includes all necessary domain names (primary and aliases)
3. Check that the certificate validation is complete and the certificate is issued
4. Ensure that the certificate ARN is correctly specified in the template parameters

### S3 Access Issues

If S3 bucket access is not working properly:

1. Verify that the S3 bucket policy allows access from the CloudFront OAI
2. Check that the bucket is not blocking public access when it should allow CloudFront access
3. Ensure that the website files are uploaded to the correct S3 bucket
4. Verify that the default root object is configured correctly in CloudFront

### WAF Issues

If WAF is blocking legitimate traffic:

1. Review WAF logs to identify which rules are blocking traffic
2. Adjust WAF rule configurations or add exceptions for legitimate traffic
3. Monitor CloudWatch metrics for WAF to understand traffic patterns
4. Consider adjusting rate limiting rules if they're too restrictive

### Real-time Dashboard Issues

If the real-time dashboard is not showing data:

1. Verify that CloudFront real-time logs are enabled and configured correctly
2. Check that Kinesis Data Streams is receiving data from CloudFront
3. Ensure that the OpenSearch Service cluster is healthy and accessible
4. Verify that the Lambda function for log processing is working correctly