English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/shared
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/shared`` builds shared services in your AWS Organizations accounts.

## TL;DR

If you just want to deploy the stack, click the button below.

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) 

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-shared.png)

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name SharedServices --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| ActiveDirectoryEdition | Enterprise / Standard | Standard | ○ | The edition of AWS Directory Service for Microsoft Active Directory |
| ActiveDirectoryEnableSso | true / false | true | ○ | Whether to enable single sign-on for a Microsoft Active Directory in AWS |
| ActiveDirectoryName | String | corp.example.com | ○ | The fully qualified domain name for the AWS Managed Microsoft AD directory |
| ActiveDirectoryPassword | String | Password1+ | ○ | The password for the default administrative user named Admin |
| ActiveDirectoryShortName | String | CORP | ○ | The NetBIOS name for your domain |
| ActiveDirectorySubnetCidrBlockForAz1 | String | 10.1.0.64/26 | ○ | The public subnet CIDR block at AZ1 |
| ActiveDirectorySubnetCidrBlockForAz2 | String | 10.1.1.64/26 | ○ | The public subnet CIDR block at AZ2 |
| SubnetTransitCidrBlockAz1 | String | 10.3.1.0/24 | ○ | The transit subnet CIDR block at AZ1 |
| SubnetTransitCidrBlockAz2 | String | 10.3.5.0/24 | ○ | The transit subnet CIDR block at AZ2 |
| TransitGatewayId | String | | | The ID of a transit gateway |
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway |
| VPCCidrBlock | String | 10.3.0.0/16 | ○ | The VPC CIDR block |

### Trusted access with IAM Identity Center

You can enable trusted access using either the AWS IAM Identity Center console or the AWS Organizations console and connect with AWS Managed Microsoft AD manually.