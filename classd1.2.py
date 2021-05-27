# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:21:05 2020

@author: USER
"""

#data cleaning

import pandas as pd
df=pd.read_csv(r"C:\Users\USER\Downloads\data\datawh_missing.csv")

''''
handling duplicate entries
handling missong values
''''

#to check duplicates
df.duplicated().sum()

#to drop duplicate rows
df.drop_duplicates(inplace=True)

#df2=df.drop_duplicates(inplace=False)the original data is stored but the changed data is 
#stored in the new data base

#########333handling missing values


#to check for the missing values in all columns
df.isnull().sum()

df=pd.read_csv(r"C:\Users\USER\Downloads\data\datawh_missing.csv",
               na_values=['.','?'])


df.isnull().sum()

#dropping those rows which has less than 3 real values
df.dropna(thresh=3,inplace=True)





df.info()
df.skew()



#filling missing values of temperature using mean
df['Temperature'].fillna(df['Temperature'].mean(),inplace=True)
df.fillna(df.median(),inplace=True)




































  





















































