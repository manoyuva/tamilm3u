import json

# Load JSON file
with open("playlist.json", "r") as f:
    items = json.load(f)

# Open output M3U file
with open("play.m3u", "w") as m3u:
    m3u.write("#EXTM3U\n")

    # If file contains a list of channels
    if isinstance(items, list):
        for item in items:
            title = item.get("content_title", "No Title")
            url = item.get("stream_url") or item.get("content_url")
            m3u.write(f'#EXTINF:-1,{title}\n{url}\n')
    
    # If single channel object
    elif isinstance(items, dict):
        title = items.get("content_title", "No Title")
        url = items.get("stream_url") or items.get("content_url")
        m3u.write(f'#EXTINF:-1,{title}\n{url}\n')

 print(f"play.m3u")
