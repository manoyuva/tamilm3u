import requests
import json

url = "https://sscloud7.in/multi/tamilott.json"

response = requests.get(url)
response.raise_for_status()

json_data = response.json()

with open("data.json", "w") as f:
    json.dump(json_data, f, indent=4)

print("✔ File saved to data.json")
