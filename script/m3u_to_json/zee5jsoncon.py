import json
import re

INPUT_M3U = "playlist/zee5.m3u"
OUTPUT_JSON = "json/zee5.json"

channels = []
current = {}

def parse_extinf(line):
    data = {}
    # Extract attributes like tvg-id="..."
    attrs = re.findall(r'(\w+(?:-\w+)*)="(.*?)"', line)
    for k, v in attrs:
        data[k] = v

    # Channel display name (after comma)
    if ',' in line:
        data['name'] = line.split(',', 1)[1].strip()
    return data

def parse_headers(header_str):
    headers = {}
    for part in header_str.split('&'):
        if '=' in part:
            k, v = part.split('=', 1)
            headers[k.lower()] = v
    return headers

with open(INPUT_M3U, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if line.startswith('#EXTINF'):
            current = parse_extinf(line)

        elif not line.startswith('#'):
            # URL line (may contain headers)
            if '|' in line:
                url, header_str = line.split('|', 1)
                current['url'] = url.strip()
                headers = parse_headers(header_str)
                if 'user-agent' in headers:
                    current['user_agent'] = headers.get('user-agent')
                if 'referer' in headers:
                    current['referer'] = headers.get('referer')
                if 'origin' in headers:
                    current['origin'] = headers.get('origin')
            else:
                current['url'] = line

            channels.append(current)
            current = {}

with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(channels, f, indent=2, ensure_ascii=False)

print(f"Converted {len(channels)} channels -> {OUTPUT_JSON}")
