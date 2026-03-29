import json
from image import handler


event = {
    'body': json.dumps({'description': 'a cute cat'})
}

response = handler(event=event, context={})

print(response)