import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()
endpoint = os.environ["VISION_ENDPOINT"]
key = os.environ["VISION_KEY"]

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

result = client.analyze(
    image_data=open("sample.jpg", "rb").read(),
    visual_features=[VisualFeatures.TAGS],
)


if __name__ == "__main__":
    print("Tags extracted from image")
    for x in result.tags["values"]:
        print(x["name"])