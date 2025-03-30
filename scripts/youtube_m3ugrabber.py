import requests
import os
import sys

def grab():
    response = requests.get('https://www.youtube.com/@euronewshu/live').text
    if '.m3u8' not in response:
        print('bad')
    else:
        a=response.split('"')
        for line in a:
            if line.endswith("index.m3u8"):
                print(line)

print('#EXTM3U')
print('#EXTINF:-1')
grab()
