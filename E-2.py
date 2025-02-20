#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 01:45:37 2024

@author: jmr
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Heatmap
data = sns.load_dataset('flights')
flight_pivot = data.pivot_table(index='month',columns='year', values='passengers')
sns.heatmap(flight_pivot, cmap='coolwarm')
plt.title('Flights Heatmap')
plt.show()
# Box Plot
data = sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill', data=data, palette='rainbow')
plt.title('Box Plot of Total Bill by Day')
plt.show()