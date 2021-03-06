# -*- coding: utf-8 -*-
"""FizzBuzz_Adhi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-AZAWnMzGDs2vyd8DOTXAzLdx3WPTKQ5
"""

'''
  Typical example of a Fizz Buzz Challenge. 
  0 if not divisbile by 3 or 5
  1 if divisible by 3 but not 5
  2 if divisible by 5 but not 3
  3 if divisible by 3 and 5
  
  The dataset size is too small for a complex non-linear algorithm to fit, hence my reccomendation is to increase the training dataset size to 10k+ rows
'''

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

#from google.colab import files  # Only used in Google Colab
#files.upload()                  # Only used in Google Colab

data = pd.read_csv("my_file.csv")  # Reading dataset
testData=pd.read_csv("testdata.csv")
data.head()
testData.head()

X = data.iloc[:,0]   # Choosing the independant column as X using integer slicing. For more info check out pandas documentation
y = data.iloc[:,1]   # Choosing the dependant column to be predicted as Y

X.head()
y.head()
testy=testData.iloc[:,0]

train_x, test_x, train_y, test_y = train_test_split(X, y,test_size=0.1, stratify=y)  # Stratified sampling in Y, setting the train:test ratio as 0.8:0.2

print(X.shape, y.shape, train_x.shape, test_x.shape, train_y.shape,test_y.shape)  # Printing the shape of each split to verify they are right

clf = RandomForestClassifier()
clf.fit(train_x.reshape(-1,1),train_y)

#predictions=clf.predict(test_x.reshape(-1,1))
predictions=clf.predict(testy.reshape(-1,1))
#print( "Train Accuracy :: ", accuracy_score(train_y, clf.predict(train_x.reshape(-1,1))))
#print( "Test Accuracy  :: ", accuracy_score(test_y, predictions))
#print( " Confusion matrix ", confusion_matrix(test_y, predictions))
#print("Trained model:",clf)
print(testy)
print(predictions)
