Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# availability-zone(en)

availability-zone sets Availability Zone in VPC.

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `AvailabilityZone` | String | | ○ | The Availability Zone name |
| `InternetGatewayId` | String | | ○ | The Internet Gateway Id |
| `NetworkLoadBalancer` | ENABLED / DISABLED | | ○ | Enable or disable Network LoadBalaner |
| `LogicalNamePrefix` | String | WebServers | ○ | The custom prefix name |
| `SNSForAlertArn` | String | | ○ | The ARN of SNS for alert |
| `SNSForDeploymentArn` | String | | ○ | The ARN of SNS for development |
| `SubnetPublicCidrBlock` | String | | | The Public subnet CIDR block |
| `SubnetPrivateCidrBlock` | String | | | The Private subnet CIDR block |
| `SubnetTransitCidrBlock` | String | | | The transit subnet CIDR block |
| `TransitGatewayId` | String | | | The ID of a transit gateway |
| `TransitGatewayDestinationCidrBlock` | String | | | The IPv4 CIDR block forward to TransitGateway |
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
| `NetworkLoadBalancer` | ENABLED / DISABLED | | ○ | NLB を有効化するかどうか |
| `LogicalNamePrefix` | String | WebServers | ○ | カスタムプリフィックス名 |
| `SNSForAlertArn` | String | | ○ | アラート用SNSのARN |
| `SNSForDeploymentArn` | String | | ○ | デプロイメント用SNSのARN |
| `SubnetPublicCidrBlock` | String | | | パブリックサブネットのCIDRブロック |
| `SubnetPrivateCidrBlock` | String | | | プライベートサブネットのCIDRブロック |
| `SubnetTransitCidrBlock` | String | | | Transit Gateway用のサブネットのCIDRブロック |
| `TransitGatewayId` | String | | | Transit Gateway Id |
| `TransitGatewayDestinationCidrBlock` | String | | | TransitGatewayに転送するCIDRブロック |
| `VPCId` | String | | ○ | VPC ID |