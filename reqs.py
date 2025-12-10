import requests
import json

url = "https://www.googleapis.com/youtube/v3/videos"

params = {
    "id": "8qioenyx4Go",
    "key": "AIzaSyCnsopNmbexdvZJMo3L_-Znmf0bdgaPTxQ",
    "part": "snippet"
}

response = requests.get(url, params=params)

data = response.json()
#data2 = json.dumps(response.json(), indent=4)



print(data["items"][0]["id"])