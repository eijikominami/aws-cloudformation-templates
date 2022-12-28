[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/shared
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/shared`` は、 AWS Organizations 内のアカウントにおける共通サービスを構築します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) 

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-shared.png)

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name SharedServices --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| ActiveDirectoryEdition | Enterprise / Standard | Standard | ○ | Microsoft Active Directory を作成する AWS Directory Service のエディション |
| ActiveDirectoryEnableSso | true / false | true | ○ | Microsoft Active Directory を用いて SSO を有効化するかどうか |
| ActiveDirectoryName | String | corp.example.com | ○ | AWS Managed Microsoft AD directory の　FQDN |
| ActiveDirectoryPassword | String | Password1+ | ○ | 管理者権限を有する Admin ユーザのパスワード |
| ActiveDirectoryShortName | String | CORP | ○ | NetBIOS 名 |
| ActiveDirectorySubnetCidrBlockForAz1 | String | 10.1.0.64/26 | ○ | AZ1 の パブリックサブネットの CIDR ブロック |
| ActiveDirectorySubnetCidrBlockForAz2 | String | 10.1.1.64/26 | ○ | AZ2 の パブリックサブネットの CIDR ブロック |
| SubnetTransitCidrBlockAz1 | String | 10.3.1.0/24 | ○ | AZ1 の トランジットサブネットの CIDR ブロック |
| SubnetTransitCidrBlockAz2 | String | 10.3.5.0/24 | ○ | AZ2 の トランジットサブネットの CIDR ブロック |
| TransitGatewayId | String | | | Transit Gateway の ID |
| TransitGatewayDestinationCidrBlock | String | | | TransitGateway に転送する CIDR ブロック |
| VPCCidrBlock | String | 10.3.0.0/16 | ○ | VPC の CIDR ブロック |

### IAM Identity Center の信頼されたアクセス

AWS IAM Identity Center のコンソール、もしくは AWS Organizations コンソールから信頼されたアクセスを有効化した上で、手動で AWS Managed Microsoft AD と接続することが可能です。