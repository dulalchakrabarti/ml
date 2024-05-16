import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_csv('hist.csv')
dttm = df['date_time_slot'].tolist()
mw = df['power_mw'].tolist()
fl = open('hist15m.csv','w')
fl.write('date'+','+'mw'+'\n')
for x,y in zip(dttm,mw):
 x = x.split()
 l = x[0].split('/')
 m = l[1]+'/'+l[0]+'/'+l[2]
 fl.write(m+' '+x[1]+','+str(y)+'\n')
 print(m,x[1],y)
fl.close()
