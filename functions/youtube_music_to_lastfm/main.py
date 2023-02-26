import json
import os
import time
# import functions_framework
from ytmusicapi import YTMusic
import pylast
import hashlib
try:
    # pip install python-dotenv
    from dotenv import load_dotenv
    load_dotenv()
except Exception as e:
    print(e)
    pass

API_KEY = os.environ.get("LASTFM_API_KEY")
API_SECRET = os.environ.get("LASTFM_API_SECRET")

username = os.environ.get("LASTFM_USERNAME")
password_hash = pylast.md5(os.environ.get("LASTFM_PASSWORD"))
assert API_KEY, "LASTFM_API_KEY is not set"


# check headers.json is here
if not os.path.exists("headers.json"):
    print("headers.json not found, please run the setup script")
    exit(1)

# Triggered from a message on a Cloud Pub/Sub topic.
# @functions_framework.cloud_event
def youtubee(_, __):
    ytmusic = YTMusic(auth=f"headers.json")
    history = ytmusic.get_history()
    # filter by 'played' = today
    history = [x for x in history if x["played"] == "Today"]

    print(f"Logging in as {username}...")
    network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=username,
        password_hash=password_hash,
    )

    lastfm_user = network.get_user(username)
    last_scrobble = list(lastfm_user.get_recent_tracks(limit=999))

    # merge in one set with id hash of title+artist
    existing_tracks = {}
    new_tracks = {}
    for s in last_scrobble:
        h = hash(f"{s.track.title}{s.track.artist}".encode("utf-8"))
        existing_tracks[h] = (s.track.title, str(s.track.artist))

    for track in history:
        h = hash(f"{track['title']}{track['artists'][0]['name']}".encode("utf-8"))
        if h in existing_tracks:
            print(f"Skipping {track['title']} - {track['artists'][0]['name']}")
            continue
        new_tracks[h] = (track["title"], track["artists"][0]["name"])
    
    # print("existing tracks:", existing_tracks)
    # print("new tracks:", new_tracks)
    # return
    print("Scrobbling...")
    for track in new_tracks.values():
        artist = track[1]
        title = track[0]
        timestamp = int(time.time())
        print(f"Scrobbling {artist} - {title} at {timestamp} to {lastfm_user}...")
        # network.scrobble(artist=artist, title=title, timestamp=timestamp)

    print("Done!")

youtubee(None, None)
