[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/security-config-rules
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/security-config-rules`` は **必要なタグが付与されていないAWSリソースを削除** します。このテンプレートは、以下のリソースに対応しています。

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

2. 以下のリンクをクリックすることで、**CloudFormationをデプロイ**することが可能です。

+ [delete-resources-without-required-tags - AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~delete-resources-without-required-tags)
+ [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings-ConfigRules&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security-config-rules/packaged.yaml)

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-delete-resources-without-required-tags.png)

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
sam build
sam package --output-template-file packaged.yaml --s3-bucket S3_BUCKET_NAME
aws cloudformation deploy --template-file packaged.yaml --stack-name DefaultSecuritySettings-ConfigRules --s3-bucket S3_BUCKET_NAM --capabilities CAPABILITY_NAMED_IAM
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AutoRemediation | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、Lambda を用いた **自動修復機能** が有効化されます。 |
| RequiredTagKey | String | createdby | ○ | AWS Configは、このタグの無いAWSリソースを削除します。 |
| RequiredTagValue | String | aws-cloudformation-templates | ○ | AWS Configは、このタグの無いAWSリソースを削除します。 |