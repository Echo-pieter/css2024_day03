# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:52:20 2024

@author: terre
"""

import numpy as np
import matplotlib.pyplot as plt

n=30000
x = np.random.uniform(size=n)
y = np.random.uniform(size=n)
plt.plot(x[x**2+y**2<=1],y[x**2+y**2<=1],'bo')
plt.plot(x[x**2+y**2>1],y[x**2+y**2>1],'ro')
plt.show()


pi = sum(x**2+y**2<=1)/n*4