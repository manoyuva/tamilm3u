import json
import sys

def convert_json_to_m3u(json_file_path, m3u_file_path):
    """
    Converts a JSON playlist file to an M3U playlist file.

    Assumes the JSON format is a list of objects like:
    [
        {"title": "Song Title 1", "runtime": 105, "path": "/path/to/song1.mp3"},
        {"title": "Song Title 2", "runtime": 321, "path": "/path/to/song2.ogg"}
    ]
    """
    try:
        # 1. Read and parse the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print("Error: JSON data should be a list of tracks.", file=sys.stderr)
            return

        # 2. Format the data into M3U lines
        m3u_lines = ["#EXTM3U"] # M3U header
        for track in data:
            title = track.get("channelname", "Unknown Title")
            runtime = track.get("logo", -1) # Use -1 if runtime is missing
            path = track.get("playbackurl", "")

            if path:
                # M3U extended format line: #EXTINF:<runtime>,<display_title>
                extinf_line = f"#EXTINF:{runtime},{title}"
                m3u_lines.append(extinf_line)
                m3u_lines.append(path)
        
        # 3. Write the lines to the M3U file
        with open(m3u_file_path, 'w', encoding='utf-8') as f:
            for line in m3u_lines:
                f.write(line + '\n')

        print(f"Successfully converted '{json_file_path}' to '{m3u_file_path}'")

    except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.", file=sys.stderr)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file {json_file_path}.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Example usage:
# Define your input JSON file path and output M3U file path
input_json = 'data/tamilott.json'
output_m3u = 'data/playlists/my_playlist.m3u'

# Run the conversion function
if __name__ == "__main__":
    convert_json_to_m3u(input_json, output_m3u)
    
