import boto3
from langchain_aws import BedrockLLM, BedrockEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS


my_knowledge_base = [
    'sadegh like to eat Kebab',
    'sadegh like to eat pizza',
    'the weather is nice today',
    'tommorw is saturday'
]

question = 'what does sadegh like to eat?'

client = boto3.client(service_name = 'bedrock-runtime', region_name = 'eu-west-2')

model = BedrockLLM(model_id = 'meta.llama3-8b-instruct-v1:0' , client= client)
embedding_model = BedrockEmbeddings(model_id='amazon.titan-embed-text-v2:0', client=client)

vectore_store = FAISS.from_texts(texts=my_knowledge_base, embedding=embedding_model)
retriever = vectore_store.as_retriever(search_kwargs = {'k':2})


results = retriever.invoke(question)

result_string = []
for result in results:
    result_string.append(result.page_content)


template = ChatPromptTemplate(
    [
        ('system','answer the question based on this context: {context}'),
        ('user', '{input}')

    ]
)

chain = template | model

response = chain.invoke({'input':question, 'context':result_string})

print(response)