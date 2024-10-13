English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/security
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates) 

``AWSCloudFormationTemplates/security`` sets basic configurations for **security**. This builds ``Amazon GuardDuty``, ``AWS Config``, ``AWS CloudTrail`` , ``AWS Security Hub`` , ``Amazon Macie`` , and related resources.

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml)  | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml) |

If you want to deploy each service individually, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| IAM | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=IAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/iam.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/iam.yaml) |
| AWS Security Hub | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SecurityHub&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/securityhub.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SecurityHub&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/securityhub.yaml) |
| Amazon GuardDuty | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=GuardDuty&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/guardduty.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=GuardDuty&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/guardduty.yaml) |
| AWS CloudTrail | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=CloudTrail&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/cloudtrail.yaml&param_LogicalName=CloudTrail) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudTrail&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/cloudtrail.yaml&param_LogicalName=CloudTrail) |
| AWS Config | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Config&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/config.yaml&param_LogicalName=Config) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Config&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/config.yaml&param_LogicalName=Config) |
| Amazon Macie | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Macie&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/macie.yaml&param_LogicalName=Macie) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Macie&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/macie.yaml&param_LogicalName=Macie) |
| Amazon Security Lake | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SecurityLake&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/securitylake.yaml&param_LogicalName=SecurityLake) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SecurityLake&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/securitylake.yaml&param_LogicalName=SecurityLake) |
| Logging | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Logging&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/logging.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Logging&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/logging.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-default-security-settings.png)

### IAM AccessAnalyzer

This template enables ``IAM Access Analyzer``. IAM Access Analyzer sends results to ``Amazon SNS`` via ``Amazon EventBridge``. 
After deploying it, [**you can designate the delegated IAM AccessAnalyzer administrator account**](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-settings.html) for your organization manually.

### AWS Security Hub

This template enables the ``AWS Security Hub`` and sets up ``Amazon SNS`` and ``Amazon EventBridge`` to receive a message when the result of a compliance check changes to Failure.
After deploying it, **Update a CloudFormation parameters to enable Security Hub and Standards**.

### Amazon GuardDuty

This template enables ``Amazon GuardDuty``. ``Amazon GuardDuty`` only sends notifications when it detects findings of **MEDIUM or higher level**.
After deploying it, [**you can designate the delegated Amazon GuardDuty administrator account**](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html) for your organization.
Choose Accounts in the navigation pane, and **Choose Enable in the banner at the top of the page**.
This action automatically turns on the Auto-enable GuardDuty configuration so that GuardDuty gets enabled for any new account that joins the organization.
Then **enable data sources in any member account** if you need.

### AWS CloudTrail

This template enables ``AWS CloudTrail`` and creates an ``S3 Bucket`` when its logs are stored.
CloudTrail Logs stored in an S3 bucket are encrypted using ``AWS KMS CMKs``.
If you have already enabled ``AWS Control Tower``, ``AWS CloudTrail`` is enabled at all account in your organizations regardless of deploying the template.

### AWS Config

This template creates an AWS Config ``delivery channel``, a ``configuration recorder`` and some ``managed rules``, as follows.

+ [CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-drift-detection-check.html)
+ [CLOUDFORMATION_STACK_NOTIFICATION_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-notification-check.html)

The following rules enable ``Automatic Remediation`` feature and attached ``SSM Automation Documents``.

