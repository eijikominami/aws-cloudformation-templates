[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/network
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/network`` は、VPCやネットワーク関連のリソースを設定します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Network&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/template.yaml) |

以下のボタンから、個別のAWSサービスを有効化することも可能です。

| 作成されるAWSサービス | 米国西部 (オレゴン) | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- | --- |
| Availability Zone | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=AvailabilityZone&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/az.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=AvailabilityZone&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/az.yaml) |[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=AvailabilityZone&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/az.yaml) |
| Global Accelerator | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=GlobalAccelerator&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/globalaccelerator.yaml) | | |
| IPAM | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=IPAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/ipam.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=IPAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/ipam.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IPAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/ipam.yaml) |
| Network Access Analyzer | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=NetworkAccessAnalyzer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkaccessanalyzer.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=NetworkAccessAnalyzer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkaccessanalyzer.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=NetworkAccessAnalyzer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkaccessanalyzer.yaml) |
| Network Firewall | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=NetworkFirewall&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkfirewall.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=NetworkFirewall&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkfirewall.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=NetworkFirewall&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/networkfirewall.yaml) |
| Route 53 | | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Route53&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/route53resolver.yaml) | |
| TransitGateway | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=TransitGateway&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/transitgateway.yaml) |
| VPN | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=VPN&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/network/vpn.yaml) |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-network.png)

## Deployment

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file az.yaml --stack-name AvailabilityZone --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file egress.yaml --stack-name EgressVPC --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file globalaccelerator.yaml --stack-name GlobalAccelerator
aws cloudformation deploy --template-file ipam.yaml --stack-name IPAM --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file networkaccessanalyzer.yaml --stack-name NetworkAccessAnalyzer --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file networkfirewall.yaml --stack-name NetworkFirewall --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file route53resolver.yaml --stack-name Route53
aws cloudformation deploy --template-file transitgateway.yaml --stack-name TransitGateway --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file vpn.yaml --stack-name VPN --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| CustomerGatewayOutsideIpAddress | String | | | インターネットから疎通可能なカスタマーゲートウェイアドレス |
| DomainName | String | | | ドメイン名 |
| FirewallCidrBlockForEgressAz1 | String | 10.0.0.128/26 | | AZ1 の Egress VPC Firewall サブネットの CIDR ブロック | 
| FirewallCidrBlockForEgressAz2 | String | 10.0.4.128/26 | | AZ2 の Egress VPC Firewall サブネットの CIDR ブロック | 
| IPAMProvisionedCidrs | String | 10.0.0.0/8 | ○ | IPAM に指定する CIDR | 
| OnpremDnsIp | String | | | DNS クエリを転送するオンプレミスのIPアドレス |
| PrincipalsToAssociateWithIPAM | String | | | IPAM に関連付ける 1 つ以上のプリンシパルのリスト | 
| PrincipalsToAssociateWithRoute53ResolverRule | String | | | Route 53 Resolver Rule に関連付ける 1 つ以上のプリンシパルのリスト | 
| PrincipalsToAssociateWithTransitGateway | String | | | Transit Gateway に関連付ける 1 つ以上のプリンシパルのリスト | 
| PrivateCidrBlockForDNSAz1 | String | 10.0.8.0/24 | ○ | AZ1 の DNS VPC Private サブネットの CIDR ブロック |
| PrivateCidrBlockForDNSAz2 | String | 10.0.12.0/24 | ○ | AZ2 の DNS VPC Private サブネットの CIDR ブロック |
| PublicCidrBlockForEgressAz1 | String | 10.0.0.0/26 | ○ | AZ1 の Egress VPC パブリックサブネットの CIDR ブロック | 
| PublicCidrBlockForEgressAz2 | String | 10.0.4.0/26 | ○ | AZ2 の Egress VPC パブリックサブネットの CIDR ブロック | 
| Route53ResolverDirection | BOTH / INBOUND_ONLY / OUTBOUND_ONLY / DISABLED | DISABLED | ○ | Route 53 が受け付ける DNS クエリ |
| TransitCidrBlockForEgressAz1 | String | 10.0.0.64/26 | ○ | AZ1 の Egress VPC Transit サブネットの CIDR ブロック | 
| TransitCidrBlockForEgressAz2 | String | 10.0.4.64/26 | ○ | AZ2 の Egress VPC Transit サブネットの CIDR ブロック | 
| TransitCidrBlockForDNSAz1 | String | 10.0.11.0/24 | ○ | AZ1 の DNS VPC Transit サブネットの CIDR ブロック | 
| TransitCidrBlockForDNSAz2 | String | 10.0.15.0/24 | ○ | AZ2 の DNS VPC Transit サブネットの CIDR ブロック | 
| TransitGatewayDefaultRouteTableId | String | | | Transit Gateway のデフォルトルートテーブル ID | 
| TransitGatewayDestinationCidrBlock | String | | | Transit Gateway に転送するサブネットの CIDR ブロック | 
| VPCCidrBlockForEgress | String | 10.0.0.0/21 | ○ | Egress VPC の CIDR ブロック | 
| VPCCidrBlockForDNS | String | 10.0.8.0/21 | ○ | DNS VPC の CIDR ブロック | 

### マルチアカウント対応

Amazon Transit Gateway や Amazon VPC IP Address Manager (IPAM) を `Network` アカウントで使用する場合には、`AWS Organizations` にて `AWS Resource Access Manager` を有効化してください。 VPC Reachability Analyzer を `Network` アカウントで使用する場合には、VPC Reachability Analyzer の Settings から `信頼されたアクセス` を有効化してください。

### Availablity Zone

