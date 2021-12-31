import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
cid = '5410e774c83040bb85936efc4672828a'
secret = 'e893db8c750a439489d6a8c11560e470'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
token = 'BQBM5OrZgJUgas4LosYfq_kH6JxDe9q8TofjhPoA1T6KY_WA9wIIkEumg-8sT4kdpGvaPj1pELBFklY40qRci7Z99tp8x_ACkF5sogjTMb-ny6XwXqr48xmG9JX7Ei5TtJoBiRDkFAumWkQUAiWAPomYEoJAtME'
spotify = spotipy.Spotify(token)

def get_track_name(trackId):
    return spotify.track(trackId)['name']

def get_acoustic_feature(trackId, featureName):
    return spotify.audio_features(trackId)[0][featureName]

# labelled dataset
dataset = [{"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"}, 
       {"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"},
       {"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"},
       {"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"},
       {"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"}]

# return data as [genre, track_name, track_id, acousticness, danceability, energy, instrumentalness,
# key, liveness, loudness, mode, speechiness, tempo, time_signature, valence]
data = [[]]
for i in dataset:
    genre = i.get("genre")
    trackId = i.get("trackId")
    data.append([genre, get_track_name(trackId), trackId, 
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
df = pd.DataFrame(data, columns = ['genre', 'track_name', 'track_id', 'acousticness', 'danceability', 'energy',
                                   'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness',
                                   'tempo', 'time_signature', 'valence'])


print(df)