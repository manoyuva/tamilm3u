import json


def json_to_m3u(input_file, output_file="data/playlists/sports_playlists.m3u"):
    """
    Converts JSON IPTV data to an M3U playlist file and extracts EPG sources.

    Args:
        input_file (str): Path to the JSON file containing channel data.
        output_file (str): Name of the M3U file to be created.
    """
    try:
        # Read JSON data from the file
        with open(input_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Extract channels data
        channels = data.get("js", {}).get("channeldata", [])
        epg_sources = set()

        # Start writing the M3U file
        with open(output_file, "w", encoding="utf-8") as m3u_file:
            m3u_file.write("#EXTM3U\n")

            for channel in channels:
                # Extract relevant data
                name = channel.get("channelname", "Unknown")
                tvg_id = channel.get("Id", "")
                group_title = channel.get("area", "Undefined")
                logo = channel.get("logo", "")
               ## url = channel.get("cmds", [{}])[0].get("url", "")
                url = channel.get("playbackurl", "")
                epg_data = channel.get("Id", [])

                # Collect EPG sources
                for epg in epg_data:
                    epg_url = epg.get("url", "")
                    if epg_url:
                        epg_sources.add(epg_url)

                # Skip if no stream URL is found
                if not url:
                    continue

                # Write EXTINF line
                extinf_line = (
                    f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{name}" '
                    f'group-title="{group_title}" tvg-logo="{logo}",{name}\n'
                )
                m3u_file.write(extinf_line)

                # Write URL line
                m3u_file.write(f"{url}\n")

        # Save EPG sources to a separate file
        if epg_sources:
            with open("epg_sources.txt", "w", encoding="utf-8") as epg_file:
                epg_file.write("\n".join(epg_sources))
            print("EPG sources saved to epg_sources.txt")

        print(f"M3U playlist saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Path to the input JSON file
    input_file = "data/tamilott.json"

    # Generate the M3U playlist and EPG sources
    json_to_m3u(input_file, "data/playlists/sports_playlists.m3u")
