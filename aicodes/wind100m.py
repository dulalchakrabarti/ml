#This program downloads the basic wind data available from NOAA servers
#Author: Dulal Chakrabarti
#Date: 22.03.2024
#
# Install python modules
import pandas as pd
import numpy as np
import xarray as xr
import requests
def get_df(mydate,hh):
 '''
 in: date,hh
 out:df
 '''
 import time
 import datetime
 import math
 import pytz
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
 params = {'ugrd100m':'WINDX','vgrd100m':'WINDY'}
 keylist = params.keys()
 for key in keylist:
  dair1 = dair[key][0:25,448,282]
  dair_all = dair_all.merge(dair1)
 df = dair_all.to_dataframe()
 df['ws2'] = df['ugrd100m']**2+df['vgrd100m']**2
 lws = df['ws2'].tolist()
 lws1 = [math.sqrt(x) for x in lws]
 lws2 = [round(x,2) for x in lws1]
 df['ws'] = lws2
 #lws3 = [float(wp[str(x)])*.019 for x in lws2]
 #df['mw'] = lws3
 fname = 'rev_'+mydate+hh+'.csv'
 df.to_csv(fname)
 df1 = pd.read_csv(fname,parse_dates=['time'],index_col=['time'])
 df2 = pd.DataFrame(df1.resample('15min').interpolate().ffill())
 local_timezone = pytz.timezone('Asia/Kolkata')
 df2['ist']=df2.index.tz_localize('UTC').tz_convert(local_timezone)
 df2.set_index(['ist'], inplace = True)
 df2.drop(['lat','lon','ugrd100m','vgrd100m','ws2'], axis='columns', inplace=True)
 dttm = df2.index.tolist()
 dt_tm = [x.strftime('%Y-%m-%d %H:%M') for x in dttm]
 tm = [x.split() for x in dt_tm]
 tm1 = [x[1].split(':') for x in tm]
 tm2 = [(x[0]+':'+x[1]+'-'+x[0]+':'+str(int(x[1])+15)) for x in tm1]
 tm3 = [x[0] for x in tm]
 tm4 = [(x+' '+y) for x,y in zip(tm3,tm2)]
 df2['time_slot'] = tm4
 #df2.set_index(['time_slot'], inplace = True)
 lws = df2['ws'].tolist()
 lws1 = [round(x,2) for x in lws]
 #lmw = df2['mw'].tolist()
 #lmw1 = [int(x) for x in lmw]
 df2['ws'] = lws1
 df2.set_index(['time_slot'], inplace = True)
 #print(df2.head)
 #df2['mw'] = lmw1
 return df2
#
#Wind data from GFS 0.25
#
#Store power curve in a dictionary
wpow = [line.rstrip('\n') for line in open('wind2pow.csv')]
wp = {}
for p in wpow:
 p = p.split(',')
 wp[p[0]] = p[1]
df = pd.DataFrame()
while 'True':
 mydate = input('Forecast date(20240408)?')
 if mydate == '':
  df.to_csv('tmp.csv')
  exit()
 hh = input('Forecast time in UTC(00)?')
 mydf = get_df(mydate,hh)
 df = pd.concat([df,mydf],axis=0)

