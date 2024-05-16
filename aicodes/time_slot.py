import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_csv('hist.csv')
dttm = df['date_time_slot'].tolist()
mw = df['power_mw'].tolist()
fl = open('slot15m.csv','w')
fl.write('date'+','+'mw'+'\n')
add = 15
count=0
for x,y in zip(dttm,mw):
 x = x.split()
 l = x[0].split('/')
 m = l[1]+'/'+l[0]+'/'+l[2]
 x3 = x[1].split(':')
 x2 = int(x3[1])+add
 if x2 > 45:
  x2 = '00'
 txt = x[1]+'-'+str(x2)
 if count < 96:
  fl.write(m+' '+txt+'\n')
  count+=1
 else:
  exit()
fl.close()
