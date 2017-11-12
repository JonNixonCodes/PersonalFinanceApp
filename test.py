from BasicData import *
import pickle
import numpy as np
import datetime as dt

watchlist = ["TLS.AX", "WFD.AX"]
#UpdateStockData(watchlist)
all_data = LoadData(watchlist)
#PrintData(watchlist)
GraphData(watchlist)