このテンプレートは、 ``Availability Zone`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **AvailabilityZone** | AWS::EC2::AvailabilityZone::Name | | ○ | AZ名 |
| InternetGatewayId | String | | | Internet Gateway Id |
| NetworkAddressTranslation | ENABLED / DISABLED | DISABLED　| | NAT Gateway を作成するかどうか |
| NetworkLoadBalancer | ENABLED / DISABLED | DISABLED　| | NetworkLoadBalancer を作成するかどうか |
| SubnetPrivateCidrBlock | String | 10.0.0.0/24 | ○ | プライベートサブネットのCIDRブロック |
| SubnetPublicCidrBlock | String | 10.0.0.0/24 | ○ | パブリックサブネットのCIDRブロック |
| SubnetTransitCidrBlock | String | | | トランジットサブネットのCIDRブロック |
| SubnetFirewallCidrBlock | String | | | Firewall サブネットのCIDRブロック |
| **VPCId** | AWS::EC2::VPC::Id | | ○ | VPC id  |

### Egress/Ingress VPC

このテンプレートは、 ``Egress/Ingress Central VPC`` を構成します。

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| SubnetFirewallCidrBlockForAz1 | String | 10.0.0.128/26| ○ | AZ1 の Firewall サブネットの CIDR ブロック | 
| SubnetFirewallCidrBlockForAz2 | String | 10.0.4.128/26| ○ | AZ2 の Firewall サブネットの CIDR ブロック | 
| SubnetPublicCidrBlockForAz1 | String | 10.0.0.0/26 | ○ | AZ1 の Public サブネットの CIDR ブロック |
| SubnetPublicCidrBlockForAz2 | String | 10.0.4.0/26 | ○ | AZ2 の Public サブネットの CIDR ブロック |
| SubnetTransitCidrBlockForAz1 | String | 10.0.0.64/26 | ○ | AZ1 の Transit サブネットの CIDR ブロック |
| SubnetTransitCidrBlockForAz2 | String | 10.0.4.64/26 | ○ | AZ1 の Transit サブネットの CIDR ブロック |
| TransitGatewayDefaultRouteTableId | String | | | Transit Gateway のデフォルトルートテーブル ID | 
| TransitGatewayDestinationCidrBlock | String | | | Transit Gateway に転送するサブネットの CIDR ブロック | 
| VPCCidrBlock | String | 10.0.0.0/21 | ○ | VPC の CIDR ブロック | 

### Global Accelerator

このテンプレートは、 ``Global Accelerator`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **EndpointId** | String | | ○ | ELBのARN, Elastic IP, EC2のインスタンスID |
| **EndpointGroupRegion** | String | | ○ | エンドポイントグループを置くリージョン |
| FromPort | Number | 80 | |  ポートの開始番号 |
| HealthCheckIntervalSeconds | 10 / 30 | 30 | | エンドポイントへのヘルスチェック感覚 |
| HealthCheckPath | String | / | | HTTP、HTTPSの場合のヘルスチェックパス |
| HealthCheckPort | Number | 80 | | エンドポイントへのヘルスチェックポート |
| HealthCheckProtocol | TCP / HTTP / HTTPS | TCP | |エンドポイントへのヘルスチェックプロトコル |
| IpAddressType | IPV6 / IPV4 | IPV4 | | サポートするIPアドレスタイプ |
| Name | String | Default | | アクセラレータの名前 |
| Protocol | TCP / UDP | TCP | | クライアントがアクセラレータにアクセスするプロトコル |
| ThresholdCount | Number | 3 | | 正常もしくは異常と判断するヘルスチェックの数 |
| ToPort | Number | 80 | | ポートの終了番号 |

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
| **VPCId** | AWS::EC2::VPC::Id | | ○ | VPC id  |

### Route 53

このテンプレートは、 ``Route 53 Resolver`` を構成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| Direction | BOTH / INBOUND_ONLY / OUTBOUND_ONLY / DISABLED | DISABLED | ○ | Route 53 が受け付ける DNS クエリ |
| DomainName | String | | | ドメイン名 |
| OnpremDnsIp | String | | | DNS クエリを転送するオンプレミスのIPアドレス |
| PrincipalsToAssociateWithRoute53ResolverRule | String | | | Route 53 に関連付ける 1 つ以上のプリンシパルのリスト |
| SubnetPrivateCidrBlockForAz1 | String | 10.0.8.0/24 | ○ | AZ1 の Private サブネットの CIDR ブロック |
| SubnetPrivateCidrBlockForAz2 | String | 10.0.12.0/24 | ○ | AZ2 の Private サブネットの CIDR ブロック |
| TransitCidrBlockForDNSAz1 | String | 10.0.11.0/24 | ○ | AZ1 の Transit サブネットの CIDR ブロック | 
| TransitCidrBlockForDNSAz2 | String | 10.0.15.0/24 | ○ | AZ2 の Transit サブネットの CIDR ブロック | 
| **TransitGatewayId** | String | | ○ | Transit Gateway ID | 
| VPCCidrBlock | String | 10.0.8.0/21 | ○ | VPC の CIDR ブロック | 

参加している各アカウントで、プライベートホストゾーン ID、リージョン、関連付ける VPC ID (DNS-VPC) を使用して認証を作成します。

> aws route53 create-vpc-association-authorization --hosted-zone-id HOSTED_ZONE_ID --vpc VPCRegion=REGION,VPCId=VPC_ID

Network アカウントで、参加している各アカウントのホストゾーンに DNS-VPC を関連付けます。

> aws route53 associate-vpc-with-hosted-zone --hosted-zone-id HOSTED_ZONE_ID --vpc VPCRegion=REGION,VPCId=VPC_ID

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

Transit Gateway アタッチメント作成後、 **カスタマーネットワーク行きの Transit Gateway ルートを手動で追加する必要があります** 。