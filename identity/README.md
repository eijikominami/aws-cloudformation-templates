English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/identity
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/identity`` sets AWS Identity Services to manage identities, resources, and permissions securely at scale.

## Prerequisites

Before deploying this template, ensure you have:

- VPC with private subnets configured (for Managed Microsoft AD)
- Domain name planned for Active Directory (for Managed Microsoft AD)
- Understanding of IAM Identity Center instance requirements

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
aws cloudformation deploy --template-file templates/identitycenter.yaml --stack-name IdentityCenter --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AdministratorGroupId | String | | | The identity store group id that receives administrator access |
| AdministratorTargetAccountIds | CommaDelimitedList | 000000000000 | conditional | The account ids that administrator access is assigned to |
| DefaultSessionDuration | String | PT12H | ○ | The length of time that the application user sessions are valid for in the ISO-8601 standard |
| InstanceArn | String |  |  | The ARN of the IAM Identity Center instance under which the operation will be executed |
| ManagementAccountId | String |  |  | The management account id that organizations and service catalog access is assigned to |
| ReadOnlyGroupId | String |  |  | The identity store group id that receives read only access |
| ReadOnlyTargetAccountIds | CommaDelimitedList | 000000000000 | conditional | The account ids that read only access is assigned to |

## AWS Managed Microsoft AD

This template configures ``AWS Managed Microsoft AD``.

### Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file templates/microsoftad.yaml --stack-name MicrosoftAD --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| EC2ImageId | AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> | /aws/service/ami-windows-latest/Windows_Server-2022-Japanese-Full-Base | ○ | The EC2 Image Id |
| Edition | Standard / Enterprise | Standard | ○ | The edition of AWS Directory Service for Microsoft Active Directory |
| EnableSso | true / false | true | ○ | Whether to enable single sign-on for a Microsoft Active Directory in AWS |
| **Name** | String | corp.example.com | ○ | The fully qualified domain name for the AWS Managed Microsoft AD directory |
| Password | String | Password1+ | ○ | The password for the default administrative user named Admin |
| **ShortName** | String | CORP | ○ | The NetBIOS name for your domain |
| SubnetPrivateCidrBlockForAz1 | String | 10.3.0.0/26 | ○ | The private subnet CIDR block at AZ1 |
| SubnetPrivateIdForAz1 | String | | conditional | The private subnet id at AZ1 |
| SubnetPrivateCidrBlockForAz2 | String | 10.3.64.0/26 | ○ | The private subnet CIDR block at AZ2 |
| SubnetPrivateIdForAz2 | String | | conditional | The private subnet id at AZ2 |
| VPCId | String | | ○ | The VPC id |

### Installing the Active Directory administration tools

