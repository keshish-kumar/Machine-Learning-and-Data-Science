# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:32:18 2020

@author: USER
"""

''' PANDAS 
-Data import/export
-data selection & filtering
  -basics of staticstics
-data cleaning
-data aggregation
'''
#importing data from a particular file 
import pandas as pd
'''
pandas series=1d
pandas dataframe=2d
pandas panel=3d
'''
#schanging the index
df=pd.read_csv(r"C:\Users\USER\Downloads\data\datawh.csv",index_col=['Dates'])


#solving the error of the data
#r refers to raw string doesnt take the existence of \n \t etc
df=pd.read_csv(r"C:\Users\USER\Downloads\data\datanh.csv",header=None)
df.columns=['Temperature','Humidity','air','pressure']


df=pd.read_excel(r"C:\Users\USER\Downloads\data\data.xlsx")
#####################import a particular data from url
url="https://coinmarketcap.com/currencies/bitcoin/historical-data/"
dfs=pd.read_html(url)

type(dfs)
len(dfs)
df1=dfs[0] 
df2=dfs[1]
df3=dfs[2]

#export

df3.to_excel(r"C:\Users\USER\Downloads\data\bitcoin.xlsx")



#####################dAta exploration and filtering


import pandas as pd
df=pd.read_csv(r"C:\Users\USER\Downloads\data\datawh.csv",index_col=['Dates'])
''''
exploration-understand data etc
'''

df.shape
print(df.columns)
df.head() #top 5 rows
df.head(2) # top 2 rows
df.tail()# tail rows last 5


df.info()#total summary of the data

df.describe()# total statistical data

###################
df['Temperature'] #takes a particular column data

df[['Temperature','Humidity','Pressure','Air Quality']] # a series shown

type(df[['Temperature','Humidity','Pressure','Air Quality']] )# a dataframe


df['05-05-2018':'12-05-2018']

df['05-05-2018':'12-05-2018']['Temperature']

df['05-05-2018':'12-05-2018'][['Temperature','Humidity']]

df.iloc[5:18,1:3]#fetches data from the particular locaion 


##################################################################
#filtering

df[df['Temperature']>2000]#one condition data filter




df[df['Temperature']>2000][df['Humidity']>200]#two condition data filter

#and
df[(df['Temperature']>2000) & (df['Humidity']>200)]

#OR

df[(df['Temperature']>2000) | (df['Humidity']>200)]
###################################################################

# staticstics


df.describe()

df['Temperature'].mean()
df['Temperature'].median()
df['Temperature'].mode()
df['Temperature'].min()
df['Temperature'].max()
df['Temperature'].var()
df['Temperature'].std()
df['Temperature'].skew()


































































































































