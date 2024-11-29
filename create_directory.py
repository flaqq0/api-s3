import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    body = event['body']
    bucket_name = body['bucket_name']
    directory_name = body['directory_name']
    
    s3_client.put_object(Bucket=bucket_name, Key=(directory_name + '/'))
    
    return {
        'statusCode': 200,
        'body': f'Directory {directory_name} created in bucket {bucket_name}.'
    }

