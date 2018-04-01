
# Spotify remote control

Simple remote control for spotify apps from terminal.

Project of the book [Python Programming Blueprints](https://www.packtpub.com/mapt/book/application_development/9781786468161?utm_source=all%20updates&utm_campaign=a532fdc6a6-Mapt_new_title_releases_25_01_18&utm_medium=email&utm_term=0_c970747b22-a532fdc6a6-169822065&mc_cid=a532fdc6a6&mc_eid=b722ebf882)

## Improviments 
 - Erro handler using curses panels
 - Bootstrap for html autorize page

## Install

pip install -r requirements.txt

## Run

In order to make Spotify Terminal client work properly,  you should grant special rights to it, so first launch spotify_auth and autorize the 
app

### Create a Spotify APP:
    - https://beta.developer.spotify.com/dashboard/applications
    - Edit settings and put http://localhost:3000/callback in Redirect URIs field

### Authorize app 
python spotify_auth.py and access http://localhost:3000

### launch remote control

python app.py

*Tips: you may need a premium account to work properly. Spotify need be running into some device and playing some music..

## Commands
 - Search: F2
 - Exit: ctrl + c or "q"

 ## Others

[![Youtube Video Demonstration](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=EfJIJ_9e8vQ)
