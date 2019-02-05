#!/usr/bin/python

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import sys
from io import BytesIO


# To Do:: create the training/test set from SQL query
# Import training tax data
dataset = pd.read_csv('/tmp/tax_data.csv')


# Split into training and test
X = dataset.values[:,0:5] #independant variables
Y = dataset.values[:,5:6] #solve for dependant variable
X_train,X_test,Y_train,Y_test =  train_test_split( X, Y, test_size =0.3, random_state = 100)

# To Do:: save static model and load
# Create the DTree classification model
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, Y_train)

# Predict Y from the X_test data
y_pred_en = clf_entropy.predict(X_test)

# Accuracy Score
# print("Accuracy is ", accuracy_score(Y_test,y_pred_en)*100)

# Pass input to the dataframe
data = sys.stdin
df = pd.read_csv(data,header=None)
rawdata = str(df.to_csv(header=False,index=False,encoding='utf-8'))

# Predit if the input is fraud as predicted by the model
isFraud = clf_entropy.predict(df)
predictResult = isFraud[0]

# Get the the value of the numpy array.  This is a hack >.<
# To Do:: find a numpy function that emits the raw value
if isFraud < 1:
 # print(0)
 cleanResult = 0
else:
 # print(1)
 cleanResult = 1

# If the prediction emits a 1 it's fraud else not
# print(rawdata)
# print(predictResult)

memsql_row = (str(cleanResult)+','+str(rawdata))

print(memsql_row.strip())
