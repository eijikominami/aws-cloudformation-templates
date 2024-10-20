[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/web-servers
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/web-servers`` は、 ``Network Load Balancer``や ``VPC`` 、 ``EC2`` インスタンスなどの **EC2で構成されたWebサイトホスティング** に関連するAWSサービスを設定します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=WebServers&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WebServers&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/template.yaml) |

以下のボタンから、個別のAWSサービスを有効化することも可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| Data Lifecycle Manager | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DataLifecycleManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/dlm.yaml&param_LogicalName=DataLifecycleManager) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DataLifecycleManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/dlm.yaml&param_LogicalName=DataLifecycleManager) |
| WAF | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/edge/waf.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/edge/waf.yaml) |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-web-servers.png)

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name WebServers --capabilities CAPABILITY_NAMED_IAM
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AccountIdForAnalysis | String | | | 転送先の分析用AWSアカウント |
| ACMValidationMethod | String | DNS | 条件付き | ドメインの検証方法 |
| ACMDomainName | String | | | 証明書のドメイン名 |
| AlarmLevel | NOTICE/WARNING | NOTICE | | CloudWatch アラームのアラームレベル |
| AutoScalingMaxSize | Number | 1 | ○ | |
| AutoScalingLoadBalancerType | None, application, network | None | ○ | 'None'を指定した場合、ELBは作成されません。 |
| BucketNameForAnalysis | String | | | 転送先の分析用 S3 バケット |
| BucketNameForArtifact | String | | | アーティファクトを保存する S3 バケット名 |
| CentralizedLogBucketName | String | | | 集約ログバケット名 |
| CertificateManagerARN | String | | | ARNを指定した場合、**CloudFront** もしくは **Elastic Load Balancer** に **SSL証明書** が紐付けられます。 |
| CloudFrontDefaultTTL | Number | 86400 | ○ | |
| CloudFrontMinimumTTL | Number | 0 | ○ | |
| CloudFrontMaximumTTL |  Number | 31536000 | ○ | |
| CloudFrontViewerProtocolPolicy | allow-all / redirect-to-https / https-only | redirect-to-https | ○ | |
| CloudFrontAdditionalName | String | | | AdditionalNameを指定した場合、**CloudFront** に **エイリアス名** が紐付けられます。 |
| CloudFrontSecondaryOriginId | String | | | SecondaryOriginIdを指定した場合、**CloudFront** に **セカンダリS3バケット** が紐付けられます。 |
| CloudFrontRestrictViewerAccess | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、**CloudFront** の **Restrict Viewer Access** が有効化されます。 |
| CloudFront403ErrorResponsePagePath | String | | | エラーコード403のページパス |
| CloudFront404ErrorResponsePagePath | String | | | エラーコード404のページパス |
| CloudFront500ErrorResponsePagePath | String | | | エラーコード500のページパス |
| CodeStarConnectionArn | String | | | CodeStar connection の ARN |
| ComputeType | INSTANCE / CONTAINER / APPRUNNER | INSTANCE | ○ | コンピュート基盤 |
| DesiredCapacity | Number | 1 | ○ | | 
| DockerFilePath | String | | | Dockerfile のパス | 
| DomainName | String | | | ドメイン名 | 
| EC2DailySnapshotScheduledAt | String | 17:00 | ○ | スナップショット作成時刻 (UTC) |
| EC2ImageId | AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> | /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64 | ○ | Amazon Linux 2 AMI (HVM), SSD Volume Type (64bit x86) |
| EC2InstanceType | String | t3.micro | ○ | | 
| EC2PatchingAt | Number | 3 | ○ | パッチ処理を開始する時刻 |
| EC2KeyName | String | | | 値が指定されない場合は、 **SSHキー** は設定されません。 |
| EC2VolumeSize | Number | 8 | ○ | |
| GitHubOwnerNameForArtifact | String | | | Artifact の GitHub オーナー名 |
| GitHubRepoNameForArtifact | String | | | Artifact の GitHub リポジトリ名 |
| GitHubBranchNameForArtifact | String | | | Artifact の GitHub ブランチ名 |
| GitHubBranchNameForBuildSpec | String | | | BuildSpec の GitHub ブランチ名 |
| GlobalInfrastructure | NONE / CLOUDFRONT / GLOBAL_ACCELERATOR | | ○ | CloudFront や Global Accelerator を有効にするかどうか |
| Logging | ENABLED / DISABLED | ENABLED | ○ | ENABLEDを指定した場合、ログ機能が有効化されます。 |
| LogGroupNameTransferredToS3 | String | | | S3 にログを転送する CloudWatch Log Group 名 |
| Route53HostedZoneId | String | | | Route53のホストゾーンID |
| SubnetPrivateCidrBlockForAz1 | String | 10.1.0.0/24 | ○ | AZ1 の プライベートサブネットの CIDR ブロック |
| SubnetPrivateCidrBlockForAz2 | String | 10.1.2.0/24 | ○ | AZ2 の プライベートサブネットの CIDR ブロック |
| SubnetPrivateCidrBlockForAz3 | String | 10.1.4.0/24 | ○ | AZ3 の プライベートサブネットの CIDR ブロック |
| SubnetPublicCidrBlockForAz1 | String | 10.1.1.0/25 | ○ | AZ1 の パブリックサブネットの CIDR ブロック |
| SubnetPublicCidrBlockForAz2 | String | 10.1.3.0/25 | ○ | AZ2 の パブリックサブネットの CIDR ブロック |
| SubnetPublicCidrBlockForAz3 | String | 10.1.5.0/25 | ○ | AZ3 の パブリックサブネットの CIDR ブロック |
| SubnetTransitCidrBlockForAz1 | String | 10.1.1.128/25 | ○ | AZ1 の トランジットサブネットの CIDR ブロック |
| SubnetTransitCidrBlockForAz2 | String | 10.1.3.128/25 | ○ | AZ2 の トランジットサブネットの CIDR ブロック |
| SubnetTransitCidrBlockForAz3 | String | 10.1.5.128/25 | ○ | AZ3 の トランジットサブネットの CIDR ブロック |
| TransitGatewayId | String | | | Transit Gateway の Id |
| TransitGatewayDestinationCidrBlock | String | | | TransitGatewayに転送するアドレス範囲 |
| VPCCidrBlock | String | 10.1.0.0/21 | ○ | VPC の CIDR ブロック |
| WebACL | ENABLED / DISABLED | DISABLED | ○ | DISABLED に設定された場合、AWS WAFは作成されません。 |
| WebACLArnForCloudFront | String | | | CloudFrontにアタッチするWAFのARN |

## トラブルシューティング

`AWS-GatherSoftwareInventory` を含むSSM State Manager の関連付けが既に存在する場合、このテンプレートは失敗します。`IgnoreResourceConflicts` オプションを ENABLED に設定してこのテンプレートを実行してください。