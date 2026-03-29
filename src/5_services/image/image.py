import boto3
from botocore.config import Config
import base64
import json
from time import time


s3_bucket_name = 'image-bedrock-api-bucket'

bedrock_client = boto3.client(service_name = 'bedrock-runtime', 
                              region_name = 'us-west-2')
s3_client = boto3.client(service_name = 's3', region_name = 'eu-west-2')


def handler(event, context):
    body = json.loads(event['body'])
    description = body.get('description')
    if description:
        config = get_titan_config(description=description)
        response = bedrock_client.invoke_model(
            body = config,
            modelId = 'amazon.titan-image-generator-v2:0'
        )
        body = json.loads(response.get('body').read())
        base_image_64 = body.get('images')[0]
        signed_url = save_image_to_s3(base_image_64)
        return {
                'statusCode': 200,
                'body': json.dumps({"url": signed_url}) 
            }
        
    return {
            'statusCode': 400,
            'text': json.dumps({'error':'the descripation required!'})
        }


def save_image_to_s3(image: str):
    image_file = base64.b64decode(image)
    timestamp = int(time())
    image_name = str(timestamp) + '.jpg'

    s3_client.put_object(
        Bucket = s3_bucket_name,
        Key = image_name,
        Body = image_file
    )

    signed_url = s3_client.generate_presigned_url(
        'get_object',
        Params = {'Bucket': s3_bucket_name, 'Key': image_name},
        ExpiresIn = 3600
    )

    return signed_url


def get_titan_config(description: str):
    return json.dumps(
        {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {
                "text": description,      
            },
            "imageGenerationConfig": {
                "quality": "standard",
                "numberOfImages": 1,
                "height": 512,
                "width": 512,
                "cfgScale": 8.0,
                "seed": 42
            }
        }
    )
