import talib 
import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'AAPL'
data = yf.download(ticker, period='5y', interval='1d')

#Calculate Keltner Channel
atr = talib.ATR(data['High'], data['Low'], data['Close'], 10)

ema = talib.EMA(data['Close'], timeperiod=20)
middle = ema 
upper = ema + 2 * atr
lower = ema - 2 * atr

data['KC_Upper'] = upper
data['KC_Middle'] = middle 
data['KC_Lower'] = lower

print(data)

plt.plot(data['Close'])
plt.plot(data['KC_Upper'])
plt.plot(data['KC_Middle'])
plt.plot(data['KC_Lower'])
plt.show()