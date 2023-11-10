# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:02:01 2023

@author: jawad
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = 'C:\Program Files\Spyder\pkgs\pandas\io\Question 1 International Student Enrollment Trends in the UK.xlsx'  # Update the file path if needed
df = pd.read_excel(file_path)

# Plotting
plt.figure(figsize=(10, 6))

countries = ['India', 'Pakistan', 'Bangladesh', 'Sri_Lanka', 'Afghanistan']

for country in countries:
    plt.plot(df['Year'], df[country], label=country)

plt.title('Number of International Students in the UK (2008-2022)')
plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.legend()
plt.grid(True)
plt.show()
