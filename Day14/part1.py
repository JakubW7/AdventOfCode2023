import numpy as np

def stone_sum(pos, num):
    """Get score given position of first stone and number of stones"""
    sum = 0
    for i in range(num): sum += pos - i
    return sum

# Get input
f = open("Day14/input.txt","r")
input = [[*x.strip("\n")] for x in f]
f.close
input = np.array(input).T

total = 0

# For every line of stones get score for all moving stones after every non-movable stone 
for line in input:
    line = line[::-1]
    stone_num = 0
    for i, char in enumerate(line):
        if char == "#" and stone_num != 0: 
            total += stone_sum(i, stone_num)
            stone_num = 0
            continue
        if char == 'O': stone_num += 1
    total += stone_sum(len(line), stone_num)

print(total)



