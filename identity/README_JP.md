[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/network
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/network`` は、アイデンティティ、リソース、アクセス許可をセキュアかつ大規模に管理可能な AWS Identity Services を構築します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| Services | Launchers |
| --- | --- |
| AWS Managed Microsoft AD | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MicrosoftAD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/microsoftad.yaml) |

## Deployment

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file microsoftad.yaml --stack-name MicrosoftAD
```

デプロイ時に、以下のパラメータを指定することができます。

### AWS Managed Microsoft AD

このテンプレートは、 ``AWS Managed Microsoft AD`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| Edition | Standard / Enterprise | Standard | ○ | Microsoft Active Directory のエディション |
| EnableSso | true / false | true | ○ | シングルサインオンを有効化するかどうか |
| Name | String | corp.example.com | ○ | ドメイン名 |
| Password | String | Password1+ | ○ | Admin ユーザのドメイン名 |
| ShortName | String | CORP | ○ | The NetBIOS name for your domain |
| SubnetPublicCidrBlockForAz1 | String | 10.0.0.0/24 | ○ | AZ1 にあるパブリックサブネットのCIDRブロック |
| SubnetTransitCidrBlockAz1 | String | 10.0.0.2/24 | ○ | AZ1 にあるプライベートサブネットのCIDRブロック |
| SubnetPublicCidrBlockForAz2 | String | 10.0.1.0/24 | ○ | AZ2 にあるパブリックサブネットのCIDRブロック |
| SubnetTransitCidrBlockAz2 | String | 10.0.3.0/24 | ○ | AZ2 にあるプライベートサブネットのCIDRブロック |
| TransitGatewayDestinationCidrBlock | String | | | TransitGateway のCIDRブロック |
| VPCCidrBlock | String | String | 10.0.0.0/21 | VPC のCIDRブロック |