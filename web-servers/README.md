English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/web-servers
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/web-servers`` builds ``Network Load Balancer``, ``VPC`` and ``EC2`` instances and related resources for **EC2-based website hosting**.

## Prerequisites

Before deploying this template, ensure you have:

- VPC and subnets configured for EC2 instances and load balancers
- Key pair created for EC2 instance access
- Understanding of Auto Scaling and load balancing requirements
- S3 bucket for storing deployment artifacts and logs

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=WebServers&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WebServers&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/template.yaml) |

If you want to deploy each service individually, click the buttons below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| Data Lifecycle Manager | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DataLifecycleManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/dlm.yaml&param_LogicalName=DataLifecycleManager) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DataLifecycleManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/dlm.yaml&param_LogicalName=DataLifecycleManager) |
| WAF | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/edge/waf.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/edge/waf.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-web-servers.png)

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name WebServers --capabilities CAPABILITY_NAMED_IAM
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AccountIdForAnalysis | String | | | The AWS account id for log analysis |
| ACMValidationMethod | String | DNS | Conditional | The validation method that you own or control the domain |
| ACMDomainName | String | | | The domain name created by Certification Manager |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| AutoScalingMaxSize | Number | 1 | ○ | |
| AutoScalingLoadBalancerType | None, application, network | None | ○ | If you set 'None', an ELB is NOT created |
| BucketNameForAnalysis | String | | | The Amazon S3 bucket name for log analysis |
| BucketNameForArtifact | String | | | The bucket name artifact art stored |
| CentralizedLogBucketName | String | | | The centralize S3 bucket name for logging |
| CertificateManagerARN | String | | | If it's NOT empty, **SSL Certification** is associated with **CloudFront** or **Elastic Load Balancer** |
| CloudFrontDefaultTTL | Number | 86400 | ○ | CloudFront Default TTL |
| CloudFrontMinimumTTL | Number | 0 | ○ | CloudFront Minimum TTL |
| CloudFrontMaximumTTL | Number | 31536000 | ○ | CloudFront Maximum TTL |
| CloudFrontViewerProtocolPolicy | allow-all / redirect-to-https / https-only | redirect-to-https | ○ | CloudFront Viewer Protocol Policy |
| CloudFrontAdditionalName | String | | | If it's NOT empty, **Alias name** is set on **CloudFront** |
| CloudFrontSecondaryOriginId | String | | | If it's NOT empty, **Secondary S3 bucket** is associated with **CloudFront** |
| CloudFrontRestrictViewerAccess | ENABLED / DISABLED | DISABLED | ○ | Enable or disable Restrict Viewer Access |
| CloudFront403ErrorResponsePagePath | String | | | The path to the 403 custom error page |
| CloudFront404ErrorResponsePagePath | String | | | The path to the 404 custom error page |
| CloudFront500ErrorResponsePagePath | String | | | The path to the 500 custom error page |
| CodeStarConnectionArn | String | | | The Amazon Resource Name (ARN) of the CodeStar connection |
| ComputeType | INSTANCE / CONTAINER / APPRUNNER | INSTANCE | ○ | The category of computing platform |
| DesiredCapacity | Number | 1 | ○ | If it's NOT Disabled, AutoScalingGroup and Network Load Balancer are created | 
| DockerFilePath | String | | | The path of Dockerfile | 
| DomainName | String | | | Domain name | 
| EC2DailySnapshotScheduledAt | String | 17:00 | ○ | Starting time of daily snapshot. (UTC) |
| EC2ImageId | AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> | /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64 | ○ | Amazon Linux 2023 AMI (HVM), SSD Volume Type (64bit x86) |
| EC2InstanceType | String | t3.micro | ○ | | 
| EC2PatchingAt | Number | 3 | ○ | Starting time of patching process |
| EC2KeyName | String | | |  If it's empty, **SSH key** will NOT be set |
| EC2VolumeSize | Number | 8 | ○ | |
| GitHubOwnerNameForArtifact | String | | | The GitHub owner name of the artifact repository |
| GitHubRepoNameForArtifact | String | | | The GitHub repository name of the artifact repository |
| GitHubBranchNameForArtifact | String | | | The Branch name of GitHub for the artifact repository |
| GitHubBranchNameForBuildSpec | String | | | The Branch name of GitHub for Buildspec |
| **GlobalInfrastructure** | NONE / CLOUDFRONT / GLOBAL_ACCELERATOR | NONE | ○ | Enable or disable CloudFront, Global Accelerator |
| Logging | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, Logging is enabled |
| LogGroupNameTransferredToS3 | String | | | The log group name transfferd to an S3 bucket |
| Route53HostedZoneId | String | | | Route53 hosted zone id |
| SubnetPrivateCidrBlockForAz1 | String | 10.1.0.0/24 | ○ | Private subnet of AZ1 |
| SubnetPrivateCidrBlockForAz2 | String | 10.1.2.0/24 | ○ | Private subnet of AZ2 |
| SubnetPrivateCidrBlockForAz3 | String | 10.1.4.0/24 | ○ | Private subnet of AZ3 |
| SubnetPublicCidrBlockForAz1 | String | 10.1.1.0/25 | ○ | Public subnet of AZ1 |
| SubnetPublicCidrBlockForAz2 | String | 10.1.3.0/25 | ○ | Public subnet of AZ2 |
| SubnetPublicCidrBlockForAz3 | String | 10.1.5.0/25 | ○ | Public subnet of AZ3 |
| SubnetTransitCidrBlockForAz1 | String | 10.1.1.128/25 | ○ | Transit subnet of AZ1 |
| SubnetTransitCidrBlockForAz2 | String | 10.1.3.128/25 | ○ | Transit subnet of AZ2 |
| SubnetTransitCidrBlockForAz3 | String | 10.1.5.128/25 | ○ | Transit subnet of AZ3 |
| TransitGatewayId | String | | | The ID of a transit gateway |
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway |
| VPCCidrBlock | String | 10.1.0.0/21 | ○ | The VPC CIDR block |
| WebACL | ENABLED / DISABLED | DISABLED | ○ | If **Disabled** is set, AWS WAF does NOT created |
| WebACLArnForCloudFront | String | | | Web ACL ARN for CloudFront |

## Troubleshooting

### SSM State Manager Issues

If `SSM State Manager Association` already has `AWS-GatherSoftwareInventory`, the template will **fail**. Deploy this template with the `IgnoreResourceConflicts` option enabled.

### EC2 Instance Issues

If EC2 instances are not launching or are unhealthy:

1. Verify that the AMI ID is valid and available in your region
2. Check that the instance type is available in the selected availability zones
3. Ensure that the key pair exists if SSH access is required
4. Verify that security groups allow the necessary traffic for your application

### Load Balancer Issues

If the load balancer is not distributing traffic correctly:

1. Verify that target groups have healthy instances registered
2. Check that security groups allow traffic between the load balancer and instances
3. Ensure that health check settings are appropriate for your application
4. Verify that the load balancer is deployed in the correct subnets

### Auto Scaling Issues

If Auto Scaling is not working as expected:

1. Check that the launch template or configuration is correct
2. Verify that the Auto Scaling group has the correct subnets configured
3. Ensure that scaling policies are properly configured
4. Monitor CloudWatch metrics to understand scaling behavior

### CodePipeline/CodeDeploy Issues

If CI/CD pipeline is failing:

1. Verify that the GitHub connection is properly configured
2. Check that the CodeBuild project has the necessary permissions
3. Ensure that the deployment configuration matches your application requirements
4. Review CloudWatch Logs for detailed error messages
