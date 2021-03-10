import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

scope = 'playlist-read-private, user-library-modify, user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri="https://localhost",
                                               scope=scope,
                                               open_browser=False))

results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    print(item['name'])
    playlist = sp.playlist(item['id'])
    track_ids = [ track['track']['id'] for track in playlist['tracks']['items']]
    i = len(track_ids)
    j = 0
    while (i > 0):
        start = j * 50
        end = (j + 1) * 50 if i > 50 else len(track_ids)
        check_ids = track_ids[j * 50: (j + 1) * 50]
        already_saved_ids = sp.current_user_saved_tracks_contains(check_ids)
        send_ids = [ id for id, flag in zip(check_ids, already_saved_ids) if flag == False]

        j += 1
        i -= 50
        if len(send_ids) > 0:
            sp.current_user_saved_tracks_add(tracks=send_ids)