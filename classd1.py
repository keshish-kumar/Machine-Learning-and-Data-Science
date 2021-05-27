# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:07:17 2020

@author: USER
"""
################numpy
x=[4,5,3]
y=[3,2,8]

print(x+y)

import numpy as np
x=np.array([7,2,6])
y=np.array([6,3,4])
print(x+y)



x=np.array([7,2,6,4,5,6])#can be only of one data type
x.dtype




x=np.array([[7,5,3],
           [1,2,3],
           [3,2,5],
           [3,6,9]])
print(x)
print(x.dtype)
print(x.shape)
print(x.size)


x.min()
x.max()
x.mean()
x.max(axis=0)#column wise check for biggest no
x.min(axis=0)#same as above but small vaue


x.max(axis=1)#row wise check for smallest no
x.min(axis=1)#same but samll no


x.mean(axis=0)
x.mean(axis=1)

x=np.arange(2,20,3)#array for the range from 2 to 20
x


x=np.linspace(2,20,21)#linspace= (stop-start)/(n-1)
x

x=np.ones((5,2),dtype='int32')
x

x=np.zeros((2,3))
x
x=np.logspace(0,6,7)
x

###########################################
#random numbers in numpy

x=np.random.rand(5)#random nos positive 0 to 1
x

x=np.random.randn(10)#random nos negative and positive 0 to 1
x

x=np.random.randint(low=10,high=20,size=(4,3))
x
###################################
np.sin(np.deg2rad(90))
np.sqrt(456788)#square root
np.cbrt(27)#cuberoot
######################

#linear algebra
m=np.matrix([[4,5,6],[3,1,8],[6,7,2]])
np.linalg.inv(m)#inverse
np.linalg.det(m)# determinant
#solving of the question equation
'''
3x-7y=1
4x-y=22
'''
a=[[3,-7],[4,1]]
b=[1,22]
np.linalg.solve(a,b)
























































