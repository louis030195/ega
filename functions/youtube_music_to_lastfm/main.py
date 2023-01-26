import json
import os
import time
# import functions_framework
from ytmusicapi import YTMusic
# from dotenv import load_dotenv
import pylast
import hashlib
# load_dotenv()

API_KEY = os.environ.get("LASTFM_API_KEY")
API_SECRET = os.environ.get("LASTFM_API_SECRET")

username = os.environ.get("LASTFM_USERNAME")
password_hash = pylast.md5(os.environ.get("LASTFM_PASSWORD"))
assert API_KEY, "LASTFM_API_KEY is not set"


# Triggered from a message on a Cloud Pub/Sub topic.
# @functions_framework.cloud_event
def youtubee(_, __):
    ytmusic = YTMusic(auth=f"headers.json")
    history = ytmusic.get_history()

    print(f"Logging in as {username}...")
    network = pylast.LastFMNetwork(
        api_key=API_KEY,
        api_secret=API_SECRET,
        username=username,
        password_hash=password_hash,
    )

    lastfm_user = network.get_user(username)
    last_scrobble = list(lastfm_user.get_recent_tracks())

    # merge in one set with id hash of title+artist
    unique_tracks = {}
    for track in history:
        h = hashlib.sha256()
        hh = h.update(f"{track['title']}{track['artists'][0]['name']}".encode("utf-8"))
        unique_tracks[hh] = (track["title"], track["artists"][0]["name"])
    for s in last_scrobble:
        h = hashlib.sha256()
        hh = h.update(f"{s.track.title}{s.track.artist}".encode("utf-8"))
        unique_tracks[hh] = (s.track.title, s.track.artist)

    print("Scrobbling...")
    for track in unique_tracks.values():
        artist = track[1]
        title = track[0]
        timestamp = int(time.time())
        print(f"Scrobbling {artist} - {title} at {timestamp} to {lastfm_user}...")
        network.scrobble(artist=artist, title=title, timestamp=timestamp)

    print("Done!")
