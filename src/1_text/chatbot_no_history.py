import boto3
import json


client = boto3.client(service_name='bedrock-runtime', region_name = 'eu-west-2')


def get_configuration_model(user_input):
    return json.dumps(
        {
        "prompt": f'''You are a precise and factual AI assistant.
        Answer the following question clearly and directly.
        Do not add extra explanations, opinions, or creative text.

        Question:
        {user_input}

        Answer: ''',
        "temperature": 0,
        "top_p": 1,
        "max_gen_len": 512
    }
    )

print('Hello, I am a bot model. How can I assist you Today?')


while True:
    user_input = input('User: ')

    if user_input.lower() == 'exit':
        break

    response = client.invoke_model(
        body = get_configuration_model(user_input=user_input) ,
        modelId= 'meta.llama3-8b-instruct-v1:0' ,
        accept="application/json", 
        contentType="application/json"
    )
    response_body = json.loads(response.get('body').read())
    print(f"Bot: {response_body['generation']}")