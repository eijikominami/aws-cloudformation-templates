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
| EC2InstanceType | String | t3.small | ○ | EC2 のインスタンスタイプ |
| Edition | Standard / Enterprise | Standard | ○ | Microsoft Active Directory のエディション |
| EnableSso | true / false | true | ○ | シングルサインオンを有効化するかどうか |
| **Name** | String | corp.example.com | ○ | ドメイン名 |
| Password | String | Password1+ | ○ | Admin ユーザーのパスワード |
| ServicesToRepair | String | | | セキュアチャネルが健全になった時点で稼働している必要がある管理インスタンス上の Windows サービス（カンマ区切り） |
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

#### ID ソースを変更したらサインインできなくなった

ID ソースを Active Directory と外部 ID プロバイダーの間で変更すると、ユーザー、グループ、アカウント割り当てがすべて削除されます。外部 ID プロバイダーの場合は SCIM でユーザーとグループを再度プロビジョニングし、新しいグループ ID を `AdministratorGroupId` と `ReadOnlyGroupId` に指定してスタックを更新してください。

#### 初回のデプロイが ConflictException で失敗する

同じアカウント割り当てがスタックの外に既に存在しています。既存の割り当てを削除してからデプロイしてください。`AWS::SSO::Assignment` は更新できず、変更すると置き換えになります。権限セットの名前を変更した場合も置き換えになり、その権限セットの割り当てはすべて削除されます。

#### 管理アカウントへの割り当てが明示的な拒否で失敗する

`sso.amazonaws.com` の委任管理者アカウントからは、管理アカウントへの割り当てを作成できません。Control Tower が作成した権限セットの割り当ても削除できません。管理アカウントから実行するか、委任管理者アカウントでは `ManagementAccountId` を空にしてください。

#### プロビジョニングのログに name: The attribute name is required が出続ける

姓と名のどちらも持たないアカウントは、Microsoft Entra ID から IAM Identity Center にプロビジョニングできません。AWS Managed Microsoft AD の既定の管理者アカウントがこれに該当します。エンタープライズアプリケーションに割り当てたグループから、そのアカウントを外してください。

#### ユーザーをテンプレートで作成できない

CloudFormation には Identity Store のユーザーのリソースがありません。外部 ID プロバイダーを使う場合は、ユーザーとグループを ID プロバイダー側で管理してください。

#### Amazon Quick などのアプリケーションをテンプレートで作成できない

`AWS::SSO::Application` が作成できるのは OAuth 2.0 のカスタマー管理アプリケーションだけです。AWS のサービスが登録するアプリケーションと SAML 2.0 のアプリケーションは、各サービスのコンソールで作成し、その ARN をパラメータに指定してください。

### AWS Managed Microsoft AD の問題

AWS Managed Microsoft AD が正しく動作しない場合は、以下を確認してください。

1. VPC とサブネットで DNS 解決が構成されているか
2. セキュリティグループが Active Directory に必要なポートを許可しているか
3. ドメイン名が既存のドメインと競合していないか
4. パスワードが複雑さの要件を満たしているか

#### Admin のパスワードがパラメータと一致しない

`Password` パラメータは変更しないでください。作成時のみ指定できるプロパティのため、変更するとディレクトリが作り直され、中のユーザーやコンピューターがすべて失われます。パスワードは [ResetUserPassword](https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html) で変更してください。今と同じ値も指定できます。

#### 正しいパスワードで認証できない

Admin のパスワードが失効している可能性があります。既定のパスワードポリシーでは管理者アカウントにも有効期限があり、失効するとパスワードの誤りとして拒否されます。`net use \\<ドメインコントローラー>\IPC$ /user:<ドメイン>\Admin <パスワード>` を実行し、システムエラー 2242 なら失効、1326 なら誤りです。失効している場合は `ResetUserPassword` で再設定してください。

#### 管理インスタンスでドメインアカウントのサービスが動かない

管理インスタンスとドメインコントローラーの間のセキュアチャネルが壊れています。AMI から置き換えた直後や、通信が切れたあとに起きます。`SystemAssociationForRepairingDomainTrust` が 30 分ごとに `nltest /sc_reset` でチャネルを張り直し、`ServicesToRepair` のサービスを起動します。すぐに直す場合は、このアソシエーションを手動で実行してください。

アソシエーションが失敗する場合は、機械アカウントのパスワードがディレクトリと食い違っています。ドメインの資格情報で `Reset-ComputerMachinePassword` を実行してください。`AWS-JoinDirectoryServiceDomain` を再実行しても、参加済みのインスタンスには何もしないため直りません。

修復できたかどうかは `nltest /sc_verify:<ドメイン>` で確認してください。`NERR_Success` が返れば正常です。

### ドメインコントローラーへのアクセスの問題

ドメインコントローラーへ接続できない場合は、以下を確認してください。

1. 正しい VPC とサブネットから接続しているか
2. セキュリティグループがポート 3389 の RDP アクセスを許可しているか
3. ドメイン管理者の資格情報が正しいか
4. ドメインコントローラーが正常な状態か

