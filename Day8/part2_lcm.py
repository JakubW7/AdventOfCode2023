import math

# Get input
f = open("Day8/input.txt","r")
input = []
for x in f:
    input.append(x)
f.close

# Separate input and make dictionary with directions
directions = input[0][:-1]
network = input[2:]
network_dict = {}
for line in network:
    network_dict[line[:3]] = [line[7:10], line[12:15]]
starts = []

# Get starting points
for key in network_dict.keys():
    if key[2] == "A":
        starts.append(key)

# Get number of steps where every starting points loops and find least common multiple of them
steps_list = []
for i in range(len(starts)):
    steps = 0
    token = True
    while token == True:
        for x in directions:
            if token == False:
                break
            if x == "L":
                starts[i] = network_dict[starts[i]][0]
            else:
                starts[i] = network_dict[starts[i]][1]
            steps += 1
            if starts[i][2] == "Z":
                steps_list.append(steps)
                token = False
print(math.lcm(*steps_list))    
