English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/network
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/network`` sets VPC and network elements.

## Prerequisites

- AWS Organizations setup (for cross-account networking features)
- Route 53 hosted zones for DNS management (if using custom domains)
- On-premises network configuration details (for VPN and hybrid connectivity)
- Appropriate IAM permissions for VPC, Transit Gateway, and networking services

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/templates/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/templates/template.yaml) | 

If you want to deploy each service individually, click the button below.

| Services | US West (Oregon) | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- | --- |
| Availability Zone | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=AvailabilityZone&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/az.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=AvailabilityZone&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/az.yaml) |[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=AvailabilityZone&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/az.yaml) |
| Global Accelerator | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=GlobalAccelerator&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/globalaccelerator.yaml) | | |
| IPAM | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=IPAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/ipam.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=IPAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/ipam.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IPAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/ipam.yaml) |
| Network Access Analyzer | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=NetworkAccessAnalyzer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkaccessanalyzer.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=NetworkAccessAnalyzer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkaccessanalyzer.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=NetworkAccessAnalyzer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkaccessanalyzer.yaml) |
| Network Firewall | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=NetworkFirewall&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkfirewall.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=NetworkFirewall&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkfirewall.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=NetworkFirewall&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkfirewall.yaml) |
| Route 53 | | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Route53&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/route53resolver.yaml) | |
| TransitGateway | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) |
| VPN | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-network.png)

## Deployment

## Deployment

Execute the command to deploy the main template.

```bash
aws cloudformation deploy --template-file templates/template.yaml --stack-name Network --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

Or deploy individual components:

```bash
aws cloudformation deploy --template-file templates/az.yaml --stack-name AvailabilityZone --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/egress.yaml --stack-name EgressVPC --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/globalaccelerator.yaml --stack-name GlobalAccelerator
aws cloudformation deploy --template-file templates/ipam.yaml --stack-name IPAM --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/networkaccessanalyzer.yaml --stack-name NetworkAccessAnalyzer --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/networkfirewall.yaml --stack-name NetworkFirewall --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/route53resolver.yaml --stack-name Route53
aws cloudformation deploy --template-file templates/transitgateway.yaml --stack-name TransitGateway --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/vpn.yaml --stack-name VPN --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

## Troubleshooting

### VPC and Subnet Configuration Issues

If you encounter VPC or subnet configuration problems:

1. Verify that CIDR blocks do not overlap with existing VPCs
2. Ensure subnet CIDR blocks are within the VPC CIDR range
3. Check that availability zones are available in your region
4. Verify that you have sufficient IP addresses for your requirements

### Transit Gateway Connectivity Issues

If Transit Gateway connections are not working:

1. Check route table configurations and propagations
2. Verify that security groups and NACLs allow required traffic
3. Ensure that Transit Gateway attachments are in the correct state
4. Check for conflicting routes in route tables

### VPN Connection Problems

If VPN connections are failing:

1. Verify that the customer gateway IP address is correct and accessible
2. Check that BGP configuration matches on both sides
3. Ensure that security groups allow VPN traffic
4. Verify that on-premises firewall rules allow VPN traffic

### DNS Resolution Issues

If DNS resolution is not working:

1. Check that Route 53 resolver rules are properly configured
2. Verify that DNS forwarder IP addresses are correct
3. Ensure that VPC DNS resolution and DNS hostnames are enabled
4. Check that security groups allow DNS traffic (port 53)

### Network Firewall Issues

If Network Firewall is not filtering traffic correctly:

1. Verify that firewall rules are properly configured
2. Check that traffic is being routed through the firewall subnets
3. Ensure that firewall policies match your security requirements
4. Review firewall logs for blocked or allowed traffic patterns
```

You can provide optional parameters as follows:

| Name | Type | Default | Requied | Details | 
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| CentralizedLogBucketName | String | | | The centralize S3 bucket name for logging |
| CustomerGatewayOutsideIpAddress | String | | |  The Internet-routable IP address for the customer gateway's outside interface |
| DnsIpAz1 | String | 10.0.8.53 | | The IPv4 address that you want to use for DNS queries |
| DnsIpAz2 | String | 10.0.10.53 | | The IPv4 address that you want to use for DNS queries |
| DnsIpAz3 | String | 10.0.12.53 | | The IPv4 address that you want to use for DNS queries |
| DomainName | String | | | The name of the domain |
| FirewallCidrBlockForEgressAz1 | String | 10.0.0.128/26 | | The firewall subnet CIDR block for Egress at AZ1 |
| FirewallCidrBlockForEgressAz2 | String | 10.0.2.128/26 | | The firewall subnet CIDR block for Egress at AZ2 | 
| FirewallCidrBlockForEgressAz3 | String | 10.0.4.128/26 | | The firewall subnet CIDR block for Egress at AZ3 |
| HomeNetworkCidr | String | 10.0.0.0/8 | ○ | The CIDR of your home network | 
| OnpremDnsIp | String | | | One IPv4 address that you want to forward DNS queries to |
| OrganizationId | String | | | The Organizations ID |
| PrivateCidrBlockForDNSAz1 | String | 10.0.8.0/24 | ○ | The private subnet CIDR block for DNS at AZ1 |
| PrivateCidrBlockForDNSAz2 | String | 10.0.10.0/24 | ○ | The private subnet CIDR block for DNS at AZ2 |
| PrivateCidrBlockForDNSAz3 | String | 10.0.12.0/24 | ○ | The private subnet CIDR block for DNS at AZ3 |
| PublicCidrBlockForEgressAz1 | String | 10.0.0.0/26 | ○ | The public subnet CIDR block for Egress at AZ1 | 
| PublicCidrBlockForEgressAz2 | String | 10.0.2.0/26 | ○ | The public subnet CIDR block for Egress at AZ2 | 
| PublicCidrBlockForEgressAz3 | String | 10.0.4.0/26 | ○ | The public subnet CIDR block for Egress at AZ3 | 
| TransitCidrBlockForEgressAz1 | String | 10.0.0.64/26 | ○ | The transit subnet CIDR block for Egress at AZ1 | 
| TransitCidrBlockForEgressAz2 | String | 10.0.4.64/26 | ○ | The transit subnet CIDR block for Egress at AZ2 | 
| TransitCidrBlockForDNSAz1 | String | 10.0.11.0/24 | ○ | The transit subnet CIDR block for DNS at AZ1 | 
| TransitCidrBlockForDNSAz2 | String | 10.0.13.0/24 | ○ | The transit subnet CIDR block for DNS at AZ2 | 
| TransitCidrBlockForDNSAz3 | String | 10.0.15.0/24 | ○ | The transit subnet CIDR block for DNS at AZ3 | 
| TransitGatewayDefaultRouteTableId | String | | | The id of the default Transit Gateway Route Table | 
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway | 
| VPCCidrBlockForEgress | String | 10.0.0.0/21 | ○ | The Egress VPC CIDR block | 
| VPCCidrBlockForDNS | String | 10.0.0.0/21 | ○ | The DNS VPC CIDR block | 

`TransitGatewayDefaultRouteTableId` is enabled after creating  Transit Gateway.

### Integrate Amazon Transit Gateway, IPAM, and VPC Reachability Analyzer with AWS Organizations

If you use Amazon Transit Gateway or Amazon VPC IP Address Manager (IPAM) in your `Network` account, enable `AWS Resource Access Manager` in `AWS Organizations`.　If you use VPC Reachability Analyzer in your `Network` account, turn on `Trusted Access` in Settings of VPC Reachability Analyzer.

### Availability Zone

This template configures ``Availability Zone``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| **AvailabilityZone** | AWS::EC2::AvailabilityZone::Name | | ○ | The Availability Zone name |
| InternetGatewayId | String | | | The Internet Gateway Id |
| NetworkAddressTranslation | ENABLED / DISABLED | DISABLED　| ○ | Enable or disable NetworkAddressTranslation (NAT) |
| NetworkLoadBalancer | ENABLED / DISABLED | DISABLED　| ○ | Enable or disable Network LoadBalaner |
| SubnetPrivateCidrBlock | String | 10.0.0.0/24 | ○ | The Private subnet CIDR block |
| SubnetPublicCidrBlock | String | 10.0.0.0/24 | ○ | The Public subnet CIDR block |
| SubnetTransitCidrBlock | String | | | The transit subnet CIDR block |
| SubnetFirewallCidrBlock | String | | | The firewall subnet CIDR block |
| **VPCId** | AWS::EC2::VPC::Id | | ○ | The VPC id  |

### Egress VPC

This template configures ``Egress Central VPC``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| CentralizedLogBucketName | String | | | The centralize S3 bucket name for logging |
| HomeNetworkCidr | String | 10.0.0.0/8 | ○ | The CIDR of your home network | 
| ResolverInboundRuleId | String |  |  | The ID of the Resolver inbound rule that you associated with the VPC that is specified by VPCId| 
| ResolverOutboundRuleId | String |  |  | The ID of the Resolver outbound rule that you associated with the VPC that is specified by VPCId | 
| SubnetFirewallCidrBlockForAz1 | String | 10.0.0.128/26 | ○ | The firewall subnet CIDR block at AZ1 | 
| SubnetFirewallCidrBlockForAz2 | String | 10.0.2.128/26 | ○ | The firewall subnet CIDR block at AZ2 | 
| SubnetFirewallCidrBlockForAz3 | String | 10.0.4.128/26 | ○ | The firewall subnet CIDR block at AZ3 | 
| SubnetPublicCidrBlockForAz1 | String | 10.0.0.0/26 | ○ | The public subnet CIDR block at AZ1 |
| SubnetPublicCidrBlockForAz2 | String | 10.0.2.0/26 | ○ | The public subnet CIDR block at AZ2 |
| SubnetPublicCidrBlockForAz3 | String | 10.0.4.0/26 | ○ | The public subnet CIDR block at AZ3 |
| SubnetTransitCidrBlockForAz1 | String | 10.0.0.64/26 | ○ | The transit subnet CIDR block at AZ1 |
| SubnetTransitCidrBlockForAz2 | String | 10.0.2.64/26 | ○ | The transit subnet CIDR block at AZ2 |
| SubnetTransitCidrBlockForAz3 | String | 10.0.4.64/26 | ○ | The transit subnet CIDR block at AZ3 |
| TransitGatewayDefaultRouteTableId | String | | | The id of the default Transit Gateway Route Table | 
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway | 
| **TransitGatewayId** | String | | ○ | The ID of the transit gateway | 
| VPCCidrBlock | String | 10.0.0.0/21 | ○ | The VPC CIDR block | 

### Global Accelerator

This template configures ``Global Accelerator``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| **EndpointId** | String | | ○ | The Amazon Resource Name (ARN) of the ELB, the Elastic IP address or  the EC2 instance ID |
| **EndpointGroupRegion** | String | | ○ | The AWS Regions where the endpoint group is located |
| FromPort | Number | 80 | |  The first port in the range of ports, inclusive |
| HealthCheckIntervalSeconds | 10 / 30 | 30 | | The time—10 seconds or 30 seconds—between health checks for each endpoint |
| HealthCheckPath | String | / | | If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks |
| HealthCheckPort | Number | 80 | | The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group |
| HealthCheckProtocol | TCP / HTTP / HTTPS | TCP | | The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group |
| IpAddressType | IPV6 / IPV4 | IPV4 | | The IP address type that an accelerator supports |
| Name | String | Default | | The name of the accelerator |
| Protocol | TCP / UDP | TCP | | The protocol for the connections from clients to the accelerator |
| ThresholdCount | Number | 3 | | The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy |
| ToPort | Number | 80 | | The last port in the range of ports, inclusive |

### IP Address Manager (IPAM)

This template configures ``IP Address Manager (IPAM)``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| PrincipalsToAssociateWithIPAM | String | | | Specifies a list of one or more principals to associate with IPAM |
| ProvisionedCidrs | String | 10.0.0.0/8 | ○ | The CIDR of your home network  |

### Network Firewall

This template configures ``Network Firewall``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| CentralizedLogBucketName | String | | | The centralize S3 bucket name for logging |
| HomeNetworkCidr | String | 10.0.0.0/8 | ○ | The CIDR of your home network | 
| SubnetIdAz1 | String | | | The firewall subnet id in AZ1 |
| SubnetIdAz2 | String | | | The firewall subnet id in AZ2 |
| SubnetIdAz3 | String | | | The firewall subnet id in AZ3 |
| **VPCId** | AWS::EC2::VPC::Id | | ○ | The VPC id  |

### Route 53

This template configures ``Route 53 Resolver``.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| DnsIpAz1 | String | 10.0.8.53 | | The IPv4 address that you want to use for DNS queries |
| DnsIpAz2 | String | 10.0.10.53 | | The IPv4 address that you want to use for DNS queries |
| DnsIpAz3 | String | 10.0.12.53 | | The IPv4 address that you want to use for DNS queries |
| DomainName | String | | | The name of the domain |
| OnpremDnsIp | String | | | One IPv4 address that you want to forward DNS queries to |
| PrincipalsToAssociateWithRoute53ResolverRule | String | | | Specifies a list of one or more principals to associate with Route 53 Resolver Rule |
| SubnetPrivateCidrBlockForAz1 | String | 10.0.8.0/24 | ○ | The private subnet CIDR block at AZ1 |
| SubnetPrivateCidrBlockForAz2 | String | 10.0.10.0/24 | ○ | The private subnet CIDR block at AZ2 |
| SubnetPrivateCidrBlockForAz3 | String | 10.0.12.0/24 | ○ | The private subnet CIDR block at AZ3 |
| SubnetTransitCidrBlockForAz1 | String | 10.0.11.0/24 | ○ | The transit subnet CIDR block at AZ1 | 
| SubnetTransitCidrBlockForAz2 | String | 10.0.13.0/24 | ○ | The transit subnet CIDR block at AZ2 | 
| SubnetTransitCidrBlockForAz3 | String | 10.0.15.0/24 | ○ | The transit subnet CIDR block at AZ3 | 
| **TransitGatewayId** | String | | ○ | The ID of the transit gateway | 
| VPCCidrBlock | String | 10.0.8.0/21 | ○ | The VPC CIDR block | 

In each participating account, create the authorization using the private hosted zone ID, the region, and the VPC ID that you want to associate (DNS-VPC)

> aws route53 create-vpc-association-authorization --hosted-zone-id HOSTED_ZONE_ID --vpc VPCRegion=REGION,VPCId=VPC_ID

In the Network account, associate the DNS-VPC with the hosted zone in each participating account.

> aws route53 associate-vpc-with-hosted-zone --hosted-zone-id HOSTED_ZONE_ID --vpc VPCRegion=REGION,VPCId=VPC_ID   

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

After creating a Transit Gateway attachment, **add Transit Gateway route to a customer network manually**.