+ [IAM_PASSWORD_POLICY](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)
+ [IAM_ROOT_ACCESS_KEY_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/iam-root-access-key-check.html)
+ [S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-server-side-encryption-enabled.html)
+ [VPC_FLOW_LOGS_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/vpc-flow-logs-enabled.html)
+ [VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS](https://docs.aws.amazon.com/config/latest/developerguide/vpc-sg-open-only-to-authorized-ports.html)
+ [VPC_DEFAULT_SECURITY_GROUP_CLOSED](https://docs.aws.amazon.com/config/latest/developerguide/vpc-default-security-group-closed.html)

``AWS Security Hub`` creates some related config rules for security checks automatically.
When ``AWS Config`` detects noncompliant resources, it sends a notification to ``Amazon SNS``.

If you have already enabled ``AWS Control Tower``, ``AWS Config`` is enabled at all account in your organizations regardless of deploying the template.

### Amazon Macie

This template configures ``Amazon Macie``.
After deploying it, [**you can designate the delegated Amazon Macie administrator account**](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-macie.html) for your organization.
Choose Accounts in the navigation pane, and **Choose Enable in the banner at the top of the page**.
This action automatically turns on the Auto-enable Macie configuration so that Macie gets enabled for any new account that joins the organization.

### Logging

This template builds ``Amazon Security Lake`` and [``SIEM on Open Search Service``](https://github.com/aws-samples/siem-on-amazon-opensearch-service/) using AWS CloudFormation StackSets.

If you want to use Security Lake for an organization, you must use your Organizations management account to [designate a delegated Security Lake administrator](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html#initial-account-setup).
If you integrates ``SIEM on Open Search Service`` with ``Security Lake``, [**change visibility timeout of SQS from 5 minutes to 10 minutes**](https://github.com/aws-samples/siem-on-amazon-opensearch-service/blob/main/docs/securitylake.md#enabling-and-configuring-security-lake).

After setting up the SIEM on OpenSearch Service, **add a notification configuration to the S3 bucket** by following [these steps](https://github.com/aws-samples/siem-on-amazon-opensearch-service/blob/main/docs/controltower.md#preparation-with-your-log-archive-account). Additionally, update the CloudFormation parameters as needed.

### Amazon EventBridge

This template creates ``Amazon EventBridge`` for ``AWS Health`` and ``AWS Trusted Advisor``.
EventBridge transfer its events to ``Amazon SNS``.

### Other Resources

This template creates some other resources, such as ``Service-linked Role``, ``IAM Role``, ``S3 Bucket``, ``Amazon SNS``, and so on.

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name DefaultSecuritySettings --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows:

| Name | Type | Default | Requied | Details | 
| --- | --- | --- | --- | --- |
| AuditAccountId | String | | | The id of the audit account |
| AWSCloudTrail | ENABLED / CREATED_BY_CONTROL_TOWER / DISABLED | ENABLED | | Enable or disable AWS CloudTrail |
| AWSCloudTrailAdditionalFilters | String | | | Additional expression of CloudWatch Logs metric filters |
| AWSCloudTrailS3Trail | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, creating trail is enabled |
| AWSConfig | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, AWS Config is enabled |
| AWSConfigAutoRemediation | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, **AWSConfigAutoRemediation** by SSM Automation and Lambda are enabled |
| AmazonGuadDuty | ENABLED / NOTIFICATION_ONLY / DISABLED | ENABLED | ○ | If it is ENABLED, Amazon GuardDuty is enabled |
| AmazonMacie | ENABLED / NOTIFICATION_ONLY / DISABLED | ENABLED | ○ | If it is ENABLED, Amazon Macie is enabled |
| AWSSecurityHub | String | STANDARDS_ONLY | ○ | If it is ENABLED, AWS Security Hub enabled |
| AWSSecurityHubStandards | CommaDelimitedList | FSBP, CIS | ○ | | The standard that you want to enable |
| IAMAccessAnalyzer | String | ACCOUNT | ○ | If it is ACCOUNT or ORGANIZATION, IAM Access Analyzer is enabled |
| IAMUserArnToAssumeAWSSupportRole | String | | | IAM User ARN to assume AWS Support role |
| LogArchiveAccountId | String | | | The id of the log archive account |
| SecurityOUId | String | | | The id of the security OU |
| SIEM | ENABLED / DISABLED | DISABLED | ○ | Enable or disable SIEM environment |
| SIEMControlTowerLogBucketNameList | String | | | The S3 log bucket names in the Log Archive account. **Specify after installing OpenSearch Service.** |
| SIEMControlTowerRoleArnForEsLoader | String | | | The IAM Role ARN to be assumed by aes-siem-es-loader. **Specify after installing OpenSearch Service.** |
| SIEMControlTowerSqsForLogBuckets | String | | | The SQS ARN for S3 log buckets in Log Archive Account. **Specify after installing OpenSearch Service.** |
| SIEMEsLoaderServiceRoleArn | String | | | The ARN of lambda function aes-siem-es-loader. **Specify after installing OpenSearch Service.** |
| SIEMGeoLite2LicenseKey | String | | | The license key from MaxMind to enrich geoip location |
| SIEMSecurityLakeExternalId | String | | | The Security Lake external ID for cross account. **Specify after installing OpenSearch Service.** |
| SIEMSecurityLakeRoleArn | String | | | The IAM Role ARN to be assumed by aes-siem-es-loader. **Specify after installing OpenSearch Service.** |
| SIEMSecurityLakeSubscriberSqs | String | | | The SQS ARN of Security Lake Subscriber. **Specify after installing OpenSearch Service.** |
| SIEMEmail | String | | | The email as SNS topic, where Amazon OpenSearch Service will send alerts to |

### Designating a GuardDuty and a Security Hub administrator account

If you use Amazon GuardDuty or AWS Security Hub in your `Security tooling` or `Security view-only (Audit)` account, [set these accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html) as the delegated administrator accounts in the management accounts.

## Comply with the Security Hub Standards

This template helps you to comply with the following items.

| Control Id | Rules | FSBP | CIS | Remediation |
| --- | --- | --- | --- | --- |
| CloudTrail.1 | Ensure CloudTrail is enabled in all Regions | ○ | ○ | This template enables **CloudTrail** and related resources in all Regions |
| CloudTrail.4 | Ensure CloudTrail log file validation is enabled | ○ | ○ | This template enables **CloudTrail** and related resources in all Regions |
| CloudTrail.5 | Ensure CloudTrail trails are integrated with Amazon CloudWatch Logs | ○ | ○ | This template enables **CloudTrail** and related resources in all Regions |
| CloudTrail.6 | Ensure the S3 bucket CloudTrail logs to is not publicly accessible |  | ○ | This template enables **CloudTrail** and related resources in all Region |
| CloudTrail.7 | Ensure S3 bucket access logging is enabled on the CloudTrail S3 bucket |  | ○ | This template enables **CloudTrail** and related resources in all Region |
| CloudWatch.1 | Ensure a log metric filter and alarm exist for usage of "root" account |  | ○ | This template creates a log metric filter and alarm  |
| CloudWatch.2 | Ensure VPC flow logging is enabled in all VPCs |  | ○ | This template creates a log metric filter and alarm  |
| CloudWatch.3 | Ensure a log metric filter and alarm exist for AWS Management Console sign-in without MFA |  | ○ | This template creates a log metric filter and alarm |
| CloudWatch.6 | Ensure a log metric filter and alarm exist for AWS Management Console authentication failures |  | ○ | This template creates a log metric filter and alarm |
| CloudWatch.7 | Ensure a log metric filter and alarm exist for disabling or scheduled deletion of customer created CMKs |  | ○ | This template creates a log metric filter and alarm |
| CloudWatch.8 | Ensure a log metric filter and alarm exist for S3 bucket policy changes |  | ○ | This template creates a log metric filter and alarm |
| CloudWatch.9 | Ensure a log metric filter and alarm exist for AWS Config configuration changes |  | ○ | This template creates a log metric filter and alarm |
| CloudWatch.10 | Ensure a log metric filter and alarm exist for security group changes |  | ○ | This template creates a log metric filter and alarm |
| CloudWatch.11 | Ensure a log metric filter and alarm exist for changes to Network Access Control Lists (NACL) |  | ○ | This template creates a log metric filter and alarm |
| CloudWatch.12 | Ensure a log metric filter and alarm exist for changes to network gateways |  | ○ | This template creates a log metric filter and alarm |
| CloudWatch.13 | Ensure a log metric filter and alarm exist for route table changes |  | ○ | This template creates a log metric filter and alarm |
| CloudWatch.14 | Ensure a log metric filter and alarm exist for VPC changes |  | ○ | This template creates a log metric filter and alarm |
| Config.1 | AWS Config should be enabled | ○ | ○ | ed | This template enables **Config** and related resources in all Regions |
| EC2.2 | Ensure the default security group of every VPC restricts all traffic | ○ | ○ | **Config** checks it and **SSM Automation** remediates the policy automatically |
| EC2.6 | Ensure VPC flow logging is enabled in all VPCs | ○ | ○ | **Config** checks it and **SSM Automation** remediates the policy automatically |
| EC2.13 | Ensure no security groups allow ingress from 0.0.0.0/0 to port 22 |  | ○ | **Config** checks it and **SSM Automation** remediates the policy automatically |
| EC2.14 | Ensure no security groups allow ingress from 0.0.0.0/0 to port 3389 |  | ○ | **Config** checks it and **SSM Automation** remediates the policy automatically |
| IAM.3 | Ensure access keys are rotated every 90 days or less | ○ | ○ | **Config** checks it and **Lambda** removes it automatically |
| IAM.4 | IAM root user access key should not exist	| ○ | ○ | **Config** checks it and **SSM Automation** remediates the policy automatically |
| IAM.7 | Password policies for IAM users should have strong configurations | ○ | ○ | **Config** checks it and **SSM Automation** remediates the policy automatically |
| IAM.18 | Ensure a support role has been created to manage incidents with AWS Support | ○ | ○ | This template creates IAM Role for AWS Support |
| IAM.22 | Ensure credentials unused for 45 days or greater are disabled | ○ | ○ | **Config** checks it and **Lambda** removes it automatically |
| S3.17 | S3 buckets should have server-side encryption enabled | | | **Config** checks it and **SSM Automation** remediates the policy automatically |