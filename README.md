# Spotify Controller

I never used to like songs on Spotify but directly put them into playlists. I figured I never like to listen to songs from different genres at the same time so I would never listen to my "Liked Songs" playlist. But I think liking songs improves the suggestions that Spotify gives (not sure if this is true though).

Now, I have the classic developers dilema. Do I do this task manually in 30 mins or spend an afternoon (or admittedly longer) building a way to automate this. As with all things I initially decided the more complicated route.

I noticed that the Spotify API does not have an end point for liking tracks so I had a few ideas:
 - Build a browser extension to control safari. However I have recently moved to macOS and I'm still climbing that learning curve.
 - Use Selenium and Python to automate a browser session. I kept hitting walls on this and again realised the learning curve was more than I was willing to put in for "30 mins" manual work.
 - Eventually, I realised adding songs to "Saved tracks" was the same as liking songs. This is possible via the Spotify API.

## Spotipy like all songs in playlist

This script allows you to like all the songs that are in your private and collaborative playlists. It primarily uses the [spotipy](https://spotipy.readthedocs.io/en/2.17.1/) library which is a thin wrapper over the [Spotify Web API](https://developer.spotify.com/documentation/web-api/).

Requirements for this to work:
 - Create an appp in the Spotify developer dashboard
 - Make the REDIRECT_URI https://localhost
 - Put your CLIENT_ID and CLIENT_SECRETE in a config.py (see example)
 - Follow the links from the terminal when prompted
 
 
 ## Spotipy unlike songs from playlist
 
 This scripts allows you to unlike all the songs from a specific playlist. The name of the playlist must be valid for the currently logged in user. You only need to authenticate once so this script used work if you followed the steps above for the first script.
 
