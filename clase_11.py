import urllib.request

# URL LIB
html = urllib.request.urlopen('https://dennky.com/')
for line in html:
    print(line.decode().strip())