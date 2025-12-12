import json

def json_to_m3u(json_file="channels.json", m3u_file="channels.m3u", default_group="India"):
    """Convert a JSON playlist file to an M3U playlist file."""

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    channels = data.get("channels", [])

    with open(m3u_file, "w", encoding="utf-8") as m3u:
        m3u.write("#EXTM3U\n")

        for ch in channels:
            name = ch.get("name", "Unknown")
            logo = ch.get("logo", "")
            url = ch.get("url", "")
            group = ch.get("group", default_group)

            if not url:
                continue  # skip channels with no URL

            m3u.write(
                f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}" group-title="{group}",{name}\n'
            )
            m3u.write(url + "\n")

    print(f"✔ M3U file created: {m3u_file}")
