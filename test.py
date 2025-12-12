import json

def json_to_m3u(json_file, m3u_file):
    with open("playlist.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    with open("playlist.m3u", "w", encoding="utf-8") as out:
        out.write("#EXTM3U\n")

        # Loop through groups like "DS1", "DS2"...
        for group_key in data:
            group = data[group_key]
            channels = group.get("Channels", [])

            for ch in channels:
                name = ch.get("Name", "No Name")
                logo = ch.get("Logo", "")
                url = ch.get("Url", "")

                if not url:
                    continue

                # Write EXTINF line with logo
                if logo:
                    out.write(f'#EXTINF:-1 tvg-logo="{logo}",{name}\n')
                else:
                    out.write(f"#EXTINF:-1,{name}\n")

                # Write URL
                out.write(f"{url}\n")

    print("✔ M3U file created:", m3u_file)
    
