import numpy as np

def find_reflection(pattern):
    """Find index of row before reflection"""
    for i, line in enumerate(pattern):
        if i == len(pattern) - 1: return 0
        to_start = i + 1
        to_end = len(pattern) - (i + 1)
        flag = True
        for j in range(min(to_start, to_end)):
            if pattern[i - j] != pattern[(i + 1) + j]:
                flag = False
                break
        if flag == True: return i + 1

# Get input
f = open("Day13/input.txt","r")
input = []
sub_input = []
for x in f:
    if x.strip("\n") == "" : 
        input.append(sub_input)
        sub_input = []
        continue
    sub_input.append([*x.strip("\n")])
input.append(sub_input)    
f.close

score = 0
# For every pattern try to find reflection, if there is none transpose pattern then do it again
for pattern in input:
    result = find_reflection(pattern)
    if result == 0: score += find_reflection(np.array(pattern).T.tolist()) 
    else: score += result * 100
print(score)