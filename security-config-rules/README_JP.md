[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/security-config-rules
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/security-config-rules`` は **必要なタグが付与されていない AWS リソースを削除** します。このテンプレートは、以下のリソースに対応しています。

## 前提条件

デプロイの前に以下を準備してください。

- 有効化され設定された AWS Config サービス
- SAM デプロイアーティファクト用の S3 バケット
- リソースタグ戦略とポリシーの理解
- Config ルールと Lambda 関数に対する適切な IAM 権限

+ Amazon S3 - Bucket
+ Amazon DynamoDB - Table
+ Amazon API Gateway - API
+ AWS Lambda - Function

```bash
.
├── README.md                       <-- この導入ガイド
├── README_EN.md                    <-- 導入ガイド（英語版）
└── sam-app
    ├── checkRequiredTags           <-- Lambda用ディレクトリ（AWS Config カスタムルール）
    │   ├── lambda_function.py      <-- メイン関数
    │   └── requirements.txt        <-- ライブラリの依存関係ファイル
    ├── deleteUnapplicableResources <-- Lambda用ディレクトリ
    │   ├── lambda_function.py      <-- メイン関数
    │   └── requirements.txt        <-- ライブラリの依存関係ファイル
    └── template.yaml               <-- SAMテンプレート
```

## TL;DR

1. このテンプレートを実行する前に、本プロジェクトに含まれる ``Security`` テンプレートを実行してください。

+ [Security Template](../security/README_JP.md)

2. 以下のリンクをクリックすることで、**CloudFormationをデプロイ** することが可能です。

+ [delete-resources-without-required-tags - AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~delete-resources-without-required-tags)
+ [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings-ConfigRules&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security-config-rules/packaged.yaml)

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-delete-resources-without-required-tags.png)

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
cd sam-app
sam build
sam package --output-template-file packaged.yaml --s3-bucket S3_BUCKET_NAME
aws cloudformation deploy --template-file packaged.yaml --stack-name DefaultSecuritySettings-ConfigRules --s3-bucket S3_BUCKET_NAME --capabilities CAPABILITY_NAMED_IAM
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | CloudWatch アラームのアラームレベル |
| AWSConfigAutoRemediation | ENABLED / DISABLED | DISABLED | ○ | ENABLED を指定した場合、Lambda を用いた **自動修復機能** が有効化されます。 |
| RequiredTagKey | String | createdby | ○ | AWS Config は、このタグの無い AWS リソースを削除します。 |
| RequiredTagValue | String | aws-cloudformation-templates | ○ | AWS Config は、このタグの無い AWS リソースを削除します。 |

## トラブルシューティング

### Config ルールの問題

Config ルールがリソースを正しく評価しない場合：

1. AWS Config が有効化され、監視したいリソースタイプを記録していることを確認してください
2. カスタム Config ルール用の Lambda 関数が正しい権限を持っていることを確認してください
3. Config ルールパラメータがタグ要件と一致していることを確認してください
4. Config ルール Lambda 関数の CloudWatch ログでエラーを監視してください

### リソース削除の問題

リソースが期待通りに削除されない場合：

1. 自動修復 Lambda 関数がリソースを削除するために必要な権限を持っていることを確認してください
2. リソースがタグルールに従って実際に非準拠であることを確認してください
3. 削除 Lambda 関数が Config ルールコンプライアンス変更によってトリガーされていることを確認してください
4. 削除 Lambda 関数の CloudWatch ログでエラーを確認してください

### 誤った削除の問題

リソースが誤って削除される場合：

1. タグキーと値の要件が制限的すぎないかを確認してください
2. Config ルール評価ロジックが準拠リソースを正しく識別していることを確認してください
3. 削除前に猶予期間や通知の実装を検討してください
4. 本番環境以外で Config ルールを最初にテストしてください

### 権限の問題

Lambda 関数が権限により失敗する場合：

1. Lambda 実行ロールが Config とリソース削除に必要な権限を持っていることを確認してください
2. リソースが複数のアカウントにまたがる場合、クロスアカウント権限が設定されていることを確認してください
3. AWS Config 用のサービスリンクロールが作成されていることを確認してください
4. IAM ポリシーがターゲットリソースで必要なアクションを許可していることを確認してください