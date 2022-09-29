from typing import ItemsView
import requests
from getkeys import *

url = "https://bringatrailer.com/wp-json/bringatrailer/1.0/data/keyword-filter"

querystring = {"bat_keyword_pages":"2904138","sort":"td","page":"2","results":"items"}

payload = ""
headers = {
    "Accept": "application/json",
    "Cookie": "OptanonConsent=isIABGlobal=false&datestamp=Wed+Sep+28+2022+21%3A10%3A38+GMT-0400+(EDT)&version=202209.1.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false; __stripe_mid=24cea6a8-fc6e-4253-b35c-d17599ac2c741b15b4; __stripe_sid=5b809a5b-39c4-4038-8e4f-8bd7a8028ecd08d9e8; usprivacy=1YNN; _ga=GA1.2.1792864127.1663778338; wordpress_logged_in_7f934e8f367cd1991ef8af2c0ccfabdb=glensmith1414%7C1665356337%7CzA6CdVkniq2MvOkNZSkeYC0jHc9j3TN6BJ2xdEzJmAp%7Cc83f2e64dd605dc59b54aedb9aedba23f78d275cf01bb039fcbecd0fcbdcf275; __gads=ID=a567fad4910fb822-22a15e8944d70075:T=1663778339:RT=1664146725:S=ALNI_MYgTeQNJLp8YSPGg2wQsEn2K9QNHw; __gpi=UID=000008697587ad26:T=1663778339:RT=1664146725:S=ALNI_MbKgZF8VDZ_gJcEx72QVDBaG8J9Zw; iterableEndUserId=glensmith1414%40gmail.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "bringatrailer.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://bringatrailer.com/bmw/e90-e92-m3/",
    "Connection": "keep-alive",
    "x-wp-nonce": "23c7d551ad"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

r1=response.json()
r2=response.text

keys_list=[]

get_keys(r1, keys_list)

print(response.json())

