import json

def json_to_m3u("playlist.json", "playlist.m3u"):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(m3u_file, 'w', encoding='utf-8') as m3u:
        m3u.write("#EXTM3U\n")

        for item in data:
            title = item.get("title", "Unknown")
            url = item.get("url", "")
            tvg_id = item.get("tvg-id", "")
            tvg_logo = item.get("tvg-logo", "")
            group = item.get("group", "")

            m3u.write(
                f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-logo="{tvg_logo}" group-title="{group}",{title}\n'
            )
            m3u.write(f"{url}\n\n")

    print(f"Created: {m3u_file}")


# Example usage:
json_to_m3u("playlist.json", "playlist.m3u")
