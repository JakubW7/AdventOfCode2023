import re

f = open("input.txt", "r")
count = 0
for x in f:
    match = re.findall(r"\d", x)
    count += int(match[0]) * 10
    count += int(match[-1])
print(count)
f.close()