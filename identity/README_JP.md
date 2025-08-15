[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/identity
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/identity`` は、アイデンティティ、リソース、アクセス許可をセキュアかつ大規模に管理可能な AWS Identity Services を構築します。

## 前提条件

デプロイの前に以下を準備してください。

- プライベートサブネットが設定された VPC（Managed Microsoft AD 用）
- Active Directory 用に計画されたドメイン名（Managed Microsoft AD 用）
- IAM Identity Center インスタンス要件の理解

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| AWS IAM Identity Center | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=IdentityCenter&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/identitycenter.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IdentityCenter&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/identitycenter.yaml) |
| AWS Managed Microsoft AD | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MicrosoftAD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/microsoftad.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MicrosoftAD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/microsoftad.yaml) |

## AWS IAM Identity Center

このテンプレートは、 ``AWS IAM Identity Center`` を構成します。

### デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file templates/identitycenter.yaml --stack-name IdentityCenter --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| DefaultSessionDuration | String | PT12H | ○ | ISO-8601 におけるアプリケーションユーザーのセッション有効期間 |
| InstanceArn | String |  |  | IAM Identity Center の ARN |

## AWS Managed Microsoft AD

このテンプレートは、 ``AWS Managed Microsoft AD`` を構成します。

### デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file templates/microsoftad.yaml --stack-name MicrosoftAD --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | CloudWatch アラームのアラームレベル |
| EC2ImageId | AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> | /aws/service/ami-windows-latest/Windows_Server-2022-Japanese-Full-Base | ○ | EC2 のイメージ ID |
| Edition | Standard / Enterprise | Standard | ○ | Microsoft Active Directory のエディション |
| EnableSso | true / false | true | ○ | シングルサインオンを有効化するかどうか |
| **Name** | String | corp.example.com | ○ | ドメイン名 |
| Password | String | Password1+ | ○ | Admin ユーザーのパスワード |
| **ShortName** | String | CORP | ○ | NetBIOS 名 |
| SubnetPrivateCidrBlockForAz1 | String | 10.3.0.0/24 | ○ | AZ1 にあるプライベートサブネットの CIDR ブロック |
| SubnetPrivateIdForAz1 | String | | ○ | AZ1 のプライベートサブネット ID |
| SubnetPrivateCidrBlockForAz2 | String | 10.3.4.0/24 | ○ | AZ2 にあるプライベートサブネットの CIDR ブロック |
| SubnetPrivateIdForAz2 | String | | ○ | AZ2 のプライベートサブネット ID |
| SubnetPrivateCidrBlockForAz3 | String | 10.3.8.0/24 | 条件付き | AZ3 にあるプライベートサブネットの CIDR ブロック |
| SubnetPrivateIdForAz3 | String | | 条件付き | AZ3 のプライベートサブネット ID |
| VPCId | String | | ○ | VPC ID |

### AWS Managed Microsoft AD を用いたユーザーとグループを管理

このテンプレートのデプロイ完了後、[Active Directory 管理ツールのインストール](https://docs.aws.amazon.com/ja_jp/directoryservice/latest/admin-guide/ms_ad_install_ad_tools.html)を行ってください。次に `DOMAIN\Admin` ユーザーに切り替えた上で、**Active Directory Users and Computers tool** を用いて、[ユーザーとグループの作成](https://docs.aws.amazon.com/ja_jp/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.html)を行ってください。

### セキュリティイベントログの Amazon CloudWatch Logs および Amazon S3 への保存

ドメインコントローラーのセキュリティイベントログを Amazon CloudWatch Logs および Amazon S3 に保存するためには、**マネジメントコンソールから手動で**ログ転送機能を有効にします。

