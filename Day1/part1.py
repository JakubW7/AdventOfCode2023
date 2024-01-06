import re

f = open("input.txt", "r")
count = 0

# Solution is to find all digits using regex and add the matches to count
for x in f:
    match = re.findall(r"\d", x)
    count += int(match[0]) * 10
    count += int(match[-1])
print(count)
f.close()