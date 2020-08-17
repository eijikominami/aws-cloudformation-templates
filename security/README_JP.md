[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/security
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/security`` は、 ``Amazon Inspector``, ``Amazon GuardDuty``, ``AWS Config``, ``AWS CloudTrail`` , ``AWS Security Hub``, ``Amazon Detective`` などの **セキュリティ** に関連するAWSサービスを設定します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ**することが可能です。

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml) 

以下のボタンから、個別のAWSサービスを有効化することも可能です。

| 作成されるAWSサービス | 個別のCloudFormationテンプレート |
| --- | --- |
| IAM | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/iam.yaml) |
| AWS Security Hub | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SecurityHub&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/securityhub.yaml) |
| Amazon Detective | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Detective&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/detective.yaml) |
| Amazon Inspector | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Inspector&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/inspector.yaml&param_LogicalNamePrefix=Inspector) |
| Amazon GuardDuty | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=GuardDuty&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/guardduty.yaml) |
| AWS CloudTrail | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudTrail&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/cloudtrail.yaml&param_LogicalNamePrefix=CloudTrail) |
| AWS Config | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Config&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/config.yaml&param_LogicalNamePrefix=Config) |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-default-security-settings.png)

### IAM AccessAnalyzer

このテンプレートは、 ``IAM Access Analyzer`` を有効化します。
IAM Access Analyzer は、 ``Amazon EventBridge`` 経由で ``Amazon SNS`` に結果を通知します。

### AWS Security Hub

このテンプレートは、 ``AWS Security Hub`` を有効化します。
また、コンプライアンスチェックが失敗したとき、 ``Amazon SNS`` は ``Amazon EventBridge`` 経由でメッセージを受け取ります。

### Amazon Detective

このテンプレートは、 ``AWS Detective`` の　behavior graph を有効化します。

### Amazon GuardDuty

このテンプレートは、 ``Amazon GuardDuty`` を有効化します。
``Amazon GuardDuty`` は、**MEDIUM以上の検出結果を検出時に通知を送信** します。

### AWS CloudTrail

このテンプレートは、 ``AWS CloudTrail`` を有効化し、ログを蓄積する ``S3バケット`` を生成します。
S3バケットに蓄積されたログは、``AWS KMS`` 上で作成された ``CMK`` によって暗号化されます。

### Amazon Inspector

このテンプレートは、以下の Amazon Inspector ``アセスメントターゲット`` といくつかの ``アセスメントテンプレート`` を作成します。

+ [Network Reachability](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_network-reachability.html)
+ [Common Vulnerabilities and Exposures](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_cves.html)
+ [Center for Internet Security (CIS) Benchmarks](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_cis.html)
+ [Security Best Practices for Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_security-best-practices.html)

Amazon Inspector は、``Amazon EventBridge``　によって **毎週月曜日午前9時** に実行されます。

このテンプレートは、以下のリージョンをサポートしています。

+ US East (N. Virginia)
+ US East (Ohio)
+ US West (N. California)
+ US West (Oregon)
+ Asia Pacific (Tokyo)
+ Asia Pacific (Seoul)
+ Asia Pacific (Sydney)
+ EU (Frankfurt)
+ EU (Ireland)
+ EU (London)
+ EU (Stockholm)

### AWS Config

このテンプレートは、Amazon Config ``デリバリーチャンネル``、 ``レコーダ``と、以下の ``マネージドルール`` を作成します。

+ [CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-drift-detection-check.html)
+ [CLOUDFORMATION_STACK_NOTIFICATION_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-notification-check.html)

以下のルールは、``自動修復機能`` が有効化されており、 ``SSM Automation Documents`` が紐づけられています。

