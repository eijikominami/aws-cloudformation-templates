English / [**日本語**](README_JP.md)

# AWSCloudFormationTemplates/cloudops
![Build Status](https://codebuild.ap-northeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZ3Z5MUkzdXRFcEtqM25ST0lZdW93ZVBKTnRXTk1WRGFUNkk2MzFpVERGNHp1dHU2RDNReU5IUlAvTitlRGgxNE03N3Y4ejZFaTNDVmpXdDZDK1pjRUFBPSIsIml2UGFyYW1ldGVyU3BlYyI6IllkWXQ5VVNaWE9QSnZkN3EiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-templates)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-templates)
 
``AWSCloudFormationTemplates/cloudops`` builds services for operational capabilities, such as ``Systems Manager`` and  ``DevOps Guru``.

## CloudOps

If you just want to deploy the stack, click the button below.

| US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- |
| [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=CloudOps&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/template.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CloudOps&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/template.yaml) |

If you want to deploy each service individually, click the button below.

| Services | US East (Virginia) | Asia Pacific (Tokyo) |
| --- | --- | --- |
| CloudWatch Application Insights | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=ApplicationInsights&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/applicationinsights.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=ApplicationInsights&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/applicationinsights.yaml) |
| CloudWatch Internet Monitor | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=InternetMonitor&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/internetmonitor.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=InternetMonitor&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/internetmonitor.yaml) |
| CodeGuru Reviewer | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=CodeGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/codeguru.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=CodeGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/codeguru.yaml) |
| DevOps Guru | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=DevOpsGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/devopsguru.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=DevOpsGuru&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/devopsguru.yaml) |
| Resource Explorer | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=ResourceExplorer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/resourceexplorer.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=ResourceExplorer&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/resourceexplorer.yaml) |
| Systems Manager | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SystemsManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/ssm.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/ssm.yaml) |
| Systems Manager Incident Manager | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=SystemsManagerIncidentManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/incidentmanager.yaml) | [![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=SystemsManagerIncidentManager&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/incidentmanager.yaml) |

Execute the command to deploy.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name CloudOps --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| **ApplicationInsight** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `ApplicationInsights` stack is deployed |
| CodeGuruTargetRepository | String | eijikominami/aws-cloudformation-templates | ○ | The GitHub owner name and repository name for AWS CodeGuru Reviewer |
| **IncidentManager** | ENABLED / DISABLED | DISABLED | ○ | If it is ENABLED, `IncidentManager` stack is deployed |
| IncidentManagerAlias | String | admimistrator | ○ | The unique and identifiable alias of the contact or escalation plan |
| IncidentManagerChatbotSnsArn | String | | | The SNS targets that AWS Chatbot uses to notify the chat channel of updates to an incident |
| IncidentManagerDisplayName | String | Administrator | ○ | The full name of the contact or escalation plan |
| IncidentManagerDurationInMinutes | Number | 1 | ○ | The time to wait until beginning the next stage |
| IncidentManagerEmail | String | | | The email address |
| IncidentManagerPhoneNumber | String | | | The Phone Number |
| IncidentManagerWorkloadName | String | Workload | ○ | The workload name |
| SSMAdminAccountId | Strig | | | AWS Account ID of the primary account (the account from which AWS Systems Manager Automation will be initiated) |
| SSMIgnoreResourceConflicts | ENABLED / DISABLED | DISABLED | ○ | If **Enabled** is set, the resources does NOT created |
| SSMOrganizationId | String | | | The Organizations ID |
| SSMPatchingAt | Number | 3 | ○ | Starting time of patching process. (Local Time) |

![](../images/architecture-cloudops.png)

### Application Insight

This template sets ``Amazon CloudWatch Application Insight``.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| **SNSForAlertArn** | String | | ○ | The ARN of an Amazon SNS topic |

### CodeGuru Reviewer

This template sets ``Amazon CodeGuru Reviewer``.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| **CodeGuruTargetRepository** | String | eijikominami/aws-cloudformation-templates | ○ | The GitHub owner name and repository name for AWS CodeGuru Reviewer |

### DevOps Guru

This template sets a notification channel of ``AWS DevOps Guru``.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| **SNSForAlertArn** | String | | ○ | The ARN of an Amazon SNS topic |

### Systems Manager

This template sets ``AWS Systems Manager``.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| AdminAccountId | String | | | AWS Account ID of the primary account (the account from which AWS Systems Manager Automation will be initiated) |
| AlarmLevel | NOTICE / WARNING | NOTICE | ○ | The alarm level of CloudWatch alarms |
| **IgnoreResourceConflicts** | ENABLED / DISABLED | DISABLED | ○ | Enable or disable AWS Systems Manager Incident Manager |
| OrganizationId | String | | | The Organizations ID |
| **PatchingAt** | Number | 3 | ○ | Daily patching time (H) |

If you use AWS Systems Manager Explorer in your `Shared Network` account, enable `Trusted Access` of **Systems Manager** and **AWS Trusted Advisor** in `AWS Organizations`.

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

## Amazon CloudWatch Internet Monitor

This template creates ``Amazon CloudWatch Internet Monitor``.

| Name | Type | Default | Required | Details |  
| --- | --- | --- | --- | --- |
| **ResourceNames** | String |  | ○ | The resources that have been added for the monitor |

## Amazon CloudWatch Synthetics

CloudWatch Synthetics creates canaries, configurable scripts that run on a schedule, and monitors your endpoints. If you just want to deploy the stack, click the button below.

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=Synthetics&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-templates/cloudops/synthetics-heartbeat.yaml) 

Execute the command to deploy with ``CanaryName``, ``DomainName`` and ``WatchedPagePath``.

```bash
aws cloudformation deploy --template-file synthetics-heartbeat.yaml --stack-name Synthetics --parameter-overrides CanaryName=XXXXX DomainName=XXXXX WatchedPagePath=XXXXX
```

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| IncidentManagerArn | String | | | Systems Manager Incident Manager response plan ARN |
| IncidentDurationInSeconds | Number | 600 | ○ | The time to wait until starting an incident |
| IncidentSuccessPercentThreshold | Number | 50 | ○ | The threshold of success percent starting an incident |
| **CanaryName** | String | | ○ | The name for this canary |
| **DomainName** | String | | ○ | The domain name that hearbeat scripts watches |
| WatchedPagePath | String | /index.html | ○ | The page path that hearbeat scripts watches |

![](../images/architecture-synthetics.png)

### AWS Lambda

This template creates ``hearbeat scripts`` using AWS Lambda function that load the specified URL and store a screenshot of the page and an HTTP archive file (HAR file). They also store logs of accessed URLs. 

### Amazon S3

The S3 bucket stores screenshots, HAR files, and logs from the hearbeat scripts.

### Amazon CloudWatch Alarm

This template creates Amazon CloudWatch custom metrics and alarms.
These alarms are trigged when the success rate is less than **90%**.