[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/security
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/security`` は、 ``Amazon GuardDuty``, ``AWS Config``, ``AWS CloudTrail`` , ``AWS Security Hub``, ``Amazon Macie`` などの **セキュリティ** に関連するAWSサービスを設定します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml)  | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml) |

以下のボタンから、個別のAWSサービスを有効化することも可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| IAM | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=IAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/iam.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IAM&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/iam.yaml) |
| AWS Security Hub | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SecurityHub&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/securityhub.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SecurityHub&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/securityhub.yaml) |
| Amazon GuardDuty | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=GuardDuty&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/guardduty.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=GuardDuty&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/guardduty.yaml) |
| AWS CloudTrail | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=CloudTrail&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/cloudtrail.yaml&param_LogicalName=CloudTrail) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudTrail&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/cloudtrail.yaml&param_LogicalName=CloudTrail) |
| AWS Config | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Config&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/config.yaml&param_LogicalName=Config) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Config&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/config.yaml&param_LogicalName=Config) |
| Amazon Macie | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Macie&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/macie.yaml&param_LogicalName=Macie) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Macie&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/macie.yaml&param_LogicalName=Macie) |
| Amazon Security Lake | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SecurityLake&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/securitylake.yaml&param_LogicalName=SecurityLake) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SecurityLake&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/securitylake.yaml&param_LogicalName=SecurityLake) |
| ロギング | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=Logging&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/logging.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Logging&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/logging.yaml) |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-default-security-settings.png)

### IAM AccessAnalyzer

