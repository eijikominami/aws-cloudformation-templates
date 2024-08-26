English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/shared
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/shared`` builds shared services in your AWS Organizations accounts.

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) |

If you want to deploy each service individually, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| FluentBit (Syslog) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=FluentBit&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/fluentbit.yaml)  | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=FluentBit&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/fluentbit.yaml) |

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
| AccountIdForArchive | String | | | The AWS account id for log archive |
| ActiveDirectoryEdition | Enterprise / Standard | Standard | ○ | The edition of AWS Directory Service for Microsoft Active Directory |
| ActiveDirectoryEnableSso | true / false | true | ○ | Whether to enable single sign-on for a Microsoft Active Directory in AWS |
| ActiveDirectoryName | String | corp.example.com | ○ | The fully qualified domain name for the AWS Managed Microsoft AD directory |
| ActiveDirectoryPassword | String | Password1+ | ○ | The password for the default administrative user named Admin |
| ActiveDirectoryShortName | String | CORP | ○ | The NetBIOS name for your domain |
| ActiveDirectorySubnetCidrBlockForAz1 | String | 10.3.0.64/26 | ○ | The public subnet CIDR block at AZ1 |
| ActiveDirectorySubnetCidrBlockForAz2 | String | 10.3.64.64/26 | ○ | The public subnet CIDR block at AZ2 |
| ActiveDirectorySubnetCidrBlockForAz3 | String | 10.3.128.64/26 | ○ | The public subnet CIDR block at AZ3 |
| BucketNameForArchive | String | | | The Amazon S3 bucket name for log archive |
| DomainName | String | | | The private domain name which this VPC has |
| FluentBitForSyslog | ENABLED / DISABLED | true | ○ | Whether to enable FluentBit for collecting syslog format logs |
| IdentityCenterArn | String | | | The ARN of the IAM Identity Center instance under which the operation will be executed |
| SubnetPrivateCidrBlockAz1 | String | 10.3.0.64/26 | ○ | The private subnet CIDR block at AZ1 |
| SubnetPrivateCidrBlockAz2 | String | 10.3.64.64/26 | ○ | The private subnet CIDR block at AZ2 |
| SubnetPrivateCidrBlockAz3 | String | 10.3.128.64/26 | ○ | The private subnet CIDR block at AZ3 |
| SubnetTransitCidrBlockAz1 | String | 10.3.0.128/26 | ○ | The transit subnet CIDR block at AZ1 |
| SubnetTransitCidrBlockAz2 | String | 10.3.64.128/26 | ○ | The transit subnet CIDR block at AZ2 |
| SubnetTransitCidrBlockAz3 | String | 10.3.128.128/26 | ○ | The transit subnet CIDR block at AZ3 |
| ResolverRuleId | String | | | The ID of the Resolver rule that you associated with the VPC that is specified by VPCId |
| TransitGatewayId | String | | | The ID of a transit gateway |
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway |
| VPCCidrBlock | String | 10.3.0.0/16 | ○ | The VPC CIDR block |

### Fluentbit

This template configures FluentBit for Syslog.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| AccountIdForArchive | String | | | The AWS account id for log archive |
| AppPort | Number | 514 | ○ | The port on which the container is listening |
| BucketNameForArchive | String | | | The Amazon S3 bucket name for log archive |
| Cpu | Number | 1024 | ○ | The number of cpu units reserved for the container |
| CpuArchitecture | String | ARM64 | The CPU architecture |
| DesiredCapacity | String | 1 | ○ | The number of instantiations |
| SubnetIdAz1 | AWS::EC2::Subnet::Id | | ○ | The subnet id at AZ1 |
| SubnetIdAz2 | AWS::EC2::Subnet::Id | | ○ | The subnet id at AZ2 |
| SubnetIdAz3 | AWS::EC2::Subnet::Id | | ○ | The subnet id at AZ3 |
| Memory | String | 3072 | ○ | The amount (in MiB) of memory to present to the container |
| VPCCidrBlock | String | 10.3.0.0/16 | ○ | The VPC CIDR block |
| VPCId | AWS::EC2::VPC::Id | | ○ | VPC Id | 

### Trusted access with IAM Identity Center

You can enable trusted access using either the AWS IAM Identity Center console or the AWS Organizations console and connect with AWS Managed Microsoft AD manually.