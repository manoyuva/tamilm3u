import requests
import json

url = "https://sscloud7.in/multi/tamilott.json"

response = requests.get(url)
data = response.json()

with open("channels.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("JSON downloaded: channels.json")