After deploying this template, [install the Active Directory Administration Tools on Windows Server](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_install_ad_tools.html#install_ad_tools_winserver). Next, switch the user to `DOMAIN\Admin` and [create users and groups](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.html) with the **Active Directory Users and Computers tool**.

### Storing Security Event Logs in Amazon CloudWatch Logs and Amazon S3

To store domain controller security event logs in Amazon CloudWatch Logs and Amazon S3, you need to manually enable the log forwarding feature through the AWS Management Console. This configuration allows you to forward security events from your domain controllers for monitoring and audit purposes.

### Replacing the management instance from the latest AMI

This template creates a nested Data Lifecycle Manager stack that builds an AMI from the management instance. The policy is an `IMAGE_MANAGEMENT` policy over instances that carry the `Environment` tag and the `TagKey` and `TagValue` pair, and it runs weekly. When an AMI becomes available, an EventBridge rule named `<LogicalName>-RegisterLatestImage-<region>` invokes a function that writes the id of that AMI to the SSM parameter `/<LogicalName>/ami/latest`.

`EC2ImageId` defaults to the AMI that AWS publishes, so the parameter is written but never read. Pointing `EC2ImageId` at `/<LogicalName>/ami/latest` makes the management instance start from the newest AMI instead, and the next stack update then replaces the instance whenever that parameter has changed.

Software installed on the management instance by hand therefore survives a replacement only when it was installed before the AMI was built. Installing software and then updating the stack before the weekly schedule has run replaces the instance from an older AMI, and the software is no longer present. Build an AMI and update the parameter as soon as an installation finishes.

The root volume is deleted on termination, so a replaced instance keeps nothing of its own. Two signs tell whether the new instance started from an AMI that already carried the software: the Windows computer name is the same as before, and the event log holds records that predate the launch time of the instance.

## Troubleshooting

### IAM Identity Center Issues

If IAM Identity Center is not working properly:

1. Verify that you have the necessary permissions to manage IAM Identity Center
2. Check that the Identity Center instance is properly configured in your region
3. Ensure that permission sets are correctly assigned to users and groups
4. Verify that external identity providers are properly configured if using SAML

#### Changing the identity source deletes every user, group and assignment

Changing the identity source between Active Directory and an external identity provider deletes every user, every group and every account assignment in the instance. CloudTrail records a `DisassociateProfile` event with `allAssignmentsDeleted` set to true for each one. Record the group ids of the identity store before the change, because the assignments this template creates reference them through `AdministratorGroupId` and `ReadOnlyGroupId`.

#### An account assignment cannot be updated in place

`AWS::SSO::Assignment` declares every property as create-only and has no update handler, so any change replaces the resource. An assignment that already exists outside the stack makes the create fail with `ConflictException`. Delete the existing assignment before the first deployment that manages it.

The same applies to the `Name` of `AWS::SSO::PermissionSet`. Renaming a permission set replaces it, which also deletes every assignment that references it.

#### A delegated administrator cannot assign access to the management account

An account that is the delegated administrator for `sso.amazonaws.com` cannot create an assignment that targets the Organizations management account. The call fails with an explicit deny in a resource-based policy that no IAM policy can override, and deleting an assignment on a permission set that Control Tower created is refused in the same way. Run both from the management account.

Leave `ManagementAccountId` empty when the stack runs in a delegated administrator account. The resources for the management account are then not created.

#### A user without a first and last name fails to provision

The SCIM endpoint of IAM Identity Center requires the `name` attribute and answers `400` with `name: The attribute name is required` when it is absent. Microsoft Entra ID builds that attribute from `givenName` and `surname`, so a directory account that has neither is never created. The default administrative account of AWS Managed Microsoft AD is one of them.

The provisioning job retries such an entry every cycle without ever succeeding. The failure is scoped to the entry, so `countSuccessiveCompleteFailures` stays at zero and the job is not quarantined, but the log fills with the same error. Remove the account from the groups that are assigned to the enterprise application instead of giving it a name.

#### An identity store user cannot be created by CloudFormation

`AWS::IdentityStore::Group` and `AWS::IdentityStore::GroupMembership` exist, but there is no resource for a user. When an external identity provider provisions users through SCIM, the groups and the memberships are also owned by that provider, so declaring them here creates two owners for the same object.

#### An AWS managed application cannot be created by CloudFormation

`AWS::SSO::Application` only supports OAuth 2.0 customer managed applications. It cannot create the applications that AWS services register themselves, such as Amazon Quick or Amazon CodeCatalyst, and it cannot create a SAML 2.0 customer managed application. `AWS::SSO::ApplicationAssignment` can still assign principals to an application that already exists, but its ARN has to be supplied as a parameter because nothing in the template creates it.

### Managed Microsoft AD Issues

If Managed Microsoft AD is not functioning correctly:

1. Verify that the VPC and subnets have proper DNS resolution configured
2. Check that security groups allow the necessary Active Directory ports
3. Ensure that the domain name doesn't conflict with existing domains
4. Verify that the password meets complexity requirements

### Domain Controller Access Issues

If you cannot access domain controllers:

1. Verify that you're connecting from the correct VPC and subnets
2. Check that the security groups allow RDP access on port 3389
3. Ensure that the domain admin credentials are correct
4. Verify that the domain controllers are in a healthy state