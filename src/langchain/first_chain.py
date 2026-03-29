from langchain_aws import BedrockLLM as Bedrock
from langchain_core.prompts import PromptTemplate
import boto3

AWS_REGION = 'us-west-2'

client = boto3.client(service_name = 'bedrock-runtime', region_name = AWS_REGION)

model = Bedrock(model_id = "meta.llama3-8b-instruct-v1:0", client=client)

def invoke_model():
    response = model.invoke("""
            You must follow the rules strictly.

            Rules:
            - Answer in one word only
            - Do not explain
            - Do not add anything

            Question:
            What is the highest mountain in the world?

            Answer:
            """)
    print(response)


def first_chain():
    prompt = PromptTemplate.from_template(
        'give me some explanation for this product: {product_name}'
    )

    chain = prompt | model

    print(prompt.format(product_name = 'PS5'))

    response = chain.invoke({'product_name': 'ps5'})
    print(response)

# invoke_model()
first_chain()