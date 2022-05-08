English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/cloudops
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiT1o3djE0RFpweWErRDl6SkpwTGsySVJKbWk0ajhreUlEaXAvTHh3ZzdaS2wzNVR5V1hpZkZRRVRtcFIvNncydWdad2w4TG9MRVMzVGFvMlZKY2RNYUowPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0vOGVWdGFEWTlyYVdDZUwiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/cloudops`` builds services for operational capabilities, such as ``CodeGuru Profiler`` and  ``DevOps Guru``.

## TL;DR

If you just want to deploy the stack, click the button below.

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudOps&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/template.yaml) 

If you want to deploy each service individually, click the button below.

| Services | Launchers |
| --- | --- |
| CodeGuru Profiler | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CodeGuruProfiler&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/codeguruprofiler.yaml) |
| DevOps Guru | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DevOpsGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/devopsguru.yaml) |
| Systems Manager | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/ssm.yaml) |
| Systems Manager Incident Manager | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManagerIncidentManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/systemsmanagerincidentmanager.yaml) |

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture-cloudops.png)

## Deployment

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name CloudOps --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| IncidentManager | ENABLED / DISABLED | ENABLED | ○ | If it is ENABLED, `IncidentManager` stack is deployed |
| IncidentManagerAlias | String | admimistrator | ○ | The unique and identifiable alias of the contact or escalation plan |
| IncidentManagerChatbotSnsArn | String | | | The SNS targets that AWS Chatbot uses to notify the chat channel of updates to an incident |
| IncidentManagerDisplayName | String | Administrator | ○ | The full name of the contact or escalation plan |
| IncidentManagerDurationInMinutes | Number | 1 | ○ | The time to wait until beginning the next stage |
| IncidentManagerEmail | String | | | The email address |
| IncidentManagerPhoneNumber | String | | | The Phone Number |
| IncidentManagerWorkloadName | String | Workload | ○ | The workload name |
| SSMIgnoreResourceConflicts | ENABLED / DISABLED | DISABLED | ○ | If **Enabled** is set, the resources does NOT created |
| SSMPatchingAt | Number | 3 | ○ | Starting time of patching process. (Local Time) |

### CodeGuru Profiler

This template creates a profiling group of ``AWS CodeGuru Profiler``.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| **AgentPermission** | String | | ○ | The agent permissions attached to this profiling group |
| ProfilingGroupName | String | Default | ○ | The name of the profiling group |
| **SNSForAlertArn** | String | | ○ | The ARN of an Amazon SNS topic |

### DevOps Guru

This template sets a notification channel of ``AWS DevOps Guru``.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| **SNSForAlertArn** | String | | ○ | The ARN of an Amazon SNS topic |

### Systems Manager Incident Manager

This template sets a notification channel of ``AWS Systems Manager Incident Manager``.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| Alias | String | admimistrator | ○ | The unique and identifiable alias of the contact or escalation plan |
| ChatbotSnsArn | String | | | The SNS targets that AWS Chatbot uses to notify the chat channel of updates to an incident |
| DisplayName | String | Administrator | ○ | The full name of the contact or escalation plan |
| DurationInMinutes | Number | 1 | ○ | The time to wait until beginning the next stage |
| Email | String | | | The email address |
| PhoneNumber | String | | | The Phone Number |
| WorkloadName | String | Workload | ○ | The workload name |