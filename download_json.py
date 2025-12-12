import requests
import json

JSON_URL = "https://sscloud7.in/multi/tamilott.json"

response = requests.get(JSON_URL)
data = response.json()

with open("channels.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("JSON downloaded: channels.json")
