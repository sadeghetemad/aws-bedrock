import json
from rag import handler


event = {
    'body': json.dumps({'question': 'what is the conditional probability?'})
}

response = handler(event=event, context={})

print(response)