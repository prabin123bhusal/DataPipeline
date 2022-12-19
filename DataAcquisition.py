

# # Data Acquisition from API


import requests
import csv

from requests.api import head

url = 'https://api.coincap.io/v2/assets'

headers = {
    'Accept' : 'application/json',
    'Content-Type' : 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})
myjson = response.json()
ourdata = []
csvheader = ['SYMBOL', 'NAME', 'PRICE(USD)']


for x in myjson['data']:
    listing = [x['symbol'], x['name'], x['priceUsd']]
    ourdata.append(listing)


with open('data.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(ourdata)


print("done")

