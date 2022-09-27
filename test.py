from getkeys import *

f = open('/Users/glensmith/Documents/Code Stuff/Bring a Trailor/New_Request-1664149914834.json')

data = json.load(f)

f.close()
keys = []

get_keys(data,keys)

print(keys)