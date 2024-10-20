English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/identity
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/identity`` sets AWS Identity Services to manage identities, resources, and permissions securely at scale.

## TL;DR

If you just want to deploy the stack, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| AWS IAM Identity Center | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=IdentityCenter&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/identitycenter.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IdentityCenter&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/identitycenter.yaml) |
| AWS Managed Microsoft AD | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MicrosoftAD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/microsoftad.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MicrosoftAD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/microsoftad.yaml) |

## AWS IAM Identity Center

This template configures ``AWS IAM Identity Center``.

### Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file identitycenter.yaml --stack-name IdentityCenter --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| DefaultSessionDuration | String | PT12H | ○ | The length of time that the application user sessions are valid for in the ISO-8601 standard |
| InstanceArn | String |  |  | The ARN of the IAM Identity Center instance under which the operation will be executed |

## AWS Managed Microsoft AD

This template configures ``AWS Managed Microsoft AD``.

### Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file microsoftad.yaml --stack-name MicrosoftAD --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| EC2ImageId | AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> | /aws/service/ami-windows-latest/Windows_Server-2022-Japanese-Full-Base | ○ | The EC2 Image Id |
| Edition | Standard / Enterprise | Standard | ○ | The edition of AWS Directory Service for Microsoft Active Directory |
| EnableSso | true / false | true | ○ | Whether to enable single sign-on for a Microsoft Active Directory in AWS |
| Name | String | corp.example.com | ○ | The fully qualified domain name for the AWS Managed Microsoft AD directory |
| Password | String | Password1+ | ○ | The password for the default administrative user named Admin |
| ShortName | String | CORP | ○ | The NetBIOS name for your domain |
| SubnetPrivateCidrBlockForAz1 | String | 10.3.0.0/24 | conditional | The private subnet CIDR block at AZ1 |
| SubnetPrivateIdForAz1 | String | | conditional | The private subnet id at AZ1 |
| SubnetPrivateCidrBlockForAz2 | String | 10.3.4.0/24 | conditional | The private subnet CIDR block at AZ2 |
| SubnetPrivateIdForAz2 | String | | conditional | The private subnet id at AZ2 |
| SubnetPrivateCidrBlockForAz3 | String | 10.3.8.0/24 | conditional | The private subnet CIDR block at AZ3 |
| SubnetPrivateIdForAz3 | String | | conditional | The private subnet id at AZ3 |
| TransitGatewayDestinationCidrBlock | String | | | The IPv4 CIDR block forward to TransitGateway |
| VPCId | String | | ○ | The VPC id |

### Installing the Active Directory administration tools

After deploying this template, [install the Active Directory Administration Tools on Windows Server](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_install_ad_tools.html#install_ad_tools_winserver). Next, switch the user to `DOMAIN\Admin` and [create users and groups](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.html) with the **Active Directory Users and Computers tool**.