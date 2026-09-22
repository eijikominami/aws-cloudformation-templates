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
- CloudWatch Synthetics の結果が格納された S3 バケット（Synthetics 機能用）

## TL;DR

以下のボタンをクリックすることで、CloudFormation をデプロイすることが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) |

## アーキテクチャ

3 つのパイプラインは Glue データベース・Athena WorkGroup・S3 テーブルバケットを共有します。各生データは個別の Glue ジョブが読み取り、そのバケット内の Apache Iceberg テーブルへ書き込みます。テーブルはフェデレーテッドカタログ `s3tablescatalog` を通じて Athena から参照できます。

テーブル名とカラム名は小文字にする必要があります。S3 Tables は名前または定義に大文字を含むテーブルを公開せず、バケットを統合していても Athena は `Unsupported Federation Resource - Invalid table or column names` でクエリを失敗させます。

CloudFront Logs と Google Analytics のジョブは Visual ETL ジョブです。CloudFormation が作るのは箱だけで、フローは Glue コンソールで作成し、ジョブ定義用の別リポジトリで管理します。Synthetics のジョブはスクリプト形式で、`AWS::Glue::Job` として宣言します。
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
| CloudFrontLogPrefix | String | | | CloudFront アクセスログが格納される S3 プレフィックス |
| CloudFrontLogSourceAccountId | String | | | クロスアカウントレプリケーション元のアカウント ID |
| CloudFrontLogSourceRoleName | String | | | レプリケーション元の IAM ロール名 |
| **SyntheticsSourcePaths** | String | | ○ | Synthetics のレポートが格納される S3 パスをカンマ区切りで指定する（Canary のアーティファクトバケットごとに 1 つ） |
| SyntheticsLookbackDays | Number | 3 | | Synthetics のジョブが 1 回の実行で読むレポートの日数 |
| GoogleAnalyticsClientId | String | | | Google OAuth2 クライアントアプリケーション ID（Google Cloud Console から取得） |
| **GoogleAnalyticsClientSecret** | String | | | Google Analytics 4 OAuth2 クライアントシークレット |
| GoogleAnalyticsRefreshToken | String | | | Google Analytics 4 OAuth2 リフレッシュトークン |
| GoogleAnalyticsAccessToken | String | | | Google Analytics 4 OAuth2 アクセストークン |
| QuickAccountId | String | | | クロスアカウントで Athena へのアクセスを許可する Amazon Quick アカウントの AWS アカウント ID |
| LogicalName | String | analytics | ○ | リソースのカスタムプレフィックス名 |

機能の有効化条件: CloudFront Logs リソースは `CloudFrontLogDomainName` 設定時、Synthetics リソースは `SyntheticsSourcePaths` 設定時、Google Analytics リソースは `GoogleAnalyticsClientSecret` 設定時に作成されます。

ETL ジョブは 19:00 UTC（JST 4:00）に実行されます。

### CloudFront Logs

``AWSCloudFormationTemplates/analytics/cloudfront-logs`` は、AWS Glue と Amazon Athena を使用して CloudFront 標準アクセスログを分析するリソースを作成します。

### Google Analytics

``AWSCloudFormationTemplates/analytics/google-analytics`` は、AWS Glue Visual ETL を使用して Google Analytics 4 データ処理リソースを作成します。

### CloudWatch Synthetics

``AWSCloudFormationTemplates/analytics/synthetics`` は、AWS Glue と Amazon Athena を使用して CloudWatch Synthetics Canary の実行結果を分析するリソースを作成します。

**設計: Spark のパスフィルタによる混在ファイルの読み込み**

CloudWatch Synthetics は 1 回の実行ごとに同じ S3 プレフィックス配下に複数種類のファイルを格納します（JSON レポート、PNG スクリーンショット、HTML HAR ファイル、ログファイル、Chromium クラッシュダンプ）。Glue ETL ジョブは以下の Spark 読み込みオプションでレポートファイルのみを読み込みます:

1. `pathGlobFilter: "SyntheticsReport-*.json"` — レポート JSON ファイルのみを選択し、バイナリ・ログアーティファクトを読み込み時に除外する。
2. `recursiveFileLookup: "true"` — 実行ごとのプレフィックス構造を再帰的に走査する。
3. `multiline: "true"` — 各レポートは複数行にまたがる 1 つの整形済み JSON オブジェクトのため、`_corrupt_record` を避けるにはマルチライン解析が必須。

登録済みの Iceberg メタデータファイルが S3 に存在しない場合は、Glue API でカタログ登録を削除してテーブルを再作成することで自己修復します。
