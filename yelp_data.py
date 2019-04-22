

import json
import requests
import sys
import urllib
import yelp_info
import sqlite3

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode


API_KEY= yelp_info.api_key

#code below is for adding columns into the db the first time
#conn = sqlite3.connect('pancakes.sqlite')
#cur = conn.cursor()
#addIDColumn = "ALTER TABLE Yelp ADD COLUMN id TEXT"
#addPriceColumn = "ALTER TABLE Yelp ADD COLUMN price TEXT"
#cur.execute(addIDColumn)
#cur.execute(addPriceColumn)


def add_yelp_info(db_filename, restaurant, id, price):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    cur.execute('INSERT INTO Yelp(restaurants, id, price) VALUES (?,?,?)', (restaurant, id, price))
    conn.commit()
    cur.close()

offset = 0
limit = 20

for i in range(5):
    url = 'https://api.yelp.com/v3/businesses/search'									
    headers = {'Authorization': 'bearer %s' % API_KEY}
    params = {
        'term': 'pancake',
        'location': 'Atlanta, GA',
        'limit': limit,
        'offset': offset}
    response = requests.get(url=url, params=params, headers=headers)
    results = response.json()['businesses'] 
    for b in results:
        business_name = b['name']
        business_id = b['id']
        if 'price' in b:
            business_price = b['price']
        else:
            business_price = "N/A"
        add_yelp_info("pancakes.sqlite", business_name, business_id, business_price)
    offset += 20
    

