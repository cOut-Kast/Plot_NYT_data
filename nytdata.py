# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:21:52 2020

@author: Man
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import data from git
url='https://raw.githubusercontent.com/alex/nyt-2020-election-scraper/master/all-state-changes.csv'
dat=pd.read_csv(url, error_bad_lines=False)

#pick out pennsylvania
penn=dat.loc[dat['state'] == 'Pennsylvania (EV: 20)']

#collect trump votes. He swaps from leading to trailing candidate so you have to pull different columns
tdat=penn.loc[dat['leading_candidate_name'] == 'Trump']
tdat2=penn.loc[dat['trailing_candidate_name'] == 'Trump']
tdat=tdat.copy()
tdat2=tdat2.copy()

#collect biden votes. 
bdat=penn.loc[dat['leading_candidate_name'] == 'Biden']
bdat2=penn.loc[dat['trailing_candidate_name'] == 'Biden']
bdat=bdat.copy()
bdat2=bdat2.copy()

#pulls the timestamps and coverts to datetime format
tdat['timestamp']= pd.to_datetime(tdat['timestamp'])
tdat2['timestamp']= pd.to_datetime(tdat2['timestamp'])
bdat['timestamp']= pd.to_datetime(bdat['timestamp'])
bdat2['timestamp']= pd.to_datetime(bdat2['timestamp'])

#converts everything to numpy
ts_t=tdat['timestamp'].to_numpy()
ts_t2=tdat2['timestamp'].to_numpy()
ts_b=bdat['timestamp'].to_numpy()
ts_b2=bdat2['timestamp'].to_numpy()

#converts time data to numpy
v_t=tdat['leading_candidate_votes'].to_numpy()
v_t2=tdat2['trailing_candidate_votes'].to_numpy()

v_b=bdat['leading_candidate_votes'].to_numpy()
v_b2=bdat2['trailing_candidate_votes'].to_numpy()

#combine the data from when trump was leading with the data from when trump is trailing
# also reverse the index order since its reverse-chronological
v_t=np.append(v_t[::-1],v_t2[::-1])
ts_t=np.append(ts_t[::-1],ts_t2[::-1])

#combine the data from when biden was leading with the data from when biden is trailing
v_b=np.append(v_b,v_b2)
ts_b=np.append(ts_b,ts_b2)

#plot trumps cumulative votes                                               
plt.plot(ts_t,v_t,color='red')
plt.xticks(rotation=90)
plt.show()
#plot biden cumulative votes   
plt.plot(ts_b,v_b,color='blue')
plt.xticks(rotation=90)
plt.show()

#calculates the newvotes by taking difference between cummulative votes
nv_b=np.diff(v_b[::-1])
nv_t=np.diff(v_t)

#takes ratio of new votes for biden divided new votes for trump
nv_ratio=np.divide(nv_b,nv_t)

#plots
plt.figure(2)
plt.scatter(ts_b[1:],nv_ratio)
plt.xticks(rotation=90)
plt.xlabel('Time')
plt.ylabel('Biden/Trump Ratio')
plt.show()

