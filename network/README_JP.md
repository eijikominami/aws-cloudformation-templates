[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/network
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/network`` は、VPCやネットワーク関連のリソースを設定します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| Services | Launchers |
| --- | --- |
| TransitGateway | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) |
| VPN | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) |

## Deployment

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file transitgateway.yaml --stack-name TransitGateway
aws cloudformation deploy --template-file vpn.yaml --stack-name VPN
```

デプロイ時に、以下のパラメータを指定することができます。

### Global Accelerator

このテンプレートは、 ``Global Accelerator`` を構成します。

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| EndpointId | String | ○ | | ELBのARN, Elastic IP, EC2のインスタンスID |
| EndpointGroupRegion | String | ○ | | エンドポイントグループを置くリージョン |
| FromPort | Number | | 80 |  ポートの開始番号 |
| HealthCheckIntervalSeconds | 10 / 30 | | 30 | エンドポイントへのヘルスチェック感覚 |
| HealthCheckPath | String | | / | HTTP、HTTPSの場合のヘルスチェックパス |
| HealthCheckPort | Number | | 80 | エンドポイントへのヘルスチェックポート |
| HealthCheckProtocol | TCP / HTTP / HTTPS | | TCP |エンドポイントへのヘルスチェックプロトコル |
| IpAddressType | IPV6 / IPV4 | | IPV4 | サポートするIPアドレスタイプ |
| Name | String | | Default | アクセラレータの名前 |
| Protocol | TCP / UDP | | TCP | クライアントがアクセラレータにアクセスするプロトコル |
| ThresholdCount | Number | | 3 | 正常もしくは異常と判断するヘルスチェックの数 |
| ToPort | Number | | 80 | ポートの終了番号 |

### Transit Gateway

このテンプレートは、 ``Transit Gateway`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **CertificateManagerARN** | List<AWS::EC2::Subnet::Id> | | ○ | サブネットID |
| **CertificateManagerARN** | AWS::EC2::VPC::Id | | ○ | VPC ID |

### VPN

このテンプレートは、 ``Site-to-Site VPN`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **CustomerGatewayOutsideIpAddress** | String | | ○ | インターネットルーティング可能なカスタマーゲートウェイのIPアドレス |
| StaticRoutesOnly | true or false | false | ○ | 静的ルーティングかどうかの設定 |
| TransitGatewayId | String | | ○ | Transit Gateway ID | 