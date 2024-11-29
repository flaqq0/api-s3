import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['body']['bucket_name']
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': f'Bucket {bucket_name} created successfully.'
        }
    except ClientError as e:
        return {
            'statusCode': 400,
            'body': f'Error creating bucket: {str(e)}'
        }

