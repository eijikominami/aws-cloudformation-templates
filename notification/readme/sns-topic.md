Please scroll down for the Japanese version. / **日本語の説明は下にあります。**

# sns-topic(en)

sns-topic creates Amazon SNS topic and related CloudWatch Alarm.

## Parameters

You can provide optional parameters as follows.

| Name | Type | Default | Requied | Details | 
| --- | --- | --- | --- | --- |
| CrossAccountSubscriberAccountId | String | | | Account ID allowed to subscribe to this topic (for cross-account webhook forwarding) |
| TopicName | String | Default | ○ | Amazon SNS Topic Name |

---------------------------------------

# sns-topic(ja)

sns-topic は、Amazon SNS トピックとこれに関連する CloudWatch アラームを作成します。

## パラメータ

以下のパラメータを指定できます。

| パラメータ | タイプ | デフォルト値 | 必須 | 内容 | 
| --- | --- | --- | --- | --- |
| CrossAccountSubscriberAccountId | String | | | このトピックへのクロスアカウント Subscribe を許可するアカウント ID |
| TopicName | String | Default | ○ | Amazon SNS トピック名 |
