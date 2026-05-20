English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/devops
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

`AWSCloudFormationTemplates/devops` は DevOps 運用向けの **AWS フロンティア AI エージェント**をセットアップします。`AWS DevOps Agent` および自律的なインシデント対応・根本原因分析・運用改善に必要な関連リソースを含みます。

## TL;DR

各サービスを個別にデプロイする場合は、以下のボタンをクリックしてください。

| サービス | US East（バージニア北部） | Asia Pacific（東京） |
| --- | --- | --- |
| AWS DevOps Agent | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DevOpsAgent&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/devops/templates/devops-agent.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DevOpsAgent&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/devops/templates/devops-agent.yaml) |

## アーキテクチャ

### AWS DevOps Agent

`AWS DevOps Agent` は常時稼働の**フロンティア AI エージェント**で、インシデントを自律的に解決・予防し、AWS・マルチクラウド・オンプレミス環境全体にわたってアプリケーションの信頼性を最適化し、オンデマンドの SRE タスクを処理します。

このテンプレートは AWS DevOps Agent のすべての前提条件をプロビジョニングします：

- **IAM ロール** — リソース発見用サービスロール（`aidevops.amazonaws.com` + `AIDevOpsAgentAccessPolicy`）と Web コンソールアクセス用 Operator App ロール（`AIDevOpsOperatorAppAccessPolicy`）
- **Agent Space** — エージェントがアクセスできる AWS リソースとツール統合のスコープを定義する論理コンテナ。Lambda バックの Custom Resource でプロビジョニング
- **AWS アカウント関連付け** — Agent Space にプライマリアカウントへのアクセスを付与し、トポロジー自動発見と CloudWatch アラーム監視を有効化
- **Operator App** — IAM 認証による DevOps Agent Web コンソールへのアクセスを有効化
- **EventChannel（Webhook）** — 外部オブザーバビリティツール（Datadog, Grafana, PagerDuty 等）からの調査トリガー用インバウンド Webhook エンドポイント

#### インシデント対応の仕組み

デプロイ後、AWS DevOps Agent は関連付けられた IAM ロールを使用して AWS 環境を継続的に監視します。CloudWatch アラームが ALARM 状態になると、自動的に調査を開始します（AWS ネイティブアラームに追加の SNS 設定不要）。スタック全体のメトリクス・ログ・デプロイイベント・コード変更を相関分析し、根本原因を特定して修復手順を提案します。

```
CloudWatch アラーム  ──（IAM ロールポーリング）──▶  DevOps Agent  ──▶  調査
外部ツール          ──（Webhook POST）──────────▶  DevOps Agent  ──▶  調査
```

| リソース | 説明 |
| --- | --- |
| `IAMRoleForAgentSpace` | AWS DevOps Agent がリソース発見のために引き受けるサービスロール |
| `IAMRoleForWebappAdmin` | Operator App（Web コンソール）アクセス用ロール |
| `IAMRoleForCustomResourceLambda` | CloudFormation Custom Resource Lambda の実行ロール |
| `ServerlessFunctionForAgentSpaceCustomResource` | DevOps Agent API 経由で Agent Space を作成・更新・削除する Lambda |
| `CustomResourceForAgentSpace` | Agent Space セットアップを統括する CloudFormation Custom Resource |
| `CloudWatchAlarmForLambdaErrors` | Custom Resource Lambda エラーに対するアラーム |

| 出力 | 説明 |
| --- | --- |
| `AgentSpaceId` | Agent Space の一意識別子 |
| `IAMRoleForAgentSpaceArn` | DevOps Agent サービスロールの ARN |
| `IAMRoleForWebappAdminArn` | Operator App ロールの ARN |
| `ConsoleUrl` | AWS DevOps Agent コンソールの Agent Space への直接リンク |
| `WebhookUrl` | 外部アラートソース用インバウンド Webhook URL |
