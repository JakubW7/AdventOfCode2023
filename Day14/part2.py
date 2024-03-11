import numpy as np

def move_rocks(input):
    """Move rock as far to the right as possible"""
    for line in input:
        stop_point = len(line)
        move = False
        for i, char in reversed(list(enumerate(line))):
            if line[i] == ".": move = True
            if line[i] == "#": stop_point = i; move = False
            if line[i] == "O" and move == True:
                line[i] = "."
                line[stop_point - 1] = "O"
                stop_point -= 1
            if line[i] =="O": stop_point -= 1
    return input

def turn(input):
    """Turn whole dish to the right"""
    input = np.array(input).T
    for i, line in enumerate(input):
        input[i] = input[i][::-1]
    return input

def cycle(input):
    """Do whole cycle of moving rocks and turning dish to the right till dish is back in original position"""
    for i in range(4):
        input = move_rocks(turn(input))
    return input

def score(input):
    """Get score of given stone pattern"""
    sum = 0
    for i, line in enumerate(input):
        sum += np.count_nonzero(line == "O") * (len(input) - i)
    return sum

# Get input
f = open("Day14/input.txt","r")
input = [[*x.strip("\n")] for x in f]
f.close

# Run for 200 cycles saving scores
scores = []
for i in range(200):
    input = cycle(input)
    scores.append(score(input))

print(scores)

# After running 200 cycles you have to inspect score list to find repeating pattern and then calculate what will be the score after 1000000000 cycles  