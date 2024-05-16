import pandas as pd
import requests
import json
from bs4 import BeautifulSoup

gl = open('awslatlong.csv','w')
url = "http://aws.imd.gov.in:8091/AWS/networkmeta.php?a=ARG&b=ALL_STATE"
html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows:
 cols = tr.findAll('td')
 lst = []
 for td in cols:
  lst.append(td.get_text())
 buf = ','.join(x for x in lst)
 print(buf)
 gl.write(buf+'\n')
url = "http://aws.imd.gov.in:8091/AWS/networkmeta.php?a=AWS&b=ALL_STATE"
html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows:
 cols = tr.findAll('td')
 lst = []
 for td in cols:
  lst.append(td.get_text())
 buf = ','.join(x for x in lst)
 print(buf)
 gl.write(buf+'\n')
url = "http://aws.imd.gov.in:8091/AWS/networkmeta.php?a=AGRO&b=ALL_STATE"
html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")
table = soup.find('table')
rows = table.findAll('tr')
for tr in rows:
 cols = tr.findAll('td')
 lst = []
 for td in cols:
  lst.append(td.get_text())
 buf = ','.join(x for x in lst)
 print(buf)
 gl.write(buf+'\n')

