English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/network
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/network`` sets VPC and network elements.

## TL;DR

If you just want to deploy the stack, click the button below.

| Services | Launchers |
| --- | --- |
| TransitGateway | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) |
| VPN | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) |

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file transitgateway.yaml --stack-name TransitGateway
aws cloudformation deploy --template-file vpn.yaml --stack-name VPN
```

You can provide optional parameters as follows.

### Transit Gateway

This template configures ``Transit Gateway``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| **CertificateManagerARN** | List<AWS::EC2::Subnet::Id> | | ○ | The IDs of one or more subnets |
| **CertificateManagerARN** | AWS::EC2::VPC::Id | | ○ | The ID of the VPC |

### VPN

This template configures ``Site-to-Site VPN``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| **CustomerGatewayOutsideIpAddress** | String | | ○ | The Internet-routable IP address for the customer gateway's outside interface |
| StaticRoutesOnly | true or false | false | ○ | Indicates whether the VPN connection uses static routes only |
| TransitGatewayId | String | | ○ | The ID of the transit gateway associated with the VPN connection | 