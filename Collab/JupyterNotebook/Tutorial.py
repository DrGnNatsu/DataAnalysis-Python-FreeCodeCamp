import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import requests

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe

    # ====================================================================================================
    # x = np.linspace(0, 10, 500)
    # y = np.cumsum(np.random.randn(500, 6), 0)
    #
    # plt.figure(figsize=(12, 7))
    # plt.plot(x, y)
    # plt.legend('ABCDEF', ncol=2, loc='upper left')  # Legend: create a legend with 2 columns
    # plt.show()

    # ====================================================================================================
    def get_historic_price(symbol, after='2018-09-01'):
        url = 'https://api.kraken.com/0/public/OHLC'
        pair = f"{symbol.upper()}USD"  # XBTUSD when symbol='xbt' for example

        resp = requests.get(url, params={
            "pair": pair,
            'interval': 60,
            'since': str(int(pd.Timestamp(after).timestamp()))
        })
        resp.raise_for_status()

        data = resp.json()

        results_key = [k for k in data['result'].keys() if k != 'last'][0]
        results = [
            (close_time, float(open), float(high), float(low), float(close), float(volume))
            for (close_time, open, high, low, close, vwap, volume, count)
            in data['result'][results_key]
        ]
        df = pd.DataFrame(results, columns=[
            'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume'
        ])
        df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
        df.set_index('CloseTime', inplace=True)
        return df


    last_week = (pd.Timestamp.now() - pd.offsets.Day(7))
    print(last_week)

    btc = get_historic_price('btc', after=last_week)
    eth = get_historic_price('eth', after=last_week)

    print(f"{btc.head()}\n")
    print(f"{btc.info()}\n")
    btc['ClosePrice'].plot(figsize=(15, 7))
    plt.show()

    print(f"{eth.head()}\n")
    print(f"{eth.info()}\n")
    eth['ClosePrice'].plot(figsize=(15, 7))
    plt.show()

    # ====================================================================================================
    # output_notebook()
    #
    # p1 = figure(x_axis_type="datetime", title="Crypto Prices", width=800)
    # p1.grid.grid_line_alpha = 0.3
    # p1.xaxis.axis_label = 'Date'
    # p1.yaxis.axis_label = 'Price'
    #
    # print(f"BTC Index:\n{btc.index}\n")
    # p1.line(str(btc.index), btc['ClosePrice'], color='#f2a900', legend='Bitcoin')
    # # p1.line(eth.index, eth['ClosePrice'], color='#A6CEE3', legend='Ether')
    #
    # p1.legend.location = 'top_left'
    #
    # show(p1)

    # ====================================================================================================
    with pd.ExcelWriter('cryptos.xlsx') as writer:
        btc.to_excel(writer, sheet_name='Bitcoin')
        eth.to_excel(writer, sheet_name='Ether')

    writer._save()
