from pytube import Playlist, YouTube
import os

# Replace 'YOUR_PLAYLIST_URL' with the actual URL of the YouTube playlist you want to download
playlist_url = 'https://youtube.com/playlist?list=PLt1MjqWQPImEhLdNWrBOX3m6hE0XDI0ph'
output_dir="C:\j7 file\Projects\Python-based downloader\ytmusic"

# Create a Playlist object and retrieve the video URLs
playlist = Playlist(playlist_url)
video_urls = playlist.video_urls

# Download each video as an mp3 file
for video_url in video_urls:
    
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    output_file = stream.download(output_path=output_dir)
    base, ext = os.path.splitext(output_file)
    new_file = base + '.mp3'
    print("Downloading"+new_file)
    os.rename(output_file, new_file)
