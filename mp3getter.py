from pytube import YouTube
import os

# Define the video URL and output directory
video_url = 'https://youtu.be/MiRzzGoYSx4'
output_dir = 'C:\j7 file\Projects\Python-based downloader\ytmusic'

# Create a YouTube object and retrieve the audio stream
yt = YouTube(video_url)
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream and save as an MP3 file
output_file = audio_stream.download(output_path=output_dir)
base, ext = os.path.splitext(output_file)
new_file = base + '.mp3'
os.rename(output_file, new_file)
