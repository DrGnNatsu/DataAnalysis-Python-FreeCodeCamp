import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

x = np.linspace(0, 10, 5)
print(x)
y = np.cumsum(np.random.randn(5, 6), 0)
print(y)
plt.figure(figsize=(12, 7))
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')

plt.show()
