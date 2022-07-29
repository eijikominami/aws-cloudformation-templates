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

### Global Accelerator

This template configures ``Global Accelerator``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| EndpointId | String | ○ | | The Amazon Resource Name (ARN) of the ELB, the Elastic IP address or  the EC2 instance ID |
| EndpointGroupRegion | String | ○ | | The AWS Regions where the endpoint group is located |
| FromPort | Number | | 80 |  The first port in the range of ports, inclusive |
| HealthCheckIntervalSeconds | 10 / 30 | | 30 | The time—10 seconds or 30 seconds—between health checks for each endpoint |
| HealthCheckPath | String | | / | If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks |
| HealthCheckPort | Number | | 80 | The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group |
| HealthCheckProtocol | TCP / HTTP / HTTPS | | TCP | The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group |
| IpAddressType | IPV6 / IPV4 | | IPV4 | The IP address type that an accelerator supports |
| Name | String | | Default | The name of the accelerator |
| Protocol | TCP / UDP | | TCP | The protocol for the connections from clients to the accelerator |
| ThresholdCount | Number | | 3 | The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy |
| ToPort | Number | | 80 | The last port in the range of ports, inclusive |

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