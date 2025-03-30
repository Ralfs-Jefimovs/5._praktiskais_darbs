import requests
import json
from urllib.parse import urlencode

# def get_spotify_access_token(client_id, client_secret):
#     url = "https://accounts.spotify.com/api/token"
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     data = {
#         "grant_type": "client_credentials"
#     }
#     response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
#     response.raise_for_status()
#     return response.json()["access_token"]

# def get_authorization_url(client_id, redirect_uri, scope):
#     url = "https://accounts.spotify.com/authorize"
#     params = {
#         "client_id": client_id,
#         "response_type": "code",
#         "redirect_uri": redirect_uri,
#         "scope": scope
#     }
#     return f"{url}?{urlencode(params)}"

# def get_access_token_with_auth_code(client_id, client_secret, code, redirect_uri):
#     url = "https://accounts.spotify.com/api/token"
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     data = {
#         "grant_type": "authorization_code",
#         "code": code,
#         "redirect_uri": redirect_uri
#     }
#     response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
#     response.raise_for_status()
#     return response.json()["access_token"]

# def get_user_profile(access_token):
#     url = "https://api.spotify.com/v1/me"
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     return response.json()

# def get_artist_details(access_token, artist_id):
#     url = f"https://api.spotify.com/v1/artists/{artist_id}"
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     return response.json()

# CLIENT_ID = "d847e720143541b780f3ace76ddc0a46"
# CLIENT_SECRET = "229762102f4e408fa97fee06c1b21e10"
# REDIRECT_URI = "https://oauth.pstmn.io/v1/callback" 
# SCOPE = "user-read-private user-read-email"

if __name__ == "__main__":
    # Simple Spotify API call to fetch track details
    CLIENT_ID = "d847e720143541b780f3ace76ddc0a46"
    CLIENT_SECRET = "229762102f4e408fa97fee06c1b21e10"
    
    # Step 1: Get an access token using client credentials
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    response.raise_for_status()
    access_token = response.json()["access_token"]
    
    # Step 2: Use the access token to fetch track details
    track_id = "3n3Ppam7vgaVa1iaRUc9Lp"  # Example: "Mr. Brightside" by The Killers
    track_url = f"https://api.spotify.com/v1/tracks/{track_id}"
    track_headers = {
        "Authorization": f"Bearer {access_token}"
    }
    track_response = requests.get(track_url, headers=track_headers)
    track_response.raise_for_status()
    track_details = track_response.json()
    
    # Step 3: Remove "available_markets" from the track details
    if "available_markets" in track_details:
        del track_details["available_markets"]
    
    # Step 4: Print the filtered track details
    print(json.dumps(track_details, indent=4))

