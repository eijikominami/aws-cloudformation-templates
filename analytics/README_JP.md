English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/analytics
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates) 

``AWSCloudFormationTemplates/analytics`` は ``Amazon AppFlow``, ``AWS Glue`` などを用いてデータ分析環境を構築します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Analytics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/analytics/template.yaml) | 

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-analytics.png)

## デプロイ

Google Analytics と接続する場合、[新しい OAuth クライアントをセットアップ](https://aws.amazon.com/jp/blogs/news/analyzing-google-analytics-data-with-amazon-appflow-and-amazon-athena/)し、Google API 経由で authorization code を取得します。

```bash
https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=GOOGLE_ANALYTICS_CLIENT_ID&redirect_uri=https://AWS_REGION.console.aws.amazon.com/appflow/oauth&scope=https://www.googleapis.com/auth/analytics.readonly&access_type=offline
```

次に以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name Analytics --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| GoogleAnalyticsAuthCode | String | | | The code provided by the connector when it has been authenticated |
| GoogleAnalyticsClientId | String | | | The identifier for OAuth2 |
| GoogleAnalyticsClientSecret | String | | | The client secret used by the OAuth client to authenticate |
| **GoogleAnalyticsEntityName** | String | | ◯ | The entity name (path) of Google Analytics |
| GoogleAnalyticsScheduleRate | Number | 24 | ◯ | The rate at which the scheduled flow will run |
| GlueDatabaseName | String | datalake | ◯ | Prefix that is used for the created resources (20 chars, a-z, 0-9 and _ only) |
| GlueJobNumberOfWorkers | Number | 2 | ◯ | The number of workers of a defined workerType that are allocated when a job runs |
| GlueJobWorkerType | String | G.1X | ◯ | The type of predefined worker that is allocated when a job runs |
| SourceAccountIAMRoleArn | String | | | The role arn of account id source bucket is contained |