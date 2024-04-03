# Get input
f = open("Day18/input.txt","r")
input = [x.split() for x in f]
f.close    

# Get positions of all vertices and number of trenches
n_trenches = 0
x, y = 0, 0
trenches = []
for line in input:
    length = int(line[2][2:7], 16)
    if line[2][7] == "3":
        y -= length
        n_trenches += length
        trenches.append([x, y])
    if line[2][7] == "1":
        y += length
        n_trenches += length
        trenches.append([x, y])
    if line[2][7] == "0":
        x += length
        n_trenches += length
        trenches.append([x, y])
    if line[2][7] == "2":
        x -= length
        n_trenches += length
        trenches.append([x, y])

# Calculate area of the polygon using shoelace formula
area = 0
for i in range(len(trenches) - 1):
    area += trenches[i][0] * trenches[i + 1][1] - trenches[i + 1][0] * trenches[i][1]
area += trenches[-1][0] * trenches[0][1] - trenches[0][0] * trenches[-1][1]
area = area / 2

# Calculate number of points inside polygon using Pick's theorem
n_points = abs(area) - n_trenches/2 + 1

solution = n_points + n_trenches
print(solution)