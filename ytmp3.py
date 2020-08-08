from __future__ import unicode_literals
from pytube import Playlist, YouTube
import re
import youtube_dl

url = 'https://www.youtube.com/playlist?list=PLO5y_0J9rFCQRF5WOBW2P2hrajFiKAHa1'

playlist = Playlist(url)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))
for url in playlist.video_urls:
    print(url)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': False,
    'outtmpl': 'downloads/%(title)s.%(ext)s'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for url in playlist.video_urls:
        ydl.download([url])

