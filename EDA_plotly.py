# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:23:29 2024

@author: terre
"""


'''
Using the plotly libarary
'''

# import plotly.express as px


# # create two lists to plot the realtionship between them
# react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
# temp = [180, 200, 220, 240, 260]


# fig = px.line(x=temp, y=react_conv)

# fig.write_html("plot.html")


import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x="year", y="lifeExp", color='country')
fig.write_html("plot.html")


# This is used to automatically open up a browser of your plot
import webbrowser
webbrowser.open("plot.html")