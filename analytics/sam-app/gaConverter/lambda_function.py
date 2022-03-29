import pandas as pd
import boto3
import urllib.parse
import json
from datetime import datetime as dt

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.parse.unquote(event['Records'][0]['s3']['object']['key'])

    s3_client = boto3.client('s3')
    raw_object = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    raw_data = json.loads(raw_object['Body'].read().decode('utf-8'))
    
    record_dates = [dt.strptime(r['dimensions'][0], '%Y%m%d%H') for r in raw_data['reports'][0]['data']['rows']]
    devices = [r['dimensions'][1] for r in raw_data['reports'][0]['data']['rows']]
    user_counts = [int(r['metrics'][0]['values'][0]) for r in raw_data['reports'][0]['data']['rows']]
    df = pd.DataFrame({
        'year': [r.year for r in record_dates],
        'month': [r.month for r in record_dates],
        'day': [r.day for r in record_dates],
        'hour': [r.hour for r in record_dates],
        'device': devices,
        'user_count': user_counts
    })
    
    output_file = dt.now().strftime('%Y%m%d%H%M%S')
    output_path = '/tmp/{}.parquet'.format(output_file)
    df.to_parquet(output_path)

    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    bucket.upload_file(output_path, 'GoogleAnalytics-parquet/{}.parquet'.format(output_file))