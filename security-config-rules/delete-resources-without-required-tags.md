Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# delete-resources-without-required-tags (en)

`delete-resources-without-required-tags` deletes AWS resources without required tags. This template covers the following resources.

+ Amazon S3 - Bucket
+ Amazon DynamoDB - Table
+ Amazon API Gateway - API
+ AWS Lambda - Function

```bash
.
├── README.md                       <-- Instructions file (Japanese)
├── README_EN.md                    <-- This instructions file
└── sam-app
    ├── checkRequiredTags           <-- Source code for a lambda function（ **AWS Config Custom Rules** ）
    │   ├── lambda_function.py      <-- Lambda function code
    │    requirements.txt           <-- Lambda function code
    ├── deleteUnapplicableResources <-- Source code for a lambda function
    │   ├── lambda_function.py      <-- Lambda function code
    │   └── requirements.txt        <-- Lambda function code
    └── template.yaml               <-- SAM Template
```

## Architecture

The following sections describe the individual components of the architecture.

![](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/architecture-delete-resources-without-required-tags.png)

## Deployment

Execute the command to deploy.

```bash
sam build
sam package --output-template-file packaged.yaml --s3-bucket S3_BUCKET_NAME
aws cloudformation deploy --template-file packaged.yaml --stack-name DefaultSecuritySettings-ConfigRules --s3-bucket S3_BUCKET_NAM --capabilities CAPABILITY_NAMED_IAM
```

You can give optional parameters as follows.

| Name | Parameter | Details | 
| --- | --- | --- | 
| AutoRemediation | ENABLED / DISABLED | If it is ENABLED, **AutoRemediation** by SSM Automation and Lambda are enabled. |
| RequiredTagKey | string | AWS Config removes AWS resouces without this tag. |
| RequiredTagValue | string | AWS Config removes AWS resouces without this tag. |

---------------------------------------

# delete-resources-without-required-tags (ja)

``delete-resources-without-required-tags`` は **必要なタグが付与されていないAWSリソースを削除** します。このテンプレートは、以下のリソースに対応しています。

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
    │   ├── lambda_function.py      <-- メイン関数
    │   └── requirements.txt        <-- ライブラリの依存関係
    ├── deleteUnapplicableResources <-- Lambda用ディレクトリ
    │   ├── lambda_function.py      <-- メイン関数
    │   └── requirements.txt        <-- ライブラリの依存関係
    └── template.yaml               <-- SAMテンプレート
```

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/architecture-delete-resources-without-required-tags.png)

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