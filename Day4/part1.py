sum = 0
f = open('Day4/input.txt', 'r')
for x in f:
    # Clean lines
    line = x.split(":")[1]
    winnum = line.split("|")[0].split(" ")
    yournum = line.split("|")[1].strip("\n").split(" ")
    while "" in winnum:
        winnum.remove("")
    while "" in yournum:
        yournum.remove("")
    # Check your numbers for winning numbers and add powers    
    power = -1
    for n in winnum:
        if n in yournum:
            power += 1
    if power > -1:
        sum += pow(2, power)
print(sum)
f.close()

