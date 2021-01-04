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
| Data Lifecycle Manager | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DataLifecycleManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/dlm.yaml&param_LogicalNamePrefix=DataLifecycleManager) |
| Systems Manager | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/ssm.yaml&param_LogicalNamePrefix=SystemsManager) |
| WAF | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/network/waf.yaml) |

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
| AutoScalingDesiredCapacity | Number | 1 | ○ | If it's NOT Disabled, AutoScalingGroup and Network Load Balancer are created. | 
| AutoScalingMaxSize | Number | 1 | ○ | |
| AutoScalingLoadBalancerType | None, application, network | None | ○ | If you set 'None', an ELB is NOT created. |
| CertificateManagerARN | String | | | If it's NOT empty, **SSL Certification** is associated with **Elastic Load Balancer**. |
| DomainName | String | | | The CNAME attached to Elastic Load Balancer | 
| EC2DailySnapshotScheduledAt | String | 17:00 | ○ | Starting time of daily snapshot. (UTC) |
| EC2ImageId | AWS::EC2::Image::Id | ami-068a6cefc24c301d2 | ○ | Amazon Linux 2 AMI (HVM), SSD Volume Type (64bit x86) |
| EC2InstanceType | String | t3.micro | ○ | | 
| EC2PatchingAt | Number | 3 | ○ | Starting time of patching process. |
| EC2KeyName | String | | |  If it's empty, **SSH key** will NOT be set. |
| EC2VolumeSize | Number | 8 | ○ | |
| IgnoreResourceConflicts | ENABLED / DISABLED | DISABLED | ○ | If **Enabled** is set, the resources does NOT created. |
| Route53HostedZoneId | String | | | Route53 hosted zone id |
| SSMPatchingAt | Number | 3 | ○ | Starting time of patching process. (Local Time) |
| SubnetPublicCidrBlockForAz1 | String | 10.0.0.0/24 | ○ | Public subnet of AZ1 |
| SubnetExternalCidrBlockForAz1 | String | 10.0.1.0/24 | ○ | Private subnet of AZ1 |
| SubnetPublicCidrBlockForAz2 | String | 10.0.4.0/24 | ○ | Public subnet of AZ2 |
| SubnetExternalCidrBlockForAz2 | String | 10.0.5.0/24 | ○ | Private subnet of AZ2 |
| WebACL | ENABLED / DISABLED | DISABLED | ○ | If **Disabled** is set, AWS WAF does NOT created. |
| VPCCidrBlock | String | 10.0.0.0/21 | ○ | |

## Trouble Shooting

If `SSM State Manager Association` already has `AWS-GatherSoftwareInventory`, the template will **fail**. Deploy this template with the `IgnoreResourceConflicts` option enabled.