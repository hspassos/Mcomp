import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

prices_df = pd.read_csv('prices-split-adjusted.csv')
print(prices_df.head())

x = prices_df.iloc[:30, 2].values
y = prices_df.iloc[:30, 3].values

#plt.plot(x, y)

regressor = LinearRegression()
regressor.fit(x, y)

plt.show()