[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/media
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/media`` は、 ``AWS Elemental Media Services`` を構築します。

> [!NOTE]
> [**eijikominami/aws-cloudformation-samples/media**](hhttps://github.com/eijikominami/aws-cloudformation-samples/blob/master/media/README_JP.md) にサンプルテンプレート集があります。

## TL;DR

以下のボタンをクリックすることで、**CloudFormationをデプロイ** することが可能です。

| 作成されるAWSサービス | 米国東部 (バージニア北部) | アジアパシフィック (東京) |
| --- | --- | --- |
| Deadline Cloud | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DeadlineCloud&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/deadlinecloud.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DeadlineCloud&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/deadlinecloud.yaml) |
| IVS | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=IVS&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/ivs.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IVS&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/ivs.yaml) |
| MediaConnect | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MediaConnect&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediaconnect.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaConnect&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediaconnect.yaml) |
| MediaLive | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MediaLive&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/medialive.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaLive&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/medialive.yaml) |
| MediaPackage | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MediaPackage&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediapackage.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaPackage&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediapackage.yaml) |
| MediaStore | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MediaStore&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediastore.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaStore&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediastore.yaml) |

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file deadlinecloud.yaml --stack-name DeadlineCloud --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file ivs.yaml --stack-name IVS --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file mediaconnect.yaml --stack-name MediaConnect --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file medialive.yaml --stack-name MediaLive --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file mediapackage.yaml --stack-name MediaPackage --capabilities CAPABILITY_NAMED_IAM
aws cloudformation deploy --template-file mediastore.yaml --stack-name MediaStore --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

### Deadline Cloud

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| **IdentityCenterInstanceArn** | String | | ○ | IAM Identity Center の ARN |
| MaxWorkerCount | Number | 10 | ○ | Fleet の Worker の最大数 |
| MinWorkerCount | Number | 0 | ○ | Fleet の Worker の最小数 |

### IVS

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| Authorized | true or false | false | ○ | 再生承認の有効化 |
| LatencyMode | NORMAL or LOW | LOW | ○ | 動画レイテンシー |
| Type | STANDARD or BASIC | STANDARD | ○ | チャンネルタイプ |

### MediaConnect

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| DestinationIpAddressOrEntitlementArn1 | String | | | 送信先のIPアドレスもしくはARN |
| DestinationPort1 | String | 5001 | | MediaConnectが送信に用いるポート |
| DestinationProtocol1 | String | | | 送信に用いるプロトコル |
| DestinationIpAddressOrEntitlementArn2 | String | | | 送信先のIPアドレスもしくはARN |
| DestinationPort2 | String | 5002 | | MediaConnectが送信に用いるポート |
| DestinationProtocol2 | String | | | 送信に用いるプロトコル |
| DestinationIpAddressOrEntitlementArn3 | String | | | 送信先のIPアドレスもしくはARN |
| DestinationPort3 | String | 5001 | | MediaConnectが送信に用いるポート |
| DestinationProtocol4 | String | | | 送信に用いるプロトコル |
| DestinationIpAddressOrEntitlementArn1 | String | | | 送信先のIPアドレスもしくはARN |
| DestinationPort4 | String | 5001 | | MediaConnectが送信に用いるポート |
| DestinationProtocol4 | String | | | 送信に用いるプロトコル |
| DestinationIpAddressOrEntitlementArn5 | String | | | 送信先のIPアドレスもしくはARN |
| DestinationPort5 | String | 5001 | | MediaConnectが送信に用いるポート |
| DestinationProtocol5 | String | | | 送信に用いるプロトコル |
| DestinationIpAddressOrEntitlementArn6 | String | | | 送信先のIPアドレスもしくはARN |
| DestinationPort6 | String | 5001 | | MediaConnectが送信に用いるポート |
| DestinationProtocol6 | String | | | 送信に用いるプロトコル |
| DestinationIpAddressOrEntitlementArn7 | String | | | 送信先のIPアドレスもしくはARN |
| DestinationPort7 | String | 5001 | | MediaConnectが送信に用いるポート |
| DestinationProtocol7 | String | | | 送信に用いるプロトコル |
| DestinationIpAddressOrEntitlementArn8 | String | | | 送信先のIPアドレスもしくはARN |
| DestinationPort8 | String | 5001 | | MediaConnectが送信に用いるポート |
| DestinationProtocol8 | String | | | 送信に用いるプロトコル |
| FujitsuQoSSenderControlPort | Number | 9900 | | 送信リクエストを行う際に用いるポート |
| IngestPort | Number | 9177 | | 受信ポート |
| InputAllowedCidr | String | 0.0.0.0/0 | | 送信元のIPアドレスの範囲 |
| MinLatency | Number | 100 | | SRTを用いる際の最小遅延値 |
| OutputAllowedCidr | String | 0.0.0.0/0 | |  送信先のIPアドレスの範囲 |
| SenderIpAddressOrEntitlementArn | String | | | 送信元のIPアドレスもしくはARN |
| SenderType | String | srt-listener | ○ | 受信に用いるプロトコル |
| SrtCallerSourceListenerPort | Number | 2000 | | SRT caller を用いる際の送信元ポート |

