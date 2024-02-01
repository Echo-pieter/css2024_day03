# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:20:07 2024

@author: terre
"""

import numpy as np
import matplotlib.pyplot as plt

# define two matrices
a = np.array([[1,2,3],[4,5,6],[7,8,-9]])
b = np.array([3,-4,2])


# determine the determinant

d = np.linalg.det(a)

if(d>0):
    print('Matrix is solvable (not indeterminate)')


# solve the equations
sol =np.linalg.solve(a,b)




# fitting an equation

# import csv file as numpy array
data = np.loadtxt('noisydata.csv',skiprows=1,delimiter=',')

# determine the average of the data
data_avg = np.mean(data,axis=0)



# extract data from 
pressure = data[:,0]
flowrate = data[:,1]



# using polyfit
fit = np.polyfit(pressure, flowrate,2)


# evaluate the fitted polynomial on the data
flowfit = np.polyval(fit, pressure)



# plot the results
plt.plot(pressure,flowrate,'go',label='original')
plt.plot(pressure,flowfit,'k-',label='fit')
plt.xlabel('Pressure')
plt.ylabel('Flowrate')
plt.legend()
plt.show()


# filtering numpy arrays

pressure_filt = pressure[pressure > 5]















