import boto3
import json


client = boto3.client(service_name='bedrock-runtime', region_name = 'eu-west-2')

history = []

def get_history():
    return '\n'.join(history)

def get_configuration_model():
    return json.dumps(
        {
        "prompt": f"""<|begin_of_text|>
            <|start_header_id|>system<|end_header_id|>
            You are a precise and factual AI assistant. Answer briefly and directly.
            <|eot_id|>
            <|start_header_id|>user<|end_header_id|>
            {get_history()}
            <|eot_id|>
            <|start_header_id|>assistant<|end_header_id|>
            """,
        "temperature": 0,
        "top_p": 1,
        "max_gen_len": 512
    }
    )

print('Hello, I am a bot model. How can I assist you Today?')


while True:
    user_input = input('User: ')
    history.append('user: ' + user_input)

    if user_input.lower() == 'exit':
        break

    response = client.invoke_model(
        body = get_configuration_model() ,
        modelId= 'meta.llama3-8b-instruct-v1:0' ,
        accept="application/json", 
        contentType="application/json"
    )
    response_body = json.loads(response.get('body').read())
    model_output = response_body['generation'].strip()
    print(f"Bot: {model_output}")
    history.append('assistant:' + model_output)
