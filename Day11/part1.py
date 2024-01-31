# Get input
f = open("Day11/testinput.txt","r")
input = []
for x in f:
    input.append(x.strip("\n"))
f.close

# Locate indexes where you need to input lines
expand_vertcial = [*range(len(input[0]))]
expand_horizontal = []
for i in range(len(input)):
    if "#" not in input[i]:
        expand_horizontal.append(i)
    for j in range(len(input[i])):
        if input[i][j] == '#' and j in expand_vertcial:
            expand_vertcial.remove(j)
                   
# Expand at located indexes 
for i in range(len(input)):
    for j in expand_vertcial[::-1]:
        input[i] = input[i][:j] + "." + input[i][j:]
for i in expand_horizontal[::-1]:
    input.insert(i, "." * len(input[0]))

# Find distances
sum = 0 
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            for k in range(i, len(input)):
                for m in range(len(input[k])):
                    if (input[k][m] == "#" and k > i) or (input[k][m] == "#" and m > j):
                            sum += (k - i) + abs(m - j)
print(sum)
