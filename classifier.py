from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB  
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from math import floor
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import neighbors
# from spotify import get_track_name, get_acoustic_feature


# preprocess data

# load dataset
df = pd.read_csv(r'.\datset.csv', index_col=False)
# drop columns
df = df.drop(['Unnamed: 0','track_name','track_id', 'artist'], axis=1)
df = df.drop(df.index[0])

# numerically encode genres
# genre_map = {"eerie":1,
#             "gritty":2,
#             "melancholy":3,
#             "peaceful":4,
#             "hopeful":5,
#             "adventure":6,
#             "dystopia":7,
#             "light_academia":8,
#             "gothic":9,
#             "epic":10,
#             "battle":11,
#             "suspense":12,
#             "dreamy":13,
#             "elegant":14,
#             "sensual":15,
#             "ethereal":16,
#             "tragedy":17,
#             "sentimental":18,
#             "urban":19,
#             "romance":20,
#             "slice_of_life":21,
#             "coming_of_age":22,
#             "cyberpunk":23,
#             "supernatural":24,
#             "eccentric":25}
genre_map = {"eerie":101,
            "suspense":102,
            "battle":103,
            "epic":201,
            "adventure":202,
            "hopeful":203,
            "peaceful":301,
            "slice_of_life":302,
            "coming_of_age":303,
            "elegant":304,
            "dystopia":401,
            "tragedy":402,
            "gritty":403,
            "gothic":404,
            "melancholy":501,
            "sentimental":502,
            "eccentric":601,
            "supernatural":602,
            "urban":701,
            "cyberpunk":702,
            "dreamy":801,
            "ethereal":802,
            "romance":901,
            "sensual":902,
            "light_academia":25}
df = df.replace(genre_map)

# scale numerical data
scaler = StandardScaler()
num_cols = list(df.columns)[2:]
df[num_cols] = scaler.fit_transform(df[num_cols])

# split dataset for training and testing
feature = df.drop(['genre','mode','key'], axis=1)
target = df['genre']
print(target)
# Set Training and Testing Data as 9:1
X_train, X_test, y_train, y_test = train_test_split(feature , target, 
                                                    shuffle = True, 
                                                    test_size=0.1, 
                                                    random_state=1)
# Show the Training and Testing Data
print('Shape of training feature:', X_train.shape)
print('Shape of testing feature:', X_test.shape)
print('Shape of training label:', y_train.shape)
print('Shape of training label:', y_test.shape)

#Building KNN model, using k=5 neighbours
# classifier = neighbors.KNeighborsClassifier(n_neighbors=5,n_jobs=-1)

# Naive Bayes algorithm
#classifier = GaussianNB()  
#Random forest
classifier = RandomForestClassifier(random_state=42, n_jobs=-1, max_depth=5,
                                       n_estimators=100, oob_score=True)

classifier.fit(X_train, y_train)  
#Predict the model with the test data




y_preds = classifier.predict(X_test)
y_preds = (y_preds[y_preds>0]/100).astype(int)
y_test = (y_test[y_test>0]/100).astype(int)
print("Real", y_test)
print("Predicted", y_preds)

# Analysis
#Create the confusion matrix using test data and predictions
print(metrics.confusion_matrix(y_test, y_preds))
print(metrics.classification_report(y_test, y_preds))

# Uses a new song's trackId and genre(provided by user), adds them to the dataframe, and then partialfits
# def fitnewsong(trackId, genre):
#     df.loc[len(df.index)] = [genre,get_acoustic_feature(trackId, 'acousticness'),
#         get_acoustic_feature(trackId, 'danceability'),
#         get_acoustic_feature(trackId, 'energy'),
#         get_acoustic_feature(trackId, 'instrumentalness'),
#         get_acoustic_feature(trackId, 'liveness'),
#         get_acoustic_feature(trackId, 'loudness'),
#         get_acoustic_feature(trackId, 'speechiness'),
#         get_acoustic_feature(trackId, 'tempo'),
#         get_acoustic_feature(trackId, 'time_signature'),
#         get_acoustic_feature(trackId, 'valence')           
#        ]
#     feature = df.drop(['genre'], axis=1)
#     target = df['genre'] 
#     knn.partial_fit(feature[-1:], target[-1:])
print(df)