[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/cloudops
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/cloudops`` は、``Systems Manager`` や ``DevOps Guru`` などの運用の可用性に関するサービスを構築します。

## CloudOps

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=CloudOps&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudOps&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/template.yaml) |

以下のボタンから、個別のAWSサービスを有効化することも可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| CloudWatch Application Insights | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=ApplicationInsights&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/applicationinsights.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=ApplicationInsights&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/applicationinsights.yaml) |
| CloudWatch Internet Monitor | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=InternetMonitor&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/internetmonitor.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=InternetMonitor&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/internetmonitor.yaml) |
| CodeGuru Reviewer | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=CodeGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/codeguru.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CodeGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/codeguru.yaml) |
| DevOps Guru | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DevOpsGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/devopsguru.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DevOpsGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/devopsguru.yaml) |
| Resource Explorer | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=ResourceExplorer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/resourceexplorer.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=ResourceExplorer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/resourceexplorer.yaml) |
| Systems Manager | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SystemsManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/ssm.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/ssm.yaml) |
| Systems Manager Incident Manager | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SystemsManagerIncidentManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/incidentmanager.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManagerIncidentManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/incidentmanager.yaml) |

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name CloudOps --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **ApplicationInsights** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`ApplicationInsights` スタックがデプロイされます。 |
| CodeGuruTargetRepository | String | eijikominami/aws-cloudformation-templates | ○ | CodeGuru で使用する GitHub オーナー名とリポジトリ名 |
| **IncidentManager** | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`IncidentManager` スタックがデプロイされます。 |
| IncidentManagerAlias | String | admimistrator | ○ | 連絡先のエイリアス |
| IncidentManagerChatbotSnsArn | String | | | AWS Chatbot の ARN |
| IncidentManagerDisplayName | String | Administrator | ○ | 連絡先のエイリアス |
| IncidentManagerDurationInMinutes | Number | 1 | ○ | 次のステージに移行する時間（分） |
| IncidentManagerEmail | String | | | Eメールアドレス |
| IncidentManagerPhoneNumber | String | | | 電話番号 |
| IncidentManagerWorkloadName | String | Workload | ○ | ワークロード名 |
| SSMAdminAccountId | Strig | | | SSM の管理を行う AWS アカウントの ID |
| SSMIgnoreResourceConflicts | ENABLED / DISABLED | DISABLED | ○ | ENABLED に設定された場合、当該のリソースは生成されません。 |
| SSMOrganizationID | String | | | AWS Organizations ID |
| SSMPatchingAt | Number | 3 | ○ | パッチ適用処理開始時刻 (現地時) |

![](../images/architecture-cloudops.png)

### Application Insight

このテンプレートは、``CloudWatch Application Insight`` を作成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **SNSForAlertArn** | String | | ○ | The ARN of an Amazon SNS topic |

### CodeGuru Reviewer

このテンプレートは、``Amazon CodeGuru Reviewer`` を作成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **CodeGuruTargetRepository** | String | eijikominami/aws-cloudformation-templates | ○ | The GitHub owner name and repository name for AWS CodeGuru Reviewer |

### DevOps Guru

このテンプレートは、``AWS DevOps Guru`` の通知チャンネルを作成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **SNSForAlertArn** | String | | ○ | SNSトピックのARN |

### Systems Manager

このテンプレートは、``AWS Systems Manager`` を作成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **AdminAccountId** | String | | | AWS Systems Manager Automation を設定する AWS アカウント ID |
| **IgnoreResourceConflicts** | ENABLED / DISABLED | DISABLED | ○ | AWS Systems Manager Incident Manager を有効化するかどうか |
| **OrganizationID** | String | | | AWS Organizations ID |
| **PatchingAt** | Number | 3 | ○ | 日時のパッチ時刻 |

AWS Systems Manager Explorer を `Shared Services` アカウントで使用する場合には、`AWS Organizations` にて  **Systems Manager** と **AWS Trusted Advisor** の `アクセス有効化` を設定してください。

### Systems Manager Incident Manager

このテンプレートは、``AWS Systems Manager Incident Manager`` を作成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| Alias | String | admimistrator | ○ | 連絡先のエイリアス |
| ChatbotSnsArn | String | | | AWS Chatbot の ARN |
| DisplayName | String | Administrator | ○ | 連絡先のエイリアス |
| DurationInMinutes | Number | 1 | ○ | 次のステージに移行する時間（分） |
| Email | String | | | Eメールアドレス |
| PhoneNumber | String | | | 電話番号 |
| WorkloadName | String | Workload | ○ | ワークロード名 |

## Amazon CloudWatch Synthetics

CloudWatch Synthetics は、カナリアおよび設定可能なスクリプトを作成し、指定されたエンドポイントを監視します。 以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Synthetics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/synthetics-heartbeat.yaml)

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

![](../images/architecture-synthetics.png)

### AWS Lambda

このテンプレートは、 Lambda を用いて ``ハートビートスクリプト`` を作成します。この関数は特定のURLを読み込んで、そのスクリーンショットとファイル、およびログを保存します。

### Amazon S3

S3バケットは、ハートビートスクリプトが取得したスクリーンショットとファイル、ログを保存します。

### Amazon CloudWatch Alarm

このテンプレートは、CloudWatch のカスタムメトリクスとアラームを作成します。
これらのアラームは、成功率が90%を下回ったときにトリガされます。