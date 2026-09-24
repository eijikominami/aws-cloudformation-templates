[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/identity
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/identity`` は、アイデンティティ、リソース、アクセス許可をセキュアかつ大規模に管理可能な AWS Identity Services を構築します。

## 前提条件

デプロイの前に以下を準備してください。

- プライベートサブネットが設定された VPC（Managed Microsoft AD 用）
- Active Directory 用に計画されたドメイン名（Managed Microsoft AD 用）
- IAM Identity Center インスタンス要件の理解

## TL;DR

以下のボタンをクリックすることで、この **CloudFormationをデプロイ** することが可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| AWS IAM Identity Center | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=IdentityCenter&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/identitycenter.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IdentityCenter&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/identitycenter.yaml) |
| AWS Managed Microsoft AD | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MicrosoftAD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/microsoftad.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MicrosoftAD&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/identity/microsoftad.yaml) |

## AWS IAM Identity Center

このテンプレートは、 ``AWS IAM Identity Center`` を構成します。

### デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file templates/identitycenter.yaml --stack-name IdentityCenter --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AdministratorGroupId | String | | | 管理者権限を付与する Identity Store のグループ ID |
| AdministratorTargetAccountIds | CommaDelimitedList | 000000000000 | conditional | 管理者権限を付与する AWS アカウント ID |
| DefaultSessionDuration | String | PT12H | ○ | ISO-8601 におけるアプリケーションユーザーのセッション有効期間 |
| InstanceArn | String |  |  | IAM Identity Center の ARN |
| ManagementAccountId | String |  |  | Organizations と Service Catalog の権限を付与する管理アカウントの ID |
| ReadOnlyGroupId | String |  |  | 参照権限を付与する Identity Store のグループ ID |
| ReadOnlyTargetAccountIds | CommaDelimitedList | 000000000000 | conditional | 参照権限を付与する AWS アカウント ID |

## AWS Managed Microsoft AD

このテンプレートは、 ``AWS Managed Microsoft AD`` を構成します。

### デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file templates/microsoftad.yaml --stack-name MicrosoftAD --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | CloudWatch アラームのアラームレベル |
| EC2ImageId | AWS::SSM::Parameter::Value<AWS::EC2::Image::Id> | /aws/service/ami-windows-latest/Windows_Server-2022-Japanese-Full-Base | ○ | EC2 のイメージ ID |
| Edition | Standard / Enterprise | Standard | ○ | Microsoft Active Directory のエディション |
| EnableSso | true / false | true | ○ | シングルサインオンを有効化するかどうか |
| **Name** | String | corp.example.com | ○ | ドメイン名 |
| Password | String | Password1+ | ○ | Admin ユーザーのパスワード |
| **ShortName** | String | CORP | ○ | NetBIOS 名 |
| SubnetPrivateCidrBlockForAz1 | String | 10.3.0.0/26 | ○ | AZ1 にあるプライベートサブネットの CIDR ブロック |
| SubnetPrivateIdForAz1 | String | | 条件付き | AZ1 のプライベートサブネット ID |
| SubnetPrivateCidrBlockForAz2 | String | 10.3.64.0/26 | ○ | AZ2 にあるプライベートサブネットの CIDR ブロック |
| SubnetPrivateIdForAz2 | String | | 条件付き | AZ2 のプライベートサブネット ID |
| VPCId | String | | ○ | VPC ID |

### AWS Managed Microsoft AD を用いたユーザーとグループを管理

