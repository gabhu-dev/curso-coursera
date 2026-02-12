import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import http, json, ssl

url = 'https://py4e-data.dr-chuck.net/comments_2351319.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ssl.create_default_context())
data = uh.read().decode()
print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

info = json.loads(data)
print('User count:', len(info))

total = 0

for item in info['comments']:
    total += int(item['count'])

print('Sum:', total)