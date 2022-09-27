import json
from unittest import result

def get_keys(dl, keys_list):
    if isinstance(dl, dict):
        keys_list += dl.keys()
        map(lambda x: get_keys(x, keys_list), dl.values())
    elif isinstance(dl, list):
        map(lambda x: get_keys(x, keys_list), dl)

# keys = []
# get_keys(dl, keys)

# print(keys)
# # [u'a', u'inLanguage', u'description', u'priceCurrency', u'geonames_address', u'price', u'title', u'availabl', u'uri', u'seller', u'publisher', u'a', u'hasIdentifier', u'hasPreferredName', u'uri', u'fallsWithinState1stDiv', u'score', u'fallsWithinCountry', u'fallsWithinCountyProvince2ndDiv', u'geo', u'a', u'hasType', u'label', u'a', u'label', u'a', u'uri', u'hasName', u'a', u'label', u'a', u'uri', u'hasName', u'a', u'label', u'a', u'uri', u'lat', u'lon', u'a', u'address', u'a', u'name', u'a', u'description', u'a', u'name', usury']

# print(list(set(keys)))    # unique list of keys
# # [u'inLanguage', u'fallsWithinState1stDiv', u'label', u'hasName', u'title', u'hasPreferredName', u'lon', u'seller', u'score', u'description', u'price', u'address', u'lat', u'fallsWithinCountyProvince2ndDiv', u'geo', u'a', u'publisher', u'hasIdentifier', u'name', u'priceCurrency', u'geonames_address', u'hasType', u'availabl', u'uri', u'fallsWithinCountry']