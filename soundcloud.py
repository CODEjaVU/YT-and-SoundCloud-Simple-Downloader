import requests
from bs4 import BeautifulSoup

playlist_url = 'https://soundcloud.com/quang-vu-nguyen-623507723/sets/piano?si=9c7c93413efc46d184dbbe09d547fdb7' # replace with the URL of the SoundCloud playlist you want to download
response = requests.get(playlist_url)

soup = BeautifulSoup(response.text, 'html.parser')

# find the download link of each track in the playlist
for track in soup.find_all('li', {'class': 'trackList__item'}):
    print('Downloading track')
    title = track.find('a', {'class': 'trackItem__trackTitle'}).text.strip()
    artist = track.find('a', {'class': 'trackItem__username'}).text.strip()
    download_link = track.find('a', {'class': 'sc-link-download'})['href']

    # download the track
    filename = f"{artist} - {title}.mp3"
    response = requests.get(download_link)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {filename}")
