# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:41:33 2024

@author: terre
"""

import pandas as pd
import matplotlib.pyplot as plt


iris_data = pd.read_csv("iris.csv")


# remove the Iris prefix from the class column
iris_data['class'] = iris_data['class'].str.replace('Iris-', '')


# scatter plot sepal_length vs sepal_width


# plt.scatter(iris_data['sepal_length'], iris_data['sepal_width'])
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')

# plt.show()



# bar plot

# plt.bar(iris_data['class'], iris_data['sepal_length'])
# plt.show()


'''
Using seaborne
'''

# import seaborn as sns

# sns.pairplot(iris_data, hue='class')


# plt.show()


# draw a pie chart of the number of different iris species

class_count = iris_data['class'].value_counts()

plt.pie(class_count, labels=class_count.index)

plt.show()























