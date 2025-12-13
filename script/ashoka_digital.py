import json

"""
Convert Ashoka Digital API JSON to M3U playlist

JSON structure:
{
  "status": "ok",
  "posts": [ { channel_name, channel_url, channel_image, category_name, user_agent } ]
}
"""

INPUT_JSON = "json/ashoka_digital.json"
OUTPUT_M3U = "playlist/ashoka_digital.m3u"

with open(INPUT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

posts = data.get("posts", [])

with open(OUTPUT_M3U, "w", encoding="utf-8") as m3u:
    m3u.write("#EXTM3U\n")

    for ch in posts:
        name = ch.get("channel_name", "Unknown")
        url = ch.get("channel_url", "")
        logo = ch.get("channel_image", "")
        group = ch.get("category_name", "Ashoka Digital")
        ua = ch.get("user_agent", "")

        if not url:
            continue

        # Add user-agent if provided
        ext_opts = ""
        if ua and ua.lower() != "default":
            ext_opts = f' http-user-agent="{ua}"'

        m3u.write(
            f'#EXTINF:-1 tvg-name="{name}" '
            f'tvg-logo=https://www.ashokadigital.net/_next/image?url=https://livetv.ashokadigital.net/upload/logo/"{logo}&w=1920&q=75"'
            f'group-title="{group}",{name}\n'
        )
        m3u.write(f'{url}{ext_opts}\n')

print(f"Converted {len(posts)} channels -> {OUTPUT_M3U}")

