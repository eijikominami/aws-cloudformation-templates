English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/media
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/media`` builds AWS Elemental Media Services.

## Prerequisites

Before deploying this template, ensure you have:

- IAM Identity Center instance configured (for Deadline Cloud)
- S3 buckets prepared for media content storage and archiving
- Understanding of media streaming protocols and requirements
- Content Delivery Network (CDN) endpoints configured (for MediaTailor)

> [!NOTE]
> You can also get useful sample templates at [**eijikominami/aws-cloudformation-samples/media**](https://github.com/eijikominami/aws-cloudformation-samples/tree/master/media).

## TL;DR

If you just want to deploy the stack, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| Deadline Cloud | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DeadlineCloud&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/deadlinecloud.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DeadlineCloud&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/deadlinecloud.yaml) |
| IVS | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=IVS&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/ivs.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=IVS&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/ivs.yaml) |
| MediaConnect | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MediaConnect&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediaconnect.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaConnect&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediaconnect.yaml) |
| MediaLive | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MediaLive&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/medialive.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaLive&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/medialive.yaml) |
| MediaPackage | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MediaPackage&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediapackage.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaPackage&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediapackage.yaml) |
| MediaStore | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=MediaStore&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediastore.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=MediaStore&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/media/mediastore.yaml) |

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file templates/deadlinecloud.yaml --stack-name DeadlineCloud --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/ivs.yaml --stack-name IVS --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/mediaconnect.yaml --stack-name MediaConnect --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/medialive.yaml --stack-name MediaLive --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
aws cloudformation deploy --template-file templates/mediapackage.yaml --stack-name MediaPackage --capabilities CAPABILITY_NAMED_IAM
aws cloudformation deploy --template-file templates/mediastore.yaml --stack-name MediaStore --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows.

### Deadline Cloud

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| **IdentityCenterInstanceArn** | String | | ○ | The ARN of the IAM Identity Center instance responsible for authenticating monitor users |
| MaxWorkerCount | Number | 10 | ○ | The maximum number of workers specified in the fleet |
| MinWorkerCount | Number | 0 | ○ | The minimum number of workers in the fleet |

### IVS

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| Authorized | true or false | false | ○ | Whether the channel is authorized |
| LatencyMode | NORMAL or LOW | LOW | ○ | Channel latency mode |
| Type | STANDARD or BASIC | STANDARD | ○ | The channel type |

### MediaConnect

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| DestinationIpAddressOrEntitlementArn1 | String | | | The IP address or the ARN of the the distination |
| DestinationPort1 | String | 5001 | | The port to use when MediaConnect distributes content to the output |
| DestinationProtocol1 | String | | | The protocol that is used by the distination |
| DestinationIpAddressOrEntitlementArn2 | String | | | The IP address or the ARN of the the distination |
| DestinationPort2 | String | 5002 | | The port to use when MediaConnect distributes content to the output |
| DestinationProtocol2 | String | | | The protocol that is used by the distination |
| DestinationIpAddressOrEntitlementArn3 | String | | | The IP address or the ARN of the the distination |
| DestinationPort3 | String | 5001 | | The port to use when MediaConnect distributes content to the output |
| DestinationProtocol4 | String | | | The protocol that is used by the distination |
| DestinationIpAddressOrEntitlementArn1 | String | | | The IP address or the ARN of the the distination |
| DestinationPort4 | String | 5001 | | The port to use when MediaConnect distributes content to the output |
| DestinationProtocol4 | String | | | The protocol that is used by the distination |
| DestinationIpAddressOrEntitlementArn5 | String | | | The IP address or the ARN of the the distination |
| DestinationPort5 | String | 5001 | | The port to use when MediaConnect distributes content to the output |
| DestinationProtocol5 | String | | | The protocol that is used by the distination |
| DestinationIpAddressOrEntitlementArn6 | String | | | The IP address or the ARN of the the distination |
| DestinationPort6 | String | 5001 | | The port to use when MediaConnect distributes content to the output |
| DestinationProtocol6 | String | | | The protocol that is used by the distination |
| DestinationIpAddressOrEntitlementArn7 | String | | | The IP address or the ARN of the the distination |
| DestinationPort7 | String | 5001 | | The port to use when MediaConnect distributes content to the output |
| DestinationProtocol7 | String | | | The protocol that is used by the distination |
| DestinationIpAddressOrEntitlementArn8 | String | | | The IP address or the ARN of the the distination |
| DestinationPort8 | String | 5001 | | The port to use when MediaConnect distributes content to the output |
| DestinationProtocol8 | String | | | The protocol that is used by the distination |
| FujitsuQoSSenderControlPort | Number | 9900 | | The port that the flow uses to send outbound requests to initiate connection with the sender |
| IngestPort | Number | 9177 | | The port that the flow listens on for incoming content |
| InputAllowedCidr | String | 0.0.0.0/0 | | The range of IP addresses that are allowed to contribute content to your source |
| MinLatency | Number | 100 | | The minimum latency in milliseconds for SRT-based streams |
| OutputAllowedCidr | String | 0.0.0.0/0 | | The range of IP addresses that are allowed to initiate output requests to this flow |
| SenderIpAddressOrEntitlementArn | String | | | The IP address or the ARN of the the sender |
| SenderType | String | srt-listener | ○ | The protocol that is used by the source |
| SrtCallerSourceListenerPort | Number | 2000 | | Source port for SRT-caller protocol |

