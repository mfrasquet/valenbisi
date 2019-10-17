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

#Meteo data --------------------------------------------------

#Load meteo data

with open('/home/miguel/Desktop/Python_files/valenbisi/key2.txt') as f:
    key2 = f.readlines()
    
url2 = 'https://api.weatherbit.io/v2.0/current?city=Valencia,ES&key='+key2[0]
response2 = urllib.request.urlopen(url2)

data2 = response2.read()
encoding2 = response2.info().get_content_charset('utf-8')
JSON_object2 = json.loads(data2.decode(encoding2))
meteo=JSON_object2['data']
temp=meteo[0]['app_temp']
rain=meteo[0]['precip']
  

#Bike data ---------------------------------------------------------------

#Load bikes data

with open('/home/miguel/Desktop/Python_files/valenbisi/key.txt') as f:
    key = f.readlines()


url = 'https://api.jcdecaux.com/vls/v1/stations?contract=valence&apiKey='+key[0]
response = urllib.request.urlopen(url)

data = response.read()
encoding = response.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))

#Create data frame
now = datetime.datetime.now()
stations=[]
bikes_free=[now,temp,rain]
stands_free=[now,temp,rain]
for line in JSON_object:
    
    stations.append(line['number'])
    
    bikes_free.append(round(100*line['available_bikes']/line['bike_stands']))
    stands_free.append(round(100*line['available_bike_stands']/line['bike_stands']))
    

data_B=pd.read_csv('/home/miguel/Desktop/Python_files/valenbisi/valenbisi/data_B.csv', sep='\t',index_col=False)
data_B.loc[len(data_B)+1] = bikes_free
data_B.to_csv('/home/miguel/Desktop/Python_files/valenbisi/valenbisi/data_B.csv', sep='\t', index=False)

data_S=pd.read_csv('/home/miguel/Desktop/Python_files/valenbisi/valenbisi/data_S.csv', sep='\t',index_col=False)
data_S.loc[len(data_S)+1] = stands_free
data_S.to_csv('/home/miguel/Desktop/Python_files/valenbisi/valenbisi/data_S.csv', sep='\t', index=False)
