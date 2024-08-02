import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':

    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe

    sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

    print(f"{sales.head()}\n")
    print(f"{sales.info()}\n")
    print(f"{sales.describe()}\n")
    print(f"{sales['Unit_Cost'].describe()}\n")
