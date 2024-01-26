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

# Follow directions until ZZZ 
steps = 0
start = 'AAA'
while True:
    for i in directions:
        if i == "L":
            start = network_dict[start][0]
        else:
            start = network_dict[start][1]
        steps += 1
        if start == "ZZZ":
            print(steps)
            quit()
        