import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

anchors = []
currentLink = 'http://py4e-data.dr-chuck.net/known_by_Fruin.html'

for i in range(7):
  html = urllib.request.urlopen(currentLink)
  if len(anchors) == 0:
    anchors.append(currentLink)
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  anchors.append(tags[17].get('href', None))
  currentLink = tags[17].get('href', None)

for anchor in anchors:
  print(anchor)