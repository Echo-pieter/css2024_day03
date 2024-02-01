# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:23:49 2024

@author: terre
"""

# EDA = Exploratory data analysis (visually representing data)

'''
Using matplotlib
'''

import matplotlib.pyplot as plt

# create two lists to plot the realtionship between them
react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200, 220, 240, 260]



# plotting a line chart


# the first parameter is the x axis values and the next parameter is the y axis values
# plt.plot(temp, react_conv)

# add a title and labels for the axis
# plt.xlabel('Temperature')
# plt.ylabel('reaction converstion')
# plt.title('chemical experiment')

# plt.show()







# plotting a barchart


day1_attendees = [70, 20, 64, 90, 80]
day1_names = ["blessing", "mali", "pangi", "tafi", "shini"] 


# first parameter is the x axis vals and second is the y axis vals
# plt.bar(day1_names, day1_attendees)

# plt.show()





# plotting a scatter plot

x_scatter = [1,2,3,4,5]

y_scatter = [2,4,6,8,10]


# plt.scatter(x_scatter, y_scatter)

# plt.show()


# plotting a histogram

x_histogram = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]


plt.hist(x_histogram)
plt.show()












