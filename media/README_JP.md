[**English**](README.md) / 日本語

# AWSCloudFormationTemplates/media
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/media`` は、 ``AWS Elemental Media Services`` を構築します。

## TL;DR

以下のボタンをクリックすることで、**CloudFormationをデプロイ** することが可能です。

| 作成されるAWSサービス | リージョン | 個別のCloudFormationテンプレート |
| --- | --- | --- |
| IVS | 東京 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IVS&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/ivs.yaml) |
| MediaLive | 東京 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaLive&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/medialive.yaml) |
| MediaPackage | 東京 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaPackage&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediapackage.yaml) |
| MediaStore | 東京 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaStore&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediastore.yaml) |

## デプロイ

以下のコマンドを実行することで、CloudFormationをデプロイすることが可能です。

```bash
aws cloudformation deploy --template-file ivs.yaml --stack-name IVS --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file medialive.yaml --stack-name MediaLive --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file mediapackage.yaml --stack-name MediaPackage --capabilities CAPABILITY_NAMED_IAM
aws cloudformation deploy --template-file mediastore.yaml --stack-name MediaStore --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

デプロイ時に、以下のパラメータを指定することができます。

### IVS

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| Authorized | true or false | false | ○ | 再生承認の有効化 |
| LatencyMode | NORMAL or LOW | LOW | ○ | 動画レイテンシー |
| Type | STANDARD or BASIC | STANDARD | ○ | チャンネルタイプ |

### MediaLive

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| AdMarker | ENABLED or DISABLED | DISABLED | ○ | Ad Markerを使用するかどうか |
| AudioBitrate | Number | 96000 | ○ | 音声ビットレート（bps） |
| AutoInputFailover | ENABLED or DISABLED | ENABLED | ○ | Auto input failoverを使用するかどうか |
| ChannelClass | STANDARD or SINGLE_PIPELINE | STANDARD | ○ | チャネルクラス |
| FramerateDenominator | Number | 1001 | ○ | Framerate denominator |
| FramerateNumerator | Number | 30000 | ○ | Framerate numerator |
| GopNumBFrames | Number | 3 | ○ | リファレンスフレームあたりのBフレームの数 |
| GopSize | Number | 60 | ○ | GOPサイズ |
| H264Profile | String | HIGH | ○ | H.264プロファイル |
| H264Level | String | H264_LEVEL_4_1 | ○ | H.264レベル |
| Height | Number | 540 | ○ | ビデオの高さ（px）|
| HlsBucket | String | | | HLSファイルの送信バケット名 |
| InputType | RTMP / ELEMENTAL_LINK / S3 | ENABLED | ○ | 入力タイプ |
| InputStreamKey | String | stream | | ストリームキー |
| InputWhitelistRules | String | 0.0.0.0/0 | ○ | 許可するIPアドレス範囲 |
| MediaPackageChannelId | String | | | MediaPackage のチャネルID |
| MediaStoreEndpoint | String | | | MediaStore のエンドポイントURL |
| OutputType | String | RTMP | ○ | 出力先のタイプ |
| OutputRtmpUrl1 | String | | | 出力先のRTMP URL1 |
| OutputRtmpStreamName1 | String | | | 出力先のRTMPストリーム名1 |
| OutputRtmpUrl2 | String | | | 出力先のRTMP URL2 |
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
| CdnContentSegmentUrlPrefix | String | | ○ | コンテンツをキャッシュしている CDN のURL |
| MaxDurationSeconds | Number | 120 | ○ | プリロールの最大秒 |
| PersonalizationThresholdSeconds | Number | 8 | ○ | 埋められなかった広告時間の最大秒 |
| **SlateAdUrl** | String | | ○ | 広告で使用されなかった時間に挿入されるスレートのURL |
| **VideoContentSourceUrl** | String | | ○ | マニフェストファイルのURL |