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
params = {'ugrdprs':'WINDX','vgrdprs':'WINDY'}
keylist = params.keys()
for key in keylist:
 #print(dair[key].shape)
 dair1 = dair[key][0:25,0,447:450,282:284]
 dair_all = dair_all.merge(dair1)
df = dair_all.to_dataframe()
df1 = pd.DataFrame()
df1['ws'] = df['ugrdprs']**2+df['vgrdprs']**2
lws = df1['ws'].tolist()
lws1 = [math.sqrt(x) for x in lws]
lws2 = [round(x) for x in lws1]
lws3 = [wp[str(x)] for x in lws2]
df['kw'] = lws3
df.to_csv('rev_'+mydate+hh+'.csv')
#print('Downloaded rev_'+mydate+hh+'.csv wind data....')
df2=pd.read_csv('rev_'+mydate+hh+'.csv')
#print(df2['lat'].max(),df2['lat'].min(),df2['lon'].max(),df2['lon'].min())
x = np.linspace(df2['lon'].min(),df2['lon'].max(),64)
y = np.linspace(df2['lat'].min(),df2['lat'].max(),64)
arr = np.meshgrid(x, y)
x_1 = np.ravel(arr[0])
y_1 = np.ravel(arr[1])
df3 = pd.DataFrame({'lon':x_1,'lat':y_1})
df3.to_csv('b2g.csv')

