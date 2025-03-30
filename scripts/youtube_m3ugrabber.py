import requests
import os
import time

a = os.system("yt-dlp -g 'https://www.youtube.com/@euronewshu/live' --cookies cookies.firefox-private.txt")
print('#EXTM3U')
print('#EXTINF:-1')
print(a)
