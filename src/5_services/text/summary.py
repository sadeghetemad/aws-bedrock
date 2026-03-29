import boto3
import json

client = boto3.client(service_name = 'bedrock-runtime', region_name = 'eu-west-2')

def handler(event):
    body = json.loads(event['body'])
    text = body.get('text')
    points = event['queryStringParameters']['points']
    if text and points:
        response = client.invoke_model(
            body = get_lama_config(text, points),
            modelId = 'meta.llama3-8b-instruct-v1:0',
            accept="application/json", 
            contentType="application/json"
        )
        response_body = json.loads(response['body'].read())
        result = response_body.get('generation')
        return {
            'status_code': 200,
            'body': json.dumps({'summary': result})
        }
    return {
        'status_code': 400,
        'body': json.dumps({'error':'text and points required!'})
    }

def get_lama_config(text: str, points: str):

    prompt = f"""
You are a strict summarization system.

Task:
Summarize the given text into exactly {points} bullet points.

Rules:
- Output ONLY the bullet points
- No explanations, no extra text
- Do NOT use markdown or code blocks
- Do NOT include ``` or the word "python"
- Each bullet must be one short sentence
- Maximum 3 lines total
- Follow the exact format below

Text:
{text}

Output format:
- point 1
- point 2
- point 3

"""

    return json.dumps(
        {
            "prompt": prompt,
            "temperature": 0.2,
            "top_p": 0.9,
            "max_gen_len": 100
        }
    )