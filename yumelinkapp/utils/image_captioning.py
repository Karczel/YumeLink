import requests
from yumelink import settings

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": f"Bearer {settings.HUGGABLE_FACE_API_KEY}"}

def query(image_url):
    response = requests.post(API_URL, headers=headers, json={"inputs": image_url})
    return response.json()

# output = query("cats.jpg")