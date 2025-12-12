import json
import sys

def json_to_m3u(json_file, m3u_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    channels = data.get("channeldata", [])

    with open(m3u_file, "w", encoding="utf-8") as m3u:
        m3u.write("#EXTM3U\n")

        for ch in channels:
            name = ch.get("channelname", "Unknown")
            logo = ch.get("logo", "")
            url = ch.get("playbackurl", "")
            group = ch.get("area", "")

            if not url:
                continue

            m3u.write(
                f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}" group-title="{group}",{name}\n'
            )
            m3u.write(url + "\n")


if __name__ == "__main__":
    json_to_m3u(sys.argv[1], sys.argv[2])
