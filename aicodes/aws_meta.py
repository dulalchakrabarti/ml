import pandas as pd
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
date = input('Input date(2018-03-29)?')
time = input('Input time in UTC(1)?')

gl = open('aws_meta.csv','w')
geolocator = Nominatim(user_agent="aws_meta", timeout = None)
count=0
st_lst = ['ANDAMAN_AND_NICOBAR','ANDHRA_PRADESH','ARUNACHAL_PRADESH','ASSAM','BANGLADESH','BHUTAN','BIHAR','CHANDIGARH','CHHATISGARH','DAMAN_AND_DIU','DELHI',
'GOA','GUJARAT','HARYANA','HIMACHAL_PRADESH','JAMMU_AND_KASHMIR','JHARKHAND','KARNATAKA','KERALA','LAKSHADWEEP','MADHYA_PRADESH',
'MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','NEPAL','ORISSA','PUDUCHERRY','PUNJAB','RAJASTHAN','SIKKIM',
'TAMIL_NADU','TELANGANA','TRIPURA','UTTARAKHAND','UTTAR_PRADESH','WEST_BENGAL']
gl.write('stn'+','+'lat'+','+'lon'+','+'rain'+'\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=aws&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
 html = requests.get(url).text
 soup = BeautifulSoup(html,"lxml")
 table = soup.find('table')
 rows = table.findAll('tr')
 for tr in rows:
  cols = tr.findAll('td')
  lst = []
  for td in cols:
   lst.append(td.get_text())
  if len(lst) > 2:
   name = lst[2]
   location = geolocator.geocode(name)
   if location != None:
    gl.write(name+','+str(location.latitude)+','+str(location.longitude)+'\n')
   else:
    gl.write(name+','+'not found'+'\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=arg&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
 html = requests.get(url).text
 soup = BeautifulSoup(html,"lxml")
 table = soup.find('table')
 rows = table.findAll('tr')
 for tr in rows:
  cols = tr.findAll('td')
  lst = []
  for td in cols:
   lst.append(td.get_text())
  if len(lst) > 2:
   name = lst[2]
   location = geolocator.geocode(name)
   if location != None:
    gl.write(name+','+str(location.latitude)+','+str(location.longitude)+'\n')
   else:
    gl.write(name+','+'not found'+'\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=agro&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
 html = requests.get(url).text
 soup = BeautifulSoup(html,"lxml")
 table = soup.find('table')
 rows = table.findAll('tr')
 for tr in rows:
  cols = tr.findAll('td')
  lst = []
  for td in cols:
   lst.append(td.get_text())
  if len(lst) > 2:
   name = lst[2]
   location = geolocator.geocode(name)
   if location != None:
    gl.write(name+','+str(location.latitude)+','+str(location.longitude)+'\n')
   else:
    gl.write(name+','+'not found'+'\n')
for item in st_lst:
 url = "http://aws.imd.gov.in:8091/AWS/dataview.php?a=AWSAGRO&b="+item+"&c=ALL_DISTRICT&d=ALL_STATION&e="+date+"&f="+date+"&g="+time+"&h=ALL_MINUTE"
 html = requests.get(url).text
 soup = BeautifulSoup(html,"lxml")
 table = soup.find('table')
 rows = table.findAll('tr')
 for tr in rows:
  cols = tr.findAll('td')
  lst = []
  for td in cols:
   lst.append(td.get_text())
  if len(lst) > 2:
   name = lst[2]
   location = geolocator.geocode(name)
   if location != None:
    gl.write(name+','+str(location.latitude)+','+str(location.longitude)+'\n')
   else:
    gl.write(name+','+'not found'+'\n')

