import boto3
import json


agent_client = boto3.client(service_name = 'bedrock-agent-runtime', region_name = 'eu-west-2')


def handler(event, context):
    body = json.loads(event['body'])
    question = body.get('question')
    if question:
        response = agent_client.retrieve_and_generate(
            input={'text': question},
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": "ODJMOXOK42",
                "modelArn": "arn:aws:bedrock:eu-west-2::foundation-model/amazon.nova-lite-v1:0"
                }
            }
        )
        answer = response.get('output').get('text')
        return {
            'statusCode': 200,
            'body': json.dumps({'answer': answer})
        }
    
    return {
            'statusCode': 400,
            'body': json.dumps({'error': 'question needed.'})
        }