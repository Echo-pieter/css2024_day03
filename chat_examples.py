# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:50:04 2024

@author: terre
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('chat_files/poker_2016_09_27.csv', names=['Time', 'NUN',
                                                           'x', 'y', 'z'])


# conver the string time to DateTime type
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time


# plot the results
plt.plot(df['Time'], df['x'], label='x')
plt.plot(df['Time'], df['y'], label='y')
plt.plot(df['Time'], df['z'], label='z')

plt.show()


