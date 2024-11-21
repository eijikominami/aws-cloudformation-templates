[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/migration
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/migration`` は、移行に関連するサービスを構築します。

## 移行

以下のボタンから、個別のAWSサービスを有効化することが可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| AWS Application Migration Service (AWS MGN) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MGN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/migration/mgn.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MGN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/migration/mgn.yaml) |

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file mgn.yaml --stack-name MGN --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

### AWS Application Migration Service (AWS MGN)

このテンプレートは ``AWS Application Migration Service (AWS MGN)`` を作成します。

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](https://docs.aws.amazon.com/ja_jp/prescriptive-guidance/latest/patterns/images/pattern-img/21346c0f-0643-4f4f-b21f-fdfe24fc6a8f/images/bd0dfd42-4ab0-466f-b696-804dedcf4513.png)

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | CloudWatch アラームのアラームレベル |
| DnsIpAz1 | String | 10.0.0.53 | | Route53 に割り当てる IP アドレス | 
| DnsIpAz2 | String | 10.0.1.53 | | Route53 に割り当てる IP アドレス | 
| DnsIpAz3 | String | 10.0.2.53 | | Route53 に割り当てる IP アドレス | 
| **SourceCidrBlock** | String | 0.0.0.0/0 | ○ | ソースサーバの CIDR ブロック |
| SubnetCidrBlockAz1 | String | 10.0.0.0/24 | | AZ1 の CIDR ブロック |
| SubnetCidrBlockAz2 | String | 10.0.1.0/24 | | AZ2 の CIDR ブロック |
| SubnetCidrBlockAz3 | String | 10.0.2.0/24 | | AZ3 の CIDR ブロック |
| SubnetIdAz1 | String | | | AZ1 のサブネット ID |
| SubnetIdAz2 | String | | | AZ2 のサブネット ID |
| SubnetIdAz3 | String | | | AZ3 のサブネット ID |
| **VPCCidrBlock** | String | 10.0.0.0/22 | ○ | VPC の CIDR ブロック |
| VPCId | String | | | VPC Id |