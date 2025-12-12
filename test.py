import requests
import json

def download_json(url="https://sscloud7.in/multi/tamilott.json", filename="data.json"):
    """Download JSON data from a URL and save it."""
    print("Downloading JSON...")
    response = requests.get(url)
    data = response.json()

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"✔ JSON saved as {filename}")
    return filename


def json_to_m3u(json_file, m3u_file="playlist.m3u"):
    """Convert JSON file to M3U file."""
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(m3u_file, "w", encoding="utf-8") as m3u:
        m3u.write("#EXTM3U\n")

        for item in data:
            name = item.get("display_name") or item.get("name") or "Unknown"
            url = item.get("url", "")
            logo = item.get("logo", "")

            if url:
                m3u.write(f'#EXTINF:-1 tvg-logo="{logo}",{name}\n')
                m3u.write(url + "\n")

    print(f"✔ M3U file created: {m3u_file}")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

json_url = "https://sscloud7.in/multi/tamilott.json"

# Step 1: Download JSON
json_file = download_json(json_url, "channels.json")

# Step 2: Convert downloaded JSON to M3U
json_to_m3u(json_file, "playlist.m3u")
