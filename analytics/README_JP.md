[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/analytics
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/analytics`` は、Google Analytics 4 連携および CloudFront アクセスログ分析を含む分析データ処理基盤を構築します。

## 前提条件

デプロイの前に以下を準備してください。

- CloudFront アクセスログが格納された S3 バケット（CloudFront Logs 機能用）
- API アクセスが有効な Google Analytics 4 プロパティ（Google Analytics 機能用）
- Google Cloud Console で設定済みの OAuth 2.0 認証情報（Google Analytics 機能用）

## TL;DR

以下のボタンをクリックすることで、CloudFormation をデプロイすることが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) |

## デプロイ

SAM CLI を使用してデプロイします。

```bash
cd sam-app
sam build
sam deploy --guided
```

オプションのパラメータは以下の通りです。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **CloudFrontLogDomainName** | String | | | CloudFront ディストリビューションのドメイン名 |
| **CloudFrontLogPrefix** | String | | | CloudFront アクセスログが格納される S3 プレフィックス |
| **CloudFrontLogSourceAccountId** | String | | | クロスアカウントレプリケーション元のアカウント ID |
| **CloudFrontLogSourceRoleName** | String | | | レプリケーション元の IAM ロール名 |
| **GoogleAnalyticsPropertyId** | String | | | Google Analytics 4 プロパティ ID |
| **GoogleAnalyticsAccountId** | String | | | Google Analytics 4 アカウント ID |
| **GoogleAnalyticsClientSecret** | String | | | Google Analytics 4 OAuth2 クライアントシークレット |
| **GlueJobTimeout** | Number | 60 | | Glue ジョブのタイムアウト（分） |
| **GlueWorkerCount** | Number | 5 | | Glue ワーカー数 |
| **LogicalName** | String | analytics | ○ | リソースのカスタムプレフィックス名 |

### CloudFront Logs

``AWSCloudFormationTemplates/analytics/cloudfront-logs`` は、AWS Glue と Amazon Athena を使用して CloudFront 標準アクセスログを分析するリソースを作成します。

このテンプレートは以下を作成します:
- CloudFront 標準ログ形式の Glue テーブル（33 フィールド、LazySimpleSerDe）
- スキーマ検出用 Glue Crawler（オンデマンド）
- 専用クエリ結果出力先を持つ Athena WorkGroup
- 一般的な分析パターンの Athena Named Queries（日別リクエスト数、ステータスコード分布、実ユーザーアクセス）
- Crawler 用の最小権限 IAM ロール

### Google Analytics

``AWSCloudFormationTemplates/analytics/google-analytics`` は、AWS Glue Visual ETL を使用して Google Analytics 4 データ処理リソースを作成します。

このテンプレートは以下を作成します:
- GA4 から S3 へのデータ取り込み用 Glue Visual ETL Job（Custom Resource 経由で管理）
- Google Analytics 4 用 Glue Connection（OAuth2 認証）
- GA4 コアレポート用 Glue Table（Apache Iceberg 形式）
- OAuth2 クライアント認証情報格納用 Secrets Manager シークレット
- Visual ETL Job ライフサイクル管理用 Lambda 関数
- Lambda エラー、Glue ジョブ失敗、推定請求額に対する CloudWatch Alarms
- 日次スケジュール実行用 Glue Trigger（オプション、JST 4:00）
