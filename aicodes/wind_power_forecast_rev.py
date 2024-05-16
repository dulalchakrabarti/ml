#Wind power forecast for Powerica Gujrat
#Author: D. Chakrabarti
import requests
import datetime
import os
import math
import pandas as pd
# Remove old files
cmd = "rm rev_*AMB* rev_*BTV* rev_*CPD* rev_*NGH* rev_*TDI* rev_*TKD*"
returned_value = os.system(cmd)  # returns the exit code in unix
if returned_value == 0:
 print('Successfully removed old site files')
# Calculate day ahead
NextDay_Date = datetime.datetime.today() #+ datetime.timedelta(days=1)
daynext = NextDay_Date.strftime ('%d-%m-%y') # format the date to ddmmyy
#Store power curve in a dictionary
wpow = [line.rstrip('\n') for line in open('wind2pow.csv')]
wp = {}
for p in wpow:
 p = p.split(',')
 wp[p[0]] = p[1]
#Read turbine location names
lines = [line.rstrip('\n') for line in open('turb_name.csv')]
# Read and calculate wind revision forecast for current day
for num in range(len(lines)):
 line = lines[num].split(',')
 fl = open('rev_'+line[3],'w+')
 fl.write('site'+','+'lat'+','+'lon'+','+'time'+','+'ws(m/s)'+','+'pow(kw)'+'\n')
 url = 'https://mosdac.gov.in/apienergy/wind?lat='+line[1]+'&lon='+line[2]
 response = requests.get(url)
 data = response.json()
#Filter day ahead data and calculate wind power for each site and add to total power
 ptot = 0
 for dct in data:
  if daynext in dct['time']:
   spd =math.floor(float(dct['speed']))
   ptot+=int(wp[str(spd)])
   fl.write(line[3]+','+line[1]+','+line[2]+','+dct['time']+','+str(spd)+','+wp[str(spd)]+'\n')
 fl.close()
p = pd.DataFrame()
for line in lines:
 line = line.split(',')
 df = pd.read_csv('rev_'+line[3])
 p[line[3]] = df[['pow(kw)']]
p['time'] = df[['time']]
column_names = list(p.columns)
p['power_total']= p[column_names[:-2]].sum(axis=1)
pt1 = p['time'].tolist()
pt2 = p['power_total'].tolist()
dfd = {'time':pt1,'power(kw)':pt2}
dfp = pd.DataFrame.from_dict(dfd)
dfp.to_csv('fc_day_rev1.csv')

