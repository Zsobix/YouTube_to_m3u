import requests
import os
import time

print('#EXTM3U')
print('#EXTINF:-1')
time.sleep(1)
os.system("yt-dlp -g 'https://www.youtube.com/@euronewshu/live' --cookies cookies.firefox-private.txt"
