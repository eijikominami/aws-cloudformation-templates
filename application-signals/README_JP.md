[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/application-signals
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/application-signals`` は、 ``Amazon CloudWatch Synthetics`` を作成します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Synthetics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/application-signals/synthetics-heartbeat.yaml) 

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-application-signals.png)

### Amazon CloudWatch Synthetics

CloudWatch Synthetics は、カナリアおよび設定可能なスクリプトを作成し、指定されたエンドポイントを監視します。

### AWS Lambda

このテンプレートは、 Lambda を用いて ``ハートビートスクリプト`` を作成します。この関数は特定のURLを読み込んで、そのスクリーンショットとファイル、およびログを保存します。

### Amazon S3

S3バケットは、ハートビートスクリプトが取得したスクリーンショットとファイル、ログを保存します。

### Amazon CloudWatch Alarm

このテンプレートは、CloudWatch のカスタムメトリクスとアラームを作成します。
これらのアラームは、成功率が90%を下回ったときにトリガされます。

## デプロイ

``CanaryName``, ``DomainName``, ``WatchedPagePath`` パラメータとともに以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file synthetics-heartbeat.yaml --stack-name Synthetics --parameter-overrides CanaryName=XXXXX DomainName=XXXXX WatchedPagePath=XXXXX
```

デプロイ時に、以下のパラメータを指定することができます。

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| IncidentManagerArn | String | | | カナリア名 |
| IncidentDurationInSeconds | Number | 600 | ○ | インシデントの基準となる時間 |
| IncidentSuccessPercentThreshold | Number | 50 | ○ | インシデントの基準となるアクセス成功率（％） |
| **CanaryName** | String | | ○ | カナリア名 |
| **DomainName** | String | | ○ | スクリプトが監視するドメイン名 |
| WatchedPagePath | String | /index.html | ○ | スクリプトが監視するページのパス |