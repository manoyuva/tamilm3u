import json

def json_to_m3u(json_file, m3u_file="playlist.m3u"):
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

    print(f"✔ M3U created: {m3u_file}")


json_to_m3u("channels.json", "playlist.m3u")
