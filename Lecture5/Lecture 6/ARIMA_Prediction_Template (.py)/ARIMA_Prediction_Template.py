#!/usr/bin/env python
# coding: utf-8

#%%


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


#%%


from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.stattools import adfuller, kpss

from sklearn.metrics import mean_absolute_error,mean_absolute_percentage_error, mean_squared_error


#%%


from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA


#%%


df=pd.read_pickle('') # data are stored in '*****.pkl' file

