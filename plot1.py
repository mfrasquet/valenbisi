#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:53:39 2019

@author: miguel
"""
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt 


data=pd.read_csv('bikes.csv', sep='\t',index_col=False)


week_day=[]
for i in range(0,len(data)):
    week_day.append(datetime.strptime(data['date'][i],'%Y-%m-%d %H:%M:%S.%f').weekday())

data['week_day']=week_day    

# 0-> Monday 1->Tuesday ...
filtered_df = data.loc[data.week_day.eq(1)].reset_index()


fig, ax = plt.subplots(figsize=(7,4))
for j in range(0,int(len(filtered_df)/72)):
    date_plot=[]
    bikes_plot=[]   
    for i in range(0,72):
        date_plot.append(i)
        bikes_plot.append(filtered_df['bikesHome'][i+j*72])
    plt.scatter(date_plot, bikes_plot) 

#filtered_df.plot(x='date', y='bikesHome', lw=0, marker='o', figsize=(8,4)) 

#filtered_df['date'] = filtered_df.date.astype(np.int64)


#plt.scatter(filtered_df['date'], filtered_df['bikesHome'])
#filtered_df.plot(x=filtered_df['date'], y=filtered_df['bikesHome'], kind='scatter', ax=ax)
#ax.set_xticklabels([datetime.fromtimestamp(ts / 1e9).strftime('%H:%M:%S') for ts in ax.get_xticks()])
#ax.set_yticklabels([datetime.fromtimestamp(ts / 1e9).strftime('%H:%M:%S') for ts in ax.get_yticks()])
#plt.show()
#
#data.plot(x='date', y='b', lw=0, marker='o', figsize=(8,4)) 