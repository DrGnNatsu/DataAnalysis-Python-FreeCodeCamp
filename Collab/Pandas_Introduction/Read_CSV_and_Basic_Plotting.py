import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe
    # =====================================================================
    # # Read the CSV file
    # df = pd.read_csv('ipynb_file/data/btc-market-price.csv', header=None)
    # df.columns = ['Timestamp', 'Price']
    # # Convert the Timestamp column to a datetime type
    # df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    # # Set the Timestamp column as the index
    # df.set_index('Timestamp', inplace=True)

    # Putting it all together: we can combine the previous steps into a single line of code
    df = pd.read_csv(
        'ipynb_file/data/btc-market-price.csv',
        header=None,
        names=['Timestamp', 'Price'],
        index_col=0,
        parse_dates=True
    )

    print(f"{df.head()}\n")
    print(f"{df.shape}\n")
    print(f"{df.dtypes}\n")
    print(f"{df.tail(3)}\n")  # Last 3 rows

    print(f"{df.dtypes}\n")

    print(f"{df.loc['2017-09-29']}\n")

    # Plotting basics
    df.plot()
    plt.show()

    plt.plot(df.index, df['Price'], color='blue', label='Bitcoin Price')
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.title('Bitcoin Price')
    plt.legend()  # This will add the legend: bảng chú giải
    plt.figure(figsize=(12, 6))
    plt.show()

    x = np.arange(-10, 11)
    plt.plot(x, x ** 2)
    plt.show()

    # =====================================================================
    # More challenging parsing
    eth = pd.read_csv('ipynb_file/data/eth-price.csv')

    print(f"{eth.head()}\n")
    print(f"{eth.dtypes}\n")

    eth = pd.read_csv('ipynb_file/data/eth-price.csv', parse_dates=True)
    # eth = pd.read_csv('data/eth-price.csv', parse_dates=True):
    # Attempts to parse the date columns in the CSV file automatically.
    # eth = pd.read_csv('ipynb_file/data/eth_price.csv'):
    # This line does not include the parse_dates parameter, so no date parsing is attempted.

    print(f"{eth.dtypes}\n")
    print(f"{pd.to_datetime(eth['UnixTimeStamp']).head()}\n")
    print(f"{pd.read_csv('ipynb_file/data/eth-price.csv', parse_dates=[0]).head()}\n")

    eth = pd.read_csv('ipynb_file/data/eth-price.csv', parse_dates=True, index_col=0)
    print(f"{eth.info()}\n")
    print(f"{eth.head()}\n")

    prices = pd.DataFrame(index=df.index)
    print(f"{prices.head()}\n")

    prices['Bitcoin'] = df['Price']
    prices['Ether'] = eth['Value']

    print(f"{prices.head()}\n")

    prices.plot(figsize=(12, 6))
    plt.show()

    prices.loc['2017-12-01':'2018-01-01'].plot(figsize=(12, 6))
    plt.show()
