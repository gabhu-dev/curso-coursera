import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import http, json, ssl

# JSON
servie_url = 'http://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    address = address.strip()
    params = dict()
    params['q'] = address

    url = servie_url + urllib.parse.urlencode(params)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ssl.create_default_context())
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    js = json.loads(data)

    lat = js['features'][0]['properties']['lat']
    lng = js['features'][0]['properties']['lon']
    print('lat', lat, 'lng', lng)
    location = js['features'][0]['properties']['formatted']
    print(location)
