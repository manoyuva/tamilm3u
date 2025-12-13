import json

"""
Custom JSON to M3U converter for OTT-style JSON
(Supports `channeldata` array inside each content object)
"""

INPUT_JSON = "channels.json"
OUTPUT_M3U = "output.m3u"

with open(INPUT_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(OUTPUT_M3U, "w", encoding="utf-8") as m3u:
    m3u.write("#EXTM3U\n")

    for content in data:
        group = content.get("content_title", "OTT")
        country = content.get("content_sub_title", "")

        channels = content.get("channeldata", [])
        for ch in channels:
            name = ch.get("channelname", "Unknown")
            url = ch.get("playbackurl", "")
            logo = ch.get("logo", "")
            ch_country = ch.get("area", country)

            m3u.write(
                f'#EXTINF:-1 tvg-name="{name}" '
                f'tvg-logo="{logo}" '
                f'tvg-country="{ch_country}" '
                f'group-title="{group}",{name}\n'
            )
            m3u.write(f"{url}\n")

print("JSON successfully converted to M3U")

