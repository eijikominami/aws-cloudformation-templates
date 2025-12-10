[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/global
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/global`` は、バージニア北部 (`us-east-1`) リージョンに ``AWS Certificate Manager`` と ``CloudFront`` および ``Billing`` に関する ``CloudWatch`` アラームを作成します。

## 前提条件

デプロイの前に以下を準備してください。

- SSL 証明書検証用に登録されたドメイン名
- CloudFront メトリクス監視用の CloudFront ディストリビューション ID（CloudFront を監視する場合）
- Cost and Usage Reports 用の S3 バケット（CUR を有効にする場合）

## TL;DR

以下のボタンをクリックすることで、**CloudFormationをデプロイ** することが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=GlobalSettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/global/template.yaml) | |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-global.png)

### AWS Certificate Manager

このテンプレートは、 ``AWS Certificate Manager`` を用いてSSL証明書を作成します。

### CloudWatch Alarm

このテンプレートは、 ``Billing`` と ``CloudFront`` (エラー率、リクエスト数、ダウンロードサイズ) のCloudWatchアラームを作成します。

### その他

このテンプレートは、 ``Amazon SNS`` などのリソースも合わせて作成します。

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。 
``AWS Certificate Manager``, ``CloudFront``, ``Billing``は、``us-east-1`` リージョンでのみリソース作成が可能であるため、 ``us-east-1`` リージョンで実行してください。

```bash
aws cloudformation deploy --template-file templates/template.yaml --stack-name GlobalSettings --region us-east-1
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| ACMValidationMethod | DNS / EMAIL | DNS | ○ | ドメインを所有または管理していることを検証するために使用する方法 |
| **ACMDomainName** | String | | | ドメイン名を指定した場合、**SSL証明書**が作成されます。 |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | CloudWatch アラームのアラームレベル |
| BillingAlertThreshold | Number | 0 | ○ | 0以外の値を指定した場合、**CloudWatchアラーム**が作成されます。 |
| BudgetName | String | Total | ○ | 予算名。 ``BillingAlertThreshold`` を変更する場合は、この値も変更してください。 |
| CentralizedLogBucketName | String | | | 集約ログバケット名 |
| CloudFrontErrorRateThreshold | Number | 0 | ○ | 0以外の値を指定した場合、**CloudWatchアラーム**が作成されます。 |
| CloudFrontErrorRequestPerMinuteThreshold | Number | 0 | ○ | 0以外の値を指定した場合、**CloudWatchアラーム**が作成されます。 |
| CloudFrontBytesDownloadedPerMinuteThreshold | Number | 0 | ○ | 0以外の値を指定した場合、**CloudWatchアラーム**が作成されます。 |
| CloudFrontDistributionId | String | | | 監視対象の CloudFront のディストリビューション ID |
| CostUsageReport | ENABLED / DISABLED | DISABLED　| | ENABLED に設定された場合、Cost Usage Report が作成されます。 |
| DomainName | String | | | Route53 に登録するドメイン名 | 
| NotificationThreshold | Number | 10 | ○ | Cost Explorer から通知が送られる閾値 | 
| WebACL | ENABLED / DISABLED | DISABLED | ○ | DISABLED に設定された場合、AWS WAF は作成されません。 |