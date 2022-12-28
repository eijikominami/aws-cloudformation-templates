[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/network
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/network`` は、VPCやネットワーク関連のリソースを設定します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/template.yaml)

以下のボタンから、個別のAWSサービスを有効化することも可能です。

| Services | Launchers |
| --- | --- |
| Availability Zone | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=AvailabilityZone&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/az.yaml) |
| Global Accelerator | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=GlobalAccelerator&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/globalaccelerator.yaml) |
| IPAM | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IPAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/ipam.yaml) |
| Network Access Analyzer | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=NetworkAccessAnalyzer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkaccessanalyzer.yaml) |
| Network Firewall | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=NetworkFirewall&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkfirewall.yaml) |
| Route 53 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Route53&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/route53.yaml) |
| TransitGateway | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) |
| VPN | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-network.png)

## Deployment

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file az.yaml --stack-name AvailabilityZone
aws cloudformation deploy --template-file globalaccelerator.yaml --stack-name GlobalAccelerator
aws cloudformation deploy --template-file ipam.yaml --stack-name IPAM
aws cloudformation deploy --template-file networkaccessanalyzer.yaml --stack-name NetworkAccessAnalyzer
aws cloudformation deploy --template-file networkfirewall.yaml --stack-name NetworkFirewall
aws cloudformation deploy --template-file route53.yaml --stack-name Route53
aws cloudformation deploy --template-file transitgateway.yaml --stack-name TransitGateway
aws cloudformation deploy --template-file vpn.yaml --stack-name VPN
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| IPAMProvisionedCidrs | String | 10.0.0.0/8 | ○ | The CIDR provisioned to the IPAM pool | 
| PrincipalsToAssociateWithIPAM | String | | | Specifies a list of one or more principals to associate with IPAM | 
| PrincipalsToAssociateWithTransitGateway | String | | | Specifies a list of one or more principals to associate with Transit Gateway | 
| SubnetPublicCidrBlockForAz1 | String | 10.0.0.0/26 | ○ | AZ1 の パブリックサブネットの CIDR ブロック | 
| SubnetTransitCidrBlockAz1 | String | 10.0.0.64/26 | ○ | AZ1 の Transit サブネットの CIDR ブロック | 
| SubnetFirewallCidrBlockForAz1 | String | 10.0.0.128/26 | | AZ1 の Firewall サブネットの CIDR ブロック | 
| SubnetPublicCidrBlockForAz2 | String | 10.0.4.0/26 | ○ | AZ2 の パブリックサブネットの CIDR ブロック | 
| SubnetTransitCidrBlockAz2 | String | 10.0.4.64/26 | ○ | AZ2 の Transit サブネットの CIDR ブロック | 
| SubnetFirewallCidrBlockForAz2 | String | 10.0.4.128/26 | | AZ2 の Firewall サブネットの CIDR ブロック | 
| TransitGatewayDefaultRouteTableId | String | | | Transit Gateway のデフォルトルートテーブル ID | 
| TransitGatewayDestinationCidrBlock | String | | | Transit Gateway に転送するサブネットの CIDR ブロック | 
| VPCCidrBlock | String | 10.0.0.0/16 | ○ | VPC の CIDR ブロック | 

### マルチアカウント対応

Amazon Transit Gateway や Amazon VPC IP Address Manager (IPAM) を `Network` アカウントで使用する場合には、`AWS Organizations` にて `AWS Resource Access Manager` を有効化してください。 VPC Reachability Analyzer を `Network` アカウントで使用する場合には、VPC Reachability Analyzer の Settings から `信頼されたアクセス` を有効化してください。

### Availablity Zone

このテンプレートは、 ``Availability Zone`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AvailabilityZone | AWS::EC2::AvailabilityZone::Name | | ○ | AZ名 |
| InternetGatewayId | String | | | Internet Gateway Id |
| NetworkAddressTranslation | ENABLED / DISABLED | DISABLED　| | NAT Gateway を作成するかどうか |
| NetworkLoadBalancer | ENABLED / DISABLED | DISABLED　| | NetworkLoadBalancer を作成するかどうか |
| SubnetPrivateCidrBlock | String | 10.0.0.0/24 | ○ | プライベートサブネットのCIDRブロック |
| SubnetPublicCidrBlock | String | 10.0.0.0/24 | ○ | パブリックサブネットのCIDRブロック |
| SubnetTransitCidrBlock | String | | | トランジットサブネットのCIDRブロック |
| SubnetFirewallCidrBlock | String | | | Firewall サブネットのCIDRブロック |
| VPCId | AWS::EC2::VPC::Id | | ○ | VPC id  |

### Global Accelerator

このテンプレートは、 ``Global Accelerator`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
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

### IP Address Manager (IPAM)

このテンプレートは、 ``IP Address Manager (IPAM)`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| PrincipalsToAssociateWithIPAM | String | | | IPAM に関連付ける 1 つ以上のプリンシパルのリスト |
| ProvisionedCidrs | String | 10.0.0.0/8 | ○ | IPAM に指定する CIDR |

### Network Firewall

このテンプレートは、 ``Network Firewall`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| SubnetIdAz1 | String | | | The firewall subnet id in AZ1 |
| SubnetIdAz2 | String | | | The firewall subnet id in AZ2 |
| SubnetIdAz3 | String | | | The firewall subnet id in AZ3 |

### Route 53

このテンプレートは、 ``Route 53`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| SecurityGroupId | AWS::EC2::SecurityGroup::Id | | ○ | セキュリティグループのId |
| SubnetId1 | String | | ○ | DNSクエリが出されるサブネットのId |
| SubnetId2 | String | | | DNSクエリが出されるサブネットのId |
| SubnetId3 | String | | | DNSクエリが出されるサブネットのId |

### Transit Gateway

このテンプレートは、 ``Transit Gateway`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| PrincipalsToAssociateWithTransitGateway | String | | | Transit Gateway を共有するプリンシパル |

### VPN

このテンプレートは、 ``Site-to-Site VPN`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **CustomerGatewayOutsideIpAddress** | String | | ○ | インターネットルーティング可能なカスタマーゲートウェイのIPアドレス |
| StaticRoutesOnly | true or false | false | ○ | 静的ルーティングかどうかの設定 |
| TransitGatewayId | String | | ○ | Transit Gateway ID | 