import json

import requests
import pandas as pd

url = 'https://cdn.storelocatorwidgets.com/json/eef7a3033941a58b67950dd68d7c7ac9?callback=slw&_=1755797754918'
res = requests.get(url)
json_data = json.loads(res.text[4:-1])  # Remove the 'slw(' prefix and ')' suffix
rows=[]
for store in json_data['stores']:
    data = store['data']
    filters = data.get('filters', [])
    row = {
        'storeid': store['storeid'],
        'name': store['name'],
        'address': data['address'],
        'website': data.get('website', None),
        'phone': data.get('phone', None),
        'email': data.get('email', None),
        'map_lat': data['map_lat'],
        'map_lng': data['map_lng'],
        'google_placeid': store['google_placeid'],
        'filters': ', '.join(filters),
        'country': store['country'],
        'timezone': store['timezone'],
    }
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv('stores.csv', index=False, encoding='utf-8-sig', header=True)
print(f"Exported {len(rows)} stores to stores.csv")