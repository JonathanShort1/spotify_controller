import requests
import urllib

CLIENT_ID = 'f0900b3b1a3141f79deb2ca0f37185c2'
CLIENT_SECRET = 'bc2c74a0a41743e1bd24991957b9c316'

AUTHORIZE = 'https://accounts.spotify.com/authorize'

code = requests.get(AUTHORIZE, {
    'client_id' : CLIENT_ID,
    'response_type' : 'code',
    'redirect_uri' : 'https://localhost',
    'scope' : 'playlist-read-private'
})

print(code)

code_url = code.url

print(code_url)
print()

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

print(auth_response_data)

# save the access token
access_token = auth_response_data['access_token']



headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'

ALL_PLAYLISTS = 'me/playlists'

playlists_req = requests.get(BASE_URL + ALL_PLAYLISTS, headers=headers)

playlists_req = playlists_req.json()

print(playlists_req)