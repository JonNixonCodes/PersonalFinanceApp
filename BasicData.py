"""
Save watchlists, Save stock data, Display stock trends
Jonathan Yu
"""
import datetime as dt
import time
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import pickle

style.use('ggplot')


def CreateWatchlist(name, stocks):
    """Create watchlist with name, and stocks"""
    watchlist_dir = 'watchlists/'
    fname = watchlist_dir+name+'.pkl'
    fp = open(fname, 'wb')
    pickle.dump(stocks, fp)
    fp.close()


def LoadWatchlist(name):
    """Load saved watchlist with name"""
    watchlist_dir = "watchlists/"
    fname = watchlist_dir+name+".pkl"
    fp = open(fname, 'rb')
    watchlist = pickle.load(fp)
    fp.close()
    return watchlist
    

def UpdatePriceData(watchlist):
    """Update and save price data on stocks in watchlist"""
    today = dt.datetime.today()
    end = today
    start = dt.datetime(today.year-5,today.month,today.day)
    stock_data_dir = "stock_data/"
    for stock in watchlist:
        print("{}:price".format(stock))
        #read data from web
        print("downloading...", end="")
        df = web.DataReader(stock, 'yahoo', start, end)
        #save data to file
        print("saving...", end="")
        fname = "{}{}_price.csv".format(stock_data_dir,stock)
        df.to_csv(fname)
        print("DONE")


def UpdateDividendData(watchlist):
    """Update and save dividend data on stocks in watchlist"""
    today = dt.datetime.today()
    end = today
    start = dt.datetime(today.year-5,today.month,today.day)
    stock_data_dir = "stock_data/"
    for stock in watchlist:
        print("{}:dividends".format(stock))
        #read data from web
        print("downloading...", end="")
        df = web.DataReader(stock, 'yahoo-dividends', start, end)
        #save data to file
        print("saving...", end="")
        fname = "{}{}_div.csv".format(stock_data_dir,stock)
        df.to_csv(fname)
        print("DONE")
        

def UpdateStockData(watchlist):
    """Update and save all data on stocks in watchlist"""
    #update stock prices
    UpdatePriceData(watchlist)
    #update dividend data
    UpdateDividendData(watchlist)

        
def LoadData(watchlist):
    """Load data from stocks in watchlist, store in dictionary"""
    all_data = {}
    stock_data_dir = "stock_data/"    
    for stock in watchlist:
        #read stock price data from file
        fname = "{}{}_price.csv".format(stock_data_dir, stock)
        df_price = pd.read_csv(fname, parse_dates=True, index_col=0)        
        #read stock dividend data from file
        fname = "{}{}_div.csv".format(stock_data_dir, stock)
        df_dividends = pd.read_csv(fname, parse_dates=True, index_col=0)
        #add stock data to dictionary
        all_data[stock] = {"price":df_price, "dividends":df_dividends}
    return all_data


def PrintData(watchlist):
    all_data = LoadData(watchlist)
    for stock in watchlist:
        print(stock)
        df = all_data[stock]
        print(df)
    

def GraphData(watchlist):
    """Save graphs of data on stocks in watchlist"""
    graph_dir = "graphs/"    
    all_data = LoadData(watchlist)
    for index,stock in enumerate(watchlist):
        df_price = all_data[stock]['price']
        #100 moving average
        df_price['100ma'] = df_price['Close'].rolling(window=100, min_periods=0).mean()
        #show figure
        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
        ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
        ax1.plot(df_price.index, df_price['Close'])
        ax1.plot(df_price.index, df_price['100ma'])
        #ax2.bar(df_price.index, df_price['Volume'])
        ax2.plot(df_price.index, df_price['Volume'])
        #save file
        fname = "{}{}.png".format(graph_dir, stock)
        plt.savefig(fname, bbox_inches='tight')
        #plt.show()
        

def main():
    return


if __name__=='__main__':
    main()
