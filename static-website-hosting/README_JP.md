[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/static-website-hosting
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/static-website-hosting`` は、 ``Amazon CloudFront``, ``Amazon S3`` などの **静的Webサイトホスティング** に関連するAWSサービスを設定します。

## 前提条件

デプロイの前に以下を準備してください。

- 登録されたドメイン名と設定された Route53 ホストゾーン
- AWS Certificate Manager で作成された SSL 証明書（CloudFront 用に us-east-1 で）
- ウェブサイトアーティファクトとログを保存する S3 バケット
- CloudFront ディストリビューションとキャッシュ動作の理解

## TL;DR

1. このテンプレートを実行する前に、本プロジェクトに含まれる ``Security`` テンプレートと ``Global Settings`` テンプレートの両方を実行してください。

+ [Security Template](../security/README_JP.md)
+ [Global Settings Template](../global/README_JP.md)

2. 以下のボタンをクリックすることで、**CloudFormationをデプロイ** することが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting/template.yaml) | 

以下のボタンから、個別のAWSサービスを有効化することも可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| Synthetics | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Synthetics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/synthetics-heartbeat.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Synthetics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/synthetics-heartbeat.yaml) |
| Real-time Dashboard | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=RealtimeLogs&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/edge/realtime-dashboard.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=RealtimeLogs&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/edge/realtime-dashboard.yaml) |
| WAF | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/edge/waf.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WAF&templateURL=https://s3.amazonaws.com/eijikominami/aws-cloudformation-templates/edge/waf.yaml) |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-static-website-hosting.png)

### Amazon S3

#### オリジン

このテンプレートは、WebディストリビューションのオリジンとしてS3バケットを作成します。
``オリジンアクセスアイデンティティ``（``OAI``）を用いたCloudFrontからのアクセスは許可されますが、匿名ユーザからの直接アクセスは拒否されます。

#### ログの保存

S3やCloudFrontで生成されたログは、このテンプレートで作成されたS3バケットに保存されます。

### Amazon CloudFront

このテンプレートは、CloudFrontを作成します。
CloudFrontは、``Custom Domain Name with ACM``、 ``Aliases``、 ``Origin Access Identity``、 ``Secondary Origin``、``Logging``に対応します。

### AWS WAF

