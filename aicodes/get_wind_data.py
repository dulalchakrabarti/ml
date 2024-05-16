import requests
import xarray as xr
import math
import pandas as pd
date = input('Input date(YYYYMMDD)?')
tm = input('Input time in UTC(00 or 06 or 12 or 18)?')
urlair="http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs"+date+"/gfs_0p25_1hr_"+tm+"z"
dair=xr.open_dataset(urlair)
dair_all = xr.Dataset()
time = dair.variables['time']
lat = dair.variables['lat']
lon = dair.variables['lon']
lev = dair.variables['lev']
params = {'ugrdprs':'WINDX','vgrdprs':'WINDY'}
keylist = params.keys()
for key in keylist:
  dair1 = dair[key][0:120,0,448,282]
  dair_all = dair_all.merge(dair1)
df111 = dair_all.to_dataframe()
dair2_all = xr.Dataset()
for key in keylist:
  dair2 = dair[key][0:120,1,448,282]
  dair2_all = dair2_all.merge(dair2)
df321 = dair2_all.to_dataframe()
df_=pd.concat([df111,df321])
df_.to_csv("rev.csv")
print("Downloaded 5 days wind data....")
lines = [line.rstrip('\n') for line in open('rev.csv')]
gl = open('rev_turb.csv','w')
for line in lines[1:]:
 line = line.split(',')
 u = float(line[-2])
 v = float(line[-1])
 speed = math.sqrt(u*u+v*v)
 gl.write(line[0]+','+str(speed)+'\n')
 print(line[0],speed)

