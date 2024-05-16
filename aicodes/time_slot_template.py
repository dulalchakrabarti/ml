import pandas as pd
import numpy as np
from datetime import datetime
import time
df = pd.read_csv('slot15m.csv')
dttm = df['date'].tolist()
slot = {}
for item in dttm:
 item1 = item.split()
 slot[item1[1]] = []
st0 = input('Forecast start date for 18 UTC of previous day(20240408)?')
st1 = input('Forecast end date up to 18 UTC of current day(20240408)?')
lf = ['rev_'+st0+'18.csv','rev_'+st1+'00.csv','rev_'+st1+'06.csv','rev_'+st1+'12.csv','rev_'+st1+'18.csv']
for item in lf:
 try:
  lines = [line.rstrip('\n') for line in open(item)]
  for line in lines:
   print(line)
  time.sleep(1)
 except:
  print('file not found...',item)

