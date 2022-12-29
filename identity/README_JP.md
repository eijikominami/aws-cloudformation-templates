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
aws cloudformation deploy --template-file microsoftad.yaml --stack-name MicrosoftAD --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

### 複数の AWS アカウントを跨いだディレクトリの共有

**スケールと共有** タブを選択したあとに、 **共有ディレクトリセクション** の **アクション** ボタンを選択してください。次に、 **新しい共有ディレクトリを作成** を選択します。 **共有する AWS アカウントを選択** から要件に合った共有方法を選択してください。

### AWS Managed Microsoft AD

このテンプレートは、 ``AWS Managed Microsoft AD`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| Edition | Standard / Enterprise | Standard | ○ | Microsoft Active Directory のエディション |
| EnableSso | true / false | true | ○ | シングルサインオンを有効化するかどうか |
| Name | String | corp.example.com | ○ | ドメイン名 |
| Password | String | Password1+ | ○ | Admin ユーザのドメイン名 |
| ShortName | String | CORP | ○ | The NetBIOS name for your domain |
| SubnetPrivateCidrBlockForAz1 | String | 10.0.0.0/24 | ○ | AZ1 にあるプライベートサブネットのCIDRブロック |
| SubnetPrivateIdForAz1 | String | 10.0.0.2/24 | ○ | AZ1 のプライベートサブネット ID |
| SubnetPrivateCidrBlockForAz2 | String | 10.0.1.0/24 | ○ | AZ2 にあるプライベートサブネットのCIDRブロック |
| SubnetPrivateIdForAz1 | String | 10.0.3.0/24 | ○ | AZ2 のプライベートサブネット ID |
| TransitGatewayDestinationCidrBlock | String | | | TransitGateway のCIDRブロック |
| VPCCidrBlock | String | String | 10.0.0.0/21 | VPC のCIDRブロック |