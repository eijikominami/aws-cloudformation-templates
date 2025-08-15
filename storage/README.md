English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/storage
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/storage`` builds storage services including Amazon FSx.

## Prerequisites

Before deploying this template, ensure you have:

- AWS Managed Microsoft Active Directory instance configured
- VPC and subnets configured for FSx deployment
- Understanding of FSx throughput and storage capacity requirements
- Appropriate security groups and network access configured

## TL;DR

If you just want to deploy the stack, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| Amazon FSx for Windows Server | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=FSx&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/storage/fsx.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=FSx&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/storage/fsx.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

### Amazon FSx for Windows Server

This template creates Amazon FSx for Windows Server file system that provides fully managed Windows file shares. The file system is integrated with AWS Managed Microsoft Active Directory for authentication and access control.

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file templates/fsx.yaml --stack-name FSx --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows.

### Amazon FSx for Windows Server

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| **ActiveDirectoryId** | String | | ○ | The ID for an existing AWS Managed Microsoft Active Directory instance |
| AZDeploymentMode | SINGLE_AZ_2 / MULTI_AZ_1 | SINGLE_AZ_2 | ○ | Specifies the file system deployment type |
| CidrIp | String | 0.0.0.0/0 | ○ | The CIDR block for security group access |
| FSxThroughput | Number | 8 | ○ | The throughput capacity (MB/s) - 8, 16, 32, or 64 |
| PrimarySubnetAccess | String | | ○ | The subnet ID for the primary file system |
| IngressCidrIp | String | | | Additional CIDR block for ingress access |
| StorageCapacity | Number | 32 | ○ | The storage capacity (GB) - minimum 32 GB |
| SubnetIds | String | | ○ | Comma-separated list of subnet IDs |
| **VPCId** | String | | ○ | The VPC ID where FSx will be deployed |

## Troubleshooting

### FSx File System Issues

If FSx file system is not accessible:

1. Verify that the AWS Managed Microsoft Active Directory is healthy and accessible
2. Check that the security groups allow the necessary ports for SMB/CIFS traffic (port 445)
3. Ensure that the subnets have proper routing to the Active Directory domain controllers
4. Verify that the file system is in the "Available" state in the FSx console

### Active Directory Integration Issues

If FSx cannot join the Active Directory domain:

1. Verify that the Active Directory ID is correct and the directory is active
2. Check that the FSx service has the necessary permissions to join the domain
3. Ensure that DNS resolution is working properly between FSx and Active Directory
4. Verify that the security groups allow communication between FSx and AD on required ports

### Performance Issues

If FSx performance is not meeting expectations:

1. Verify that the throughput capacity is appropriate for your workload
2. Check that the storage capacity meets your performance requirements
3. Monitor CloudWatch metrics for FSx to identify bottlenecks
4. Consider upgrading to Multi-AZ deployment for better performance and availability

### Network Connectivity Issues

If clients cannot connect to FSx:

1. Verify that security groups allow SMB traffic (port 445) from client subnets
2. Check that network ACLs are not blocking the required traffic
3. Ensure that clients are domain-joined and can authenticate with Active Directory
4. Verify that the FSx DNS name resolves correctly from client machines