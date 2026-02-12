import re

# REGEX
fhand = open('cuento.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

txt = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'

print(re.findall('href="(.+)"', txt))