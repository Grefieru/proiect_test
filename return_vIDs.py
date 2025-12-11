import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


# Getting the upload playlistID from channels
def get_playlist_id(usern):

    url = "https://www.googleapis.com/youtube/v3/channels"

    params = {
        "part": "contentDetails",
        "forHandle": str(usern),
        "key": api_key
    }

    response = requests.get(url, params=params)
    print(response.status_code)
    response = response.json()

    playlistID = response['items'][0]["contentDetails"]['relatedPlaylists']["uploads"]

    return playlistID

# Returning Video IDs from playlistItems
def get_vIDs(playsID):

    video_ids = []
    next_page_token = None
    
    while True:
        url = "https://www.googleapis.com/youtube/v3/playlistItems"

        params = {
            "part": "contentDetails",
            "playlistId": str(playsID),
            "key": api_key,
            "maxResults": 50,
        }
        if next_page_token:
            params["pageToken"] = next_page_token

        response = requests.get(url, params=params).json()

        # extragem videoId-urile
        for item in response["items"]:
            video_ids.append(item["contentDetails"]["videoId"])

        # verificăm dacă mai e altă pagină
        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return video_ids

playsID = get_playlist_id("dylan.page.")

damelo = get_vIDs(playsID)
print(damelo)

# Just return the result as a JSON for visibility
def pretty_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)


