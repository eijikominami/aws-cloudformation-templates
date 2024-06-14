Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# cloudwatch-alarm-about-appflow(en)

cloudwatch-alarm-about-appflow creates Amazon CloudWatch Alarm about Amazon AppFlow.

## CloudWatch Alarm

The template creates the following alarms.

| Namespace | MetricName | FlowName | Threshold |
| --- | --- | --- | --- |
| AWS/AppFlow | **FlowExecutionsFailed** | `FlowName` | At least once a minute | 

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Required | Details | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | The custom Alram name |
| `FlowName` | String | | ○ | The AppFlow flow name |
| `Environment` | String | production | | The value of `environment` tag |
| `TagKey` | String | createdby | | A tag key |
| `TagValue` | String | aws-cloudformation-templates | | A tag value |

---------------------------------------

# cloudwatch-alarm-about-appflow(ja)

cloudwatch-alarm-about-appflow は、Amazon AppFlow に関する Amazon CloudWatch アラームを作成します。

## CloudWatch アラーム

このテンプレートは、以下のアラームを作成します。

| ネームスペース | メトリクス | FlowName | 閾値 |
| --- | --- | --- | --- | --- |
| AWS/AppFlow | **FlowExecutionsFailed** | `FlowName` | 1分間に1回以上 | 

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| `CustomAlarmName` | String | | | カスタムアラーム名 |
| `FlowName` | String | | ○ | フロー名 |
| `Environment` | String | production | | `environment` タグの値 |
| `TagKey` | String | createdby | | タグキー |
| `TagValue` | String | aws-cloudformation-templates | | タグ値 |