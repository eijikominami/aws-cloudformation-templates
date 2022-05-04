[**English**](README.md) / 日本語

# AWSCloudFormationTemplates
![GitHub Stars](https://img.shields.io/github/stars/eijikominami/aws-cloudformation-templates.svg?style=social&label=Stars)
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
AWSCloudFormationTemplates は、**アカウント作成直後に行うべきセキュリティ設定** や **Webサイトのホスティング設定** など、AWSを利用する上で有用なCloudformationテンプレートを複数提供します。

## AWS SAM ベースのサーバレスアプリーケーション

本プロジェクトには、以下の **AWS SAM ベースのサーバレスアプリーケーション** が存在し、これらのアプリケーションは、``AWS Serverless Application Repository`` で公開されています。

| アプリケーション名 | 最新バージョン | リンク |
| --- | --- | --- |
| [codepipeline-default-settings](cicd/codepipeline-default-settings.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~codepipeline-default-settings) |
| [cloudwatch-alarm-about-apigateway](monitoring/cloudwatch-alarm-about-apigateway.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-apigateway) |
| [cloudwatch-alarm-about-codebuild](monitoring/cloudwatch-alarm-about-codebuild.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-codebuild) |
| [cloudwatch-alarm-about-dynamodb-throttle](monitoring/cloudwatch-alarm-about-dynamodb-throttle.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-dynamodb-throttle) |
| [cloudwatch-alarm-about-dynamodb](monitorining/cloudwatch-alarm-about-dynamodb.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-dynamodb) |
| [cloudwatch-alarm-about-ec2](monitoring/cloudwatch-alarm-about-ec2.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-ec2) |
| [cloudwatch-alarm-about-ec2-cwagent](monitoring/cloudwatch-alarm-about-ec2-cwagent.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-ec2-cwagent) |
| [cloudwatch-alarm-about-elasticsearch](monitoring/cloudwatch-alarm-about-elasticsearch.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-elasticsearch) |
| [cloudwatch-alarm-about-events](monitoring/cloudwatch-alarm-about-events.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-events) |
| [cloudwatch-alarm-about-kinesis-data-streams](monitoring/cloudwatch-alarm-about-kinesis-data-streams.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-kinesis-data-streams) |
| [cloudwatch-alarm-about-kinesis-data-firehose](monitoring/cloudwatch-alarm-about-kinesis-data-firehose.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-kinesis-data-firehose) |
| [cloudwatch-alarm-about-lambda](monitoring/cloudwatch-alarm-about-lambda.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-lambda) |
| [cloudwatch-alarm-about-medialive](monitoring/cloudwatch-alarm-about-medialive.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-medialive) |
| [cloudwatch-alarm-about-mediastore](monitoring/cloudwatch-alarm-about-mediastore.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-mediastore) |
| [cloudwatch-alarm-about-natgateway](monitoring/cloudwatch-alarm-about-natgateway.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-natgateway) |
| [cloudwatch-alarm-about-sns](monitoring/cloudwatch-alarm-about-sns.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~cloudwatch-alarm-about-sns) |
| [sns-topic](notification/sns-topic.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~sns-topic) |
| [eventbridge-rules](eventbridge-rules.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~eventbridge-rules) |
| [delete-resources-without-required-tags](security-config-rules/delete-resources-without-required-tags.md) | 2.0.22 | [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~delete-resources-without-required-tags) |

## テンプレート

本プロジェクトには、以下の **Cloudformationテンプレート** が存在します。

| テンプレート名 | リージョン | 実行 |
| --- | --- | --- |
| [一括設定パイプライン](/cicd/README_JP.md) | 東京 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CICD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cicd/template.yaml) |
| [**セキュリティ設定**](/security/README_JP.md) | 東京| [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security/template.yaml) |
| [必須タグが付与されていないリソースの削除](/security-config-rules/README_JP.md) | 東京 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DefaultSecuritySettings-ConfigRules&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/security-config-rules/packaged.yaml) |
| [支払いやCloudFrontの監視に関する設定](/global/README_JP.md) | バージニア北部 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=GlobalSettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/global/template.yaml) |
| [**Webサイトのホスティング**](/static-website-hosting-with-ssl/README_JP.md) | 東京 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=StaticWebsiteHosting&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/static-website-hosting-with-ssl/template.yaml)  |
| [EC2ベースのWebサイトホスティング](/web-servers/README_JP.md) | 東京 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=WebServers&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/template.yaml)  |
| [**外形監視の設定**](/synthetics/README_JP.md) | 東京 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Synthetics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/synthetics/heartbeat.yaml) |
| [Systems Managerの設定](/web-servers/README_JP.md) | 東京 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/web-servers/ssm.yaml&param_LogicalNamePrefix=SystemsManager) |
| [運用の可用性に関する設定](/cloudops/README_JP.md) | 東京 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudOps&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/template.yaml) |
| [Slackへの通知](/notification/README_JP.md) | 東京 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Notification&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/notification/packaged.yaml) |
| [Amplifyを用いたCI/CD環境を構築](/amplify/README_JP.md) | 東京 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Amplify&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/amplify/template.yaml) |

本プロジェクトには、以下のサブモジュールも含まれます。

+ [エッジサービスの設定](/edge/README_JP.md)
+ [ネットワークの設定](/network/README_JP.md)
+ [**Media Services の設定**](/media/README_JP.md)
+ [CloudWatch アラームの設定](/monitoring/README_JP.md)

## アーキテクチャ

これらのテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](images/architecture.png)

### セキュリティ設定

![](images/architecture-default-security-settings.png)

### 必須タグが付与されていないリソースの削除

![](images/architecture-delete-resources-without-required-tags.png)

### Webサイトのホスティング

![](images/architecture-static-website-hosting.png)

### 支払いやCloudFrontの監視に関する設定

![](images/architecture-global.png)

### EC2ベースのWebサイトホスティング

![](images/architecture-web-servers.png)

### 外形監視の設定

![](images/architecture-synthetics.png)

### Amplifyを用いたCI/CD環境

![](images/architecture-amplify.png)

### Slackへの通知

![](images/architecture-notification.png)