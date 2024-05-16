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
mydate = input('Forecast date(20240408)?')
hh = input('Forecast time in UTC(00)?')
#
#Wind data from GFS 0.25
#
#Store power curve in a dictionary
wpow = [line.rstrip('\n') for line in open('wind2pow.csv')]
wp = {}
for p in wpow:
 p = p.split(',')
 wp[p[0]] = p[1]
urlair='http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs'+mydate+'/gfs_0p25_1hr_'+hh+'z'
print(urlair)
try:
 dair=xr.open_dataset(urlair)
 dair_all = xr.Dataset()
 time = dair.variables['time']
 lat = dair.variables['lat']
 lon = dair.variables['lon']
 lev = dair.variables['lev']
except:
 time.sleep(5)
 dair=xr.open_dataset(urlair)
 dair_all = xr.Dataset()
 time = dair.variables['time']
 lat = dair.variables['lat']
 lon = dair.variables['lon']
 lev = dair.variables['lev']
params_111 = {'ugrdprs':'WINDX','vgrdprs':'WINDY'}
params_100 = {'ugrd100m':'WIND100X','vgrd100m':'WIND100Y'}
keylist_100 = params_100.keys()
for key in keylist_100:
 #print(dair[key].shape)
 dair1 = dair[key][0:25,448,282]
 dair_all = dair_all.merge(dair1)
df100 = dair_all.to_dataframe()
fname = 'rev_'+mydate+hh+'.csv'
df100.to_csv(fname)
df100m = pd.read_csv(fname,parse_dates=['time'],index_col=['time'])
df100m['ws100'] = df100m['ugrd100m']**2+df100m['vgrd100m']**2
lws = df100m['ws100'].tolist()
lws1 = [math.sqrt(x) for x in lws]
lws2 = [round(x) for x in lws1]
lws3 = [float(wp[str(x)])*.019 for x in lws2]
df100m['mw100'] = lws3
mw15min = pd.DataFrame(df100m.resample('15min').interpolate().ffill())
print(mw15min.head)
'''
df2 = pd.DataFrame()
df2['ws100'] = df100['ugrd100m']**2+df100['vgrd100m']**2
lws = df2['ws100'].tolist()
lws1 = [math.sqrt(x) for x in lws]
lws2 = [round(x) for x in lws1]
lws3 = [float(wp[str(x)])*.019 for x in lws2]
df2['mw100'] = lws3
#df['time']= pd.to_datetime(df['time'])
print(df2.head)

keylist_111 = params_111.keys()
for key in keylist_111:
 #print(dair[key].shape)
 dair1 = dair[key][0:25,0,448,282]
 dair_all = dair_all.merge(dair1)
df111 = dair_all.to_dataframe()
df1 = pd.DataFrame()
df1['ws111'] = df111['ugrdprs']**2+df111['vgrdprs']**2
lws = df1['ws111'].tolist()
lws1 = [math.sqrt(x) for x in lws]
lws2 = [round(x) for x in lws1]
lws3 = [float(wp[str(x)])*.019 for x in lws2]
df111['mw111'] = lws3
print(df111.head)

fname = 'rev_'+mydate+hh+'.csv'
df1 = pd.read_csv(fname,parse_dates=['time'],index_col=['time'])
df2 = pd.DataFrame(df1.resample('15min').interpolate().ffill())
df2['mw15'] = df2['kw']*.019
ser15 = df2.dropna(axis=1, how='all')
ser15.to_csv('tst.csv')
'''
