# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:32:55 2024

@author: terre
"""

import pandas as pd
import matplotlib.pyplot as plt

time_series = pd.read_csv('time_series_data.csv', index_col=0)

# check to see what the data type of the Date column is 
print(time_series.info())


# convert the date column to DateTime type

time_series['Date'] = pd.to_datetime(time_series['Date'], format="%Y-%m-%d")



# plot the temperature data using a line plot
# plt.plot(time_series['Date'],time_series['Temperature'])
# plt.ylabel('Temperature')
# plt.xlabel('Date')
# plt.show()


# you can plot directly from the pandas data frame
time_series['Temperature'].plot(kind='hist', bins=20, title="Temperature")
plt.show()


