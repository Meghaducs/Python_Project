# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:22:00 2018

@author: megha
"""
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
import TimeSeriesForecasting as tsf
import linear_regression as linreg
import numpy as np

"""
Validations:
    1. Mean Squared Error
    2. R-squared
    3. Mean Absolute Error
"""
def val_tsf(dt):
    tsf_mse=[]
    tsf_r2=[]
    tsf_mae=[]
    for i in range(10):
        tsf_mse.append(mean_squared_error(dt[i][2],dt[i][1]))
        tsf_r2.append(r2_score(dt[i][2],dt[i][1]))
        tsf_mae.append(mean_absolute_error(dt[i][2],dt[i][1]))
        
    print("Mean Squared Error: " + str(np.mean(tsf_mse)))
    print("R-squared: " + str(np.max(tsf_r2)))
    print("Mean Absolute Error: " + str(np.mean(tsf_mae)))

#For AR Model:
print("For AR Model:")
val_tsf(tsf.AR_Predictions)

#For ARMA Model:
print("For ARMA Model:")
val_tsf(tsf.ARMA_Predictions)

#For ARIMA Model:
print("For ARIMA Model:")
val_tsf(tsf.ARIMA_Predictions)

#For Linear Regression Model:
mse = mean_squared_error(linreg.yTest,linreg.reg_prediction)
r2 = r2_score(linreg.yTest,linreg.reg_prediction)
mae = mean_absolute_error(linreg.yTest,linreg.reg_prediction)

adj_r2 = 1-(1-r2)*(60-1)/(60-37-1)

print("For Linear Regression Model:")
print("Mean Squared Error: " + str(mse))
print("R-squared: " + str(r2))
print("Adj. R-squared: " + str(adj_r2))
print("Mean Absolute Error: " + str(mae))