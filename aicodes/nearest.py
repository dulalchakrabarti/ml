import pandas as pd
import math
from haversine import haversine, Unit
stn = {}
turb = {}
lines = [line.rstrip('\n') for line in open('guj_aws_lat_long_50.csv')]
for inp in lines:
 lst = inp.split(',')
 if len(lst)>3:
  stn[lst[3]] = [lst[4],lst[5]]
lines = [line.rstrip('\n') for line in open('turb_name.csv')]
for inp in lines:
 lst = inp.split(',')
 if len(lst)>3:
  turb[lst[3]] = [lst[3],lst[1],lst[2]]
keylist1 = turb.keys()
sorted(keylist1)
keylist2 = stn.keys()
sorted(keylist2)
dist = []
marker = []
for key1 in keylist1:
 for key2 in keylist2:
  lat1 = float(turb[key1][1])
  lat2 = float(stn[key2][0])
  lon1 = float(turb[key1][2])
  lon2 = float(stn[key2][1])
  origin = (lat1,lon1)
  dest = (lat2,lon2)
  dist = haversine(origin, dest)
  marker.append([key1,key2,dist])
def Sort(sub_li):
 
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[2])
    return sub_li
sub_li = marker
opt_li = Sort(sub_li)
count=1
for item in opt_li:
 if float(item[2]) < 50:
  print(item,count)
  print(turb[item[0]],stn[item[1]])
  count+=1

