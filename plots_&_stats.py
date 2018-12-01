# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:07:13 2018

@author: megha
"""

import SalesData as sd
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_pacf
import matplotlib.pyplot as plt
from pandas.tools.plotting import autocorrelation_plot

"""
Basic Statistics
"""
#Sales Description:
sd.totalSales['Current Sales'].describe()

#Average and Max Sale for each Customer
cust_sales = sd.totalSales.groupby(['Customer'])['Current Sales']

print("Maximum Sales: ")
print(cust_sales.max())

print("Average Sales: ")
print(cust_sales.mean())

#Top 5 items - for each year
i_sales = sd.itemSales.groupby(['Year','Item']).agg({'Sales':sum})
g = i_sales['Sales'].groupby(level=0, group_keys=False)
print(g.nlargest(5))

"""
Business Charts
"""
#Pie Chart - Sales% - By Retailer
for year in [2015,2016,2017]:
    labels=[]
    sizes=[]
    for c in sd.Customer:
        c_sales = np.sum(sd.totalSales[sd.totalSales['Customer']==c][sd.totalSales['Year'] == year]['Current Sales'])
        if (c != 'McLane'):
            labels.append(c)
            sizes.append(c_sales)
    plt.pie(sizes, labels=labels,autopct='%1.1f%%',shadow=True)
    plt.axis('equal')
    plt.show()

#Total Sales Plot - Quarterly
tempSales = sd.totalSales
tempSales['Quarter'] = pd.Series()
for i in range(len(tempSales)):
    if (tempSales['MOY'][i] <= 3):
        tempSales['Quarter'][i] = str(tempSales['Year'][i])+'Q1'
    elif tempSales['MOY'][i] <= 6:
        tempSales['Quarter'][i] = str(tempSales['Year'][i])+'Q2'
    elif tempSales['MOY'][i] <= 9:
        tempSales['Quarter'][i] = str(tempSales['Year'][i])+'Q3'
    else:
        tempSales['Quarter'][i] = str(tempSales['Year'][i])+'Q4'

qcgroup = tempSales.groupby(['Quarter'])['Current Sales']
qcgroup.sum().plot(kind='barh')

#Boxplot for TotalSales - Yearly
HPC_Sales = sd.totalSales[sd.totalSales['Customer']=='HPC']
plt.boxplot(HPC_Sales[HPC_Sales['Year']==2017]['Current Sales'])
plt.show()

#YOY Dollar Sales Comparison - By Retailer
for c in sd.Customer:
    custSales2015 = sd.totalSales[sd.totalSales['Customer']==c][sd.totalSales['Year']==2015]
    custSales2016 = sd.totalSales[sd.totalSales['Customer']==c][sd.totalSales['Year']==2016]
    custSales2017 = sd.totalSales[sd.totalSales['Customer']==c][sd.totalSales['Year']==2017]
    plt.plot(custSales2015['MOY'],custSales2015['Current Sales'],'go--')
    plt.plot(custSales2016['MOY'],custSales2016['Current Sales'],'bo--')
    plt.plot(custSales2017['MOY'],custSales2017['Current Sales'],'ro--')
    plt.title(c + " YOY Sales Comparison")
    plt.xlabel("Months")
    plt.ylabel("Dollar Sales")
    plt.show()

#AutoCorrelation Plot for HPC - Sales
x = sd.totalSales[sd.totalSales['Customer'] == 'HPC'][['Month','Current Sales']]
Sales = x['Current Sales']
Sales.index = x['Month']
Sales.plot()
plt.show()
autocorrelation_plot(Sales)
plt.show()

plot_pacf(Sales, lags=24, alpha=0.05)
print("AutoCorrelation Coefficient: " + str(Sales.autocorr()))