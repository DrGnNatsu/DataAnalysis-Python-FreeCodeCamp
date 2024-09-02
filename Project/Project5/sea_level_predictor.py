import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Plot the line of best fit
    # Get slope, intercept, and r_value for first line of best fit
    slope, intercept, _, _, _ = linregress(x, y)

    # Extend x-values to 2050
    x_1 = np.arange(x.min(), 2051)
    plt.plot(x_1, intercept + slope * x_1, 'r', label='fitted line')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    slope, intercept, _, _, _ = linregress(x_recent, y_recent)
    x_2 = np.arange(2000, 2051)

    plt.plot(x_2, intercept + slope * x_2, 'g', label='fitted line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


if __name__ == "__main__":
    draw_plot()
