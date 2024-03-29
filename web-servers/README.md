English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/web-servers
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/web-servers`` builds ``Network Load Balancer``, ``VPC`` and ``EC2`` instances and related resources for **EC2-based website hosting**.

## TL;DR

If you just want to deploy the stack, click the button below.

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WebServers&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/template.yaml) 

If you want to deploy each service individually, click the buttons below.

| Services | Launchers |
| --- | --- |
| Data Lifecycle Manager | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DataLifecycleManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/dlm.yaml&param_LogicalName=DataLifecycleManager) |
| WAF | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/edge/waf.yaml) |

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
| AutoScalingMaxSize | Number | 1 | ○ | |
| AutoScalingLoadBalancerType | None, application, network | None | ○ | If you set 'None', an ELB is NOT created |
| ACMValidationMethod | String | DNS | Conditional | The validation method that you own or control the domain |
| ACMDomainName | String | | | The domain name created by Certification Manager |
| BucketNameForAnalysis | String | | | The Amazon S3 bucket name for log analysis |
| BucketNameForArtifact | String | | | The bucket name artifact art stored |
| CertificateManagerARN | String | | | If it's NOT empty, **SSL Certification** is associated with **CloudFront** or **Elastic Load Balancer** |
| DesiredCapacity | Number | 1 | ○ | If it's NOT Disabled, AutoScalingGroup and Network Load Balancer are created | 
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
| DomainName | String | | | Domain name | 
| EC2DailySnapshotScheduledAt | String | 17:00 | ○ | Starting time of daily snapshot. (UTC) |
| EC2ImageId | AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> | /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64 | ○ | Amazon Linux 2 AMI (HVM), SSD Volume Type (64bit x86) |
| EC2InstanceType | String | t3.micro | ○ | | 
| EC2PatchingAt | Number | 3 | ○ | Starting time of patching process |
| EC2KeyName | String | | |  If it's empty, **SSH key** will NOT be set |
| EC2VolumeSize | Number | 8 | ○ | |
| GlobalInfrastructure | NONE / CLOUDFRONT / GLOBAL_ACCELERATOR | | ○ | Enable or disable CloudFront, Global Accelerator |
| Route53HostedZoneId | String | | | Route53 hosted zone id |
| SubnetPublicCidrBlockForAz1 | String | 10.0.0.0/24 | ○ | Public subnet of AZ1 |
| SubnetPublicCidrBlockForAz2 | String | 10.0.4.0/24 | ○ | Public subnet of AZ2 |
| TransitGatewayId | String | | | The ID of a transit gateway |
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway |
| WebACL | ENABLED / DISABLED | DISABLED | ○ | If **Disabled** is set, AWS WAF does NOT created |
| WebACLArnForCloudFront | String | | | Web ACL ARN for CloudFront |
| VPCCidrBlock | String | 10.0.0.0/21 | ○ | The VPC CIDR block |

## Trouble Shooting

If `SSM State Manager Association` already has `AWS-GatherSoftwareInventory`, the template will **fail**. Deploy this template with the `IgnoreResourceConflicts` option enabled.