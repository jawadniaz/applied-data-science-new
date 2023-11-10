# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:11:38 2023

@author: jawad
"""
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from an Excel file."""
    return pd.read_excel(file_path)

def total_visits_by_city(data):
    """Calculate the total number of tourist visits for each city."""
    total_visits = {city: sum(values) for city, values in data.items()}
    return total_visits

def plot_pie_chart(total_visits):
    """Generate a pie chart for the total tourist visits to different cities."""
    fig, ax = plt.subplots()
    ax.pie(total_visits.values(), labels=total_visits.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Ensure that the pie chart is drawn as a circle.
    plt.title('Total Tourist Visits to UK Cities (2008-2022)')
    plt.show()

# File path to the Excel data
file_path = 'C:\Program Files\Spyder\pkgs\pandas\io\2 Pie plot visualization.xlsx'

# Load data from the Excel file
df = load_data(file_path)

# Extracting relevant columns (assuming the columns are named as the cities)
city_columns = ['London', 'Edinburgh', 'Manchester', 'Oxford', 'Bath']
city_data = {city: df[city].tolist() for city in city_columns}

# Calculate total visits by city
total_visits_data = total_visits_by_city(city_data)

# Generate and display the pie chart
plot_pie_chart(total_visits_data)
