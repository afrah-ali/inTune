from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import neighbors


# preprocess data

# load dataset
df = pd.read_csv(r'C:\Users\Afrah\Desktop\inTune\datset.csv', index_col=False)
# drop columns
df = df.drop(['Unnamed: 0','track_name','track_id', 'artist'], axis=1)
df = df.drop(df.index[0])

# numerically encode genres
genre_map = {"eerie":1,
            "gritty":2,
            "melancholy":3,
            "peaceful":4,
            "hopeful":5,
            "adventure":6,
            "dystopia":7,
            "light_academia":8,
            "gothic":9,
            "epic":10,
            "battle":11,
            "suspense":12,
            "dreamy":13,
            "elegant":14,
            "sensual":15,
            "ethereal":16,
            "tragedy":17,
            "sentimental":18,
            "urban":19,
            "romance":20,
            "slice_of_life":21,
            "coming_of_age":22,
            "cyberpunk":23,
            "supernatural":24,
            "eccentric":25}
df = df.replace(genre_map)

# scale numerical data
scaler = StandardScaler()
num_cols = list(df.columns)[2:]
df[num_cols] = scaler.fit_transform(df[num_cols])

# split dataset for training and testing
feature = df.drop(['genre', 'mode', 'key'], axis=1)
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

# Building KNN model, using k=5 neighbours
knn = neighbors.KNeighborsClassifier(n_neighbors=5,n_jobs=-1)
knn.fit(X_train, y_train)
#Predict the model with the test data
y_preds = knn.predict(X_test)
print("Real", y_test)
print("Predicted", y_preds)

# Analysis
#Create the confusion matrix using test data and predictions
print(metrics.confusion_matrix(y_test, y_preds))
print(metrics.classification_report(y_test, y_preds))
#print (df)