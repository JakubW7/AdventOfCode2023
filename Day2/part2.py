import re
f = open('input.txt', 'r')
count = 0
for x in f:
    r_max = 0
    g_max = 0
    b_max = 0
    x = x.split(":")[1]
    match = re.findall(r'\d+\s\w', x)
    for i in match:
        i = i.split()
        if i[1] == 'r' and int(i[0]) > r_max:
            r_max = int(i[0])         
        if i[1] == 'b' and int(i[0]) > b_max:
            b_max = int(i[0])
        if i[1] == 'g' and int(i[0]) > g_max:
            g_max = int(i[0])
    count += r_max * b_max * g_max
print(count)
f.close()
    