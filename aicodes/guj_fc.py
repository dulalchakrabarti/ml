import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi
from windrose import WindroseAxes
df1 = pd.read_excel('guj.xlsx', sheet_name = 'BKC')
df1 = df1[['Date','Time Blocks','Wind Speed (m/s)','Actual']].dropna()
df2 = pd.read_excel('guj1.xlsx', sheet_name = 'BKC')
df2 = df2[['Date','Time Blocks','Wind Speed (m/s)','Actual']].dropna()
df = pd.concat([df1,df2],axis=0)
decimals = 2    
df['Wind Speed (m/s)'] = df['Wind Speed (m/s)'].apply(lambda x: round(x, decimals))
df['Actual'] = df['Actual'].apply(lambda x: round(x, decimals))
dt = df['Date'].tolist()
tm = df['Time Blocks'].tolist()
ws = df['Wind Speed (m/s)'].tolist()
mw = df['Actual'].tolist()
pw = {}
for d,t,x,y in zip(dt,tm,ws,mw):
 #k = str(d)+t
 k = t
 if x in pw.keys():
  pw[str(x)+'_'+k].append(y)
 else:
  pw[str(x)+'_'+k] = y
df3 = pd.DataFrame.from_dict(pw,orient='index')
df3.to_csv('pcurve.csv')
keylist = pw.keys()
sorted(keylist)
ws1=[]
from scipy.interpolate import interp1d
for key in keylist:
 p = key.split('_')
 ws1.append(p[0])
x = sorted(ws)
y = x[1:]
for l in x:
 for m in y:
  n = interp1d(l, m)
  print(l,n,m)
'''
decimals = 1    
df['Wind Speed (m/s)'] = df['Wind Speed (m/s)'].apply(lambda x: round(x, decimals))
df['Actual'] = df['Actual'].apply(lambda x: round(x, decimals))
w2p = df[['Wind Speed (m/s)','Actual']].dropna()
w2p.to_csv('pcurve30-01.csv')

sheets = pd.ExcelFile('pow.xlsx').sheet_names
df = pd.concat([pd.read_excel('pow.xlsx', sheet_name = sheet) for sheet in sheets[-2:]], ignore_index = True)
print(df.head)
bkc = df['BKC'].tolist()
df1 = pd.read_csv('pcurve16-17.csv')
df2 = pd.read_csv('pcurve30-01.csv')
df = pd.concat([df1,df2],axis=0)
ws = df['Wind Speed (m/s)'].tolist()
mw = df['Actual'].tolist()
pw = {}
for x,y in zip(ws,mw):
 if x in pw.keys():
  pw[x].append(y)
 else:
  pw[x] = [y]
print(pw)
#print(bkc)
fcst1 = df['Forecaster-1'].tolist()
#print(fcst1)
dev1 = [abs((float(x)-float(y))/float(x))*100 for x,y in zip(actual,bkc)]
dev2 =[round(x) for x in dev1]
print(dev2)
dev3 = [abs((float(k)-float(l))/float(l))*100 for k,l in zip(actual,fcst1)]
dev4 =[round(m) for m in dev3]
print(dev4)
'''
