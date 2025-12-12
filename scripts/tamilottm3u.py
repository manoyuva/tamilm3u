import json

with open('data/tamilott.json') as f:
    data = json.load(f)

with open('data/playlists/sports_playlists.m3u', 'w') as f:
    f.write('#EXTM3U\n')

    for channel in data:
        name = channel['channeldata']['channelname']
        chid = channel['channeldata']['Id']
        chno = channel['channeldata']['Id']
        category = channel['channeldata']['area']
        logo = channel['channeldata']['logo']
        url = channel['channeldata']['playbackurl']

        f.write(f'#EXTINF:-1 tvg-id="{chid}" tvg-chno="{chno}" group-title="{category}" tvg-logo="{logo}", {name}\n{url}\n')

print("File saved as playlist.m3u8")
