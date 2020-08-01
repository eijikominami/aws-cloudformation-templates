[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/static-website-hosting-with-ssl
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/static-website-hosting-with-ssl`` は、 ``Amazon CloudFront``, ``Amazon S3`` などの **静的Webサイトホスティング** に関連するAWSサービスを設定します。

## TL;DR

1. このテンプレートを実行する前に、本プロジェクトに含まれる ``Security`` テンプレートと ``Global Settings`` テンプレートの両方を実行してください。

+ [Security Template](../security/README_JP.md)
+ [Global Settings Template](../global/README_JP.md)

2. 以下のボタンをクリックすることで、**CloudFormationをデプロイ**することが可能です。

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting-with-ssl/template.yaml) 

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-static-website-hosting.png)

### Amazon S3

このテンプレートは、WebディストリビューションのオリジンとしてS3バケットを作成します。
``オリジンアクセスアイデンティティ``（``OAI``）を用いたCloudFrontからのアクセスは許可されますが、匿名ユーザからの直接アクセスは拒否されます。

### Amazon CloudFront

このテンプレートは、CloudFrontを作成します。
CloudFrontは、``Custom Domain Name with ACM``、 ``Aliases``、 ``Origin Access Identity``、 ``Secondary Origin``、``Logging``に対応します。

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name StaticWebsiteHosting --parameter-overrides DomainName=XXXXX CertificateManagerARN=XXXXX
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| CertificateManagerARN | String | | | ARNを指定した場合、**CloudFront** に **SSL証明書** が紐付けられます。 |
| **DomainName** | String | | ○ | |
| CloudFrontDefaultTTL | Number | 86400 | ○ | |
| CloudFrontMinimumTTL | Number | 0 | ○ | |
| CloudFrontMaximumTTL |  Number | 31536000 | ○ | |
| CloudFrontViewerProtocolPolicy | allow-all / redirect-to-https / https-only | redirect-to-https | ○ | |
| CloudFrontAdditionalName | String | | | AdditionalNameを指定した場合、**CloudFront** に **エイリアス名** が紐付けられます。 |
| CloudFrontSecondaryOriginId | String | | | SecondaryOriginIdを指定した場合、**CloudFront** に **セカンダリS3バケット** が紐付けられます。 |
| CloudFrontRestrictViewerAccess | Enabled / Disabled | Disabled | ○ | Enabledを指定した場合、**CloudFront** の **Restrict Viewer Access** が有効化されます。 |
| CloudFront403ErrorResponsePagePath | String | | | エラーコード403のページパス |
| CloudFront404ErrorResponsePagePath | String | | | エラーコード404のページパス |
| CloudFront500ErrorResponsePagePath | String | | | エラーコード500のページパス |
| S3DestinationBucketArnOfCrossRegionReplication | String | | | ARNを指定した場合、**S3** に **クロスリージョンレプリケーション** が設定されます。 |
| SyntheticsCanaryName | String | | | SyntheticsCanaryNameを指定した場合、 **CloudWatch Synthetics** が有効化されます。 |
| LoggingEnabled | Enabled / Disabled | Enabled | ○ | Enabledを指定した場合、**CloudFront** と **S3** のログ機能が有効化されます。 |
| LogBacketName | String | | ○ | バケット名を指定しなかった場合、ログが保管されるバケット名は、 'defaultsecuritysettings-logs-${AWS::Region}-${AWS::AccountId}' になります。 |
| WebACL | Enabled / Disabled | Disabled | ○ | Disabled に設定された場合、AWS WAFは作成されません。 |

### 手動設定

本テンプレートを実行することで、 ``CloudFront`` に ``secondary origin server`` を設定することはできますが、 現時点ではCloudFormationで ``Origin Group`` がサポートされていません。
したがって、 CloudFormationのデプロイ完了後に、``Origin Group`` の作成と ``Default Cache Behavior Settings`` の**手動設定**が必要です。

1. ``Origins`` と ``Failover criteria`` を含んだ ``Origin Group`` を作成します。
2. ``Default Cache Behavior Settings`` の ``Origin or Origin Group`` に 1. で作成した ``Origin Group`` を指定します。