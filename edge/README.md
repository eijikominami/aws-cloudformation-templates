English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/edge
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/edge`` builds edge services.

## TL;DR

If you just want to deploy the stack, click the button below.

| Services | Launchers |
| --- | --- |
| CloudFront | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudFront&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/edge/cloudfront.yaml) |
| Realtime Dashboard | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=RealtimeDashboard&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/edge/realtime-dashboard.yaml) |
| WAF | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WAF&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/edge/waf.yaml) |

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file cloudfront.yaml --stack-name CloudFront --capabilities CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file realtime-dashboard.yaml --stack-name RealtimeDashboard --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file waf.yaml --stack-name WAF --capabilities CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows.

### CloudFront

This template creates ``CloudFront`` distribution.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| CertificateManagerARN | String | | | If it's NOT empty, **SSL Certification** is associated with **CloudFront** |
| CloudFrontAdditionalName | String | | | If it's NOT empty, **Alias name** is set on **CloudFront** |
| CloudFrontDefaultRootObject | String | index.html | | CloudFront Viewer Protocol Policy |
| CloudFrontDefaultTTL | Number | 86400 | ○ | CloudFront Default TTL |
| CloudFrontMinimumTTL | Number | 0 | ○ | CloudFront Minimum TTL |
| CloudFrontMaximumTTL | Number | 31536000 | ○ | CloudFront Maximum TTL |
| CloudFrontOriginAccessIdentity | String | | Conditional | The origin access identity |
| **CloudFrontOriginDomainName** | String | | ○ | The origin domain | 
| CloudFrontOriginShield | true or false | false | ○ | A flag that specifies whether Origin Shield is enabled |
| CloudFrontOriginType | S3 or NOT_S3 | S3 | ○ | The Origin Type | 
| CloudFrontRestrictViewerAccess | ENABLED / DISABLED | DISABLED | ○ | Enable or disable Restrict Viewer Access |
| CloudFrontSecondaryOriginId | String | | | If it's NOT empty, **Secondary S3 bucket** is associated with **CloudFront** |
| CloudFrontViewerProtocolPolicy | allow-all / redirect-to-https / https-only | redirect-to-https | ○ | CloudFront Viewer Protocol Policy |
| CloudFront403ErrorResponsePagePath | String | | | The path to the 403 custom error page |
| CloudFront404ErrorResponsePagePath | String | | | The path to the 404 custom error page |
| CloudFront500ErrorResponsePagePath | String | | | The path to the 500 custom error page |
| **DomainName** | String | | ○ | The CNAME attached to CloudFront |
| RealtimeDashboardElasticSearchVolumeSize | Number | 10 | ○ | The volume size (GB) of ElasticSearch Service |
| RealtimeDashboardElasticSearchInstanceType | String | r5.large.elasticsearch | ○ | The instance type of Elasticsearch Service |
| RealtimeDashboardElasticSearchMasterType | String | r5.large.elasticsearch | ○ | The master type of Elasticsearch Service |
| RealtimeDashboardElasticSearchLifetime | Number | 1 | ○ | The lifetime (hour) of ElasticSearch Service |
| RealtimeDashboardElasticSearchMasterUserName | String | root | ○ | The user name of Elasticsearch Service |
| RealtimeDashboardElasticSearchMasterUserPassword | String | Password1+ | ○ | The password of Elasticsearch Service |
| RealtimeDashboardElasticsearchVersion | String | 7.8 | ○ | The version of Elasticsearch Service |
| RealtimeDashboardKinesisFirehoseStreamNameSuffix | String | default | ○ | The suffix of the Kinesis Firehose stream |
| RealtimeDashboardState | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, Real-time Dashboard is enabled |
| RealtimeDashboardSamplingRate | Number | 100 | ○ | The sampling rate of logs sent by CloudFront |
| RealtimeDashboardKinesisShardCount | Number | 1 | ○ | The shard count of Kinesis |
| RealtimeDashboardKinesisNumberOfPutRecordThreshold | Number | 12000000 | ○ | The threshold of PutRecord API calls |
| RealtimeKinesisNumberOfPutRecordThreshold | Number | | | The threshold of PutRecord API calls |
| Route53HostedZoneId | String | | | Route53 hosted zone id |
| S3DestinationBucketArnOfCrossRegionReplication | String | | | If it's NOT empty, Cross region replication is enabled on **S3** |
| SyntheticsCanaryName | String | | | If it's NOT empty, CloudWatch Synthetics is enabled |
| UserAgent | String | | | The secret key that 'User-Agent' header contains | 
| Logging | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, Logging is enabled on **CloudFront** and **S3** |
| LogBucketName | String | | Conditional | The custom S3 bucket name for access logging |
| WebACLArn | String | | | The ARN of Web ACL |

### Realtime Dashboard

This template creates an environment about CloudFront realtime dashboard.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| ElasticSearchVolumeSize | Number | 10 | ○ | The volume size (GB) of ElasticSearch Service |
| ElasticSearchDomainName | String | cloudfront-realtime-logs | ○ | The domain name of ElasticSearch Service |
| ElasticSearchInstanceType | String | r5.large.elasticsearch | ○ | The instance type of Elasticsearch Service |
| ElasticSearchMasterType | String | r5.large.elasticsearch | ○ | The master type of Elasticsearch Service |
| ElasticSearchLifetime | Number | 1 | ○ | The lifetime (hour) of ElasticSearch Service |
| ElasticSearchMasterUserName | String | root | ○ | The user name of Elasticsearch Service |
| ElasticSearchMasterUserPassword | String | Password1+ | ○ | The password of Elasticsearch Service |
| ElasticsearchVersion | String | 7.8 | ○ | The version of Elasticsearch Service |
| SamplingRate | Number | 100 | ○ | The sampling rate of logs sent by CloudFront |
| KinesisFirehoseStreamNameSuffix | String | default | ○ | The suffix of the Kinesis Firehose stream |
| KinesisShardCount | Number | 1 | ○ | The shard count of Kinesis |
| KinesisNumberOfPutRecordThreshold | Number | 12000000 | ○ | The threshold of PutRecord API calls |

### WAF

This template sets ``AWS WAF``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| Scope | REGIONAL or CLOUDFRONT | REGIONAL | ○ | Specifies whether this is for an Amazon CloudFront distribution or for a regional application |
| **TargetResourceArn** | String | | ○ | The ARN of the resource to associate with the web ACL |