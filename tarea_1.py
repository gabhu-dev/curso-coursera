import re

# TAREA
fhand = open('demo.txt')
count = 0
for line in fhand:
    matchNumbers = re.findall('[0-9]+', line)
    for number in matchNumbers:
        count += int(number)
print(count)