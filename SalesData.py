# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:31:33 2018

@author: megha

Data Reading
"""

import pandas as pd
import numpy as np

Customer = ['HPC','C&S','Harris Teeter','HEB', 'Meijer','Supervalu','Kroger','Publix','Vitacost','McLane']
Marketing_Events = ['TV','Print','Redesign','New Campaign','FSI','DTC','In store Signage','Mobile Rebates','On-Pack Coupons']

rawfile = 'Sales_3years.xlsx'

xl = pd.ExcelFile(rawfile)

#Sales - by Customer,Month
totalSales = xl.parse('TotalSalesByPeriod')

#Change Month timestamp into month and year variables
totalSales["Year"] = 0
totalSales["MOY"] = 0
for i in range(len(totalSales)):
    totalSales.loc[i,'Year'] = totalSales.loc[i,'Month'].year
    totalSales.loc[i,'MOY'] = totalSales.loc[i,'Month'].month

#Item Sales - by Customer, Month
itemInfo = xl.parse('Item_data')
itemSales = xl.parse('Cust_Item_Sales')

#Marketing Data
Marketing = xl.parse('Marketing Events')

tSales = []
for y in [2015,2016,2017]:
    for m in range(1,13):
        tSales.append(np.sum(totalSales[totalSales['Year']==y][totalSales['MOY']==m]['Current Sales']))        
Marketing['TotalSales'] = tSales

Marketing['Events'] = 0
for e in Marketing_Events:
    Marketing['Events'] +=Marketing[e]

#Retailer Data - Kroger & Publix
Kroger = xl.parse('Kroger')
Publix = xl.parse('Publix')


"""
Data for Linear Regression
"""
#Merge Sales and Marketing Data
LmData = totalSales.merge(Marketing, how='inner', on='Month')

#Transform Categorical Data - indicator variables
LmData["isHPC"] = (LmData["Customer"]=='HPC').astype(int)
LmData["isC_S"] = (LmData["Customer"]=='C&S').astype(int)
LmData["isHarris"] = (LmData["Customer"]=='Harris Teeter').astype(int)
LmData["isHEB"] = (LmData["Customer"]=='HEB').astype(int)
LmData["isMeijer"] = (LmData["Customer"]=='Meijer').astype(int)
LmData["isSupervalu"] = (LmData["Customer"]=='Supervalu').astype(int)
LmData["isKroger"] = (LmData["Customer"]=='Kroger').astype(int)
LmData["isPublix"] = (LmData["Customer"]=='Publix').astype(int)
LmData["isVitacost"] = (LmData["Customer"]=='Vitacost').astype(int)
LmData["isMclane"] = (LmData["Customer"]=='McLane').astype(int)

#Delete Columns not required
del LmData['Customer']
del LmData['Month']

#Transform Categorical Data (Month & year)
LmData["is2015"] = (LmData["Year"]==2015).astype(int)
LmData["is2016"] = (LmData["Year"]==2016).astype(int)
LmData["is2017"] = (LmData["Year"]==2017).astype(int)

LmData["isJan"] = (LmData["MOY"]==1).astype(int)
LmData["isFeb"] = (LmData["MOY"]==2).astype(int)
LmData["isMar"] = (LmData["MOY"]==3).astype(int)
LmData["isApr"] = (LmData["MOY"]==4).astype(int)
LmData["isMay"] = (LmData["MOY"]==5).astype(int)
LmData["isJun"] = (LmData["MOY"]==6).astype(int)
LmData["isJul"] = (LmData["MOY"]==7).astype(int)
LmData["isAug"] = (LmData["MOY"]==8).astype(int)
LmData["isSep"] = (LmData["MOY"]==9).astype(int)
LmData["isOct"] = (LmData["MOY"]==10).astype(int)
LmData["isNov"] = (LmData["MOY"]==11).astype(int)
LmData["isDec"] = (LmData["MOY"]==12).astype(int)

del LmData['Year']
del LmData['MOY']
#End of Code