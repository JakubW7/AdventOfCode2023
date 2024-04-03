#Get input
f = open("Day18/input.txt","r")
input = [x.split() for x in f]
f.close    

# Get positions of all trenches
x, y = 0, 0
trenches = []
for line in input:
    line[1] = int(line[1])
    if line[0] == "U":
        for i in range(line[1]):
            y -= 1
            trenches.append([x, y])
    if line[0] == "D":
        for i in range(line[1]):
            y += 1
            trenches.append([x, y])
    if line[0] == "R":
        for i in range(line[1]):
            x += 1
            trenches.append([x, y])
    if line[0] == "L":
        for i in range(line[1]):
            x -= 1
            trenches.append([x, y])

# Calculate area of the polygon using shoelace formula
area = 0
for i in range(len(trenches) - 1):
    area += trenches[i][0] * trenches[i + 1][1] - trenches[i + 1][0] * trenches[i][1]
area += trenches[-1][0] * trenches[0][1] - trenches[0][0] * trenches[-1][1]
area = area / 2

# Calculate number of points inside polygon using Pick's theorem
n_points = abs(area) - len(trenches)/2 + 1

solution = n_points + len(trenches)
print(solution)