#This program downloads the basic wind data available from NOAA servers
#Author: Dulal Chakrabarti
#Date: 22.03.2024
#
# Install python modules
import pandas as pd
import numpy as np
import xarray as xr
import requests
import time
import datetime
import math
import glob
import re
df = pd.read_csv('rev_2024041600.csv',parse_dates=['time'],index_col=['time'])
df1 = pd.DataFrame(df.resample('15min').interpolate().ffill())
df2 = pd.DataFrame()
df2['ws'] = df1['ugrdprs']**2+df1['vgrdprs']**2
df3 = df2['ws'].astype(float).tolist()
ldf3 = [math.sqrt(x) for x in df3]
df2['fws'] = ldf3
df2.to_csv('tst1.csv')
