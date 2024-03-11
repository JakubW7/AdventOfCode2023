def move_laser(y, x, dir_y, dir_x):
    """Move laser in given direction, track coordinates laser has touched and from what direction,
    if it encounters point that has been already touched in the same direction stop the laser"""
    global score_table
    if score_table[y][x] == 0: score_table[y][x] = [[dir_y, dir_x]]
    else:
        if [dir_y, dir_x] in score_table[y][x]: return -1, -1
        score_table[y][x].append([dir_y, dir_x])
    return y + dir_y, x + dir_x

def fire_laser(y, x, dir_y, dir_x):
    """Recursively fire laser from given point and direction"""
    while True:
        if x < 0 or x >= len(input[0]) or y < 0 or y >= len(input): return 0
        if input[y][x] == ".":
            y, x = move_laser(y, x, dir_y, dir_x)
        elif input[y][x] == "/":
            dir_y, dir_x = dir_x * - 1, dir_y * -1
            y, x = move_laser(y, x, dir_y, dir_x) 
        elif input[y][x] == "\\":
            dir_y, dir_x = dir_x, dir_y
            y, x = move_laser(y, x, dir_y, dir_x)            
        elif input[y][x] == "-":
            if dir_y == 0: y, x = move_laser(y, x, dir_y, dir_x)
            else:
                dir_y, dir_x = dir_x, dir_y
                fire_laser(y, x + (dir_x * -1), dir_y, dir_x * -1)
                y, x = move_laser(y, x, dir_y, dir_x)
        elif input[y][x] == "|":
            if dir_x == 0: y, x = move_laser(y, x, dir_y, dir_x)
            else:
                dir_y, dir_x = dir_x, dir_y
                fire_laser(y + (dir_y * -1), x, dir_y * -1, dir_x)
                y, x = move_laser(y, x, dir_y, dir_x)

# Get input
f = open("Day16/input.txt","r")
input = f.read().split()
f.close         

# Fire laser from top right and count how many points has it touched
score_table = [[0 for i in range(len(input[0]))] for j in range(len(input))]
fire_laser(0, 0, 0, 1)
total = 0
for line in score_table:
    for value in line:
        if value != 0: total += 1
print(total)