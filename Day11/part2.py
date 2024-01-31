# Get input
f = open("Day11/input.txt","r")
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

# Find distances
sum = 0 
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "#":
            for k in range(i, len(input)):
                for m in range(len(input[k])):
                    if (input[k][m] == "#" and k > i) or (input[k][m] == "#" and m > j):
                            # Increase distances if there is a expanding point between galaxies
                            vertical_mult = 0
                            horizontal_mult = 0
                            for n in expand_horizontal:
                                if n < k and n > i:
                                    vertical_mult += 1
                            for n in expand_vertcial:
                                if n > min(m,j) and n < max(m,j):
                                    horizontal_mult += 1
                            sum += (k - i) + abs(m - j) + ((vertical_mult + horizontal_mult)) * 999999
print(sum)
