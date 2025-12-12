import json
import os

def json_to_m3u(json_file_path = "playlist.json", m3u_file_path ="playlist.m3u"):
    """
    Converts a JSON playlist file to an M3U playlist file.
    """
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {json_file_path} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {json_file_path}.")
        return

    if not isinstance(data, list):
        print("Error: JSON data should be a list of tracks.")
        return

    with open(m3u_file_path, 'w') as f:
        # M3U extended format header
        f.write("#EXTM3U\n")

        for track in data:
            title = track.get("title", "Unknown Title")
            runtime = track.get("runtime", -1)
            path = track.get("path")

            if path:
                # Write the extended info line
                f.write(f"#EXTINF:{runtime},{title}\n")
                # Write the file path line
                f.write(f"{path}\n")
            else:
                print(f"Warning: Missing 'path' for track '{title}'. Skipping.")

    print(f"Successfully converted '{json_file_path}' to '{m3u_file_path}'.")

# --- Usage Example ---
# Define input and output file names
input_json = "playlist.json"
output_m3u = "playlist.m3u"

# Run the conversion
json_to_m3u(input_json, output_m3u)
