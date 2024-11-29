import base64
import boto3
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Decodificar el cuerpo JSON
        body = json.loads(event['body'])  # Decodifica el JSON recibido

        # Extraer los datos necesarios
        bucket_name = body['bucket_name']
        file_name = body['file_name']
        base_64_str = body['base_64_str']

        # Decodificar el archivo Base64 y subirlo a S3
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=base64.b64decode(base_64_str))
        
        return {
            'statusCode': 200,
            'body': f'File {file_name} uploaded to bucket {bucket_name}.'
        }
    
    except KeyError as e:
        # Manejar el caso en que falta una clave en el cuerpo
        return {
            'statusCode': 400,
            'error': f'Missing key in the request body: {str(e)}'
        }
    
    except Exception as e:
        # Manejar errores generales
        return {
            'statusCode': 500,
            'error': f'Error occurred: {str(e)}'
        }
