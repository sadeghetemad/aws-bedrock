import boto3
import json
import base64
from pathlib import Path
from PIL import Image
from io import BytesIO

client = boto3.client(
    service_name='bedrock-runtime',
    region_name="us-west-2"
)

def resize_and_encode(image_path, max_size=1408):
    img = Image.open(image_path)

    img.thumbnail((max_size, max_size))

    buffer = BytesIO()
    img.save(buffer, format="PNG")

    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def get_configuration(inputImage: str):
    return json.dumps({
        "taskType": "INPAINTING",
        "inPaintingParams": {
            "text": "Make the dragon black and blue",
            "negativeText": "bad quality, low res",
            "image": inputImage,
            "maskPrompt": "cat"
        },
        "imageGenerationConfig": {
            "numberOfImages": 1,
            "height": 512,
            "width": 512,
            "cfgScale": 8.0,
        }
    })


base_dir = Path().resolve()
image_path = base_dir / "src/image/output/dragon.png"

base_image = resize_and_encode(image_path)

response = client.invoke_model(
    body=get_configuration(base_image),
    modelId="amazon.titan-image-generator-v2:0",
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())
base64_image = response_body.get("images")[0]

output_path = base_dir / "dragon_edited.png"

with open(output_path, "wb") as f:
    f.write(base64.b64decode(base64_image))

print("Done:", output_path)