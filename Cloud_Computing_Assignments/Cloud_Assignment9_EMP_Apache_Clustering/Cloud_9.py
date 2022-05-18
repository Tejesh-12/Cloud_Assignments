import pandas as pd
from sklearn import datasets
import numpy as np
import random
import operator
import math
from sklearn import metrics
from sklearn.cluster import KMeans
import seaborn as sns



df=pd.read_csv("Adult.csv")
print(df)



#K-Means Implemetation
X = df.to_numpy()
# Instantiate the KMeans models
km = KMeans(n_clusters=3, random_state=42)
# Fit the KMeans model
print(len(km.fit_predict(X)))
print(km.fit_predict(X))
# Calculate Silhoutte Score
score = metrics.silhouette_score(X, km.labels_, metric='euclidean')

# Print the score
print('Silhouetter Score: %.3f' % score)
