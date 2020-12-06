import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.figure(figsize=(10,10))
    plt.scatter(x, y, marker='x')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    xfirstline = range(1880,2050)
    yfirstline = []
    for year in xfirstline:
      yfirstline.append(intercept + slope * year)
    plt.plot(xfirstline, yfirstline, "r", label= 'Best Fit Line 1')

    # Create second line of best fit
    x2 = df[df['Year'] >= 2000] ['Year']
    y2 = df[df['Year'] >= 2000] ['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x2, y2)
    xsecondline = range(2000,2050)
    ysecondline = []
    for year in xsecondline:
      ysecondline.append(intercept + slope * year)
    plt.plot(xsecondline, ysecondline, "g", label= 'Best Fit Line 2')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    #plt.show()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()