このテンプレートは、Amazon CloudFront に ``AWS WAF`` を適用することができます。
以下の [**AWS Managed Rules rule**](https://docs.aws.amazon.com/ja_jp/waf/latest/developerguide/aws-managed-rule-groups-list.html) が有効化されます。

+ AWSManagedRulesCommonRuleSet
+ AWSManagedRulesAdminProtectionRuleSet
+ AWSManagedRulesKnownBadInputsRuleSet
+ AWSManagedRulesAmazonIpReputationList

### Synthetics Stack

このテンプレートは、外形監視に関するネストされたスタックを生成します。
このスタックの詳細は、 [こちら](../cloudops/README_JP.md) をご覧ください。

### Real-time Dashboard Stack

このテンプレートは、CloudFrontのリアルタイムログのダッシュボードに関するネストされたスタックを生成します。
これには、以下のリソースが含まれます。

#### Amazon Kinesis Data Streams

Amazon CloudFrontで生成されたリアルタイムログは、 ``Amazon Kinesis Data Streams`` と統合され、 ``Amazon Kinesis Data Firehose`` を用いて一般的なHTTPエンドポイントに対してこれらのログを配信します。

#### Amazon Kinesis Firehose とこれに関連したリソース

``Amazon Kinesis Data Firehose`` は、ログを ``Amazon S3`` や ``Amazon OpenSearch Service`` に配信します。
Kinesis Firehose は、 ``AWS Lambda`` を用いて、ログの処理やログのフォーマットの変換を行います。
Elasticsearch にログを送信できない場合、Kinesis Firehose は ``Amazon S3`` バケットにログを送信します。

#### Amazon OpenSearch Service

``Amazon OpenSearch Service`` を用いて、リアルタイムダッシュボードやアラートの作成、異常の調査、運用イベントに迅速に対応できます。
追跡できる一般的なデータポイントには、さまざまな地域から発信されたユーザのリクエストの数や、待ち時間が長くなったユニークユーザの数が含まれます。

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name StaticWebsiteHosting --parameter-overrides DomainName=XXXXX CertificateManagerARN=XXXXX
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AccountIdForAnalysis | String | | | 転送先の分析用AWSアカウント |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | CloudWatch アラームのアラームレベル |
| BucketNameForAnalysis | String | | | 転送先の分析用 S3 バケット |
| BucketNameForArtifact | String | | | アーティファクトを保存する S3 バケット名 |
| CertificateManagerARN | String | | | ARNを指定した場合、**CloudFront** に **SSL証明書** が紐付けられます。 |
| CloudFrontAdditionalMetrics | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、 追加のメトリクスが有効化されます。 |
| CloudFrontDefaultTTL | Number | 86400 | ○ | CloudFront Default TTL |
| CloudFrontMinimumTTL | Number | 0 | ○ | CloudFront Minimum TTL |
| CloudFrontMaximumTTL |  Number | 31536000 | ○ | CloudFront Maximum TTL |
| CloudFrontViewerProtocolPolicy | allow-all / redirect-to-https / https-only | redirect-to-https | ○ | |
| CloudFrontAdditionalName | String | | | AdditionalNameを指定した場合、**CloudFront** に **エイリアス名** が紐付けられます。 |
| CloudFrontSecondaryOriginId | String | | | SecondaryOriginIdを指定した場合、**CloudFront** に **セカンダリS3バケット** が紐付けられます。 |
| CloudFrontRestrictViewerAccess | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、**CloudFront** の **Restrict Viewer Access** が有効化されます。 |
| CloudFront403ErrorResponsePagePath | String | | | エラーコード403のページパス |
| CloudFront404ErrorResponsePagePath | String | | | エラーコード404のページパス |
| CloudFront500ErrorResponsePagePath | String | | | エラーコード500のページパス |
| CloudWatchAppicationSignals | ENABLED / DISABLED | ENABLED | | ENABLEDを指定した場合、**Internet Monitor** と **CloudWatch Synthetics** が有効化されます。
| CodeStarConnectionArn | String | | | CodeStar connection の ARN |
| **DomainName** | String | | ○ | ドメイン名 |
| GitHubOwnerNameForWebsite | String | | | コンテンツリポジトリの GitHub オーナー名 |
| GitHubRepoNameForWebsite | String | | | コンテンツリポジトリの GitHub リポジトリ名 |
| GitHubBranchNameForWebsite | String | | | コンテンツリポジトリの GitHub ブランチ名 |
| Logging | ENABLED / DISABLED | ENABLED | ○ | ENABLEDを指定した場合、**CloudFront** と **S3** のログ機能が有効化されます。 |
| RealtimeDashboardElasticSearchVolumeSize | Number | 10 | ○ | OpenSearch Service のボリュームサイズ（GB） |
| RealtimeDashboardElasticSearchInstanceType | String | r5.large.elasticsearch | ○ | OpenSearch Service のインスタンスタイプ |
| RealtimeDashboardElasticSearchMasterType | String | r5.large.elasticsearch | ○ | OpenSearch Service のマスタータイプ |
| RealtimeDashboardElasticSearchLifetime | Number | 1 | ○ | OpenSearch Service の生存時間 |
| RealtimeDashboardElasticSearchMasterUserName | String | root | ○ | OpenSearch Service のユーザ名 |
| RealtimeDashboardElasticSearchMasterUserPassword | String | Password1+ | ○ | OpenSearch Service のパスワード |
| RealtimeDashboardElasticsearchVersion | String | OpenSearch_2.13 | ○ | OpenSearch Service のバージョン |
| RealtimeDashboardState | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、 **Real-time Dashboard** が有効化されます。|
| RealtimeDashboardSamplingRate | Number | 100 | ○ | CloudFrontから送信するログのサンプリングレート |
| RealtimeDashboardKinesisShardCount | Number | 1 | ○ | Kinesisのシャード数 |
| RealtimeDashboardKinesisNumberOfPutRecordThreshold | Number | 12000000 | ○ | PutRecord のAPIコールの閾値 |
| Route53HostedZoneId | String | | | Route53のホストゾーンID |
| S3DestinationBucketArnOfCrossRegionReplication | String | | | ARNを指定した場合、**S3** に **クロスリージョンレプリケーション** が設定されます。 |
| SyntheticsCanaryName | String | | | SyntheticsCanaryNameを指定した場合、 **CloudWatch Synthetics** が有効化されます。 |
| WebACLArn | String | | | WebACL のARN |

### 手動設定

#### Origin failover

本テンプレートを実行することで、 ``CloudFront`` に ``secondary origin server`` を設定することはできますが、 現時点ではCloudFormationで ``Origin Group`` がサポートされていません。
したがって、 CloudFormationのデプロイ完了後に、``Origin Group`` の作成と ``Default Cache Behavior Settings`` の**手動設定**が必要です。

1. ``Origins`` と ``Failover criteria`` を含んだ ``Origin Group`` を作成します。
2. ``Default Cache Behavior Settings`` の ``Origin or Origin Group`` に 1. で作成した ``Origin Group`` を指定します。## トラブルシ
ューティング

### CloudFront の問題

CloudFront ディストリビューションがコンテンツを正しく配信しない場合：

1. オリジン S3 バケットが存在し、ウェブサイトファイルが含まれていることを確認してください
2. Origin Access Identity (OAI) が S3 バケットにアクセスする適切な権限を持っていることを確認してください
3. SSL 証明書が有効で、正しいドメイン用に発行されていることを確認してください
4. Route53 ホストゾーンが正しい DNS レコードで適切に設定されていることを確認してください

### SSL 証明書の問題

SSL 証明書が CloudFront で動作しない場合：

1. 証明書が us-east-1 リージョンで作成されていることを確認してください（CloudFront に必要）
2. 証明書が必要なすべてのドメイン名（プライマリとエイリアス）を含んでいることを確認してください
3. 証明書の検証が完了し、証明書が発行されていることを確認してください
4. 証明書 ARN がテンプレートパラメータで正しく指定されていることを確認してください

### S3 アクセスの問題

S3 バケットアクセスが正常に動作しない場合：

1. S3 バケットポリシーが CloudFront OAI からのアクセスを許可していることを確認してください
2. CloudFront アクセスを許可すべき時にバケットがパブリックアクセスをブロックしていないことを確認してください
3. ウェブサイトファイルが正しい S3 バケットにアップロードされていることを確認してください
4. CloudFront でデフォルトルートオブジェクトが正しく設定されていることを確認してください

### WAF の問題

WAF が正当なトラフィックをブロックしている場合：

1. WAF ログを確認してどのルールがトラフィックをブロックしているかを特定してください
2. WAF ルール設定を調整するか、正当なトラフィックに対する例外を追加してください
3. WAF の CloudWatch メトリクスを監視してトラフィックパターンを理解してください
4. レート制限ルールが制限的すぎる場合は調整を検討してください

### リアルタイムダッシュボードの問題

リアルタイムダッシュボードがデータを表示しない場合：

1. CloudFront リアルタイムログが有効化され正しく設定されていることを確認してください
2. Kinesis Data Streams が CloudFront からデータを受信していることを確認してください
3. OpenSearch Service クラスターが正常でアクセス可能であることを確認してください
4. ログ処理用の Lambda 関数が正しく動作していることを確認してください