import talib
import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'AAPL'
data = yf.download(ticker, period='5y', interval='1d')

#Calculate Average True Range(ATR)
atr = talib.ATR(data['High'], data['Low'], data['Close'], 10)
atr_6 = atr * 6
atr_4 = atr * 4

plt.plot(data['Close'])
plt.plot(atr)
plt.plot(atr_6)
plt.plot(atr_4)
plt.show()