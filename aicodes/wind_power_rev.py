#Wind power forecast for Powerica Gujrat
#Author: D. Chakrabarti
import requests
import datetime
import os
# Remove old files
cmd = "rm AMB* BTV* CPD* NGH* TDI* TKD*"
returned_value = os.system(cmd)  # returns the exit code in unix
if returned_value == 0:
 print('Successfully removed old site files')
# Calculate day ahead
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
#daynext = NextDay_Date.strftime ('%d-%m-%y') # format the date to ddmmyy
daynext = '01-04-24' # format the date to ddmmyy
#Store power curve in a dictionary
wpow = [line.rstrip('\n') for line in open('wind2pow.csv')]
wp = {}
for p in wpow:
 p = p.split(',')
 wp[p[0]] = p[1]
#Read turbine location names
lines = [line.rstrip('\n') for line in open('turb_name.csv')]
# Read and calculate wind forecast for day ahead
for num in range(len(lines)):
 line = lines[num].split(',')
 fl = open(line[3]+'_rev','w+')
 fl.write('site'+','+'lat'+','+'lon'+','+'time'+','+'ws(m/s)'+','+'pow(kw)'+'\n')
 url = 'https://mosdac.gov.in/apienergy/wind?lat='+line[1]+'&lon='+line[2]
 response = requests.get(url)
 data = response.json()
#Filter day ahead data and calculate wind power for each site and add to total power
 ptot = 0
 for dct in data:
  if daynext in dct['time']:
   spd = round(float(dct['speed']))
   ptot+=int(wp[str(spd)])
   fl.write(line[3]+','+line[1]+','+line[2]+','+dct['time']+','+str(spd)+','+wp[str(spd)]+'\n')
print(ptot,'KW')
