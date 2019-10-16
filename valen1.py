#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:16:45 2019

@author: miguel
"""

# Frankfurt 20/9/2019

import urllib.request
import pandas as pd
import numpy as np
import json
import datetime

#Load my key
with open('/home/miguel/Desktop/Python_files/valenbisi/key.txt') as f:
    key = f.readlines()


url = 'https://api.jcdecaux.com/vls/v1/stations?contract=valence&apiKey='+key[0]
response = urllib.request.urlopen(url)

data = response.read()
encoding = response.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))

home= JSON_object[237] #Data from the station right under my home
bikesHome=home['available_bikes']
standsHome=home['available_bike_stands']

office= JSON_object[117] #Data from the station near office at the Uni
bikesOffice=office['available_bikes']
standsOffice=office['available_bike_stands']



#Load my key
with open('/home/miguel/Desktop/Python_files/valenbisi/key2.txt') as f:
    key2 = f.readlines()
    
url2 = 'https://api.weatherbit.io/v2.0/current?city=Valencia,ES&key='+key2[0]
response2 = urllib.request.urlopen(url2)

data2 = response2.read()
encoding2 = response2.info().get_content_charset('utf-8')
JSON_object2 = json.loads(data2.decode(encoding))
meteo=JSON_object2['data']
temp=meteo[0]['temp']
  

now = datetime.datetime.now()
bikes=pd.read_csv('bikes.csv', sep='\t',index_col=False)
bikes.loc[len(bikes)+1] = [now,bikesHome,standsHome,bikesOffice,standsOffice,temp]
bikes.to_csv('bikes.csv', sep='\t', index=False)