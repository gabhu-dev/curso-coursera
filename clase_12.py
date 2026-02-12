import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# BEAUTIFUL SOUP
html = urllib.request.urlopen('https://py4e-data.dr-chuck.net/')
print(type(html))
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))