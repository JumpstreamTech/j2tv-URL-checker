# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 06:24:33 2020

Tool for checking JumpToTV video URL status

@author: Sween
"""

import requests
import pandas as pd
import os
import sys

file = 'video (4).csv'
path = r'C:\Users\Sween\Downloads'
path = os.path.join(path, '')
filepath = '' + path + '\\' + file + ''

videoChecked = pd.read_csv(filepath)

#%% check URLs for typos
videoCheck = videoChecked.sort_values('url')
#search ="http"

badURLs = videoChecked[~videoChecked['url'].str.startswith('https://') & 
       ~videoChecked['url'].str.startswith('http://')]

if len(badURLs['url']) != 0:
    print('Correct these URLs in the CSV and start over')
    print(badURLs['title'] + ' ' + badURLs['url'])
    sys.exit()
    
#%% request URL stats, add to URL Status column and write to videoChecked.csv
videoChecked['URL Status'] = videoChecked.url.apply(lambda url: requests.get(url).status_code)

videoChecked.to_csv('videoChecked.csv',index=False)