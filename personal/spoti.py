import requests, os, sys, time, spotipy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from spotipy.oauth2 import SpotifyClientCredentials

#Spotify setup
cid = "9441f3abd73b4ae8afbc212a1766dbdd"
secret = "29904f1fa1c14a68afc2e9e6dc05e174"
playlist = input("Enter Playlist URL: ")
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
playlist_URI = playlist.split("/")[-1].split("?")[0]
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#Setup driver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Create download folder in current wd
parent_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
path = os.path.join(parent_dir, "Playlist")
os.mkdir(path)

#Get playlist
songlist = []
for track in sp.playlist_tracks(playlist_URI)["items"]:
    track_name = track["track"]["name"]
    artist_name = track["track"]["artists"][0]["name"]
    songlist.append(artist_name + ' - ' + track_name)

#Loop over songs, acces myfreemp3, search, get href of first result, acces href
n = 0
for i in songlist:
    browser.get("https://myfreemp3juices.cc/") 
    query = browser.find_element(By.ID, 'query')
    query.send_keys(i)
    query.send_keys(Keys.ENTER)
    time.sleep(2)
    a = browser.find_elements(By.CLASS_NAME, 'name')
    if a:
        href = a[0].get_attribute('href')
        time.sleep(1)
        r = requests.get(href)  
        with open(os.path.join(path, i + ".mp3"), 'wb') as f:
            f.write(r.content)
        n += 1
    
browser.quit()
print('Finished. Number of downloaded songs:', str(n), 'Missed:', str(len(songlist) - n))