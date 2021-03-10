import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
import sys

scope = 'playlist-read-private, user-library-modify, user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri="https://localhost",
                                               scope=scope,
                                               open_browser=False))

def unlike_songs_from_playlist(name):
    results = sp.current_user_playlists(limit=50)
    for item in results['items']:
        if item['name'] == name:
            playlist_id = item['id']
            break


    playlist = sp.playlist(playlist_id)
    track_ids = [ track['track']['id'] for track in playlist['tracks']['items']]
    i = len(track_ids)
    j = 0
    while (i > 0):
        start = j * 50
        end = (j + 1) * 50 if i > 50 else len(track_ids)
        check_ids = track_ids[j * 50: (j + 1) * 50]
        already_saved_ids = sp.current_user_saved_tracks_contains(check_ids)
        send_ids = [ id for id, flag in zip(check_ids, already_saved_ids) if flag == True]

        j += 1
        i -= 50
        if len(send_ids) > 0:
            sp.current_user_saved_tracks_delete(tracks=send_ids)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        unlike_songs_from_playlist(sys.argv[1])
    else:
        print("Please supply one valid playlist name for the current user")