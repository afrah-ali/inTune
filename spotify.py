import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
cid = '5410e774c83040bb85936efc4672828a'
secret = 'e893db8c750a439489d6a8c11560e470'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
token = 'BQD_t96THKx75LImnD5rUuBZA-d1Kwgk-R7ERzH4hjBkP8iXHUdYRu7AtU4SJ835pv94PjfFDloE3GIq19ImP9keuxYRBkVS9bXS_yyshNQGYyR69N-Ea5Tcv_LY96mj5HAuGAqyAmKbM-nPOFP0h9Dg42iEPN0'
spotify = spotipy.Spotify(token)

def get_track_name(trackId):
    return spotify.track(trackId)['name']

def get_acoustic_feature(trackId, featureName):
    return spotify.audio_features(trackId)[0][featureName]

def get_track_artist(trackId):
    return spotify.track(trackId)['album']['artists'][0]['name']

# labelled dataset
dataset = [{"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"}, 
       {"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"},
       {"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"},
       {"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"},
       {"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"}]

# return data as [genre, track_name, artist, track_id, acousticness, danceability, energy, instrumentalness,
# key, liveness, loudness, mode, speechiness, tempo, time_signature, valence]
data = [[]]
for i in dataset:
    genre = i.get("genre")
    trackId = i.get("trackId")
    data.append([genre, get_track_name(trackId), get_track_artist(trackId), trackId,
        get_acoustic_feature(trackId, 'acousticness'),
        get_acoustic_feature(trackId, 'danceability'),
        get_acoustic_feature(trackId, 'energy'),
        get_acoustic_feature(trackId, 'instrumentalness'),
        get_acoustic_feature(trackId, 'key'),
        get_acoustic_feature(trackId, 'liveness'),
        get_acoustic_feature(trackId, 'loudness'),
        get_acoustic_feature(trackId, 'mode'),
        get_acoustic_feature(trackId, 'speechiness'),
        get_acoustic_feature(trackId, 'tempo'),
        get_acoustic_feature(trackId, 'time_signature'),
        get_acoustic_feature(trackId, 'valence')           
       ])

# create pandas DataFrame
df = pd.DataFrame(data, columns = ['genre', 'track_name', 'artist','track_id', 'acousticness', 'danceability', 'energy',
                                   'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness',
                                   'tempo', 'time_signature', 'valence'])


print(df)