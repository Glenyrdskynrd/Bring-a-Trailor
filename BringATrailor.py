from typing import ItemsView
import requests
from getkeys import *
import pandas as pd
import json


url = "https://bringatrailer.com/wp-json/bringatrailer/1.0/data/keyword-filter"

x = 2
querystring = {"bat_keyword_pages":"2904138","sort":"td","page":f"{x}","results":"items"}

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "bringatrailer.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://bringatrailer.com/bmw/e90-e92-m3/",
    "Connection": "keep-alive",
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
    

res = []

keys_list=[]
get_keys(data, keys_list)
print(keys_list)

print(type(data['page_current']))

print(data['page_current'])

