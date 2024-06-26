import pandas as pd
from geopy.geocoders import Nominatim
import time
import tabula
import math
gl = open('awslatlong.csv','w')
meta = {}
lines = [line for line in open('meta_full.csv')]
for line in lines:
 line = line.split(',')
 if line[0].isdigit():
  name = line[2]
  meta[name]=[]
count=0
keylist = meta.keys()
geolocator = Nominatim(user_agent="meta_read", timeout = None)
for key in keylist:
 location = geolocator.geocode(key)
 if location != None:
  print(key,location.latitude, location.longitude)
  gl.write(key+','+str(location.latitude)+','+str(location.longitude)+'\n')
  count+=1
  time.sleep(1.0)
print(count)
'''
# convert PDF into CSV file
tabula.convert_into("rf.pdf", "rf.csv", output_format="csv", pages='all')
gl = open('dist_lat_lon.csv','w')
df = pd.read_csv('rf.csv', delimiter=',',header=None)
df_=df.dropna()
lst = [list(row) for row in df_.values]
geolocator = Nominatim(user_agent="geoapiExercises", timeout = None)
count=0
for num in range(len(lst)):
 txt = lst[num]
 buf = txt[5].split()
 #print(txt[1],txt[2],buf[-2],buf[-1])
 add =txt[1]
 location = geolocator.geocode(add)
 if location != None:
  print(add,location.latitude, location.longitude,txt[2],buf[-2],buf[-1])
  gl.write(add+','+str(location.latitude)+','+str(location.longitude)+','+str(txt[2])+','+str(buf[-2])+','+str(buf[-1])+'\n')
  count+=1
  time.sleep(1.0)
print(count)
'''
