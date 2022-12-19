#!/usr/bin/env python
# coding: utf-8

# # Data Acquisition from API

# In[23]:


import requests
import csv

from requests.api import head


# In[24]:


url = 'https://api.coincap.io/v2/assets'


# In[25]:


headers = {
    'Accept' : 'application/json',
    'Content-Type' : 'application/json'
}


# In[26]:


response = requests.request("GET", url, headers=headers, data={})
myjson = response.json()
ourdata = []
csvheader = ['SYMBOL', 'NAME', 'PRICE(USD)']


# In[28]:


for x in myjson['data']:
    listing = [x['symbol'], x['name'], x['priceUsd']]
    ourdata.append(listing)


# In[30]:


with open('data.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(ourdata)


# In[31]:


print("done")

