import json
import requests

JSON_URL = "http://sscloud7.in/multi/tamilott.json"
OUTPUT_M3U = "playlist/TamilOtt.m3u"

# Download JSON
resp = requests.get(JSON_URL, timeout=20)
resp.raise_for_status()
data = resp.json()

lines = []
lines.append("#EXTM3U")

for app in data:
    group = app.get("content_title", "Tamil OTT")

    channels = app.get("channeldata", [])
    for ch in channels:
        name = ch.get("channelname", "Unknown")
        url = ch.get("playbackurl")
        logo = ch.get("logo", "")
        lang = ch.get("area", "tamil")

        if not url:
            continue

        lines.append(
            f'#EXTINF:-1 tvg-name="{name}" '
            f'tvg-logo="{logo}" '
            f'group-title="{group}" '
            f'tvg-language="{lang}",{name}'
        )
        lines.append(url)

with open(OUTPUT_M3U, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"M3U created: {OUTPUT_M3U}")
