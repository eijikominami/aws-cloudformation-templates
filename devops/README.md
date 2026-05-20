[**日本語**](README_JP.md) / English

# AWSCloudFormationTemplates/devops
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)

`AWSCloudFormationTemplates/devops` sets up **AWS frontier AI agents** for DevOps operations. This includes `AWS DevOps Agent` and related resources for autonomous incident response, root cause analysis, and operational excellence.

## TL;DR

If you want to deploy each service individually, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| AWS DevOps Agent | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DevOpsAgent&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/devops/templates/devops-agent.yaml) | [![cloudformation-launch-stack](https://raw.githubusercontent.com/eijikominami/aws-cloudformation-templates/master/images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DevOpsAgent&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/devops/templates/devops-agent.yaml) |

## Architecture

### AWS DevOps Agent

`AWS DevOps Agent` is an always-available **frontier AI agent** that autonomously resolves and proactively prevents incidents, optimizes application reliability, and handles on-demand SRE tasks across AWS, multicloud, and on-premises environments.

This template provisions all prerequisites for AWS DevOps Agent:

- **IAM roles** — service role (`aidevops.amazonaws.com`) with `AIDevOpsAgentAccessPolicy` for resource discovery, and operator app role with `AIDevOpsOperatorAppAccessPolicy` for web console access
- **Agent Space** — logical container defining the scope of AWS resources and tool integrations the agent can access; provisioned via a Lambda-backed Custom Resource
- **AWS account association** — grants the Agent Space access to the primary account for topology discovery and CloudWatch alarm monitoring
- **Operator App** — enables IAM-authenticated access to the DevOps Agent web console
- **EventChannel (Webhook)** — inbound webhook endpoint for triggering investigations from external observability tools (Datadog, Grafana, PagerDuty, etc.)

#### How incident response works

Once deployed, AWS DevOps Agent continuously monitors your AWS environment using the associated IAM role. When a CloudWatch alarm enters ALARM state, the agent automatically initiates an investigation — no additional SNS wiring required for AWS-native alarms. It correlates metrics, logs, deployment events, and code changes across your stack to identify root cause and propose mitigation steps.

For external observability tools, route alerts to the provisioned webhook URL.

```
CloudWatch Alarms  ──(IAM role polling)──▶  DevOps Agent  ──▶  Investigation
External Tools     ──(Webhook POST)──────▶  DevOps Agent  ──▶  Investigation
```

| Resource | Description |
| --- | --- |
| `IAMRoleForAgentSpace` | Service role assumed by AWS DevOps Agent for resource discovery |
| `IAMRoleForWebappAdmin` | Role for Operator App (web console) access |
| `IAMRoleForCustomResourceLambda` | Execution role for the CloudFormation Custom Resource Lambda |
| `ServerlessFunctionForAgentSpaceCustomResource` | Lambda that creates/updates/deletes the Agent Space via DevOps Agent API |
| `CustomResourceForAgentSpace` | CloudFormation Custom Resource orchestrating Agent Space setup |
| `CloudWatchAlarmForLambdaErrors` | Alarm on Custom Resource Lambda errors |

| Output | Description |
| --- | --- |
| `AgentSpaceId` | Agent Space unique identifier |
| `IAMRoleForAgentSpaceArn` | ARN of the DevOps Agent service role |
| `IAMRoleForWebappAdminArn` | ARN of the Operator App role |
| `ConsoleUrl` | Direct link to the Agent Space in the AWS DevOps Agent console |
| `WebhookUrl` | Inbound webhook URL for external alert sources |