このテンプレートのデプロイ完了後、[Active Directory 管理ツールのインストール](https://docs.aws.amazon.com/ja_jp/directoryservice/latest/admin-guide/ms_ad_install_ad_tools.html)を行ってください。次に `DOMAIN\Admin` ユーザーに切り替えた上で、**Active Directory Users and Computers tool** を用いて、[ユーザーとグループの作成](https://docs.aws.amazon.com/ja_jp/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.html)を行ってください。

### セキュリティイベントログの Amazon CloudWatch Logs および Amazon S3 への保存

ドメインコントローラーのセキュリティイベントログを Amazon CloudWatch Logs および Amazon S3 に保存するためには、**マネジメントコンソールから手動で**ログ転送機能を有効にします。

### 管理インスタンスを最新の AMI から置き換える

このテンプレートは、管理インスタンスから AMI を作成する Data Lifecycle Manager のネストされたスタックを作成します。ポリシーは `Environment` タグと `TagKey` および `TagValue` の組み合わせを持つインスタンスを対象とした `IMAGE_MANAGEMENT` ポリシーで、週次で実行されます。AMI が利用可能になると、`<LogicalName>-RegisterLatestImage-<region>` という名前の EventBridge ルールが関数を呼び出し、その AMI の ID を SSM パラメータ `/<LogicalName>/ami/latest` に書き込みます。

`EC2ImageId` の既定値は AWS が公開している AMI であるため、このパラメータは書き込まれるだけで参照されません。`EC2ImageId` に `/<LogicalName>/ami/latest` を指定すると、管理インスタンスは最新の AMI から起動するようになり、このパラメータが変わるたびに次回のスタック更新で管理インスタンスが置き換えられます。

そのため、管理インスタンスに手動でインストールしたソフトウェアが置き換えをまたいで残るのは、AMI が作成される前にインストールされていた場合だけです。ソフトウェアをインストールした後、週次のスケジュールが実行される前にスタックを更新すると、古い AMI から管理インスタンスが置き換えられ、そのソフトウェアは存在しなくなります。インストールが終わった時点で AMI を作成し、パラメータを更新してください。

ルートボリュームは終了時に削除されるため、置き換えられたインスタンスは自身のディスクの内容を引き継ぎません。新しいインスタンスがソフトウェアを含む AMI から起動したかどうかは、次の 2 点で判別できます。Windows のコンピューター名が置き換え前と同じであること、およびイベントログにインスタンスの起動時刻より古い記録が含まれていることです。

## トラブルシューティング

### IAM Identity Center の問題

IAM Identity Center が正しく動作しない場合は、以下を確認してください。

1. IAM Identity Center を管理する権限を持っているか
2. 対象リージョンで Identity Center インスタンスが構成されているか
3. 権限セットがユーザーとグループに正しく割り当てられているか
4. SAML を使用する場合、外部 ID プロバイダーが正しく構成されているか

#### ID ソースの変更でユーザー、グループ、割り当てがすべて削除される

ID ソースを Active Directory と外部 ID プロバイダーの間で変更すると、そのインスタンスのユーザー、グループ、アカウント割り当てがすべて削除されます。CloudTrail には削除対象ごとに `allAssignmentsDeleted` が true の `DisassociateProfile` イベントが記録されます。このテンプレートが作成する割り当ては `AdministratorGroupId` と `ReadOnlyGroupId` で Identity Store のグループ ID を参照するため、変更前にグループ ID を記録してください。

#### アカウント割り当ては更新できない

`AWS::SSO::Assignment` はすべてのプロパティが作成時のみ指定可能であり、更新ハンドラを持たないため、変更するとリソースが置き換えられます。スタックの外に同じ割り当てが既に存在する場合、作成は `ConflictException` で失敗します。CloudFormation で管理する最初のデプロイの前に、既存の割り当てを削除してください。

`AWS::SSO::PermissionSet` の `Name` も作成時のみ指定可能です。権限セットの名前を変更すると置き換えが発生し、その権限セットを参照する割り当てもすべて削除されます。

#### 委任管理者からは管理アカウントへ権限を割り当てられない

`sso.amazonaws.com` の委任管理者であるアカウントからは、Organizations の管理アカウントを対象とする割り当てを作成できません。リソースベースポリシーによる明示的な拒否となり、IAM ポリシーを追加しても解除できません。Control Tower が作成した権限セットに対する割り当ての削除も同様に拒否されます。いずれも管理アカウントから実行してください。

委任管理者のアカウントでこのスタックを実行する場合は `ManagementAccountId` を空にしてください。管理アカウント向けのリソースは作成されません。

#### 姓名を持たないユーザーはプロビジョニングされない

IAM Identity Center の SCIM エンドポイントは `name` 属性を必須とし、存在しない場合は `name: The attribute name is required` として `400` を返します。Microsoft Entra ID は `givenName` と `surname` からこの属性を組み立てるため、どちらも持たないディレクトリのアカウントは作成されません。AWS Managed Microsoft AD の既定の管理者アカウントはこれに該当します。

プロビジョニングジョブは該当するエントリを毎サイクル再試行し、成功することはありません。失敗はエントリ単位に限定されるため `countSuccessiveCompleteFailures` は 0 のままでジョブは隔離されませんが、ログには同じエラーが記録され続けます。姓名を設定するのではなく、エンタープライズアプリケーションに割り当てられているグループから該当アカウントを外してください。

#### Identity Store のユーザーは CloudFormation で作成できない

`AWS::IdentityStore::Group` と `AWS::IdentityStore::GroupMembership` は存在しますが、ユーザーに対応するリソースはありません。外部 ID プロバイダーが SCIM でユーザーをプロビジョニングする場合、グループとメンバーシップもその ID プロバイダーが所有するため、ここで宣言すると同じオブジェクトに所有者が 2 つできます。

#### AWS 管理アプリケーションは CloudFormation で作成できない

`AWS::SSO::Application` は OAuth 2.0 のカスタマー管理アプリケーションのみをサポートします。Amazon Quick や Amazon CodeCatalyst のように AWS のサービスが自身で登録するアプリケーションは作成できず、SAML 2.0 のカスタマー管理アプリケーションも作成できません。`AWS::SSO::ApplicationAssignment` は既存のアプリケーションへプリンシパルを割り当てられますが、テンプレートがアプリケーションを作成しないため、その ARN はパラメータとして与える必要があります。

### AWS Managed Microsoft AD の問題

AWS Managed Microsoft AD が正しく動作しない場合は、以下を確認してください。

1. VPC とサブネットで DNS 解決が構成されているか
2. セキュリティグループが Active Directory に必要なポートを許可しているか
3. ドメイン名が既存のドメインと競合していないか
4. パスワードが複雑さの要件を満たしているか

### ドメインコントローラーへのアクセスの問題

ドメインコントローラーへ接続できない場合は、以下を確認してください。

1. 正しい VPC とサブネットから接続しているか
2. セキュリティグループがポート 3389 の RDP アクセスを許可しているか
3. ドメイン管理者の資格情報が正しいか
4. ドメインコントローラーが正常な状態か

