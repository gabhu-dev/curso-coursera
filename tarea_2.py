import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# TAREA BEAUTIFUL SOUP
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2351316.html')
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
total = 0
for tag in tags:
    number = int(tag.string)
    total += number
print(total)