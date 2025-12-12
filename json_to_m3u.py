import json

def json_to_m3u(json_file="channels.json", m3u_file="tamilott.m3u"):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    channels = data.get("channeldata", [])

    with open(m3u_file, "w", encoding="utf-8") as m3u:
        m3u.write("#EXTM3U\n")

        for ch in channels:
            name = ch.get("channelname", "Unknown")
            logo = ch.get("logo", "")
            url = ch.get("playbackurl", "")

            if not url:
                continue  # skip channels without stream URL

            m3u.write(
                f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}" group-title="India",{name}\n'
            )
            m3u.write(url + "\n")

    print(f"✔ M3U file created: {m3u_file}")


# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    json_to_m3u("channels.json", "channels.m3u")
