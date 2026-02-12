import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

input = '''<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
  </stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(f'Count: {len(lst)}')

for item in lst:
    print(f'Name: {item.find("name").text}')
    print(f'Id: {item.find("id").text}')
    print(f'Attribute x: {item.get("x")}')