import json
import sys

def convert_json_to_m3u(json_file_path ='playlist.json', m3u_file_path = 'playlist.m3u'):
    """
    Converts a JSON playlist file to an M3U playlist file.

    Args:
        json_file_path (str): Path to the input JSON file.
        m3u_file_path (str): Path to the output M3U file.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not isinstance(data, list):
            print("Error: JSON data should be a list of stream objects.", file=sys.stderr)
            return

        with open(m3u_file_path, 'w', encoding='utf-8') as f:
            f.write("#EXTM3U\n") # M3U playlist header

            for stream in data:
                # Basic validation for required fields
                if 'title' in stream and 'url' in stream:
                    # M3U extended format line (#EXTINF) and the stream URL line
                    # -1 runtime indicates an indefinite duration stream (common for IPTV)
                    f.write(f"#EXTINF:-1,{stream['title']}\n")
                    f.write(f"{stream['url']}\n")
                else:
                    print(f"Warning: Skipping invalid stream entry (missing 'title' or 'url'): {stream}", file=sys.stderr)

        print(f"Successfully converted '{json_file_path}' to '{m3u_file_path}'")

    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found.", file=sys.stderr)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{json_file_path}'. Check file format.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# --- Example Usage ---
if __name__ == "__main__":
    # Define your input JSON file path and desired output M3U file path
    input_json = "playlist.json"
    output_m3u = "playlist.m3u"

    convert_json_to_m3u(input_json, output_m3u)
    
