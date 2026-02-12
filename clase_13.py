import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# XML
# 1. Initialize the parser
parser = ET.XMLParser()

# 2. Feed the XML data (it can be in chunks)
parser.feed("<person><name>chunk</name><email hide='yes'></email></person>") # Complete XML

# 3. Call close() to finalize and get the root element!
tree = parser.close()

# 4. Use the resulting root
# print(f"Successfully parsed root tag: {tree.tag}")
# print(f"Name: {tree.find('name').text}")
# print(f"Email hide attribute: {tree.find('email').get('hide')}")

lst = tree.findall('person')  # Example of finding all name elements under person
print(f'Count: {len(lst)}')

for item in lst:
    print(f'Item: {item.text}')