[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/shared
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/shared`` は、 AWS Organizations 内のアカウントにおける共通サービスを構築します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SharedServices&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/template.yaml) |

以下のボタンから、個別のAWSサービスを有効化することも可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| FluentBit (Syslog) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=FluentBit&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/fluentbit.yaml)  | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=FluentBit&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/shared/fluentbit.yaml) |

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
| AccountIdForArchive | String | | | ログアーカイブアカウント ID |
| ActiveDirectoryEdition | Enterprise / Standard | Standard | ○ | Microsoft Active Directory を作成する AWS Directory Service のエディション |
| ActiveDirectoryEnableSso | true / false | true | ○ | Microsoft Active Directory を用いて SSO を有効化するかどうか |
| ActiveDirectoryName | String | corp.example.com | ○ | AWS Managed Microsoft AD directory の　FQDN |
| ActiveDirectoryPassword | String | Password1+ | ○ | 管理者権限を有する Admin ユーザのパスワード |
| ActiveDirectoryShortName | String | CORP | ○ | NetBIOS 名 |
| ActiveDirectorySubnetCidrBlockForAz1 | String | 10.1.0.64/26 | ○ | AZ1 の パブリックサブネットの CIDR ブロック |
| ActiveDirectorySubnetCidrBlockForAz2 | String | 10.1.64.64/26 | ○ | AZ2 の パブリックサブネットの CIDR ブロック |
| BucketNameForArchive | String | | | ログアーカイブ用の S3 バケット名 |
| DomainName | String | | | ドメイン名 |
| FluentBitAddress1 | String | 10.3.0.14 | | FluentBit のプライベートアドレス |
| FluentBitAddress2 | String | 10.3.64.14 | | FluentBit のプライベートアドレス |
| FluentBitForSyslog | ENABLED / DISABLED | true | ○ | Syslog フォーマットのログ収集ののための FluentBit を作成するかどうか |
| IdentityCenterArn | String | | | AWS IAM Identity Center の ARN |
| SubnetPrivateCidrBlockAz1 | String | 10.3.0.64/26 | ○ | AZ1 の プライベートサブネットの CIDR ブロック |
| SubnetPrivateCidrBlockAz2 | String | 10.3.64.64/26 | ○ | AZ2 の プライベートサブネットの CIDR ブロック |
| SubnetTransitCidrBlockAz1 | String | 10.3.0.128/26 | ○ | AZ1 の トランジットサブネットの CIDR ブロック |
| SubnetTransitCidrBlockAz2 | String | 10.3.64.128/26 | ○ | AZ1 の トランジットサブネットの CIDR ブロック |
| ResolverRuleId | String | | | VPC に紐づけるリゾルバルールの ID |
| TransitGatewayId | String | | | Transit Gateway の ID |
| TransitGatewayDestinationCidrBlock | String | | | TransitGateway に転送する CIDR ブロック |
| VPCCidrBlock | String | 10.3.0.0/16 | ○ | VPC の CIDR ブロック |

### IAM Identity Center の信頼されたアクセス

AWS IAM Identity Center のコンソール、もしくは AWS Organizations コンソールから信頼されたアクセスを有効化した上で、手動で AWS Managed Microsoft AD と接続することが可能です。