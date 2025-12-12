import json

def json_to_m3u(json_file="playlist.json", m3u_file="play.m3u"):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(m3u_file, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")

        # Case 1: list of strings
        if isinstance(data, list) and all(isinstance(item, str) for item in data):
            for url in data:
                f.write(f"#EXTINF:-1,{url}\n{url}\n")

        # Case 2: list of objects
        elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
            for item in data:
                name = item.get("name", "Unknown")
                url = item.get("url", "")
                if url:
                    f.write(f"#EXTINF:-1,{name}\n{url}\n")

        else:
            print("Unsupported JSON structure.")

    print(f"M3U file created: {m3u_file}")
    
