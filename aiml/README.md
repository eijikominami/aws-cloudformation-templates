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

## Troubleshooting

### Amazon Bedrock Issues

If you encounter problems with Amazon Bedrock:

1. Verify that you have requested access to the required foundation models in your region
2. Check that your IAM roles have the necessary permissions for Bedrock services
3. Ensure that your knowledge base data sources are properly configured and accessible
4. Verify that vector embeddings are being generated correctly for your content

### Amazon Kendra Issues

If Amazon Kendra is not working as expected:

1. Verify that your S3 bucket has the correct permissions for Kendra to access documents
2. Check that your data source configuration matches your document structure
3. Ensure that the Kendra service role has permissions to access your data sources
4. Monitor the data source sync status and resolve any indexing errors

### Performance and Cost Optimization

To optimize performance and costs:

1. Choose the appropriate Kendra edition based on your query volume requirements
2. Monitor Bedrock token usage and implement caching strategies where appropriate
3. Use Kendra's relevance tuning features to improve search accuracy
4. Implement proper data lifecycle management for your knowledge bases

### Security Considerations

For enhanced security:

1. Enable encryption at rest for all AI/ML resources
2. Use VPC endpoints for private connectivity to AI/ML services
3. Implement proper access controls and audit logging
4. Consider data residency requirements for sensitive information

## Troubleshooting

### Amazon Bedrock Issues

If Bedrock models are not accessible:

1. Verify that model access has been requested and approved in the Bedrock console
2. Check that the IAM roles have the necessary permissions for Bedrock services
3. Ensure that the region supports the specific Bedrock models you're trying to use
4. Verify that the knowledge base data sources are properly configured

### Amazon Kendra Issues

If Kendra index is not working properly:

1. Verify that the S3 bucket contains the documents to be indexed
2. Check that the Kendra service role has permissions to access the S3 bucket
3. Ensure that the document formats are supported by Kendra
4. Monitor the index synchronization status in the Kendra console

### Knowledge Base Issues

If the Bedrock Knowledge Base is not returning accurate results:

1. Verify that the data sources are properly synchronized
2. Check that the embedding model is appropriate for your content type
3. Ensure that the vector database is properly configured
4. Review the knowledge base query logs for troubleshooting information