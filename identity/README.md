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
| EC2InstanceType | String | t3.small | ○ | The EC2 Instance Type |
| Edition | Standard / Enterprise | Standard | ○ | The edition of AWS Directory Service for Microsoft Active Directory |
| EnableSso | true / false | true | ○ | Whether to enable single sign-on for a Microsoft Active Directory in AWS |
| **Name** | String | corp.example.com | ○ | The fully qualified domain name for the AWS Managed Microsoft AD directory |
| Password | String | Password1+ | ○ | The password for the default administrative user named Admin |
| ServicesToRepair | String | | | A comma separated list of Windows services on the management instance that have to be running once the secure channel is sound |
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

#### Sign-in stops working after the identity source is changed

Changing the identity source between Active Directory and an external identity provider deletes every user, group and account assignment. With an external identity provider, provision the users and groups again through SCIM, then update the stack with the new group ids in `AdministratorGroupId` and `ReadOnlyGroupId`.

#### The first deployment fails with ConflictException

The same account assignment already exists outside the stack. Delete it before you deploy. `AWS::SSO::Assignment` cannot be updated, so any change replaces it. Renaming a permission set also replaces it and deletes every assignment on it.

#### An assignment to the management account fails with an explicit deny

The delegated administrator account for `sso.amazonaws.com` cannot create an assignment to the management account, or delete an assignment on a permission set that Control Tower created. Run the stack from the management account, or leave `ManagementAccountId` empty in the delegated administrator account.

#### The provisioning log keeps showing name: The attribute name is required

An account with neither a first name nor a last name cannot be provisioned from Microsoft Entra ID to IAM Identity Center. The default administrative account of AWS Managed Microsoft AD is one of them. Remove that account from the groups assigned to the enterprise application.

#### Users cannot be created by the template

CloudFormation has no resource for an identity store user. With an external identity provider, manage users and groups in the identity provider.

#### Applications such as Amazon Quick cannot be created by the template

`AWS::SSO::Application` only creates OAuth 2.0 customer managed applications. Create applications that AWS services register, and SAML 2.0 applications, in the console of each service, and pass their ARN as a parameter.

### Managed Microsoft AD Issues

If Managed Microsoft AD is not functioning correctly:

1. Verify that the VPC and subnets have proper DNS resolution configured
2. Check that security groups allow the necessary Active Directory ports
3. Ensure that the domain name doesn't conflict with existing domains
4. Verify that the password meets complexity requirements

#### The Admin password no longer matches the parameter

Do not change the `Password` parameter. It is a create-only property, so changing it replaces the directory and every user and computer in it is lost. Change the password with [ResetUserPassword](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html) instead. It also accepts the current value.

#### The correct password is refused

The Admin password may have expired. The default password policy applies a maximum age to the administrative account as well, and an expired password is refused as a wrong password. Run `net use \\<domain controller>\IPC$ /user:<domain>\Admin <password>`: system error 2242 means expired and 1326 means wrong. If it has expired, set it again with `ResetUserPassword`.

#### Services running as a domain account fail on the management instance

The secure channel between the management instance and the domain controllers is broken. This happens right after the instance is replaced from an AMI, or after the connection drops. `SystemAssociationForRepairingDomainTrust` re-establishes the channel with `nltest /sc_reset` every 30 minutes and starts the services in `ServicesToRepair`. To repair it at once, run the association manually.

If the association fails, the machine account password no longer matches the directory. Run `Reset-ComputerMachinePassword` with a domain credential. Running `AWS-JoinDirectoryServiceDomain` again does not help, because it does nothing on an instance that is already joined.

Check the result with `nltest /sc_verify:<domain>`. `NERR_Success` means the channel is sound.

### Domain Controller Access Issues

If you cannot access domain controllers:

1. Verify that you're connecting from the correct VPC and subnets
2. Check that the security groups allow RDP access on port 3389
3. Ensure that the domain admin credentials are correct
4. Verify that the domain controllers are in a healthy state