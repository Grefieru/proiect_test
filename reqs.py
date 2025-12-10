import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://www.googleapis.com/youtube/v3/videos"

params = {
    "id": "8qioenyx4Go",
    "key": api_key,
    "part": "snippet"
}

response = requests.get(url, params=params)

data = response.json()
#data2 = json.dumps(response.json(), indent=4)

print(response.status_code)

print(data["items"][0]["id"])