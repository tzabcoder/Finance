import talib
import yfinance as yf
import matplotlib.pyplot as plt 

ticker = 'AAPL'
data = yf.download(ticker, period='5y', interval='1d')

#Calculate Bollinger Bands
upper, middle, lower = talib.BBANDS(data['Close'], timeperiod=20)

data['BB_Upper'] = upper 
data['BB_Middle'] = middle
data['BB_Lower'] = lower

print(data)

plt.plot(data['Close'])
plt.plot(data['BB_Upper'])
plt.plot(data['BB_Middle'])
plt.plot(data['BB_Lower'])
plt.show()