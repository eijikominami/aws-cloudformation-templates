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
After deploying it, [**you can designate the delegated IAM AccessAnalyzer administrator account**](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-settings.html) for your organization.

### AWS Security Hub

This template enables the ``AWS Security Hub`` and sets up ``Amazon SNS`` and ``Amazon EventBridge`` to receive a message when the result of a compliance check changes to Failure.
After deploying it, **Update a configuration policy to enable Security Hub and Standards**.

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
If you integrates ``SIEM on Open Search Service`` with ``Security Lake``, [change visibility timeout of SQS from 5 minutes to 10 minutes](https://github.com/aws-samples/siem-on-amazon-opensearch-service/blob/main/docs/securitylake.md#enabling-and-configuring-security-lake).

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
| AWSCloudTrail | ENABLED / CREATED_BY_CONTROL_TOWER / DISABLED | ENABLED | Enable or disable AWS CloudTrail |
| AWSCloudTrailAdditionalFilters | String | | Additional expression of CloudWatch Logs metric filters |
| AWSCloudTrailS3Trail | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, creating trail is enabled |
| AWSConfig | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, AWS Config is enabled |
| AWSConfigAutoRemediation | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, **AWSConfigAutoRemediation** by SSM Automation and Lambda are enabled |
| AmazonGuadDuty | ENABLED / NOTIFICATION_ONLY / DISABLED | ENABLED | ○ | If it is ENABLED, Amazon GuardDuty is enabled |
| AmazonMacie | ENABLED / NOTIFICATION_ONLY / DISABLED | ENABLED | ○ | If it is ENABLED, Amazon Macie is enabled |
| AWSSecurityHub | String | STANDARDS_ONLY | ○ | If it is ENABLED, AWS Security Hub enabled |
| AWSSecurityHubStandards | CommaDelimitedList | FSBP, CIS | ○ | | The standard that you want to enable |
| EsLoaderServiceRoleArn | String | | | The ARN of lambda function aes-siem-es-loader |
| GeoLite2LicenseKeyForSIEM | String | | | The license key from MaxMind to enrich geoip location |
| IAMAccessAnalyzer | String | ACCOUNT | ○ | If it is ACCOUNT or ORGANIZATION, IAM Access Analyzer is enabled |
| IAMUserArnToAssumeAWSSupportRole | String | | | IAM User ARN to assume AWS Support role |
| LogArchiveAccountId | String | | | The id of the log archive account |
| SecurityOUId | String | | | The id of the security OU |
| SecurityLakeRoleArn | String | | | Specify IAM Role ARN to be assumed by aes-siem-es-loader |
| SecurityLakeExternalId | String | | | Specify Security Lake external ID for cross account |
| SecurityLakeSubscriberSqs | String | | | Specify SQS ARN of Security Lake Subscriber |
| SIEM | ENABLED / DISABLED | DISABLED | ○ | Enable or disable SIEM environment |
| SnsEmailForSIEM | String | | | The email as SNS topic, where Amazon OpenSearch Service will send alerts to |

### Designating a GuardDuty and a Security Hub administrator account

If you use Amazon GuardDuty or AWS Security Hub in your `Security tooling` or `Security view-only (Audit)` account, [set these accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html) as the delegated administrator accounts in the management accounts.

## Comply with the Center for Internet Security (CIS) Benchmarks

This template helps you to comply with the Center for Internet Security (CIS) Benchmarks.

| No. | Rules | Remediation |
| --- | --- | --- |
| 1.3 | Ensure credentials unused for 90 days or greater are disabled  | **Config** checks it and **Lambda** removes it automatically |
| 1.4 | Ensure access keys are rotated every 90 days or less  | **Config** checks it and **Lambda** removes it automatically |
| 1.5 | Ensure IAM password policy requires at least one uppercase letter | **Config** checks it and **SSM Automation** remediates the policy automatically |
| 1.6 | Ensure IAM password policy requires at least one lowercase letter | **Config** checks it and **SSM Automation** remediates the policy automatically |
| 1.7 | Ensure IAM password policy requires at least one symbol | **Config** checks it and **SSM Automation** remediates the policy automatically |
| 1.8 | Ensure IAM password policy requires at least one number | **Config** checks it and **SSM Automation** remediates the policy automatically |
| 1.9 | Ensure IAM password policy requires a minimum length of 14 or greater | **Config** checks it and **SSM Automation** remediates the policy automatically |
| 1.10 | Ensure IAM password policy prevents password reuse | **Config** checks it and **SSM Automation** remediates the policy automatically |
| 1.20 | Ensure a support role has been created to manage incidents with AWS Support | This template creates IAM Role for AWS Support |
| 2.1 | Ensure CloudTrail is enabled in all Regions | This template enables **CloudTrail** and related resources in all Regions |
| 2.2 | Ensure CloudTrail log file validation is enabled | This template enables **CloudTrail** and related resources in all Regions |
| 2.3 | Ensure the S3 bucket CloudTrail logs to is not publicly accessible | This template enables **CloudTrail** and related resources in all Regions |
| 2.4 | Ensure CloudTrail trails are integrated with Amazon CloudWatch Logs | This template enables **CloudTrail** and related resources in all Regions |
| 2.5 | Ensure CloudTrail trails are integrated with Amazon CloudWatch Logs | This template enables **Config** and related resources |
| 2.6 | Ensure S3 bucket access logging is enabled on the CloudTrail S3 bucket | This template enables **CloudTrail** and related resources in all Regions |
| 2.7 | Ensure CloudTrail logs are encrypted at rest using AWS KMS CMKs | This template enables **CloudTrail** and related resources in all Regions |
| 2.9 | Ensure VPC flow logging is enabled in all VPCs | **Config** checks it and **SSM Automation** enables VPC flow log automatically |
| 3.1 | Ensure VPC flow logging is enabled in all VPCs | This template creates a log metric filter and alarm |
| 3.2 | Ensure a log metric filter and alarm exist for AWS Management Console sign-in without MFA | This template creates a log metric filter and alarm |
| 3.3 | Ensure a log metric filter and alarm exist for usage of "root" account | This template creates a log metric filter and alarm |
| 3.4 | Ensure a log metric filter and alarm exist for IAM policy changes | This template creates a log metric filter and alarm |
| 3.5 | Ensure a log metric filter and alarm exist for CloudTrail configuration changes | This template creates a log metric filter and alarm |
| 3.6 | Ensure a log metric filter and alarm exist for AWS Management Console authentication failures | This template creates a log metric filter and alarm |
| 3.7 | Ensure a log metric filter and alarm exist for disabling or scheduled deletion of customer created CMKs | This template creates a log metric filter and alarm |
| 3.8 | Ensure a log metric filter and alarm exist for S3 bucket policy changes | This template creates a log metric filter and alarm |
| 3.9 | Ensure a log metric filter and alarm exist for AWS Config configuration changes | This template creates a log metric filter and alarm |
| 3.10 | Ensure a log metric filter and alarm exist for security group changes | This template creates a log metric filter and alarm |
| 3.11 | Ensure a log metric filter and alarm exist for changes to Network Access Control Lists (NACL) | This template creates a log metric filter and alarm |
| 3.12 | Ensure a log metric filter and alarm exist for changes to network gateways | This template creates a log metric filter and alarm |
| 3.13 | Ensure a log metric filter and alarm exist for route table changes | This template creates a log metric filter and alarm |
| 3.14 | Ensure a log metric filter and alarm exist for VPC changes | This template creates a log metric filter and alarm |
| 4.1| Ensure no security groups allow ingress from 0.0.0.0/0 to port 22 | **Config** checks it and **SSM Automation** remediates the rules automatically |
| 4.2| Ensure no security groups allow ingress from 0.0.0.0/0 to port 3389 | **Config** checks it and **SSM Automation** remediates the rules automatically |
| 4.3| Ensure the default security group of every VPC restricts all traffic | **Config** checks it and **SSM Automation** remediates the default security group automatically |

## Comply with the PCI DSS controls

This template helps you to comply with the PCI DSS controls.

| No. | Rules | Remediation |
| --- | --- | --- |
| PCI.CloudTrail.1 | CloudTrail logs should be encrypted at rest using AWS KMS CMKs.  | This template enables **CloudTrail** and related resources in all Regions |
| PCI.CloudTrail.2 | CloudTrail should be enabled | This template enables **CloudTrail** and related resources in all Regions |
| PCI.CloudTrail.3 | CloudTrail log file validation should be enabled | This template enables **CloudTrail** and related resources in all Regions |
| PCI.CloudTrail.4 | CloudTrail trails should be integrated with CloudWatch Logs | This template enables **CloudTrail** and related resources in all Regions |
| PCI.Config.1 | AWS Config should be enabled | This template enables **Config** and related resources in all Regions.  |
| PCI.CW.1 | A log metric filter and alarm should exist for usage of the "root" user | This template enables **CloudTrail** and related resources in all Regions |
| PCI.EC2.2 | VPC default security group should prohibit inbound and outbound traffic | **Config** checks it and **SSM Automation** remediates the default security group automatically |
| PCI.IAM.1 | IAM root user access key should not exist | **Config** checks it and **SSM Automation** remediates the default security group automatically |
| PCI.S3.4 | S3 buckets should have server-side encryption enabled | **Config** checks it and **SSM Automation** remediates the default security group automatically.s |

## Comply with the AWS Foundational Security Best Practices standard 

This template helps you to comply with the AWS Foundational Security Best Practices standard.

| No. | Rules | Remediation |
| --- | --- | --- |
| CloudTrail.1 | CloudTrail should be enabled and configured with at least one multi-Region trail | This template enables **CloudTrail** and related resources in all Regions |
| CloudTrail.2 | CloudTrail should have encryption at-rest enabled | This template enables **CloudTrail** and related resources in all Regions |
| Config.1 | AWS Config should be enabled | This template enables **Config** and related resources in all Regions |
| EC2.2 | The VPC default security group should not allow inbound and outbound traffic | **Config** checks it and **SSM Automation** remediates the default security group automatically |
| GuardDuty.1 | GuardDuty should be enabled | This template enables **GuardDuty** and related resources in all Regions |
| IAM.3 | IAM users' access keys should be rotated every 90 days or less | **Config** checks it and **SSM Automation** remediates the default security group automatically |
| IAM.4 | IAM root user access key should not exist | **Config** checks it and **SSM Automation** remediates the default security group automatically |
| S3.4 | S3 buckets should have server-side encryption enabled | **Config** checks it and **SSM Automation** remediates the default security group automatically |