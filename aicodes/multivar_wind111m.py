import time
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from haversine import haversine, Unit
lines = [line.rstrip('\n') for line in open('turb_name.csv')]
#find turbine locations at four corners
lat = []
lon = []
for line in lines:
 line = line.split(',')
 lat.append(float(line[1]))
 lon.append(float(line[2]))
sorted(lat)
sorted(lon)
print(0.25-(lat[-1]-lat[0]))
print(0.25-(lon[-1]-lon[0]))
