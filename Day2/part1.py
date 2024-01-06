import re

f = open('input.txt', 'r')
count = 0
game_n = 0

for x in f:
    flag = 0
    game_n += 1
    x = x.split(":")[1]
    match = re.findall(r'\d+\s\w', x)
    for i in match:
        i = i.split()
        if int(i[0]) > 12 and i[1] == 'r':
            flag = 1 
            break
        if int(i[0]) > 13 and i[1] == 'g':
            flag = 1
            break
        if int(i[0]) > 14 and i[1] == 'b':
            flag = 1
            break
    if flag == 1:
        continue    
    count += game_n
print(count)
f.close()
    