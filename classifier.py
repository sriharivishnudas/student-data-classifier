import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib

#Loading Dataset

X = pd.read_csv("final-values.csv")

#Training Set

X_Train = X.iloc[:, [0,1,2,3,4]].values
Y_Train = X.iloc[:, 5].values

# Feature Scaling

sc = StandardScaler()
X_Train = sc.fit_transform(X_Train)

#Classifier

classifier = GaussianNB()
classifier.fit(X_Train,Y_Train)

#Persist an arbitrary Python object into one file

joblib.dump(classifier,'NBClassifier.pkl')
