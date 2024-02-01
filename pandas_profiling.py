# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:21:12 2024

@author: terre
"""

# ydata_profiling not included in Anaconda :-(

import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('iris.csv')

profile = ProfileReport(df, title='Profiling report')

profile.to_file('report.html')



