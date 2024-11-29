import base64
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    body = event['body']
    bucket_name = body['bucket_name']
    file_name = body['file_name']
    base_64_str = body['base_64_str']
    
    s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=base64.b64decode(base_64_str))
    
    return {
        'statusCode': 200,
        'body': f'File {file_name} uploaded to bucket {bucket_name}.'
    }
