import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_csv('hist.csv')
dttm = df['date_time_slot'].tolist()
mw = df['power_mw'].tolist()
dt = []
for x,y in zip(dttm,mw):
 x = x.split()
 dt.append(x[0])
fdt = input('fcast date(ex.16/04/2024)?')
endi = dt.index(fdt)
sti = endi - (96*7)
df1 = df.loc[sti:endi]
df1.to_csv('tmp.csv')
