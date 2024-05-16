'''
==============
3D quiver plot
==============

Demonstrates plotting directional arrows at points on a 3d meshgrid.
#
#This program downloads the basic marine data available from NOAA servers
#Author: Dulal Chakrabarti
#Date: 29.01.2024
#
# Install python modules
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import metpy.calc as mpcalc
from metpy.units import units
import netCDF4
import datetime
import xarray as xr
import requests
#
hr = datetime.datetime.now(datetime.UTC)
hr1 = hr.strftime('%Y-%m-%d %H:%M:%S')
hr = int(hr1[11:13])
hr = int(hr/6)
print(hr)
if hr>=0 and hr<1:
 hr = 3
 hr_ = datetime.datetime.now(datetime.UTC)- datetime.timedelta(days=1)
 hr1_ = hr_.strftime('%Y-%m-%d %H:%M:%S')
elif hr>=1 and hr<2:
 hr = 0
elif hr>=2 and hr<3:
 hr = 1
elif hr>=3:
 hr = 2
else:
 pass
HH = ['00','06','12','18']
if hr == 3:
 dt=hr1_[:10]
 dt=dt.split('-')
 mydate = dt[0]+dt[1]+dt[2]
else:
 dt=hr1[:10]
 dt=dt.split('-')
 mydate = dt[0]+dt[1]+dt[2]
print(mydate)
#
#Wind data from GFS 0.25
#
urlair='http://nomads.ncep.noaa.gov:80/dods/gfs_0p25/gfs'+mydate+'/gfs_0p25_'+HH[hr]+'z'
print(urlair)
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
 dair1 = dair[key][0,5:13:7,360:520:9,160:480:18]
 dair_all = dair_all.merge(dair1)
df = dair_all.to_dataframe()
df.to_csv('air.csv')
print("Downloaded air data....")
df1 = pd.read_csv('air.csv')
df1['lev'][df1['lev'] == 850] = 1.5
df1['lev'][df1['lev'] == 500] = 5.8
x = df1['lon'].values
y = df1['lat'].values
z = np.array([1.5,5.8])
x,y,z = np.meshgrid(x,y,z)
ax = plt.figure(figsize=(14,14)).add_subplot(projection='3d')
u = df1['ugrdprs'].values
v = df1['vgrdprs'].values
w = np.array([0.,0.])
U, V, W = np.meshgrid(u, v, w)
ax.quiver(x, y, z, U, V, W, length=1, normalize=True)

plt.show()

