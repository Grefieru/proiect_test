import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

url = "https://www.googleapis.com/youtube/v3/videos"

#This function return the title and publishTime and can be saved in 2 variables.
def get_tile_publish(id):
    params = {
        "id": str(id),
        "key": api_key,
        "part": "snippet"
    }

    response = requests.get(url, params=params)
    print(response.status_code)
    response = response.json()
    title = response["items"][0]["snippet"]["title"]
    published = response["items"][0]["snippet"]["publishedAt"]
    
    return title, published

titlu, uptime = get_tile_publish("8qioenyx4Go")

#This function returns the title, likes, comments, as 3 variables.
def get_stats(id):

    params = {
        "id": str(id),
        "key": api_key,
        "part": "statistics"
    }

    response = requests.get(url, params=params)
    print(response.status_code)
    response = response.json()

    views = response["items"][0]["statistics"]["viewCount"]
    likes = response["items"][0]["statistics"]["likeCount"]
    comments = response["items"][0]["statistics"]["commentCount"]
    
    return views, likes, comments

views, likes, comments = get_stats("8qioenyx4Go")

print(f"The Video: {titlu}\n Publshed on: {uptime} has {views} views, {likes} likes and {comments} comments.")












#print(json.dumps(my_rez, indent=4))
#print(titlu, uptime)
#data2 = json.dumps(response.json(), indent=4)
#print(data)
#print(data["items"][0]["id"])