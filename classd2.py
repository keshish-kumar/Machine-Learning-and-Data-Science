# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:24:29 2020

@author: USER
"""

'''
data visualisation
basic=matplotlib
advance=seaborn
'''
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,1,0.5)
y=x*x
z=x*x*x

plt.plot(x,y)
plt.show()


plt.plot(x,y)
plt.show()
plt.plot(x,z)
plt.show()
  
plt.plot(x,y,label='x v/s y')
plt.plot(x,z,label='x v/s z')
plt.xlabel("value of x")
plt.ylabel("value of y")
plt.title("graph between x,y,z")
plt.legend()
plt.show()







































