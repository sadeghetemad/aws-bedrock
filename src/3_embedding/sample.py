import boto3
import json


client = boto3.client(service_name = 'bedrock-runtime', region_name = 'us-west-2')


text = 'I love Elnaz'


response = client.invoke_model(
    modelId = 'amazon.titan-embed-text-v1',
    body = json.dumps(
        {
            'inputText': text
            }
        ),
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get('body').read())
print(response_body.get('embedding'))