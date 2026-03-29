import boto3
import pprint

bedrock = boto3.client(service_name = 'bedrock', region_name = 'eu-west-2')

pp = pprint.PrettyPrinter(depth=4)


def list_foundation_models():
    models = bedrock.list_foundation_models()
    for model in models['modelSummaries']:
        pp.pprint(model)

def get_foundation_model(model_name):
    model = bedrock.get_foundation_model(modelIdentifier=model_name)
    pp.pprint(model)

list_foundation_models()
# get_foundation_model('anthropic.claude-3-7-sonnet-20250219-v1:0')