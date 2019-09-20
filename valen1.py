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