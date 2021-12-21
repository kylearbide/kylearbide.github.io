# -*- coding: utf-8 -*-
"""Plots and EDA_v2_'19-'21

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lPS1Te8IyRhJy4bOR-dUv12hRMPKiuGp
"""

!pip install yfinance
import pandas_datareader as web
from pandas_datareader import data as pdr
import yfinance as yfin
import pandas as pd
yfin.pdr_override()

BTC = pdr.get_data_yahoo("BTC-USD", start="2014-01-01", end="2021-10-31")
ETH = pdr.get_data_yahoo("ETH-USD", start="2014-01-01", end="2021-10-31")
DOGE = pdr.get_data_yahoo("DOGE-USD", start="2014-01-01", end="2021-10-31")
SP5 = pdr.get_data_yahoo("^GSPC", start="2014-01-01", end="2021-10-31")

BTC.reset_index(level=0, inplace=True)
ETH.reset_index(level=0, inplace=True)
DOGE.reset_index(level=0, inplace=True)
SP5.reset_index(level=0, inplace=True)

print(BTC.head(1))
print(ETH.head(1))
print(DOGE.head(1))
print(SP5.head(1))



Merged = SP5.merge(ETH, how = 'outer', on = "Date")
Merged = Merged.merge(DOGE, how = 'outer', on = "Date")
Merged = Merged.merge(BTC, how = 'outer', on = "Date")

Merged.head(10)

SP5.describe()

Merged.columns = ["Date","Open_SP5",	'High_SP5'	,'Low_SP5',	'Close_SP5',	'Adj_Close_SP5','Volume_SP5',"Open_ETH",	'High_ETH'	,'Low_ETH',	'Close_ETH',	'Adj_Close_ETH','Volume_ETH',"Open_DOGE",	'High_DOGE'	,'Low_DOGE',	'Close_DOGE',	'Adj_Close_DOGE','Volume_BTC',"Open_BTC",	'High_BTC'	,'Low_BTC',	'Close_BTC',	'Adj_Close_BTC','Volume_BTC']

Merged.head(10)

#Testing Append Merge 

BTC2=BTC.copy()
ETH2=ETH.copy()
DOGE2=DOGE.copy()
SP52=SP5.copy()

BTC2['asset']='BTC'
ETH2['asset']='ETH'
DOGE2['asset']='DOGE'
SP52['asset']='SP5'

#Making a data frame of the closing price for utilizing percent change of the dataframe. c1 is for change dataframe. 

Merged.columns

c1_col=['Date','Adj_Close_SP5','Adj_Close_ETH','Adj_Close_DOGE','Adj_Close_BTC']

c1=Merged[c1_col]


c1['Date']=pd.to_datetime(c1.Date)

#printing c1 to see if it is converting to date. 

c1 = c1.sort_values('Date')

#Settinng index to date 
 
 c1 =c1.set_index(c1['Date'])

#dropping the date column 
c1 =c1.drop('Date',axis=1)

c1.plot(title="Adjusted Price over Time")

#made new percent change df to limit constant recalculation. 

pc1= c1.pct_change(fill_method='ffill')

pc1=pc1*100

#Setting up a new data frame to evalyate more recent (past 2 years) price movements. 
#Commenting out this step will 

pc1 = pc1.loc['2019-10-31':'2021-10-31']

pc1.plot(title='Daily Percent Change')

#calculating correlation of the percent change columns.


corr = pc1.corr()
corr.style.background_gradient(cmap='coolwarm')

#Creating multiple histograms. Can see from the plots below that eth and BTC 
#have significantly more volatility. 
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))
plt.hist(pc1['Adj_Close_SP5'], bins=30, alpha=.5, label='Adj_Close_SP5');
plt.hist(pc1['Adj_Close_BTC'], bins=30, alpha=.5, label='Adj_Close_BTC');
plt.hist(pc1['Adj_Close_ETH'], bins=30, alpha=.5, label='Adj_Close_ETH');
plt.legend()
plt.title('Histogram of Daily Percent Change: Oct 2019 - Oct 2021')

#plt.hist(pc1['Adj Close_DOGE'], bins=30, alpha=.5, label='Adj Close_DOGE');
#took out doge because distorted plot. 
#asking max if a power transformation would be appropriate here.

#daily variance is much higher for ETH, BTC DOGE. Approx 6-10 percent. 
pc1.describe()

pc1.shape

import seaborn as sns

pc_hm = pc1



sns.heatmap(pc_hm.tail(15), annot=True)

pc_hm

"""Section below is in progress to subset the overall data set when the SP500 has a significant negative movement. """

#Subsetting the SP5 data for when there is a significant drop. This helps evaluation if eth, btc are really 
#counter cyclical. 3 standard deviations away from mean would be considered a very large drop. 

SP5_sdev=-3*pc1['Adj_Close_SP5'].std()

pc1[pc1.Adj_Close_SP5 < SP5_sdev]

pc2=pc1

pc2['num']=range(0,pc2.shape[0])

neg_days= pc2.num[pc2.Adj_Close_SP5<SP5_sdev]

neg_days

def twendays(x):
  l1=list(range(x,x+20))
  return(l1)

neg_days_value =neg_days.apply(twendays)

import itertools

neg_days_index=list(itertools.chain.from_iterable(neg_days_value))



neg_days_value[0]

#Subsetting for when the sp 500 is 3 standard deviations negative. 

pc_s =pc2.iloc[neg_days_index]
pc_s =pc_s.drop('num',axis=1,)

pc_s = pc_s[pc_s.index.duplicated(keep='first')]



#Calculating the correlation an alternative way, as a subset of the data for the 20 days after an SP500 dowturn. 

twen_corrs=[]

for x in range(0,neg_days_value.size):
  z= pc2.iloc[neg_days_value[x]].corr()
  twen_corrs.append(z.iloc[3,0])

sum(twen_corrs)/len(twen_corrs)

#Getting an average of the correlations across time. 
#Based on row patterns. 
ETH_t_crr =0.5395336899458966
BTC_corr= 0.492069949945664

#Dropping number column for correlation. Correlation is much greater when 

pcs_corr =pc_s.corr()
pcs_corr.style.background_gradient(cmap='coolwarm')

plt.figure(figsize=(8,6))
plt.hist(pc_s['Adj_Close_SP5'], bins=30, alpha=.5, label='Adj_Close_SP5');
plt.hist(pc_s['Adj_Close_BTC'], bins=30, alpha=.5, label='Adj_Close_BTC');
plt.hist(pc_s['Adj_Close_ETH'], bins=30, alpha=.5, label='Adj_Close_ETH');
plt.legend()
plt.title('Significant SP500 Drop and Percent Change: : Oct 2019 - Oct 2021')

#looks like more negative downside present in the tails of eth and btc distributions.

pc_s.describe()

pc_s

"""General Time series predictions

Rolling Averages over x days

Using days as a hyper parameter and finding how long it takes the markets to react to a large change

Taking recency into account as well, How does correlation look within the last year vs last 5 year

Outside parameters
"""
