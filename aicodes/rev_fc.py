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
l1=['guj01042023_30042023.csv','guj01052023_31052023.csv','guj01062023_30062023.csv','guj01072023_31072023.csv','guj01082023_31082023.csv','guj01092023_30092023.csv','guj01102023_31102023.csv','guj01112023_30112023.csv','guj01122023_31122023.csv','guj01012024_31012024.csv','guj01022024_29022024.csv','guj01032024_31032024.csv','guj01042023_30042023.csv']
#tser = pd.DataFrame(columns=['time','ws'])
fl = open('tar.csv','w')
for f in l1:
 lines = [line.strip() for line in open(f)]
 for line in lines:
  line1 = line.split(',')
  if line1[0] == 'TARGHADIA_AMFU':
   txt = line1[3]+','+line1[4]+','+line1[6]+','+line1[8]+'\n'
   fl.write(txt)
fl.close()
'''
 df = pd.read_csv(file,parse_dates=['time'],index_col=['time'])
 df1 = pd.DataFrame(df.resample('15min').interpolate().ffill())
 df1['mw15'] = df1['kw']*.019
 tser = pd.concat([tser,df1['mw15']])
ser15 = tser.dropna(axis=1, how='all')
ser15.to_csv('tst.csv')
'''
