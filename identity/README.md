English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/identity
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/network`` sets AWS Identity Services to manage identities, resources, and permissions securely and at scale.

## TL;DR

If you just want to deploy the stack, click the button below.

| Services | Launchers |
| --- | --- |
| AWS Managed Microsoft AD | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MicrosoftAD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/microsoftad.yaml) |

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file microsoftad.yaml --stack-name MicrosoftAD
```

You can provide optional parameters as follows.

### Allow seamless directory sharing across multiple AWS accounts

Choose the **Scale & share** tab and in the **Shared directories** section, choose **Actions**, and then choose **Create new shared directory**. On the **Choose which AWS accounts to share with page**, choose one of the following sharing methods depending on your business needs.

### AWS Managed Microsoft AD

This template configures ``AWS Managed Microsoft AD``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| Edition | Standard / Enterprise | Standard | ○ | The edition of AWS Directory Service for Microsoft Active Directory |
| EnableSso | true / false | true | ○ | Whether to enable single sign-on for a Microsoft Active Directory in AWS |
| Name | String | corp.example.com | ○ | The fully qualified domain name for the AWS Managed Microsoft AD directory |
| Password | String | Password1+ | ○ | The password for the default administrative user named Admin |
| ShortName | String | CORP | ○ | The NetBIOS name for your domain |
| SubnetPrivateCidrBlockForAz1 | String | 10.0.0.0/24 | conditional | The private subnet CIDR block at AZ1 |
| SubnetPrivateIdForAz1 | String | 10.0.0.2/24 | conditional | The private subnet id at AZ1 |
| SubnetPrivateCidrBlockForAz2 | String | 10.0.1.0/24 | conditional | The private subnet CIDR block at AZ2 |
| SubnetPrivateIdForAz1 | String | 10.0.3.0/24 | conditional | The private subnet id at AZ2 |
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway |
| VPCCidrBlock | String | String | 10.0.0.0/21 | The VPC CIDR block |