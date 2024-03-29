count = 0

def step():
    """Move to the next point and increment count"""
    global y2, x2, count
    y2, x2 = y, x
    count += 1

# Get input
f = open("Day10/input.txt","r")
input = []
for x in f:
    input.append([*x][:-1])
f.close

# Find S
y, x  = next(((i, line.index("S")) for i, line in enumerate(input) if "S" in line), None)

# Step through the whole loop
start_x, start_y = x, y
input[y][x] = "|"
y2, x2 = 0, 0
while True:
    if input[y][x] == "F":
        if y == y2 and x + 1 == x2:
            step()
            y += 1
        else:
            step()
            x += 1
    elif input[y][x] == "L":
        if y == y2 and x + 1 == x2:
            step()
            y -= 1
        else:
            step()
            x += 1
    elif input[y][x] == "|":
        if y + 1 == y2 and x == x2:
            step()
            y -= 1
        else:
            step()
            y += 1
    elif input[y][x] == "-":
        if y == y2 and x + 1 == x2:
            step()
            x -= 1
        else:
            step()
            x += 1
    elif input[y][x] == "J":
        if y == y2 and x - 1 == x2:
            step()
            y -= 1
        else:
            step()
            x -= 1
    elif input[y][x] == "7":
        if y == y2 and x - 1 == x2:
            step()
            y += 1
        else:
            step()
            x -= 1
    if y == start_y and x == start_x:
        print(count/2)
        break 
