English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/network
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/network`` sets VPC and network elements.

## TL;DR

If you just want to deploy the stack, click the button below.

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/template.yaml)

If you want to deploy each service individually, click the button below.

| Services | Launchers |
| --- | --- |
| Availability Zone | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=AvailabilityZone&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/az.yaml) |
| Global Accelerator | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=GlobalAccelerator&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/globalaccelerator.yaml) |
| IPAM | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IPAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/ipam.yaml) |
| Network Firewall | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=NetworkFirewall&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkfirewall.yaml) |
| Route 53 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Route53&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/route53.yaml) |
| TransitGateway | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) |
| VPN | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-network.png)

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file az.yaml --stack-name AvailabilityZone
aws cloudformation deploy --template-file globalaccelerator.yaml --stack-name GlobalAccelerator
aws cloudformation deploy --template-file route53.yaml --stack-name Route53
aws cloudformation deploy --template-file transitgateway.yaml --stack-name TransitGateway
aws cloudformation deploy --template-file vpn.yaml --stack-name VPN
```

You can provide optional parameters as follows:

| Name | Type | Default | Requied | Details | 
| --- | --- | --- | --- | --- |
| IPAMProvisionedCidrs | String | 10.0.0.0/8 | ○ | The CIDR provisioned to the IPAM pool | 
| PrincipalsToAssociateWithIPAM | String | | | Specifies a list of one or more principals to associate with IPAM | 
| PrincipalsToAssociateWithTransitGateway | String | | | Specifies a list of one or more principals to associate with Transit Gateway | 
| SubnetPublicCidrBlockForAz1 | String | 10.0.0.0/26 | ○ | The public subnet CIDR block at AZ1 | 
| SubnetTransitCidrBlockAz1 | String | 10.0.0.64/26 | ○ | The transit subnet CIDR block at AZ1 | 
| SubnetPrivateCidrBlockForAz1 | String | 10.0.1.0/24 | ○ | The public subnet CIDR block at AZ1 | 
| SubnetFirewallCidrBlockForAz1 | String | 10.0.0.128/26 | ○ | The firewall subnet CIDR block at AZ1 | 
| SubnetPublicCidrBlockForAz2 | String | 10.0.4.0/26 | ○ | The public subnet CIDR block at AZ2 | 
| SubnetTransitCidrBlockAz2 | String | 10.0.4.64/26 | ○ | The transit subnet CIDR block at AZ2 | 
| SubnetPrivateCidrBlockForAz2 | String | 10.0.5.0/24 | ○ | The public subnet CIDR block at AZ2 | 
| SubnetFirewallCidrBlockForAz2 | String | 10.0.4.128/26 | ○ | The firewall subnet CIDR block at AZ2 | 
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway | 
| VPCCidrBlock | String | 10.0.0.0/16 | ○ | The VPC CIDR block | 

### Integrate IPAM with AWS Organizations

If you use Amazon Transit Gateway or Amazon VPC IP Address Manager (IPAM) in your `Network` account, enable `AWS Resource Access Manager` in `AWS Organizations`.

### Availability Zone

This template configures ``Availability Zone``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AvailabilityZone | AWS::EC2::AvailabilityZone::Name | | ○ | The Availability Zone name |
| InternetGatewayId | String | | | The Internet Gateway Id |
| SubnetPublicCidrBlock | String | 10.0.0.0/24 | ○ | The Public subnet CIDR block |
| SubnetTransitCidrBlock | String | | | The transit subnet CIDR block |
| SubnetFirewallCidrBlock | String | | | The firewall subnet CIDR block |
| TransitGatewayId | String | | | The ID of a transit gateway |
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway |
| VPCId | AWS::EC2::VPC::Id | | ○ | The VPC id  |

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

### IP Address Manager (IPAM)

This template configures ``IP Address Manager (IPAM)``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| PrincipalsToAssociateWithIPAM | String | | | Specifies a list of one or more principals to associate with IPAM |
| ProvisionedCidrs | String | 10.0.0.0/8 | ○ | The CIDR provisioned to the IPAM pool |

### Network Firewall

This template configures ``Network Firewall``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| SubnetIdAz1 | String | | | The firewall subnet id in AZ1 |
| SubnetIdAz2 | String | | | The firewall subnet id in AZ2 |
| SubnetIdAz3 | String | | | The firewall subnet id in AZ3 |

### Route 53

This template configures ``Route 53``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| SecurityGroupId | AWS::EC2::SecurityGroup::Id | | ○ | The ID of one or more security groups that control access to this VPC. |
| SubnetId1 | String | | ○ | The ID of the subnet that DNS queries originate from |
| SubnetId2 | String | | | The ID of the subnet that DNS queries originate from |
| SubnetId3 | String | | | The ID of the subnet that DNS queries originate from |

### Transit Gateway

This template configures ``Transit Gateway``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| PrincipalsToAssociateWithTransitGateway | String | | | Specifies a list of one or more principals to associate with Transit Gateway |

### VPN

This template configures ``Site-to-Site VPN``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| **CustomerGatewayOutsideIpAddress** | String | | ○ | The Internet-routable IP address for the customer gateway's outside interface |
| StaticRoutesOnly | true or false | false | ○ | Indicates whether the VPN connection uses static routes only |
| TransitGatewayId | String | | ○ | The ID of the transit gateway associated with the VPN connection | 