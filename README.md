# Spotify Controller

## Like all songs in playlist

This script allows you to like all the songs that are in your private and collaborative playlists. It primarily uses the [spotipy](https://spotipy.readthedocs.io/en/2.17.1/) library which is a thin wrapper over the [Spotify Web API](https://developer.spotify.com/documentation/web-api/).

Requirements for this to work:
 - Create an app in the Spotify developer dashboard
 - Make the `REDIRECT_URI` `https://localhost`
 - Put your `CLIENT_ID` and `CLIENT_SECRET` in a `config.py` (see example)
 - Follow the links from the terminal when prompted
 
## Unlike songs from playlist

This scripts allows you to unlike all the songs from a specific playlist. The name of the playlist must be valid for the currently logged in user. You only need to authenticate once so this script should work if you followed the steps above for the first script.
 