### MediaConnect (Output)

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| CidrAllowList | String | 0.0.0.0/0 | fujitsu-qos, srt-listener | The range of IP addresses that are allowed to initiate output requests to this flow |
| DestinationIpAddressOrEntitlementArn | String | | srt-caller, zixi-push, rist, rtp-fec, rtp |  The IP address or the ARN of the the distination |
| **FlowArn** | String | | ○ | The Amazon Resource Name (ARN) of the flow this output is attached to |
| MinLatency | Number | 100 | srt-listener, srt-caller | The minimum latency in milliseconds for SRT-based streams |
| **Name** | String | | ○ | The name of the VPC interface |
| Port | Number | 9177 | fujitsu-qos, srt-listener, srt-caller, zixi-push, rist, rtp-fec, rtp | The port to use when MediaConnect distributes content to the output |
| Protocol | String | srt-listener | ○ | The protocol that is used by the source |

### MediaConvert

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| AccelerationSettings | ENABLED/PREFERRED/DISABLED | DISABLED | ○ | Specify the conditions when the service will run your job with accelerated transcoding |
| Category | String | Default | ○ | A category for the job template you are creating |
| Name | String | Default | ○ | The name of the job template you are creating |
| StatusUpdateInterval | Number | 60 | ○ | How often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events |

### MediaLive

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| AdMarker | ENABLED / DISABLED | DISABLED | ○ | Enable or disable ad marker |
| ArchiveBucket | String | | | The S3 bucket Name LIVE-to-VOD contents are stored |
| AudioBitrate | Number | 96000 | ○ | Average audio bitrate in bits/second |
| AutoInputFailover | ENABLED / DISABLED | ENABLED | ○ | Enable or disable automatic input failover |
| ChannelClass | STANDARD / SINGLE_PIPELINE | STANDARD | ○ | Select the class of channel you intend to attach this input to |
| ElementalLinkId1 | String | | | The unique ID for the Elemental Link device | 
| ElementalLinkId2 | String | | | The unique ID for the Elemental Link device |
| ElementalLinkType | HD / UHD | HD | | The type for the Elemental Link device |
| FramerateDenominator | Number | 1001 | ○ | Framerate denominator |
| FramerateNumerator | Number | 30000 | ○ | Framerate numerator |
| GopNumBFrames | Number | 3 | ○ | Number of B-frames between reference frames |
| GopSize | Number | 60 | ○ | GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits |
| H264Profile | String | HIGH | ○ | H.264 Profile |
| H264Level | String | H264_LEVEL_4_1 | ○ | H.264 Level |
| Height | Number | 540 | ○ | Output video height, in pixels |
| HlsBucket | String | | | The S3 bucket Name HLS files are sent |
| InputType | String | RTMP | ○ | Input type |
| InputStreamKey | String | stream | | A unique name for the location the RTMP stream is being pushed to |
| InputVodSourceBucket | String | | | The S3 bucket Name VOD contents exist |
| InputWhitelistRules | String | 0.0.0.0/0 | ○ | A list of one or more IPv4 CIDR addresses to allow |
| MediaPackageChannelId | String | | | The MediaPackage channel id |
| MediaStoreEndpoint | String | | | The endpoint of MediaStore |
| OutputType | S3, MEDIA_PACKAGE, MEDIA_STORE, RTMP, RTP | RTMP | ○ | Output type |
| OutputHlsBucket | String | | The S3 bucket Name HLS files are sent |
| OutputRtmpRtpUrl1 | String | | | The rtmp url a stream sends to |
| OutputRtmpStreamName1 | String | | | The rtmp stream name a stream sends to |
| OutputRtmpRtpUrl2 | String | | | The rtmp url a stream sends to |
| OutputRtmpStreamName2 | String | | | The rtmp stream name a stream sends to |
| VideoBitrate | Number | 2200000 | ○ | Average video bitrate in bits/second |
| Width | Number | 960 | ○ | Output video width, in pixels |

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
| **CdnContentSegmentUrlPrefix** | String | | ○ | A content delivery network (CDN) to cache content segments, so that content requests don’t always have to go to the origin server. |
| MaxDurationSeconds | Number | 120 | ○ | The maximum allowed duration for the pre-roll ad avail |
| PersonalizationThresholdSeconds | Number | 8 | ○ | Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break |
| **SlateAdUrl** | String | | ○ | The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads |
| **VideoContentSourceUrl** | String | | ○ | The URL prefix for the parent manifest for the stream, minus the asset ID |

## Troubleshooting

### MediaLive Issues

If MediaLive channels are not starting or streaming properly:

1. Verify that input sources are accessible and streaming correctly
2. Check that security groups allow the necessary ports for your input type
3. Ensure that output destinations (S3, MediaPackage, etc.) are properly configured
4. Verify that IAM roles have the necessary permissions for MediaLive operations

### MediaConnect Issues

If MediaConnect flows are not working:

1. Verify that source IP addresses are correctly whitelisted
2. Check that the specified ports are open and accessible
3. Ensure that the protocol settings match between source and destination
4. Verify that entitlements are properly configured for cross-account access

### MediaPackage Issues

If MediaPackage is not delivering content:

1. Verify that the MediaLive channel is successfully sending content to MediaPackage
2. Check that origin endpoints are properly configured with correct protocols
3. Ensure that CDN distributions are pointing to the correct MediaPackage endpoints
4. Verify that access policies allow the intended viewers

### Deadline Cloud Issues

If Deadline Cloud farms are not processing jobs:

1. Verify that IAM Identity Center is properly configured and accessible
2. Check that worker instances have the necessary software and licenses installed
3. Ensure that job submission queues are properly configured
4. Verify that storage locations are accessible from worker instances