Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-application-elb(en)

cloudwatch-alarm-about-application-elb creates Amazon CloudWatch Alarm about Application Load Balancer.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | TargetGroup | LoadBalancer | Threshold |
| --- | --- | --- | --- | --- |
| AWS/ApplicationELB | **UnHealthyHostCount** | `TargetGroup` | `LoadBalancer` | At least once a minute | 
| AWS/ApplicationELB | **HTTPCode_Target_5XX_Count** | `TargetGroup` | `LoadBalancer` | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `TargetGroup` | String | | ○ | The target group id |
| `LoadBalancer` | String | | ○ | The load balancer name |

---------------------------------------

# cloudwatch-alarm-about-application-elb(ja)

cloudwatch-alarm-about-application-elb は、Application Load Balancer に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | TargetGroup | LoadBalancer | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/ApplicationELB | **UnHealthyHostCount** | `TargetGroup` | `LoadBalancer` | 1分間に1回以上 | 
| AWS/ApplicationELB | **HTTPCode_Target_5XX_Count** | `TargetGroup` | `LoadBalancer` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `TargetGroup` | String | | ○ | ターゲットグループID |
| `LoadBalancer` | String | | ○ | ロードバランサー名 |