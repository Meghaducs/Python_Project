# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:41:27 2018

@author: megha
"""

import SalesData as rd   #For raw dataset

"""
Autoregression (AR)
- models the next step in the sequence as a 
  linear function of the observations at prior time steps.
"""
from statsmodels.tsa.arima_model import ARMA

AR_Predictions = []
for c in rd.Customer:
    print("For customer " + c + ":")
    x = rd.totalSales[rd.totalSales['Customer'] == c][['Month','Current Sales']]
    
    #create Test and Train data
    Sales = x['Current Sales'].diff()
    Sales.index = x['Month']
    TrainData = Sales.loc['2015-01-01':'2017-06-01',]
    TestData = Sales.loc['2017-07-01':'2017-12-01',]
    TrainData = TrainData.dropna()
    #fit model
    model = ARMA(TrainData,order=(2,0)) #AR(2) - 2nd order Autoregression
    AR_fit = model.fit()
    print(AR_fit.params)
    #make prediction
    pred = AR_fit.predict(start = '2017-07-01', end = '2017-12-01')
    AR_Predictions.append([c,pred,TestData])

#Plot Predictions
AR_fit.plot_predict(start = '2015-02-01', end = '2017-12-01')

"""
Moving Average (MA)
- models the next step in the sequence as a linear function 
  of the residual errors from a mean process at prior time steps
"""
MA_Predictions = []
for c in rd.Customer:
    print("For customer " + c + ":")
    x = rd.totalSales[rd.totalSales['Customer'] == c][['Month','Current Sales']]

    #create Test and Train data
    Sales = x['Current Sales'].diff()
    Sales.index = x['Month']
    TrainData = Sales.loc['2015-01-01':'2017-06-01',]
    TestData = Sales.loc['2017-07-01':'2017-12-01',]
    TrainData = TrainData.dropna()
    #fit model
    model = ARMA(TrainData,order=(0,1)) #MA(1) - first order moving average
    MA_fit = model.fit()
    print(MA_fit.params)
    #make prediction
    pred = MA_fit.predict(start = '2017-07-01', end = '2017-12-01')
    MA_Predictions.append([c,pred,TestData])

MA_fit.plot_predict(start = '2015-02-01', end = '2017-12-01')

"""
Autoregressive Moving Average (ARMA)
- combines both Autoregression (AR) and Moving Average (MA) models
- ARMA(p, q) : AR(p) and MA(q)
"""
ARMA_Predictions = []
for c in rd.Customer:
    print("For customer " + c + ":")
    x = rd.totalSales[rd.totalSales['Customer'] == c][['Month','Current Sales']]

    #create Test and Train data
    Sales = x['Current Sales'].diff()
    Sales.index = x['Month']
    TrainData = Sales.loc['2015-01-01':'2017-06-01',]
    TestData = Sales.loc['2017-07-01':'2017-12-01',]
    TrainData = TrainData.dropna()
    #fit model
    model = ARMA(TrainData,order=(2,1))  #AR(2) and MA(1)
    ARMA_fit = model.fit()
    print(ARMA_fit.params)
    #make prediction
    pred = ARMA_fit.predict(start = '2017-07-01', end = '2017-12-01')
    ARMA_Predictions.append([c,pred,TestData])

ARMA_fit.plot_predict(start = '2015-02-01', end = '2017-12-01')

"""
Autoregressive Integrated Moving Average (ARIMA)
- combines both Autoregression (AR) and Moving Average (MA) models 
  as well as a differencing pre-processing step of the sequence to 
  make the sequence stationary, called integration (I).
-  ARIMA(p, d, q): AR(p), I(d) and MA(q)
"""
from statsmodels.tsa.arima_model import ARIMA

ARIMA_Predictions = []
for c in rd.Customer:
    print("For customer " + c + ":")
    x = rd.totalSales[rd.totalSales['Customer'] == c][['Month','Current Sales']]

    #create Train and Test data
    Sales = x['Current Sales'].diff()
    Sales.index = x['Month']
    TrainData = Sales.loc['2015-01-01':'2017-06-01',]
    TestData = Sales.loc['2017-07-01':'2017-12-01',]
    TrainData = TrainData.dropna()
    #fit model
    model = ARIMA(TrainData,order=(2,1,0)) #AR(2), I(1), MA(0)
    ARIMA_fit = model.fit()
    print(ARIMA_fit.params)
    #make prediction
    pred = ARIMA_fit.predict(start = '2017-07-01', end = '2017-12-01', typ = 'levels')
    ARIMA_Predictions.append([c,pred,TestData])

ARIMA_fit.plot_predict(start = '2015-03-01', end = '2017-12-01')
