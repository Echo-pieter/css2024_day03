# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:05:05 2024

@author: terre
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(2,11,0.3)


# make numpy array a list


y = list(x)


s = x.shape


# difference betwene list and numpy array
t = [1,2,3]
t1 = t*2
# not the same
x2 = x*2


# # conventional python - for loop
# print("Using just python")
# for i in range(1,11):
#     print(i)
    
# print("\nusing numpy")
    
# # numpy - arange
# for i in np.arange(1,11,0.5):
#     print(i)



# squarin the numbers from 1 to 5
squares = []
for i in range(1,6):
    squares.append(i**2)
    
print(squares)



# using just numpy

squares = np.arange(1,6)**2 
print(squares)

x = np.arange(1,6)
y = x**2 
print(y)

print("\nx ",x)
print("y ", y)

# plot the x and y
plt.plot(x,y,'r*')
plt.show()

print("x # elements ",x.shape)
print("y # elements ",y.shape)


# adding the two arrays together
print("\nAdding togheter x and y")
print(x+y)


# multiplying the two arrays elementwise
print("\nMultiplying them")
print(x*y)


# doing the product
print("\nDoing the dot product")
print(x.dot(y))



# doing matrix multiplication
print("\nDoing the cross product")
print(np.matmul(x,y))


# making a normal list into a numpy array
alist = [1,2,5,6,15,22]
data = np.array(alist)
print(data)



# changing the dimenions of a numpy array
data2 = data.reshape([2,3])
print(data2)

print("\nAdding matrices together")

# adding matrices together
data3 = data2 + data2
print(data3)

print("\n")


# converting multidimensional list to multidimentional array
alist2 = [[1,2,5],[6,15,22]]
mat = np.array(alist2)
print(mat)

print("\n")

data3 = np.matmul(mat, data2.T)
print(data3)




# cross the two matrices
temp = np.cross(mat,data2.T)














































