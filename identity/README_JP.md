[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/identity
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/identity`` は、アイデンティティ、リソース、アクセス許可をセキュアかつ大規模に管理可能な AWS Identity Services を構築します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| Services | Launchers |
| --- | --- |
| AWS IAM Identity Center | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IdentityCenter&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/identitycenter.yaml) |
| AWS Managed Microsoft AD | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MicrosoftAD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/microsoftad.yaml) |

## AWS IAM Identity Center

このテンプレートは、 ``AWS IAM Identity Center`` を構成します。

### デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file identitycenter.yaml --stack-name IdentityCenter --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| DefaultSessionDuration | String | PT12H | ○ |　ISO-8601 におけるアプリケーションユーザーのセッション有効期間 |
| InstanceArn | String |  |  | IAM Identity Center の ARN |

## AWS Managed Microsoft AD

このテンプレートは、 ``AWS Managed Microsoft AD`` を構成します。

### デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file microsoftad.yaml --stack-name MicrosoftAD --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| Edition | Standard / Enterprise | Standard | ○ | Microsoft Active Directory のエディション |
| EnableSso | true / false | true | ○ | シングルサインオンを有効化するかどうか |
| Name | String | corp.example.com | ○ | ドメイン名 |
| Password | String | Password1+ | ○ | Admin ユーザのドメイン名 |
| ShortName | String | CORP | ○ | The NetBIOS name for your domain |
| SubnetPrivateCidrBlockForAz1 | String | 10.0.0.0/24 | ○ | AZ1 にあるプライベートサブネットのCIDRブロック |
| SubnetPrivateIdForAz1 | String | | ○ | AZ1 のプライベートサブネット ID |
| SubnetPrivateCidrBlockForAz2 | String | 10.0.1.0/24 | ○ | AZ2 にあるプライベートサブネットのCIDRブロック |
| SubnetPrivateIdForAz1 | String | | ○ | AZ2 のプライベートサブネット ID |
| TransitGatewayDestinationCidrBlock | String | | | TransitGateway のCIDRブロック |
| VPCCidrBlock | String | 10.0.0.0/21 | ○ | VPC のCIDRブロック |

### AWS Managed Microsoft AD を用いたユーザーとグループを管理

このテンプレートのデプロイ完了後、 [Active Directory 管理ツールのインストール](https://docs.aws.amazon.com/ja_jp/directoryservice/latest/admin-guide/ms_ad_install_ad_tools.html) を行ってください。次に '*DOMAIN*\Admin' ユーザに切り替えた上で、 *Active Directory Users and Computers tool* を用いて、 [ユーザとグループの作成](https://docs.aws.amazon.com/ja_jp/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.html)　を行ってください。