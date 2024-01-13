Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# availability-zone(en)

availability-zone sets Availability Zone in VPC.

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AvailabilityZone` | String | | ○ | The Availability Zone name |
| `InternetGatewayId` | String | | ○ | The Internet Gateway Id |
| `NetworkAddressTranslation` | ENABLED / DISABLED | DISABLED　| ○ | Enable or disable NetworkAddressTranslation (NAT) |
| `NetworkLoadBalancer` | ENABLED / DISABLED | DISABLED　| ○ | Enable or disable Network LoadBalaner |
| `LogicalName` | String | WebServers | ○ | The custom prefix name |
| `SNSForAlertArn` | String | | ○ | The ARN of SNS for alert |
| `SNSForDeploymentArn` | String | | ○ | The ARN of SNS for development |
| `SubnetPrivateCidrBlock` | String | 10.0.0.0/24 | ○ | The Private subnet CIDR block |
| `SubnetPublicCidrBlock` | String | | | The Public subnet CIDR block |
| `SubnetPrivateCidrBlock` | String | | | The Private subnet CIDR block |
| `SubnetTransitCidrBlock` | String | | | The transit subnet CIDR block |
| `VPCId` | String | | ○ | The VPC id |

---------------------------------------

# availability-zone(ja)

availability-zone は、VPC 上に Availability Zone を設定します。

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `AvailabilityZone` | String | | ○ | AZ名 |
| `InternetGatewayId` | String | | ○ | Internet Gateway ID |
| `NetworkAddressTranslation` | ENABLED / DISABLED | DISABLED　| ○ | NAT Gateway を有効化するかどうか |
| `NetworkLoadBalancer` | ENABLED / DISABLED | DISABLED　| ○ | NLB を有効化するかどうか |
| `LogicalName` | String | WebServers | ○ | カスタムプリフィックス名 |
| `SNSForAlertArn` | String | | ○ | アラート用SNSのARN |
| `SNSForDeploymentArn` | String | | ○ | デプロイメント用SNSのARN |
| `SubnetPrivateCidrBlock` | String | | | パブリックサブネットのCIDRブロック |
| `SubnetPublicCidrBlock` | String | | | パブリックサブネットのCIDRブロック |
| `SubnetPrivateCidrBlock` | String | | | プライベートサブネットのCIDRブロック |
| `SubnetTransitCidrBlock` | String | | | Transit Gateway用のサブネットのCIDRブロック |
| `VPCId` | String | | ○ | VPC ID |