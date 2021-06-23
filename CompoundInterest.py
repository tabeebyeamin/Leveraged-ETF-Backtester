import pandas as pd
import pandas_datareader.data as web
import datetime

class Stock():
    def __init__(self):
        self.ticker = None
        self.start = None
        self.end = None
        self.mult = 3

def invest(arr, start=0, dca=5000):
    for i in range(1, len(arr)):
        change = arr[i]/arr[i-1]
        start = (start + dca)*change
    return start
    
def period(arr, year=2000, start=0, dca=5000):
    print("-"*10 + str(year) + "-" + str(year+(len(arr)-1))+"-"*10)
    print("With $" + str((len(arr)-1)*dca) + " invested." )
    first21 = invest(arr, start, dca=dca)
    return first21
    

def leveraged(daily_data, mult):
    """
    100 => 130 -> 1.3X gain
    3x that is 1.9X so (1.3X-1)*3 and then add 1.
    Start any arbitrary val, like 500.
    """
    lev_daily_data = [500]
    for i in range(1, len(daily_data)):
        unlev_change = daily_data[i]/daily_data[i-1]
        lev_change = (unlev_change-1)*3+1
        lev_daily_data.append(lev_daily_data[i-1]*lev_change)
    return lev_daily_data

def backtest(stock, show_etf_data=False, show_letf_data=False):
    ticker, start_year, end_year = stock.ticker, stock.start, stock.end
    mult = stock.mult
    print("."*20+"loading backtest data for " + ticker + "."*20)
    start = datetime.datetime(start_year, 3, 1)
    end = datetime.datetime(end_year, 3, 31)
    try:
        SP500 = web.DataReader(ticker, 'yahoo', start, end)["Adj Close"].values.tolist()
    except:
        print("PLEASE MAKE SURE YOU ENTER A VALID TICKER!")
        return
    TSP500 = leveraged(SP500, mult)
    # get yearly value by getting every 252nd
    arr = []
    skip = 252
    for i in range(0, len(TSP500), skip):
        arr.append(TSP500[i])
    if (show_letf_data):
        print(arr)
    init = 0
    # zombie code :flushed:
    """
    for i in range(3):
        amount = period(arr, start=init, year=start_year)
        print("${:,.2f}". format(amount))
        init = amount
        start_year += len(arr)-1
    """
    amount = period(arr, start=init, year=start_year)
    print("${:,.2f}". format(amount))



if __name__ == "__main__":
    """
    ^GSPC: S&P500
    QQQ: NASDAQ
    AMZN: Amazon
    """
    stock = Stock()
    stock.ticker = "AMZN"
    stock.start = 2000
    stock.end = 2021
    stock.mult = 3
    backtest(stock, show_etf_data=False, show_letf_data=False)