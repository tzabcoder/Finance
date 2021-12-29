import pandas_ta as ta
import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'AAPL'

data = yf.download(ticker, period='1y', interval='1h')

#Calculate Supertrend Indicator
supertrend = ta.supertrend(data['High'], data['Low'], data['Close'], 14, 3)

print(data)
print(supertrend)

plt.plot(data['Close'])
plt.plot(supertrend)
plt.show()