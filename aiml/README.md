English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/aiml
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

``AWSCloudFormationTemplates/aiml`` creates resources for AI/ML services.

## Prerequisites

Before deploying this template, ensure you have:

- Access to Amazon Bedrock models in your region (model access must be requested separately)
- S3 bucket prepared for Kendra data sources (if using Kendra)

## TL;DR

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=AIML&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/aiml/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=AIML&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/aiml/template.yaml) |

## Architecture

![](../images/architecture-aiml.png)

## Resources

This template creates the following resources.

### Amazon Bedrock

- Amazon Bedrock Knowledge Base
- Amazon Bedrock Agent
- IAM Roles for Bedrock services

### Amazon Kendra

- Amazon Kendra Index
- Amazon Kendra Data Source
- IAM Roles for Kendra services

## Parameters

The template accepts the following parameters:

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| BedrockEnabled | String | false | Yes | Enable Amazon Bedrock resources |
| KendraEnabled | String | false | Yes | Enable Amazon Kendra resources |
| KendraEdition | String | DEVELOPER_EDITION | Yes | The edition of Amazon Kendra to use |
| S3BucketName | String | | No | S3 bucket name for Kendra data source |

## Outputs

The template outputs the following values:

| Name | Description |
| --- | --- |
| BedrockKnowledgeBaseId | The ID of the Amazon Bedrock Knowledge Base |
| BedrockAgentId | The ID of the Amazon Bedrock Agent |
| KendraIndexId | The ID of the Amazon Kendra Index |
| KendraDataSourceId | The ID of the Amazon Kendra Data Source |

## Notes

- Amazon Bedrock and Amazon Kendra are charged based on usage. Make sure to check the pricing before enabling these services.
- The template uses the latest AI/ML service features available as of June 2025.
- For production use, consider additional security configurations and data encryption settings.
