import numpy as np
import copy

def find_reflecion(pattern, ignore = 0):
    """Find index of row before reflection, with optional parameter to ignore particular result and continue"""
    for i, line in enumerate(pattern):
        if i == len(pattern) - 1: return 0
        if i == ignore - 1: continue
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

for pattern in input:
    # Get original reflections
    unchanged_result = find_reflecion(pattern)
    unchanged_result_t = find_reflecion(np.array(pattern).T.tolist())

    # For every point in pattern check if changing it gives diffrent reflection
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            smuge_pattern = copy.deepcopy(pattern)
            if pattern[i][j] == "." : smuge_pattern[i][j] = "#"
            else : smuge_pattern[i][j] = "."

            result = find_reflecion(smuge_pattern, unchanged_result)
            if result != 0 and result != unchanged_result:
                score += result * 100
                break

            result_t = find_reflecion(np.array(smuge_pattern).T.tolist(), unchanged_result_t)
            if result_t != 0 and result_t != unchanged_result_t:
                score += result_t
                break

        else: continue
        break
print(score)