+ [IAM_PASSWORD_POLICY](https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html)
+ [IAM_ROOT_ACCESS_KEY_CHECK](https://docs.aws.amazon.com/config/latest/developerguide/iam-root-access-key-check.html)
+ [S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-server-side-encryption-enabled.html)
+ [VPC_FLOW_LOGS_ENABLED](https://docs.aws.amazon.com/config/latest/developerguide/vpc-flow-logs-enabled.html)
+ [VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS](https://docs.aws.amazon.com/config/latest/developerguide/vpc-sg-open-only-to-authorized-ports.html)
+ [VPC_DEFAULT_SECURITY_GROUP_CLOSED](https://docs.aws.amazon.com/config/latest/developerguide/vpc-default-security-group-closed.html)

``AWS Security Hub`` もセキュリティチェックに関連する Config ルールを自動的に作成します。
``AWS Config`` が非準拠のリソースを検知した場合は、 ``Amazon SNS`` に通知が送信されます。

### Amazon EventBridge

このテンプレートは、 ``AWS Health`` に関する  ``CloudWatchイベント`` を作成します。
CloudWatchイベントは、Amazon SNS にこれらのイベントを転送します。

### その他

このテンプレートは、 ``Service-linked Role``、 ``IAM Role``、 ``S3 Bucket``、 ``Amazon SNS`` などのリソースも合わせて作成します。

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name DefaultSecuritySettings  --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AmazonDetective | Enabled / Disabled | Disabled | ○ | Enabledを指定した場合、Amazon Detective が有効化されます。|
| AuditOtherAccounts | Enabled / Disabled | Disabled | ○ | Enabledを指定した場合、**Config Aggregator** が有効化されます。 |
| AuditOtherRegions | Enabled / Disabled | Enabled | ○ | Enabledを指定した場合、**CloudTrail** と Config の **Include Global Resource Types** オプションが有効化されます。 |
| AutoRemediation | Enabled / Disabled | Enabled | ○ | Enabledを指定した場合、SSM Automation と Lambda を用いた **自動修復機能** が有効化されます。 |
| IAMUserArnToAssumeAWSSupportRole | String | | | AWS Support ロールを引き受けるIAMユーザのARN |
| NotificationFilterAboutSecurityChecks | DENY_ALL / MEDIUM / ALLOW_ALL | DENY_ALL | ○ | セキュリティチェックに関する通知フィルタ | 

## Center for Internet Security (CIS) ベンチマークへの準拠

このテンプレートを実行することで、Center for Internet Security (CIS) ベンチマークの以下の項目に準拠します。

| No. | ルール | 実行内容 |
| --- | --- | --- |
| 1.3 | 90 日間以上使用されていない認証情報は無効にします | **Config** で定期的に確認を行い、非準拠の場合は **Lambda** で自動的に削除します。 |
| 1.4 | アクセスキーは 90 日ごとに更新します | **Config** で定期的に確認を行い、非準拠の場合は **Lambda** で自動的に削除します。 |
| 1.5 | IAM パスワードポリシーには少なくとも 1 つの大文字が必要です | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| 1.6 | IAM パスワードポリシーには少なくとも 1 つの小文字が必要です | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| 1.7 | IAM パスワードポリシーには少なくとも 1 つの記号が必要です | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| 1.8 | IAM パスワードポリシーには少なくとも 1 つの数字が必要です | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| 1.9 | IAM パスワードポリシーは 14 文字以上の長さが必要です | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| 1.10 | IAM パスワードポリシーはパスワードの再使用を禁止しています | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| 1.20 | AWS でインシデントを管理するためのサポートロールが作成されていることを確認します | AWS Support 用のIAM Roleを作成します。 |
| 2.1 | CloudTrail はすべてのリージョンで有効になっています | **CloudTrail** と関連サービスを有効化します。 |
| 2.2 | CloudTrail ログファイルの検証は有効になっています | **CloudTrail** と関連サービスを有効化します。 |
| 2.3 | CloudTrail が記録する S3 バケットはパブリックアクセスできません | **CloudTrail** と関連サービスを有効化します。 |
| 2.4 | CloudTrail 証跡は Amazon CloudWatch Logs によって統合されています | **CloudTrail** と関連サービスを有効化します。 |
| 2.5 | すべてのリージョンで AWS Config が有効になっていることを確認します | **Config** と関連サービスを有効化します。 |
| 2.6 | S3 バケットアクセスログ記録が CloudTrail S3 バケットで有効になっていることを確認します | **CloudTrail** と関連サービスを有効化します。 |
| 2.7 | CloudTrail ログは保管時に AWS KMS CMK を使用して暗号化されていることを確認します | **CloudTrail** と関連サービスを有効化します。 |
| 2.9 | すべての VPC で VPC フローログ記録が有効になっていることを確認します  | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。  |
| 3.1 | 不正な API 呼び出しに対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.2 | MFA なしの AWS マネジメントコンソール サインインに対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.3 | ルート」アカウントに対してログメトリクスフィルタとアラームが存在することを確認します  | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.4 | MFA なしの IAM ポリシーの変更に対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.5 | MFA なしの CloudTrail 設定の変更に対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.6 | AWS マネジメントコンソール 認証の失敗に対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.7 | カスタマー作成の CMK の無効化またはスケジュールされた削除に対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.8 | S3 バケットの変更に対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.9 | AWS Config 設定の変更に対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.10 | セキュリティグループの変更に対するメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.11 | ネットワークアクセスコントロールリスト (NACL) への変更に対するログメトリクスとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.12 | ネットワークゲートウェイへの変更に対するログメトリクスとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.13 | ルートテーブルの変更に対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 3.14 | VPC の変更に対してログメトリクスフィルタとアラームが存在することを確認します | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| 4.1| どのセキュリティグループでも 0.0.0.0/0 からポート 22 への入力を許可しないようにします | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| 4.2| どのセキュリティグループでも 0.0.0.0/0 からポート 3389 への入力を許可しないようにします | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| 4.3| すべての VPC のデフォルトセキュリティグループがすべてのトラフィックを制限するようにします | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |

## PCI DSS セキュリティ標準への準拠

このテンプレートを実行することで、PCI DSS セキュリティ標準の以下の項目に準拠します。

| No. | ルール | 実行内容 |
| --- | --- | --- |
| PCI.CloudTrail.1 | CloudTrail ログは、AWS KMS CMK を使用して保存時に暗号化する必要があります。 | **CloudTrail** と関連サービスを有効化します。 |
| PCI.CloudTrail.2 | CloudTrail を有効にする必要があります。 | **CloudTrail** と関連サービスを有効化します。 |
| PCI.CloudTrail.3 | CloudTrail ログファイルの検証を有効にする必要があります。 | **CloudTrail** と関連サービスを有効化します。 |
| PCI.CloudTrail.4 | CloudTrail 証跡は CloudWatch ログと統合する必要があります。 | **CloudTrail** と関連サービスを有効化します。 |
| PCI.Config.1 | AWS Config を有効にする必要があります。 | **Config** と関連サービスを有効化します。 |
| PCI.CW.1 | 「root」ユーザーの使用には、ログメトリクスフィルターとアラームが存在する必要があります。 | ログメトリクスフィルタとCloudWatchアラームを作成します。 |
| PCI.EC2.2 | VPC のデフォルトのセキュリティグループでは、インバウンドトラフィックとアウトバウンドトラフィックが禁止されます。 | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| PCI.IAM.1 | IAM ルートユーザーアクセスキーが存在してはいけません。 | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| PCI.S3.4 | S3 バケットでは、サーバー側の暗号化を有効にする必要があります。 | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |

## AWS の基本的なセキュリティのベストプラクティス標準への準拠

このテンプレートを実行することで、AWS の基本的なセキュリティのベストプラクティス標準の以下の項目に準拠します。

| No. | ルール | 実行内容 |
| --- | --- | --- |
| CloudTrail.1 | CloudTrail を有効にし、少なくとも 1 つのマルチリージョンの証跡で設定する必要があります。 | **CloudTrail** と関連サービスを有効化します。 |
| CloudTrail.2 | CloudTrail は保管時の暗号化を有効にする必要があります。 | **CloudTrail** と関連サービスを有効化します。 |
| Config.1 | AWS Config を有効にする必要があります。 | **Config** と関連サービスを有効化します。 |
| EC2.2 | VPC のデフォルトのセキュリティグループでは、インバウンドトラフィックとアウトバウンドトラフィックが禁止されます。 | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| GuardDuty.1 | GuardDuty を有効にする必要があります。 | **GuardDuty** と関連サービスを有効化します。 |
| IAM.3 | IAM ユーザーのアクセスキーは 90 日ごとに更新する必要があります。 | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| IAM.4 | IAM ルートユーザーアクセスキーが存在してはいけません。 | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |
| S3.4 | S3 バケットでは、サーバー側の暗号化を有効にする必要があります。 | **Config** で定期的に確認を行い、非準拠の場合は **SSM Automation** で自動修復を行います。 |