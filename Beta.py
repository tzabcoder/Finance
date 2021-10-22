"""
1.) BETA CALCULATION
Measures the volatility of an individual stock compared to the
systematic risk of the entire market

Beta Coefficient(B) = Covariance(Re, Rm) / Variance(Rm)

where:
Re - return on an individual stock
Rm - return on the overall market

Beta Results:
    (1) When B = 1.0
    - Indicates that its price activity is strongly correlated with 
    the market (contains systematic risk, although can't detect idiosyncratic 
    risk)
    - Adding a stock with B = 1.0 will not add any risk to the portfolio,
    but will not generate any excess returns 
    (2) When B < 1.0 
    - Means that the asset is theoretically less volitile than the market
    - Including a stock in a portfolio with B < 1.0 will make the portfolio 
    less risky compared to the same portfolio without the stock (although
    tend to provide a lower return)
    (3) When B > 1.0
    - Means that the asset is theoretically more volitile than the market
    - Including stocks with B > 1.0 will increase the risk of the portfolio,
    but may increase the expected return
    - Note: B = 1.2 -> 20% more volitile than the market
    (4) When B < 0.0
    - A negative B means that the stock is inversely correlated with the 
    market (stock could be thought of having an opposite image of benchmark 
    trends)

-----------------------------------------------------------------
2.) VARIANCE CALCULATION
Measures how far the market's data points spread out from their 
average value

Variance = SUM[(Xi - Xm) ** 2] / (n - 1)

where:
Xi - ith data point
Xm - mean of all data points 
n - number of data points

-----------------------------------------------------------------
3.) COVARIANCE CALCULATION
Measures how the changes in a stock's returns are related to
the changes in the market's returns

Covariance(x, y) = SUM[(Xi - Xm) * (Yi - Ym)] / (n - 1)

where:
Xi - ith data point in the X set
Yi - ith data point in the Y set
Xm - mean of X data set
Ym - mean of Y data set
n - number of data points
"""

#Program Imports 
import yfinance as yf
import numpy as np

class CalcBeta:
    __MARKET_TICK = 'SPY'     #Used for market data
    __PERIOD = '5y'           #For a period of 5 years
    __INTERVAL = '1d'         #One day granularity

    def __init__(self, ticker):
        self.ticker = ticker
        self.data = self.__process_data()

    def __process_data(self):
        #Getting Data
        symbols = [self.ticker, self.__MARKET_TICK]     #stock, market
        try:
            #Download data(Keeping only the Adj Close data)
            data = yf.download(symbols, period=self.__PERIOD, interval=self.__INTERVAL, progress=False)['Adj Close'] 
        except Exception as e:
            print(e)
            exit()

        #Processing Data
        price_change = data.pct_change()                  #Convert price data to daily percent change
        df = price_change.drop(price_change.index[0])     #Drop the first row (contains Nans)

        return df

    def __Variance(self):
        data_len = len(self.data[self.__MARKET_TICK])                   #Length of market data

        market_mean = self.data[self.__MARKET_TICK].mean()              #Calculate market mean 
        var_add = self.data[self.__MARKET_TICK].add(market_mean)        #Add the mean to each data point
        var = var_add.pow(2)                                            #Square each data point
        var = var.sum()                                                 #Add all of the data points

        variance = var / (data_len - 1)                                 #Calculate Variance

        return variance

    def __Covariance(self): 
        data_len = len(self.data)                                       #Length of market data and stock data
        
        market_mean = self.data[self.__MARKET_TICK].mean()              #Calculate market mean
        stock_mean = self.data[self.ticker].mean()                      #Calculate stock mean
        market_add = self.data[self.__MARKET_TICK].add(market_mean)     #Add market mean to each data point
        stock_add = self.data[self.ticker].add(stock_mean)              #Add stock mean to each data point
        var = market_add * stock_add                                    #Multiply market and stock data
        var = var.sum()                                                 #Sum multiplied data

        covariance = var / (data_len - 1)                               #Calculate Covariance
        
        return covariance

    def Beta(self):
        variance = self.__Variance()
        covariance = self.__Covariance()

        #Note - The calculated Beta is slightly higher than Beta calculations online
        beta_coeff = covariance / variance
        return beta_coeff
