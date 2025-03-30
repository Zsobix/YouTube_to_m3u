import requests
import os
import sys

print('#EXTM3U')
print('#EXTINF:-1')
print(os.system("yt-dlp -g 'https://www.youtube.com/@euronewshu/live'"))
