import json
#channels = data.get("channeldata",[])
with open("channels.json", "r", encoding="utf-8") as f:
    channels = json.load(f)

with open("output.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for ch in channels:
        name = ch.get("channeldata","name", "")
        url = ch.get("channeldata","url", "")
        logo = ch.get("channeldata","logo", "")
        group = ch.get("channeldata","group", "")

        f.write(
            f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n'
        )
        f.write(url + "\n")
