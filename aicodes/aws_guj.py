import time
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from haversine import haversine, Unit
geolocator = Nominatim(user_agent="aws_new", timeout = None)
#read lat long file & store in a dictionary
sdate = input('Start date(2018-03-29)?')
sdte = sdate.split('-')
edate = input('End date(2018-03-29)?')
edte = edate.split('-')
stn = {}
lines = [line.rstrip('\n') for line in open('guj_aws_lat_long.csv')]
for inp in lines:
 lst = inp.split(',')
 if len(lst)>3:
  stn[lst[3]] = [lst[4],lst[5]]
#print(stn)
#http://aws.imd.gov.in:8091/AWS/dataview.php?#a=AWS&b=GUJARAT&c=RAJKOT&d=TARGHADIA_AMFU&e=2024-05-11&f=2024-05-11&g=ALL_HOUR&h=ALL_MINUTE
url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=AWS&b=GUJARAT&c=RAJKOT&d=TARGHADIA_AMFU&e="+sdate+'&f='+edate+"&g=ALL_HOUR&h=ALL_MINUTE"
html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows:
 cols = tr.findAll('td')
 lst = []
 for td in cols:
  lst.append(td.get_text().encode("utf-8"))
 if len(lst)>2:
  lst = [x.decode() for x in lst]
  name = lst[2]
  dt = lst[3]
  tm = lst[4]
  wd = lst[11]
  ws = lst[12]
  wgust = lst[13]
  txt = dt+'_'+tm+'_'+wd+'_'+ws+'_'+wgust
  stn[name].append(txt)
url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=AGRO&b=GUJARAT&c=ALL_DISTRICT&d=ALL_STATION&e="+sdate+'&f='+edate+"&g=ALL_HOUR&h=ALL_MINUTE"
html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows:
 cols = tr.findAll('td')
 lst = []
 for td in cols:
  lst.append(td.get_text().encode("utf-8"))
 if len(lst)>2:
  lst = [x.decode() for x in lst]
  name = lst[2]
  dt = lst[3]
  tm = lst[4]
  wd = lst[11]
  ws = lst[12]
  wgust = lst[13]
  txt = dt+'_'+tm+'_'+wd+'_'+ws+'_'+wgust
  stn[name].append(txt)
keylist = stn.keys()
sorted(keylist)
for key in keylist:
 origin = (22.04,70.61)
 dest = (float(stn[key][0]),float(stn[key][1]))
 dist = round(haversine(origin, dest))
 buf = [x+'_'+str(dist) for x in stn[key][2:]]
 stn[key][2:] = buf
fl = open('guj'+sdte[2]+sdte[1]+sdte[0]+'_'+edte[2]+edte[1]+edte[0]+'.csv','w')
fl.write('stn'+','+'lat'+','+'lon'+','+'date'+','+'time'+','+'wd'+','+'ws'+','+'kw'+','+'gust'+','+'dist'+'\n')
wpow = [line.rstrip('\n') for line in open('wind2pow.csv')]
wp = {}
for p in wpow:
 p = p.split(',')
 wp[p[0]] = p[1]
for key in keylist:
 obs15 = [x.split('_') for x in stn[key][2:]]
 if len(obs15) > 50:
  for item in obs15:
   if item[3] != '' and item[4] != '' and int(item[4]) > int(item[3]):
    mps = float(item[3])*.514
    mps = round(mps)
    pw = int(wp[str(mps)])*19
    txt = key+','+stn[key][0]+','+stn[key][1]+','+item[0]+','+item[1]+','+item[2]+','+str(mps)+','+str(pw)+','+str(item[-2])+','+str(item[-1])+'\n'
    fl.write(txt)
    #print(len(obs15))
fl.close()

