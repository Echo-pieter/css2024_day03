# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:10:52 2024

@author: terre
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('chat_files/csd_complexes_geometric_properties_for_activation_energies_for_css_24.xlsx')


plt.scatter(df['REFCODE'], df['Activation_Energy(kcal/mol)'])
plt.xlabel('REFCODE')
plt.ylabel('Activation_Energy(kcal/mol)')

plt.show()

