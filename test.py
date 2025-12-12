import json

def json_to_m3u("playlist.json", "playlist.m3u"):
    with open(json_file, 'r', encoding='utf-8') as f:
        channels = json.load(f)

    with open(m3u_file, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")

        for ch in channels:
            name = ch.get("name", "Unknown")
            url = ch.get("url", "")
            tvg_id = ch.get("tvg_id", "")
            tvg_logo = ch.get("tvg_logo", "")
            group = ch.get("group", "")

            f.write(f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-logo="{tvg_logo}" group-title="{group}",{name}\n')
            f.write(f"{url}\n")

    print(f"Converted {json_file} → {m3u_file} successfully!")

# Example usage
json_to_m3u("playlist.json", "playlist.m3u")
