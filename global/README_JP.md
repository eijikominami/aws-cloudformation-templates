[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/global
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/global`` は、 バージニア北部 (`us-east-1`)リージョンに ``AWS Certificate Manager`` と ``CloudFront`` および ``Billing`` に関する ``CloudWatch`` アラームを作成します。

## TL;DR

以下のボタンをクリックすることで、**CloudFormationをデプロイ** することが可能です。

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=GlobalSettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/global/template.yaml) 

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
aws cloudformation deploy --template-file template.yaml --stack-name GlobalSettings --region us-east-1
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| ACMValidationMethod | DNS / EMAIL | DNS | ○ | ドメインを所有または管理していることを検証するために使用する方法 |
| **ACMDomainName** | String | | | ドメイン名を指定した場合、**SSL証明書**が作成されます。 |
| BillingAlertThreshold | Number | 0 | ○ | 0以外の値を指定した場合、**CloudWatchアラーム**が作成されます。 |
| BudgetName | String | Total | ○ | 予算名。 ``BillingAlertThreshold`` を変更する場合は、この値も変更してください。 |
| CloudFrontErrorRateThreshold | Number | 0 | ○ | 0以外の値を指定した場合、**CloudWatchアラーム**が作成されます。 |
| CloudFrontErrorRequestPerMinuteThreshold | Number | 0 | ○ | 0以外の値を指定した場合、**CloudWatchアラーム**が作成されます。 |
| CloudFrontBytesDownloadedPerMinuteThreshold | Number | 0 | ○ | 0以外の値を指定した場合、**CloudWatchアラーム**が作成されます。 |
| CloudFrontDistributionId | String | | | 監視対象のCloudFrontのディストリビューションID |
| DomainName | String | | | Route53に登録するドメイン名 | 
| WebACL | ENABLED / DISABLED | DISABLED | ○ | DISABLED に設定された場合、AWS WAFは作成されません。 |