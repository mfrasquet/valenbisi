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

now = datetime.datetime.now()
bikes=pd.read_csv('bikes.csv', sep='\t',index_col=False)
bikes.loc[len(bikes)+1] = [now,bikesHome,standsHome,bikesOffice,standsOffice]
bikes.to_csv('bikes.csv', sep='\t', index=False)


#columnsList=['bikesHome','standsHome','bikesOffice','standsOffice']
#bikes = pd.DataFrame(columns=columnsList)

#tatus = pd.read_csv('/home/miguel/Desktop/Python_files/PLAT_VIRT/meteo/status.csv', sep='\t')
#status .drop(status .columns[0], axis=1)
#results_day=pd.DataFrame({ fecha: results})
#status=pd.concat([status,results_day], axis=1)
#status.to_csv('/home/miguel/Desktop/Python_files/PLAT_VIRT/meteo/status.csv', sep='\t', index=False)