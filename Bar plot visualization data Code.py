# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:35:30 2023

@author: jawad
"""

import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to your Excel file
file_path = 'C:\Program Files\Spyder\pkgs\pandas\io\Bar plot visualization data.xlsx'

# Load data from Excel file into a DataFrame
df = pd.read_excel(file_path)

# Plotting the bar plot
plt.figure(figsize=(15, 8))
plt.bar(df['Level1'], df['Level2'])

# Adding labels and title
plt.xlabel('Level 1')
plt.ylabel('Level 2')
plt.title('File Plan Structure - Food Standards Agency')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.tight_layout()
plt.show()
