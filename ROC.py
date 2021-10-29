import talib
import yfinance as yf
import matplotlib.pyplot as plt

PERIOD = '5y'
INTERVAL = '1d'
ticker = 'AAPL'

data = yf.download(ticker, period=PERIOD, interval=INTERVAL)

"""
ROC = ((closing price(p) - closing price(p - n)) / closing price(p - n)) * 100

where:
- closing price(n) = closing price of the most recent period
- closing price(p - n) = closing price n periods before most recent period

NOTE:
    - Smaller n values (periods before) will react more quickly to price 
    changes compared to larger n values 
    - Short n values are used for short term where larger n values are used for a 
    longer term
"""

#Calculating ROC
roc = talib.ROC(data['Adj Close'], timeperiod=200)
roc.dropna(inplace=True)

plt.plot(roc)
plt.show()
