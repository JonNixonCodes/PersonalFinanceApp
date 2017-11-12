"""
Hello world program for visualising historical stock data
using: pandas, pandas-datareader, matplotlib
"""
import datetime as dt
import time
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

watchlist = ['TLS.AX', 'ANZ.AX', 'WFD.AX']
watchlist = ['F']
end = dt.datetime(2017,11,11)
start = dt.datetime(2016,11,11)
for stock in watchlist:
    print(stock)
    df = web.DataReader(stock, 'yahoo', start, end)
    #graph data
    df.plot()
    plt.show()
    #save dataframe
    fname = stock+'.csv'
    df.to_csv(fname)
    df = pd.read_csv(fname, parse_dates=True, index_col=0)
    print(df.head())

