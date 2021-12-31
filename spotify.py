import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
cid = '5410e774c83040bb85936efc4672828a'
secret = 'e893db8c750a439489d6a8c11560e470'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
token = 'BQBYqofDMpjIBUNNQJqdUGAb0YER67vIRhaC6a8-VaJT1QW5hrITxErItbDtUK9q29-2FBWR7lfz0nEeqmdF2UbJlGwNcYRHnl2lLll3AjIEaBz4MOnifkl0hBa516NHhNqrYJ5ARcVGMntxowY0smJJzXz688A'
spotify = spotipy.Spotify(token)

def get_track_name(trackId):
    return spotify.track(trackId)['name']

def get_acoustic_feature(trackId, featureName):
    return spotify.audio_features(trackId)[0][featureName]

def get_track_artist(trackId):
    return spotify.track(trackId)['album']['artists'][0]['name']

# labelled dataset
dataset = [{"genre": "eerie", "trackId" : "3Ot8c1sAmARXl31ZckeMDR"}, 
       {"genre": "eerie", "trackId" : "4Sf5gXjMvciYzNGSrQx7BK"},
       {"genre": "eerie", "trackId" : "1dpnCy0Oa9V02tfNo6KIzp"},
       {"genre": "eerie", "trackId" : "3n69hLUdIsSa1WlRmjMZlW"},
       {"genre": "eerie", "trackId" : "3cKLaUSHmIW66lbEkpGDTX"},
       {"genre": "eerie", "trackId" : "4mBA0FHbLRbGXAqQJBepUb"},
       {"genre": "eerie", "trackId" : "4Adp5ixl3CJLBkCxGZWGUC"},
       {"genre": "gritty", "trackId" : "441TUCOSya3kCQR1yeBxqH"},
       {"genre": "gritty", "trackId" : "1oXaJxH9fv7dReSU99RPhg"},
       {"genre": "gritty", "trackId" : "6RHHbAbyIcPpvS1dP3KUGq"},
       {"genre": "melancholy", "trackId" : "4CiqKccFFYGmFPz7HVTjfW"},
       {"genre": "melancholy", "trackId" : "1fvRueeK5f60hkG1VzoXXq"},
       {"genre": "melancholy", "trackId" : "4AmcmraFjVzFb9SQDNTRyl"},
       {"genre": "melancholy", "trackId" : "15Ax8eHs3aH9MCFcIERDp8"},
       {"genre": "melancholy", "trackId" : "2v4lwSzPGMG2G8DOLSinuK"},             
       {"genre": "melancholy", "trackId" : "3C3YNkWdulBcyKGShi0v8q"},
       {"genre": "melancholy", "trackId" : "0yc6Gst2xkRu0eMLeRMGCX"},
       {"genre": "peaceful", "trackId" : "7mcM8OVEmqyTbUvO1in0oZ"},
       {"genre": "peaceful", "trackId" : "7K6LFPfjdnN6QqvGzhvpRO"},
       {"genre": "peaceful", "trackId" : "3pGTGFLKTGFOLArMq3H9jE"},
       {"genre": "peaceful", "trackId" : "1g2eirb8uaYn54iEYZl3CS"},
       {"genre": "peaceful", "trackId" : "1boXOL0ua7N2iCOUVI1p9F"},
       {"genre": "peaceful", "trackId" : "7iBSkXB0pTvZasOLf0Qxk9"},
       {"genre": "hopeful", "trackId" : "4kP7BPJ1d3WUGhykQBVEjH"},
       {"genre": "hopeful", "trackId" : "3g9mw4A8vdljOKgwrit88g"},
       {"genre": "hopeful", "trackId" : "5uIYONgpUQ7t0v7D6CTMBt"},
       {"genre": "hopeful", "trackId" : "7D49Iig0avHre9RFSUMkd2"},
       {"genre": "hopeful", "trackId" : "79irqIr5JmGSHeLtu8tntd"},
       {"genre": "hopeful", "trackId" : "6KuHjfXHkfnIjdmcIvt9r0"},
       {"genre": "hopeful", "trackId" : "6cMswWRv4lAU3mh5lclgCc"},
       {"genre": "dystopia", "trackId" : "1Fwj0wThn3kTg8D7KgWdsU"},
       {"genre": "dystopia", "trackId" : "26fVjoeuhEAsAxmPzfTRIo"},
       {"genre": "dystopia", "trackId" : "0boS4e6uXwp3zAvz1mLxZS"},
       {"genre": "dystopia", "trackId" : "4vWeIrIQQrbThS11ogLTmu"},
       {"genre": "dystopia", "trackId" : "6zLq4lYSu2W7LLxJlUWzz8"},
       {"genre": "dystopia", "trackId" : "416MsJxvxSKY96DCmbJIRs"},
       {"genre": "light_academia", "trackId" : "657XjY28KTNbkgkKxN4xtN"},
       {"genre": "light_academia", "trackId" : "7LRAg8a4Q5PrPHSGBfng22"},
       {"genre": "light_academia", "trackId" : "4w0sBSIgy945h7TZE0FUbc"},
       {"genre": "light_academia", "trackId" : "3tJjZMHLqhD8DaGgdBICnc"},
       {"genre": "light_academia", "trackId" : "1HYnjKqSSHh1tdl2Hi57zH"},
       {"genre": "light_academia", "trackId" : "0MNNKSUU9OOQ8DSGWduw79"},
       {"genre": "light_academia", "trackId" : "4k7x3QKrc3h3U0Viqk0uop"},
       {"genre": "dark_academia", "trackId" : "4NZKQIAbpUPd0jn0CzvRpS"},
       {"genre": "dark_academia", "trackId" : "22TntnVO3lQNDR5nsvxGRs"},
       {"genre": "dark_academia", "trackId" : "7xfSCgVOkQJhVxnqzepATH"},
       {"genre": "dark_academia", "trackId" : "7otCGmgp9h4CsR2LhwB6gt"},
       {"genre": "dark_academia", "trackId" : "6V46LfMpdJWfhDImW2JT7t"},
       {"genre": "dark_academia", "trackId" : "1UWhx0pFZccP4jdCIZsj7U"},
       {"genre": "dark_academia", "trackId" : "6EfZCB2wudriyD1vDjuAZ9"},
       {"genre": "epic", "trackId" : "0ZUMBOzlwNXfVE4Z8lSrsd"},
       {"genre": "suspense", "trackId" : "1NUHxg3L7gEvXk4b7Oj93r"},
       {"genre": "suspense", "trackId" : "2mkv1b3dRFyiJ4Ybq31owf"},
       ]

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