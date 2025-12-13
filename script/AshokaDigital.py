import json
import requests
import re

JSON_URL = "https://livetv.ashokadigital.net/api/api.php?get_posts=&page=1&count=3000&api_key=cda11bx8aITlKsXdsfafadskljasldfjoierKLrteaadfjalM"
OUTPUT_M3U = "playlist/AshokaDigital.m3u"

def clean_html(text):
    if not text:
        return ""
    return re.sub("<.*?>", "", text).strip()

# Download JSON
resp = requests.get(JSON_URL, timeout=30)
resp.raise_for_status()
data = resp.json()

lines = ["#EXTM3U"]

posts = data.get("posts", [])

for ch in posts:
    name = ch.get("channel_name", "Unknown")
    group = ch.get("category_name", "Live TV")
    logo = ch.get("channel_image", "")
    url = ch.get("channel_url")
    desc = clean_html(ch.get("channel_description", ""))

    if not url:
        continue

    lines.append(
        f'#EXTINF:-1 tvg-name="{name}" '
        f'tvg-logo="https://www.ashokadigital.net/_next/image?url=https://livetv.ashokadigital.net/upload/logo/{logo}&w=1920&q=75" '
        f'group-title="{group}",{name}'
    )
    lines.append(url)

with open(OUTPUT_M3U, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"M3U generated: {OUTPUT_M3U} ({len(posts)} channels)")

