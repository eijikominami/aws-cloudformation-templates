English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/migration
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/migration`` builds migration services.

## Prerequisites

Before deploying this template, ensure you have:

- Source servers prepared for migration with AWS MGN agent installed
- Network connectivity between source environment and AWS
- VPC and subnets configured for target environment
- Understanding of migration timeline and cutover requirements

## TL;DR

If you want to deploy each service individually, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| AWS Application Migration Service (AWS MGN) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MGN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/migration/mgn.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MGN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/migration/mgn.yaml) |

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file templates/mgn.yaml --stack-name MGN --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

### AWS Application Migration Service (AWS MGN)

This template sets ``AWS Application Migration Service (AWS MGN)``.

The following sections describe the individual components of the architecture.

![](https://docs.aws.amazon.com/images/prescriptive-guidance/latest/patterns/images/pattern-img/21346c0f-0643-4f4f-b21f-fdfe24fc6a8f/images/bd0dfd42-4ab0-466f-b696-804dedcf4513.png)

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| DnsIpAz1 | String | 10.0.0.53 | | The IPv4 address that you want to use for DNS queries | 
| DnsIpAz2 | String | 10.0.1.53 | | The IPv4 address that you want to use for DNS queries | 
| DnsIpAz3 | String | 10.0.2.53 | | The IPv4 address that you want to use for DNS queries | 
| **SourceCidrBlock** | String | 0.0.0.0/0 | ○ | The VPC CIDR block of source servers |
| SubnetCidrBlockAz1 | String | 10.0.0.0/24 | | The subnet CIDR block |
| SubnetCidrBlockAz2 | String | 10.0.1.0/24 | | The subnet CIDR block |
| SubnetCidrBlockAz3 | String | 10.0.2.0/24 | | The subnet CIDR block |
| SubnetIdAz1 | String | | | The private subnet Id |
| SubnetIdAz2 | String | | | The private subnet Id |
| SubnetIdAz3 | String | | | The private subnet Id |
| **VPCCidrBlock** | String | 10.0.0.0/22 | ○ | The VPC CIDR block |
| VPCId | String | | | The VPC Id |

## Troubleshooting

### MGN Agent Issues

If MGN agents are not connecting or replicating properly:

1. Verify that source servers have internet connectivity to AWS MGN endpoints
2. Check that required ports (443, 1500) are open in firewalls and security groups
3. Ensure that the MGN agent is installed with proper permissions on source servers
4. Verify that the MGN service is initialized in the target AWS region

### Replication Issues

If data replication is failing or slow:

1. Check network bandwidth and latency between source and target environments
2. Verify that source servers have sufficient disk space for staging area
3. Ensure that EBS volume types and sizes are appropriate for workload requirements
4. Monitor CloudWatch metrics for replication lag and throughput

### Launch Template Issues

If test or cutover launches are failing:

1. Verify that launch templates have correct instance types and configurations
2. Check that target subnets have sufficient IP addresses available
3. Ensure that security groups allow necessary traffic for migrated applications
4. Verify that IAM roles have permissions for EC2 instance operations

### Network Configuration Issues

If migrated instances cannot communicate properly:

1. Verify that DNS resolution is working correctly in the target VPC
2. Check that routing tables are configured for proper network access
3. Ensure that security groups and NACLs allow required application traffic
4. Verify that load balancers and other network services are properly configured