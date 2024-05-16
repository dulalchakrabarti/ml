import pandas as pd
import math
stn = {}
lines = [line.rstrip('\n') for line in open('guj_aws_lat_long.csv')]
for inp in lines:
 lst = inp.split(',')
 if len(lst)>3:
  stn[lst[3]] = [lst[4],lst[5]]
date = input('Input date(2018-03-29)?')
dte = date.split('-')
df = pd.read_csv('guj'+dte[2]+dte[1]+dte[0]+'.csv')
stn_list = df['stn'].tolist()
kw_list = df['kw'].tolist()
gust_list = df['gust'].tolist()
date_list = df['date'].tolist()
tim_list = df['time'].tolist()
fl = open('gujrev'+dte[2]+dte[1]+dte[0]+'.csv','w')
fl.write('stn'+','+'lat'+','+'lon'+','+'date'+','+'time'+','+'kw'+','+'gust'+'\n')
all_l = zip(stn_list,date_list,tim_list,kw_list,gust_list)
for item in all_l:
 if math.isnan(item[3]):
  pass
 else:
  kw1 = round(float(item[3]))
  gust1 = round(float(item[4]))
 fl.write(item[0]+','+str(stn[item[0]][0])+','+str(stn[item[0]][1])+','+item[1]+','+item[2]+','+str(kw1)+','+str(gust1)+'\n')
 print(item[0],stn[item[0]][0],stn[item[0]][1],item[1],item[2],item[3],item[4])
