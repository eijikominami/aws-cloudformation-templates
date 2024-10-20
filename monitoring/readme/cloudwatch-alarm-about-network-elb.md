Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-network-elb(en)

cloudwatch-alarm-about-network-elb creates Amazon CloudWatch Alarm about Network Load Balancer.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | TargetGroup | LoadBalancer | Threshold |
| --- | --- | --- | --- | --- |
| AWS/NetworkELB | **UnHealthyHostCount** | `TargetGroup` | `LoadBalancer` | At least once a minute | 
| AWS/NetworkELB | **PortAllocationErrorCount** | `TargetGroup` | `LoadBalancer` | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `TargetGroup` | String | | ○ | The target group id |
| `LoadBalancer` | String | | ○ | The load balancer name |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-network-elb(ja)

cloudwatch-alarm-about-network-elb Network Load Balancer に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TargetGroup | LoadBalancer | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/NetworkELB | **UnHealthyHostCount** | `TargetGroup` | `LoadBalancer` | 1分間に1回以上 | 
| AWS/NetworkELB | **PortAllocationErrorCount** | `TargetGroup` | `LoadBalancer` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `TargetGroup` | String | | ○ | ターゲットグループID |
| `LoadBalancer` | String | | ○ | ロードバランサー名 |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |