import boto3
import json
from similarity import cosine_similarity


client = boto3.client(service_name = 'bedrock-runtime', region_name='us-west-2')


facts = [
    'The first computer was invented in the 1940s.',
    'John F. Kennedy was the 35th President of the United States.',
    'The first moon landing was in 1969.',
    'The capital of France is Paris.',
    'Earth is the third planet from the sun.'
]

# query = 'what is the captial of France?'
query = 'sunset'


def get_embedding(input_txt: str)-> list[float]:
    response = client.invoke_model(
        modelId= 'amazon.titan-embed-text-v1',
        body = json.dumps(
            {
                'inputText': input_txt
            }
        )
    )
    response_body = json.loads(response.get('body').read())
    return response_body.get('embedding')

embedding_store = []

for fact in facts:
    embedding_store.append(
        {
            'text': fact,
            'embedding': get_embedding(fact)
            }
    )

query_embeding = get_embedding(query)

similarities = []

for embed in embedding_store:
    similarities.append(
        {
            'text': embed['text'],
            'similarity': cosine_similarity(embed['embedding'], query_embeding)
        }
    )

print(f"Similarities for fact: '{query}' with:")
similarities.sort(key=lambda x: x['similarity'], reverse=True)
for similarity in similarities:
    print(f"  '{similarity['text']}': {similarity['similarity']:.2f}")
