import json
#channels = data.get("channeldata",[])
with open("channels.json", "r", encoding="utf-8") as f:
    channels = json.load(f)

with open("output.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for ch in channels("channeldata"):
        name = ch.get("name", "")
        url = ch.get("url", "")
        logo = ch.get("logo", "")
        group = ch.get("group", "")

        f.write(
            f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n'
        )
        f.write(url + "\n")
