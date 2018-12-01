# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:51:13 2018

@author: megha
"""
import SalesData as sd
import numpy as np
from sklearn import linear_model

numberRows = len(sd.LmData)

#Randomly generate Test and Training Data
randomlyShuffledRows = np.random.permutation(numberRows)
trainingRows = randomlyShuffledRows[0:300] #use first 800 for training
testRows = randomlyShuffledRows[300:] #remaining rows are test set

xTrain = sd.LmData.iloc[trainingRows,1:37]
yTrain = sd.LmData.iloc[trainingRows,0]
xTest = sd.LmData.iloc[testRows,1:37]
yTest = sd.LmData.iloc[testRows,0]

#fit model
reg = linear_model.LinearRegression()
reg.fit(xTrain, yTrain)

#Predict model
reg_prediction = reg.predict(xTest)

#Coefficients and intercepts
print("Regression Coefficients: ")
print(reg.coef_)
print("Regression Intercept: " + str(reg.intercept_))

#Regression Score
print("Regression Score: " + str(reg.score(xTest,yTest)))