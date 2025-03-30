import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# Spotify API credentials
CLIENT_ID = "d847e720143541b780f3ace76ddc0a46"
CLIENT_SECRET = "229762102f4e408fa97fee06c1b21e10"
REDIRECT_URI = "https://oauth.pstmn.io/v1/callback"

# Initialize SpotifyOAuth with updated scopes
try:
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-top-read playlist-modify-private",  # Added required scope
        show_dialog=True  # Force authentication dialog
    )

    # Retrieve and validate the access token
    token_info = auth_manager.get_access_token()
    access_token = token_info["access_token"]  # Extract the access token string
    print(json.dumps({"access_token": access_token}, indent=4))

except Exception as e:
    print(json.dumps({"error": str(e)}, indent=4))
    exit()

try:
    # Initialize Spotify client with the access token
    sp = spotipy.Spotify(auth=access_token)

    # Fetch user's top tracks
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')
    if not top_tracks['items']:
        print(json.dumps({"error": "No top tracks found for the user."}, indent=4))
        exit()

    # Format and display the top tracks
    track_ids = [track["id"] for track in top_tracks["items"]]
    user_top_tracks = [
        {
            "name": track["name"],
            "artist": ", ".join(artist["name"] for artist in track["artists"]),
            "album": track["album"]["name"],
            "popularity": track["popularity"]
        }
        for track in top_tracks["items"]
    ]

    # Debugging: Print top tracks
    print(f"Top Tracks: {json.dumps(user_top_tracks, indent=4)}")

    # Create a new playlist
    user_id = sp.me()["id"]  # Get the current user's Spotify ID
    playlist_name = "My Top 10 Tracks"
    playlist_description = "A playlist of my top 10 tracks created using Spotify API"
    playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=False,
        description=playlist_description
    )
    playlist_id = playlist["id"]
    print(f"Playlist '{playlist_name}' created with ID: {playlist_id}")

    # Add top tracks to the playlist
    sp.playlist_add_items(playlist_id, track_ids)
    print(f"Added {len(track_ids)} tracks to the playlist '{playlist_name}'.")

except Exception as e:
    print(json.dumps({"error": str(e)}, indent=4))