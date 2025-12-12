import json
import sys

def json_to_m3u(json_filename, m3u_filename):
    """
    Converts a JSON playlist file to an M3U playlist file.
    """
    try:
        with open(json_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {json_filename} was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file {json_filename}.")
        sys.exit(1)

    if not isinstance(data, list):
        print("Error: JSON data should be a list of track objects.")
        sys.exit(1)

    with open(m3u_filename, 'w', encoding='utf-8') as f:
        # Write the M3U header
        f.write("#EXTM3U\n")

        for track in data:
            try:
                title = track['title']
                url = track['url']
                # Use the 'duration' if available, otherwise default to -1 (unknown)
                duration = track.get('duration', -1) 
                
                # Write the #EXTINF line
                f.write(f"#EXTINF:{duration},{title}\n")
                # Write the track URL
                f.write(f"{url}\n")
            except KeyError as e:
                print(f"Warning: Missing key {e} in one of the track entries. Skipping.")
                continue

    print(f"Successfully converted '{json_filename}' to '{m3u_filename}'.")

if __name__ == "__main__":
    # Define input and output filenames
    input_json = 'playlist.json'
    output_m3u = 'output_playlist.m3u'
    
    json_to_m3u(input_json, output_m3u)
