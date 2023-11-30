[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/cloudops
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/cloudops`` は、``Systems Manager`` や ``DevOps Guru`` などの運用の可用性に関するサービスを構築します。

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudOps&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/template.yaml) 

以下のボタンから、個別のAWSサービスを有効化することも可能です。

| 作成されるAWSサービス | 個別のCloudFormationテンプレート |
| --- | --- |
| CloudWatch Application Insights | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=ApplicationInsights&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/applicationinsights.yaml) |
| CodeGuru Profiler | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CodeGuruProfiler&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/codeguruprofiler.yaml) |
| DevOps Guru | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DevOpsGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/devopsguru.yaml) |
| ResillienceHub | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=ResillienceHub&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/resilliencehub.yaml) |
| Resource Explorer | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=ResourceExplorer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/resourceexplorer.yaml) |
| Systems Manager | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/ssm.yaml) |
| Systems Manager Incident Manager | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManagerIncidentManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/incidentmanager.yaml) |

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture-cloudops.png)

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name CloudOps --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| ApplicationInsights | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`ApplicationInsights` スタックがデプロイされます。 |
| IncidentManager | ENABLED / DISABLED | DISABLED | ○ | ENABLEDを指定した場合、`IncidentManager` スタックがデプロイされます。 |
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

### CodeGuru Profiler

このテンプレートは、``AWS CodeGuru Profiler`` のプロファイリンググループを作成します。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **AgentPermission** | String | | ○ | プロファイリンググループに付与するエージェントの権限 |
| ProfilingGroupName | String | Default | ○ | プロファイリンググループの名前 |
| **SNSForAlertArn** | String | | ○ | SNSトピックのARN |

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

#### マルチアカウント対応

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