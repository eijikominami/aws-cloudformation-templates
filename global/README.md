English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/global
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/global`` creates global settings on N.Virginia Region (`us-east-1`).

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=GlobalSettings&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/global/template.yaml) | | 

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-global.png)

### AWS Certificate Manager

This template creates an SSL certification in ``AWS Certificate Manager``.

### CloudWatch Alarm

This template creates CloudWatch Alarm about ``Billing`` and ``CloudFront`` (``Error Rate``, ``Requests`` and ``Download Bytes``).

### Other Resources

This template creates some other resources, such as ``Amazon SNS``.

## Deployment

Execute the command to deploy in the ``us-east-1`` region because ``AWS Certificate Manager``, ``CloudFront`` and ``Billing`` only support the region.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name GlobalSettings --region us-east-1
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| ACMValidationMethod | DNS / EMAIL | DNS | ○ | The method you want to use to validate that you own or control the domain associated with a public certificate.  |
| **ACMDomainName** | String | | | If it's NOT empty, **SSL certification** is created |
| AlarmLevel | NOTICE/WARNING | NOTICE | | The alarm level of CloudWatch alarms |
| BillingAlertThreshold | Number | 0 | ○ | If it's NOT ZERO, **CloudWatch Alarm** is created |
| BudgetName | String | Total | ○ | The budget name. When ``BillingAlertThreshold`` is changed, **this value also must be changed**  |
| CentralizedLogBucketName | String | | | The centralize S3 bucket name for logging |
| CloudFrontErrorRateThreshold | Number | 0 | ○ | If it's NOT ZERO, **CloudWatch Alarm** is created |
| CloudFrontBytesDownloadedPerMinuteThreshold | Number | 0 | ○ | If it's NOT ZERO, **CloudWatch Alarm** is created |
| CloudFrontDistributionId | String | | | The CloudFront Distribution Id for monitoring |
| CostUsageReport | ENABLED / DISABLED | DISABLED　| | If it is **ENABLED**, Cost Usage Report is created |
| DomainName | String | | | The name of the domain | 
| NotificationThreshold | Number | 10 | ○ | The dollar value that triggers a notification if the threshold is exceeded | 
| WebACL | ENABLED / DISABLED | DISABLED | ○ | If it is **DISABLED**, AWS WAF does NOT created |