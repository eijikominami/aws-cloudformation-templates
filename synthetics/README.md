English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/synthetics
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/synthetics`` builds ``Amazon CloudWatch Synthetics``.

## TL;DR

If you just want to deploy the stack, click the button below.

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Synthetics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/synthetics/heartbeat.yaml) 

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-synthetics.png)

### Amazon CloudWatch Synthetics

CloudWatch Synthetics creates canaries, configurable scripts that run on a schedule, and monitors your endpoints.

### AWS Lambda

This template creates ``hearbeat scripts`` using AWS Lambda function that load the specified URL and store a screenshot of the page and an HTTP archive file (HAR file). They also store logs of accessed URLs. 

### Amazon S3

The S3 bucket stores screenshots, HAR files, and logs from the hearbeat scripts.

### Amazon CloudWatch Alarm

This template creates Amazon CloudWatch custom metrics and alarms.
These alarms are trigged when the success rate is less than **90%**.

## Deployment

Execute the command to deploy with ``CanaryName``, ``DomainName`` and ``WatchedPagePath``.

```bash
aws cloudformation deploy --template-file heartbeat.yaml --stack-name Synthetics --parameter-overrides CanaryName=XXXXX DomainName=XXXXX WatchedPagePath=XXXXX
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| CanaryName | String | | ○ | The name for this canary. |
| DomainName | String | | ○ | The domain name that hearbeat scripts watches. |
| WatchedPagePath | String | /index.html | ○ | The page path that hearbeat scripts watches. |