import requests

url = "https://sscloud7.in/multi/tamilott.json"

r = requests.get(url)

with open("data.json", "wb") as f:
    f.write(r.content)

print("✔ File saved")
