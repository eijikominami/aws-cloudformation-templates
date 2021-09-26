English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/media
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/media`` builds AWS Elemental Media Services.

## TL;DR

If you just want to deploy the stack, click the button below.

| Services | Launchers |
| --- | --- |
| MediaLive | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaLive&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/medialive.yaml) |
| MediaPackage | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaPackage&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediapackage.yaml) |
| MediaStore | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaStore&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediastore.yaml) |

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file medialive.yaml --stack-name MediaLive
aws cloudformation deploy --template-file mediapackage.yaml --stack-name MediaPackage
aws cloudformation deploy --template-file mediastore.yaml --stack-name MediaStore
```

You can provide optional parameters as follows.

### MediaLive

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| AudioBitrate | Number | | ○ | Average audio bitrate in bits/second |
| AutoInputFailover | ENABLED or DISABLED | ENABLED | ○ | Enable or disable automatic input failover |
| ChannelClass | STANDARD or SINGLE_PIPELINE | STANDARD | ○ | Select the class of channel you intend to attach this input to |
| FramerateDenominator | Number | 1001 | ○ | Framerate denominator |
| FramerateNumerator | Number | 30000 | ○ | Framerate numerator |
| GopNumBFrames | Number | 3 | ○ | Number of B-frames between reference frames |
| GopSize | Number | 60 | ○ | GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits |
| H264Profile | String | HIGH | ○ | H.264 Profile |
| H264Level | String | H264_LEVEL_4_1 | ○ | H.264 Level |
| Height | Number | 540 | ○ | Output video height, in pixels |
| MediaPackageChannelId | String | | | The MediaPackage channel id |
| MediaStoreEndpoint | String | | | The endpoint of MediaStore |
| LiveSource | ENABLED or DISABLED | ENABLED | ○ | Enable or disable a live source |
| OutputType | String | RTMP | ○ | OutputType |
| RtmpUrl1 | String | | | The rtmp url a stream sends to. |
| RtmpStreamName1 | String | | | The rtmp stream name a stream sends to. |
| RtmpUrl2 | String | | | The rtmp url a stream sends to. |
| RtmpStreamName2 | String | | | The rtmp stream name a stream sends to. |
| StreamKey | String | stream | | A unique name for the location the RTMP stream is being pushed to |
| VideoBitrate | Number | 2200000 | ○ | Average video bitrate in bits/second |
| VodSourceBucket | String | | | The S3 bucket Name VOD contents exist |
| Width | Number | 960 | ○ | Output video width, in pixels |
| WhitelistRules | String | 0.0.0.0/0 | ○ | A list of one or more IPv4 CIDR addresses to allow |

### MediaPackage

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| StartoverWindowSeconds | Number | 0 | ○ | Maximum duration seconds of content to retain for startover playback |
| SegmentDurationSeconds　| Number | 3 | ○ | Duration (in seconds) of each fragment |
| VodSourceBucket | String | | | The S3 bucket Name VOD contents exist |
| VodDestinationBucket | String | | | The S3 bucket Name LIVE-to-VOD contents are stored |

### MediaStore

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 | 
| --- | --- | --- | --- | --- |
| ExpirationDate | Number | 1 | ○ |  The date objects to expire |
| MaxAgeSeconds　| Number | 30000 | ○ | The time in seconds that browser caches the preflight response |
| UserAgent | String | | ○ | The secret key that 'User-Agent' header contains |