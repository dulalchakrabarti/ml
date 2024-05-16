import pandas as pd
df = pd.read_csv('hist.csv')
slots = df['date_time_slot'].tolist()
for slot in slots:
 if '30/03/2024' in slot:
  print(slot)
'''
ptot = df['power_mw'].tolist()
l = len(slots)
p = len(ptot)
dpow_14 = {}
pl = []
tml = []
days = 1
for num in range(0,l,96):
 tml.extend(slots[num:num+96])
 pl.extend(ptot[num:num+96])
 if days%7 == 0:
  print(len(tml),len(pl))
  dpow_14[days] = [tml,pl]
  tml=[]
  pl=[]
 days+=1
keylist = dpow_14.keys()
sorted(keylist)
for key in keylist:
 d1 = {'date_time':dpow_14[key][0],'power_mw':dpow_14[key][1]}
 df = pd.DataFrame(d1)
 if key==364:
  tm = df['date_time'].tolist()
  pt = df['power_mw'].tolist()
  print(len(tm),len(pt))
  print(key,tm[0:5],pt)
''' 

