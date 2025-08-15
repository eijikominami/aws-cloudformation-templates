[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/amplify
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates) 

``AWSCloudFormationTemplates/amplify`` は、 ``AWS Amplify``, ``AWS CodeCommit`` などを用いて CI/CD 環境を構築します。

## 前提条件

デプロイの前に以下を準備してください。

- 登録済みでアクセス可能なカスタムドメイン名
- ドメイン管理用の Route 53 ホストゾーン（推奨）
- Amplify、CodeCommit、SNS サービスに対する適切な IAM 権限

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Amplify&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/amplify/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Amplify&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/amplify/template.yaml) |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-amplify.png)

## デプロイ

`DomainName` パラメータと `RepositoryName` パラメータを指定して、デプロイを実行してください。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name Amplify  --parameter-overrides DomainName=xxxxx RepositoryName=xxxxx --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | CloudWatch アラームのアラームレベル |
| AmplifyConsoleAppId | String |  | ※ | **この値は2回目以降のデプロイ時に指定できます。** |
| **DomainName** | String | | ○ | Amplify Console で使用するカスタムドメイン名 |
| **RepositoryName** | String | | ○ | CodeCommit で使用するリポジトリ名 | 