このテンプレートは、 ``IAM Access Analyzer`` を有効化します。
IAM Access Analyzer は、 ``Amazon EventBridge`` 経由で ``Amazon SNS`` に結果を通知します。 
デプロイ完了後、 [**Organizations 内の管理アカウントに権限を委任**](https://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/access-analyzer-settings.html) することが可能です。

### AWS Security Hub

このテンプレートは、 ``AWS Security Hub`` を有効化します。
また、コンプライアンスチェックが失敗したとき、 ``Amazon SNS`` は ``Amazon EventBridge`` 経由でメッセージを受け取ります。
デプロイ完了後、**ポリシーを更新して Security Hub とセキュリティ基準を設定** します。

### Amazon GuardDuty

このテンプレートは、 ``Amazon GuardDuty`` を有効化します。
``Amazon GuardDuty`` は、**MEDIUM以上の検出結果を検出時に通知を送信** します。
デプロイ完了後、 [**Organizations 内の管理アカウントに権限を委任**](https://docs.aws.amazon.com/ja_jp/guardduty/latest/ug/guardduty_organizations.html) することが可能です。
委任されたアカウントで、 **ナビゲーションペインの [設定] から [アカウント] を選択し、[自動有効化] をオンにします**。
その後、必要に応じて、 **保護プランをメンバーアカウントに適用** してください。

### AWS CloudTrail

このテンプレートは、 ``AWS CloudTrail`` を有効化し、ログを蓄積する ``S3バケット`` を生成します。
S3バケットに蓄積されたログは、``AWS KMS`` 上で作成された ``CMK`` によって暗号化されます。
``AWS Control Tower`` を使用している場合は、このテンプレートをデプロイしたかどうかに関わらず組織内の全ての AWS アカウントで、 ``AWS CloudTrail`` が有効化されます。

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

``AWS Control Tower`` を使用している場合は、このテンプレートをデプロイしたかどうかに関わらず組織内の全ての AWS アカウントで、 ``AWS Config`` が有効化されます。

### Amazon Macie

このテンプレートは、 ``AWS Macie`` を構成します。 
デプロイ完了後、 [**Organizations 内の管理アカウントに権限を委任**](https://docs.aws.amazon.com/ja_jp/organizations/latest/userguide/services-that-can-integrate-macie.html) することが可能です。
また、[Auto-enable] (自動有効化) 設定をオンにすることで、アカウントが AWS Organizations 内で組織に追加されると、Macie は新しいアカウントに対して自動的に有効化することが可能です。

### ロギング

このテンプレートは、 AWS CloudFormation スタックセットを用いて ``Amazon Security Lake`` と [``SIEM on Open Search Service``](https://github.com/aws-samples/siem-on-amazon-opensearch-service/) を構築します。
もし、 Security Lake を Organizations 内で使用する場合は、Organizations の管理アカウントを使用して委任された [Security Lake 管理者を指定](https://docs.aws.amazon.com/ja_jp/security-lake/latest/userguide/getting-started.html#initial-account-setup) する必要があります。
また、 ``SIEM on Open Search Service`` と連携させる場合には、[SQS の可視性タイムアウトを 5 分から 10 分に変更](https://github.com/aws-samples/siem-on-amazon-opensearch-service/blob/main/docs/securitylake_ja.md#security-lake-%E3%81%AE%E6%9C%89%E5%8A%B9%E5%8C%96%E3%81%A8%E8%A8%AD%E5%AE%9A)する必要があります。

### Amazon EventBridge

このテンプレートは、 ``AWS Health`` と　``AWS Trusted Advisor`` に関する  ``CloudWatchイベント`` を作成します。
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
| AuditAccountId | String | | | 監査アカウントの ID |
| AWSCloudTrail | ENABLED / CREATED_BY_CONTROL_TOWER / DISABLED | ENABLED | ENABLEDを指定した場合、AWS CloudTrail が有効化されます。 |
| AWSCloudTrailAdditionalFilters | String | | | 追加の CloudWatch Logs メトリクスフィルター |
| AWSCloudTrailS3Trail | ENABLED / DISABLED | ENABLED | ○ | ENABLEDを指定した場合、CloudTrail の証跡の作成が有効化されます。 |
| AWSConfig | ENABLED / DISABLED | ENABLED | ○ | ENABLEDを指定した場合、AWS Config が有効化されます。 |
| AWSConfigAutoRemediation | ENABLED / DISABLED | ENABLED | ○ | ENABLEDを指定した場合、SSM Automation と Lambda を用いた **自動修復機能** が有効化されます。 |
| AmazonGuardDuty | ENABLED / NOTIFICATION_ONLY / DISABLED | ENABLED | ○ | ENABLEDを指定した場合、Amazon GuardDuty が有効化されます。|
| AmazonMacie | ENABLED / NOTIFICATION_ONLY / DISABLED | ENABLED | ○ | ENABLEDを指定した場合、Amazon Macie が有効化されます。|
| AWSSecurityHub | String | STANDARDS_ONLY | ○ | ENABLEDを指定した場合、AWS Security Hub が有効化されます。 |
| AWSSecurityHubStandards | CommaDelimitedList | FSBP, CIS | ○ | 有効化するセキュリティ標準 |
| EsLoaderServiceRoleArn | String | | | aes-siem-es-loader Lambda 関数の ARN |
| GeoLite2LicenseKeyForSIEM | String | | | MaxMind が発行した GEO IP API のライセンスキー |
| IAMAccessAnalyzer | String | ACCOUNT | ○ | ACCOUNT もしくは ORGANIZATION を指定した場合、 IAM Access Analyzer が有効化されます。 |
| IAMUserArnToAssumeAWSSupportRole | String | | | AWS Support ロールを引き受けるIAMユーザのARN |
| LogArchiveAccountId | String | | | ログアーカイブアカウントの ID |
| SecurityOUId | String | | | セキュリティ OU の ID |
| SecurityLakeRoleArn | String | | | aes-siem-es-loader が使用する IAM ロール |
| SecurityLakeExternalId | String | | | Security Lake の外部 ID |
| SecurityLakeSubscriberSqs | String | | | Security Lake サブスクライバーの SQS ARN |
| SIEM | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、SIEM が有効化されます。 |
| SnsEmailForSIEM | String | | | SIEM に指定する E メールアドレス |

### マルチアカウント対応

Amazon GuardDuty や AWS Security Hub を `Security tooling` アカウント、もしくは `Security view-only (Audit)` アカウントで使用する場合は、これらのアカウントを管理アカウントにて[管理者アカウントに指定](https://docs.aws.amazon.com/ja_jp/securityhub/latest/userguide/designate-orgs-admin-account.html)してください。

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