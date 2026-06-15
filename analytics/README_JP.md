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
| **GlueJobTimeout** | Number | 60 | | Glue ジョブのタイムアウト（分、1〜2880） |
| **GlueWorkerCount** | Number | 5 | | Glue ワーカー数（2〜100） |
| **CloudFrontLogDomainName** | String | | | CloudFront ディストリビューションのドメイン名。設定すると CloudFront Logs 機能が有効化される |
| **CloudFrontLogPrefix** | String | | | CloudFront アクセスログが格納される S3 プレフィックス |
| **CloudFrontLogSourceAccountId** | String | | | クロスアカウントレプリケーション元のアカウント ID |
| **CloudFrontLogSourceRoleName** | String | | | レプリケーション元の IAM ロール名 |
| **SyntheticsResultsBucketName** | String | | | CloudWatch Synthetics の結果が格納される S3 バケット名。設定すると Synthetics 機能が有効化される |
| **SyntheticsResultsPrefix** | String | canary/ | | Synthetics 結果の S3 プレフィックス |
| **GoogleAnalyticsPropertyId** | String | | | Google Analytics 4 プロパティ ID |
| **GoogleAnalyticsAccountId** | String | | | Google Analytics 4 アカウント ID |
| **GoogleAnalyticsClientId** | String | | | Google OAuth2 クライアントアプリケーション ID（Google Cloud Console から取得） |
| **GoogleAnalyticsClientSecret** | String | | | Google Analytics 4 OAuth2 クライアントシークレット |
| **GoogleAnalyticsRefreshToken** | String | | | Google Analytics 4 OAuth2 リフレッシュトークン |
| **GoogleAnalyticsAccessToken** | String | | | Google Analytics 4 OAuth2 アクセストークン |
| **GitRepository** | String | | | Visual ETL ジョブのソース管理用 Git リポジトリ URL |
| **GitOwner** | String | | | Git リポジトリオーナー/組織名 |
| **GitBranch** | String | main | | Visual ETL ジョブのソース管理用 Git ブランチ |
| **GitFolder** | String | glue-jobs | | Git リポジトリ内のジョブ格納フォルダパス |
| **GitToken** | String | | | GitHub/GitLab 認証用パーソナルアクセストークン |
| **ScheduleEnabled** | String | false | | ETL ジョブの日次スケジュール実行を有効化（JST 4:00） |
| **AlarmLevel** | String | NOTICE | | CloudWatch アラームのレベル（NOTICE または WARNING） |
| **SNSForAlertArn** | String | | | アラート用の既存 SNS トピック ARN。空の場合は自動作成される |
| **SNSForDeploymentArn** | String | | | デプロイ通知用の既存 SNS トピック ARN。空の場合は自動作成される |
| **LogicalName** | String | analytics | ○ | リソースのカスタムプレフィックス名 |
| **Environment** | String | development | | デプロイ環境（production / test / development） |
| **TagKey** | String | createdby | | リソースタグのキー |
| **TagValue** | String | aws-cloudformation-templates | | リソースタグの値 |

機能の有効化条件: CloudFront Logs リソースは `CloudFrontLogDomainName` 設定時、Synthetics リソースは `SyntheticsResultsBucketName` 設定時、Google Analytics リソースは `GoogleAnalyticsPropertyId`・`GoogleAnalyticsAccountId`・`GoogleAnalyticsClientSecret` がすべて設定された場合に作成されます。

### CloudFront Logs

``AWSCloudFormationTemplates/analytics/cloudfront-logs`` は、AWS Glue と Amazon Athena を使用して CloudFront 標準アクセスログを分析するリソースを作成します。

このテンプレートは以下を作成します:
- 生 CloudFront 標準ログ形式の Glue テーブル（33 フィールド、LazySimpleSerDe）
- 生ログのスキーマ検出用 Glue Crawler（オンデマンド）
- 変換後データ用 Iceberg Glue テーブル（`cloudfront_access_logs_iceberg`）
- 生ログを Apache Iceberg に変換する Glue Visual ETL Job（Custom Resource 経由で管理）
- Visual ETL Job ライフサイクル管理用 Lambda 関数
- 専用クエリ結果出力先を持つ Athena WorkGroup
- 一般的な分析パターンの Athena Named Queries（日別リクエスト数、ステータスコード分布、実ユーザーアクセス）
- Crawler、ETL Job、Lambda 用の最小権限 IAM ロール
- ETL ジョブの日次スケジュール実行用 Glue Trigger（オプション、JST 4:00）

### Google Analytics

``AWSCloudFormationTemplates/analytics/google-analytics`` は、AWS Glue Visual ETL を使用して Google Analytics 4 データ処理リソースを作成します。

このテンプレートは以下を作成します:
- GA4 から S3 へのデータ取り込み用 Glue Visual ETL Job（Custom Resource 経由で管理）
- Google Analytics 4 用 Glue Connection（OAuth2 認証）
- GA4 コアレポート用 Glue Table（Apache Iceberg 形式）
- OAuth2 クライアント認証情報格納用 Secrets Manager シークレット
- Visual ETL Job ライフサイクル管理用 Lambda 関数
- Lambda エラー、Glue ジョブ失敗、推定請求額に対する CloudWatch Alarms
- GA4 取り込みジョブの日次スケジュール実行用 Glue Trigger（オプション、JST 4:00）

