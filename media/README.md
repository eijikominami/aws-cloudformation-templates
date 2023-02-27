English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/media
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/media`` builds AWS Elemental Media Services.

## TL;DR

If you just want to deploy the stack, click the button below.

| Services | AWS Region Code | Launchers |
| --- | --- | --- |
| IVS | ap-northeast-1 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IVS&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/ivs.yaml) |
| MediaLive | ap-northeast-1 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaLive&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/medialive.yaml) |
| MediaPackage | ap-northeast-1 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaPackage&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediapackage.yaml) |
| MediaStore | ap-northeast-1 | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaStore&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediastore.yaml) |

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file ivs.yaml --stack-name IVS --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file medialive.yaml --stack-name MediaLive --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file mediapackage.yaml --stack-name MediaPackage --capabilities CAPABILITY_NAMED_IAM
aws cloudformation deploy --template-file mediastore.yaml --stack-name MediaStore --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows.

### IVS

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| Authorized | true or false | false | ○ | Whether the channel is authorized |
| LatencyMode | NORMAL or LOW | LOW | ○ | Channel latency mode |
| Type | STANDARD or BASIC | STANDARD | ○ | The channel type |

### MediaLive

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| AdMarker | ENABLED or DISABLED | DISABLED | ○ | Enable or disable ad marker |
| AudioBitrate | Number | 96000 | ○ | Average audio bitrate in bits/second |
| AutoInputFailover | ENABLED or DISABLED | ENABLED | ○ | Enable or disable automatic input failover |
| ChannelClass | STANDARD or SINGLE_PIPELINE | STANDARD | ○ | Select the class of channel you intend to attach this input to |
| FramerateDenominator | Number | 1001 | ○ | Framerate denominator |
| FramerateNumerator | Number | 30000 | ○ | Framerate numerator |
| GopNumBFrames | Number | 3 | ○ | Number of B-frames between reference frames |
| GopSize | Number | 60 | ○ | GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits |
| H264Profile | String | HIGH | ○ | H.264 Profile |
| H264Level | String | H264_LEVEL_4_1 | ○ | H.264 Level |
| Height | Number | 540 | ○ | Output video height, in pixels |
| HlsBucket | String | | | The S3 bucket Name HLS files are sent |
| InputType | RTMP / ELEMENTAL_LINK / S3 | ENABLED | ○ | Input type |
| InputStreamKey | String | stream | | A unique name for the location the RTMP stream is being pushed to |
| InputVodSourceBucket | String | | | The S3 bucket Name VOD contents exist |
| MediaPackageChannelId | String | | | The MediaPackage channel id |
| MediaStoreEndpoint | String | | | The endpoint of MediaStore |
| OutputType | String | RTMP | ○ | Output type |
| OutputRtmpUrl1 | String | | | The rtmp url a stream sends to |
| OutputRtmpStreamName1 | String | | | The rtmp stream name a stream sends to |
| OutputRtmpUrl2 | String | | | The rtmp url a stream sends to |
| OutputRtmpStreamName2 | String | | | The rtmp stream name a stream sends to |
| VideoBitrate | Number | 2200000 | ○ | Average video bitrate in bits/second |
| Width | Number | 960 | ○ | Output video width, in pixels |
| WhitelistRules | String | 0.0.0.0/0 | ○ | A list of one or more IPv4 CIDR addresses to allow |

### MediaPackage

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| ArchiveBucket | String | | | The S3 bucket Name LIVE-to-VOD contents are stored |
| ManifestName | String | index | ○ | A short string that's appended to the end of the endpoint URL |
| OutputType | APPLE_HLS, ISO_DASH, ALL | APPLE_HLS | ○ | Output type |
| StartoverWindowSeconds | Number | 0 | ○ | Maximum duration seconds of content to retain for startover playback |
| SegmentDurationSeconds | Number | 3 | ○ | Duration (in seconds) of each fragment |
| VodSourceBucket | String | | | The S3 bucket Name VOD contents exist |

### MediaStore

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| ExpirationDate | Number | 1 | ○ |  The date objects to expire |
| MaxAgeSeconds | Number | 30000 | ○ | The time in seconds that browser caches the preflight response |
| UserAgent | String | | ○ | The secret key that 'User-Agent' header contains |

### MediaTailor

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| **AdDecisionServerUrl** | String | | ○ | The URL for the ad decision server (ADS) for pre-roll ads |
| CdnContentSegmentUrlPrefix | String | | ○ | A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. |
| MaxDurationSeconds | Number | 120 | ○ | The maximum allowed duration for the pre-roll ad avail |
| PersonalizationThresholdSeconds | Number | 8 | ○ | Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break |
| **SlateAdUrl** | String | | ○ | The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads |
| **VideoContentSourceUrl** | String | | ○ | The URL prefix for the parent manifest for the stream, minus the asset ID |