### MediaConnect (アウトプット)

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |  
| --- | --- | --- | --- | --- |
| CidrAllowList | String | 0.0.0.0/0 | fujitsu-qos, srt-listener | 出力要求ができる IP アドレスの範囲 |
| DestinationIpAddressOrEntitlementArn | String | | srt-caller, zixi-push, rist, rtp-fec, rtp | 配信先の IP アドレスか ARN |
| **FlowArn** | String | | ○ | この出力が関連づけられているフローの ARN |
| MinLatency | Number | 100 | srt-listener, srt-caller | 最小レイテンシー（ミリ秒） |
| **Name** | String | | ○ | VPC インタフェースの名前 |
| Port | Number | 9177 | fujitsu-qos, srt-listener, srt-caller, zixi-push, rist, rtp-fec, rtp | コンテンツを配信する際に使用するポート番号 |
| Protocol | String | srt-listener | ○ | 送信元が使用するプロトコル |

### MediaConvert

| 名前 | タイプ | デフォルト | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| AccelerationSettings | ENABLED/PREFERRED/DISABLED | DISABLED | ○ | ジョブを高速トランスコーディングで実行する条件 |
| Category | 文字列 | Default | ○ | 作成するジョブテンプレートのカテゴリ |
| Name | 文字列 | Default | ○ | 作成するジョブテンプレートの名前 |
| StatusUpdateInterval | 数値 | 60 | ○ | MediaConvert が CloudWatch Events に STATUS_UPDATE イベントを送信する頻度 |

### MediaLive

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| AdMarker | ENABLED / DISABLED | DISABLED | ○ | Ad Markerを使用するかどうか |
| ArchiveBucket | String | | | LIVE-to-VOD コンテンツを保存するバケット名 |
| AudioBitrate | Number | 96000 | ○ | 音声ビットレート（bps） |
| AutoInputFailover | ENABLED / DISABLED | ENABLED | ○ | Auto input failoverを使用するかどうか |
| ChannelClass | STANDARD / SINGLE_PIPELINE | STANDARD | ○ | チャネルクラス |
| ElementalLinkId1 | String | | | Elemental Link の ID | 
| ElementalLinkId2 | String | | | Elemental Link の ID |
| ElementalLinkType | HD / UHD | HD | | Elemental Link のタイプ |
| FramerateDenominator | Number | 1001 | ○ | フレームレートの分母 |
| FramerateNumerator | Number | 30000 | ○ | フレームレートの分子 |
| GopNumBFrames | Number | 3 | ○ | リファレンスフレームあたりのBフレームの数 |
| GopSize | Number | 60 | ○ | GOPサイズ |
| H264Profile | String | HIGH | ○ | H.264プロファイル |
| H264Level | String | H264_LEVEL_4_1 | ○ | H.264レベル |
| Height | Number | 540 | ○ | ビデオの高さ（px）|
| HlsBucket | String | | | HLSファイルの送信バケット名 |
| InputType | String | RTMP | ○ | 入力タイプ |
| InputStreamKey | String | stream | | ストリームキー |
| InputWhitelistRules | String | 0.0.0.0/0 | ○ | 許可するIPアドレス範囲 |
| MediaPackageChannelId | String | | | MediaPackage のチャネルID |
| MediaStoreEndpoint | String | | | MediaStore のエンドポイントURL |
| OutputType | S3, MEDIA_PACKAGE, MEDIA_STORE, RTMP, RTP | RTMP | ○ | 出力先のタイプ |
| OutputHlsBucket | String | | HLS ファイルの送信先バケット名 |
| OutputRtmpRtpUrl1 | String | | | 出力先のRTMP URL1 |
| OutputRtmpStreamName1 | String | | | 出力先のRTMPストリーム名1 |
| OutputRtmpRtpUrl2 | String | | | 出力先のRTMP URL2 |
| OutputRtmpStreamName2 | String | | | 出力先のRTMPストリーム名2 |
| VideoBitrate | Number | 2200000 | ○ | ビデオビットレート(bps) |
| VodSourceBucket | String | | | VODのソースバケット名 |
| Width | Number | 960 | ○ | ビデオの幅（px） |

### MediaPackage

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| ArchiveBucket | String | | | LIVE-to-VODコンテンツの格納先バケット名 |
| ManifestName | String | index | ○ | マニフェスト名 |
| OutputType | APPLE_HLS, ISO_DASH, ALL | APPLE_HLS | ○ | アウトプットタイプ |
| StartoverWindowSeconds | Number | 0 | ○ | 時間シフト（秒） |
| SegmentDurationSeconds | Number | 3 | ○ | フラグメント長（秒） |
| VodSourceBucket | String | | | VODのソースバケット名 |

### MediaStore

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| ExpirationDate | Number | 1 | ○ | 有効期限（日） |
| MaxAgeSeconds | Number | 30000 | ○ | ブラウザキャッシュのプリフライト時間 |
| UserAgent | String | | ○ | ユーザエージェント |

### MediaTailor

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| **AdDecisionServerUrl** | String | | ○ | ADS の URL |
| **CdnContentSegmentUrlPrefix** | String | | ○ | コンテンツをキャッシュしている CDN のURL |
| MaxDurationSeconds | Number | 120 | ○ | プリロールの最大秒 |
| PersonalizationThresholdSeconds | Number | 8 | ○ | 埋められなかった広告時間の最大秒 |
| **SlateAdUrl** | String | | ○ | 広告で使用されなかった時間に挿入されるスレートのURL |
| **VideoContentSourceUrl** | String | | ○ | マニフェストファイルのURL |