### CloudWatch Synthetics

``AWSCloudFormationTemplates/analytics/synthetics`` は、AWS Glue と Amazon Athena を使用して CloudWatch Synthetics Canary の実行結果を分析するリソースを作成します。

このテンプレートは以下を作成します:
- `SyntheticsReport-*.json` を読み込み Apache Iceberg に書き込む Glue ETL Job（スクリプト形式、Custom Resource 経由で管理）
- Glue Job ライフサイクル管理用 Lambda 関数
- 専用クエリ結果出力先を持つ Athena WorkGroup
- 一般的な分析用 Athena Named Queries（直近結果＋所要時間、失敗詳細、日次可用性）
- ETL Job、Lambda 用の最小権限 IAM ロール
- ETL ジョブの日次スケジュール実行用 Glue Trigger（オプション、JST 4:00）

Iceberg テーブル `synthetics_canary_iceberg` は CloudFormation ではなく Glue ジョブスクリプト（`createOrReplace`）が作成・所有します。

**設計: Spark のパスフィルタによる混在ファイルの読み込み**

CloudWatch Synthetics は 1 回の実行ごとに同じ S3 プレフィックス配下に複数種類のファイルを格納します（JSON レポート、PNG スクリーンショット、HTML HAR ファイル、ログファイル、Chromium クラッシュダンプ）。Glue ETL ジョブは以下の Spark 読み込みオプションでレポートファイルのみを読み込みます:

1. `pathGlobFilter: "SyntheticsReport-*.json"` — レポート JSON ファイルのみを選択し、バイナリ・ログアーティファクトを読み込み時に除外する。
2. `recursiveFileLookup: "true"` — 実行ごとのプレフィックス構造を再帰的に走査する。
3. `multiline: "true"` — 各レポートは複数行にまたがる 1 つの整形済み JSON オブジェクトのため、`_corrupt_record` を避けるにはマルチライン解析が必須。

ジョブは結果を `createOrReplace` で Iceberg テーブルに書き込み、登録済みの Iceberg メタデータファイルが S3 に存在しない場合は、Glue API でカタログ登録を削除してテーブルを再作成することで自己修復します。

## アーキテクチャ

### Custom Resource による Visual ETL Job 管理

Glue Visual ETL Job は CloudFormation ネイティブでは作成できないため、Lambda バックドの Custom Resource でライフサイクル（Create/Update/Delete）を管理しています。Google Analytics と CloudFront Logs のジョブは Visual ETL ジョブ（`CodeGenConfigurationNodes`）で、Synthetics のジョブは同じ Custom Resource パターンで管理されるスクリプト形式の Glue ジョブ（`synthetics-to-iceberg.py`）です。

**Visual ETL として認識されるための必須条件:**

| パラメータ | 必須 | 理由 |
| --- | --- | --- |
| `JobMode: VISUAL` | ○ | Visual ETL としてジョブを宣言 |
| `CodeGenConfigurationNodes` | ○ | **必須** — これがないと Glue コンソールで Visual エディタが表示されない |
| `Connections` | | `create_job` で渡せる。`CodeGenConfigurationNodes` 内の `connectionName` でも参照される |
| `SourceControlDetails` | | Git 連携メタデータを設定。実際の Push には `update_source_control_from_job` を別途呼ぶ必要あり |

> **注意**: 同名の Visual ETL Job を削除→再作成すると、Glue コンソールが古い状態をキャッシュして Visual エディタが表示されないことがあります。再作成時は新しいジョブ名を使用してください。

**Git 連携**: `create_job` API は `SourceControlDetails` メタデータを保存しますが、`Owner` と `AuthToken` は `get_job` レスポンスに**含まれません**。Git への Push には Custom Resource 内で `update_source_control_from_job` を呼び出し、毎回 `RepositoryOwner` と `AuthToken` を明示的に渡しています。

### Iceberg テーブル管理

CloudFront Logs / GA4 の Iceberg テーブルは CloudFormation によって以下の設定で作成されます:
- `DeletionPolicy: Retain` — スタック削除時にテーブルを保持
- `UpdateReplacePolicy: Retain` — スタック更新時にテーブルを置換しない
- `MetadataOperation: CREATE` — テーブルが存在しない場合のみ作成

これにより、手動でのスキーマ変更（Visual ETL の `EnableUpdateCatalog` 等）やジョブ実行によるスキーマ変更が、後続の CloudFormation デプロイで**上書きされない**ことを保証します。

Synthetics の Iceberg テーブル（`synthetics_canary_iceberg`）は意図的に CloudFormation で管理**しません** — Glue ジョブスクリプトが作成・所有します。CFn 管理テーブルは、物理メタデータファイルが S3 に存在しない `metadata_location` を事前登録してしまい「Location does not exist」エラーを引き起こすため廃止しました。

### Custom Resource のライフサイクル

| イベント | 動作 |
| --- | --- |
| **Create** | Glue Visual ETL Job を `CodeGenConfigurationNodes` 付きで作成し、Git に Push |
| **Update** | `CodeGenConfigurationNodes`、`--conf`（Spark/Iceberg 設定）、インフラ設定（Role, Timeout, Workers）を含むフル設定でジョブを更新 |
| **Delete** | Glue Job を削除 |
