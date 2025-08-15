[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/storage
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/storage`` は、Amazon FSx を含むストレージサービスを構築します。

## 前提条件

デプロイの前に以下を準備してください。

- 設定された AWS Managed Microsoft Active Directory インスタンス
- FSx デプロイ用に設定された VPC とサブネット
- FSx スループットとストレージ容量要件の理解
- 適切なセキュリティグループとネットワークアクセスの設定

## TL;DR

以下のボタンをクリックすることで、CloudFormation をデプロイすることが可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| Amazon FSx for Windows Server | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=FSx&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/storage/fsx.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=FSx&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/storage/fsx.yaml) |

## アーキテクチャ

このテンプレートが作成する AWS リソースのアーキテクチャについて説明します。

### Amazon FSx for Windows Server

このテンプレートは、完全に管理された Windows ファイル共有を提供する Amazon FSx for Windows Server ファイルシステムを作成します。ファイルシステムは認証とアクセス制御のために AWS Managed Microsoft Active Directory と統合されます。

## デプロイ

以下のコマンドを実行することで、CloudFormation をデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file templates/fsx.yaml --stack-name FSx --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

### Amazon FSx for Windows Server

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **ActiveDirectoryId** | String | | ○ | 既存の AWS Managed Microsoft Active Directory インスタンスの ID |
| AZDeploymentMode | SINGLE_AZ_2 / MULTI_AZ_1 | SINGLE_AZ_2 | ○ | ファイルシステムのデプロイタイプ |
| CidrIp | String | 0.0.0.0/0 | ○ | セキュリティグループアクセス用の CIDR ブロック |
| FSxThroughput | Number | 8 | ○ | スループット容量（MB/s）- 8、16、32、または 64 |
| PrimarySubnetAccess | String | | ○ | プライマリファイルシステム用のサブネット ID |
| IngressCidrIp | String | | | 追加のイングレスアクセス用 CIDR ブロック |
| StorageCapacity | Number | 32 | ○ | ストレージ容量（GB）- 最小 32 GB |
| SubnetIds | String | | ○ | カンマ区切りのサブネット ID リスト |
| **VPCId** | String | | ○ | FSx がデプロイされる VPC ID |

## トラブルシューティング

### FSx ファイルシステムの問題

FSx ファイルシステムにアクセスできない場合：

1. AWS Managed Microsoft Active Directory が正常でアクセス可能であることを確認してください
2. セキュリティグループが SMB/CIFS トラフィック（ポート 445）に必要なポートを許可していることを確認してください
3. サブネットが Active Directory ドメインコントローラーへの適切なルーティングを持っていることを確認してください
4. FSx コンソールでファイルシステムが「利用可能」状態であることを確認してください

### Active Directory 統合の問題

FSx が Active Directory ドメインに参加できない場合：

1. Active Directory ID が正しく、ディレクトリがアクティブであることを確認してください
2. FSx サービスがドメインに参加するために必要な権限を持っていることを確認してください
3. FSx と Active Directory 間で DNS 解決が正常に動作していることを確認してください
4. セキュリティグループが FSx と AD 間の必要なポートでの通信を許可していることを確認してください

### パフォーマンスの問題

FSx のパフォーマンスが期待に応えない場合：

1. スループット容量がワークロードに適していることを確認してください
2. ストレージ容量がパフォーマンス要件を満たしていることを確認してください
3. FSx の CloudWatch メトリクスを監視してボトルネックを特定してください
4. より良いパフォーマンスと可用性のために Multi-AZ デプロイへのアップグレードを検討してください

### ネットワーク接続の問題

クライアントが FSx に接続できない場合：

1. セキュリティグループがクライアントサブネットからの SMB トラフィック（ポート 445）を許可していることを確認してください
2. ネットワーク ACL が必要なトラフィックをブロックしていないことを確認してください
3. クライアントがドメインに参加し、Active Directory で認証できることを確認してください
4. FSx DNS 名がクライアントマシンから正しく解決されることを確認してください