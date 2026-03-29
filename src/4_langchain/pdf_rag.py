from langchain_aws import BedrockLLM, BedrockEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import boto3
from pathlib import Path


client = boto3.client(service_name = 'bedrock-runtime', region_name = 'eu-west-2')

model = BedrockLLM(model_id = 'meta.llama3-8b-instruct-v1:0' , client=client)
embedding_model = BedrockEmbeddings(model_id='amazon.titan-embed-text-v2:0', client=client)

base_dir = Path().resolve()
pdf = PyPDFLoader(base_dir / 'src/langchain/assets/books.pdf')
docs = pdf.load()

question = 'What themes does Gone with the Wind explore?'

splitter = RecursiveCharacterTextSplitter(separators=[".", "\n\n", "\n"], chunk_size = 200)
splited_docs = splitter.split_documents(docs)

# create vector store
vectore_stores = FAISS.from_documents(splited_docs, embedding_model)
# create retriever
retriever = vectore_stores.as_retriever(search_kwargs = {'k':2})

results = retriever.invoke(question)

result_list = []
for result in results:
    result_list.append(result.page_content)


template = ChatPromptTemplate.from_messages(
    [
        ('system', 'answer the question using this context: {context}'),
        ('user', '{input}')
    ]
)

chain = template | model

response = chain.invoke({'input':question, 'context': result_list})
print(response)