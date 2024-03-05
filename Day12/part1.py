import itertools
import re
import time

def check(springs, record):
    """Check if given springs combination is correct according to the record"""
    for i in range(len(springs)):
        if springs[i] == "#":
            if i != 0 and springs[i - 1] == ".":
                springs = springs[:i - 1] + "0" + springs[i:]
    springs = springs.replace(".","")
    code = ""
    for i in record:
        code = code + "#" * i + "0"
    springs = springs.strip("0")
    if code[:-1].strip("0") == springs:
        return True
    else:
        return False

start_time = time.time()
# Get input
f = open("Day12/input.txt","r")
input = [x.strip("\n") for x in f]
f.close

sum_total = 0
for line in input:
    sum_line = 0
    unknown_springs, record = line.split()
    record = [*map(int, record.split(","))]
    # Get all possible combinations of unknown springs
    unknown_indexes = [match.start() for match in re.finditer("\?", unknown_springs)]
    combination_list = [i for i in itertools.product("#.", repeat = len(unknown_indexes))]
    print(len(combination_list))
    # Insert every combination into springs and check if it is valid
    for combination in combination_list:
        resolve_springs = unknown_springs
        for i in range(len(unknown_indexes)):
            resolve_springs = resolve_springs[:unknown_indexes[i]] + combination[i] + resolve_springs[unknown_indexes[i] + 1:]
        if check(resolve_springs, record) is True:
            sum_line += 1
    sum_total += sum_line

print(sum_total)
print("--- %s seconds ---" % (time.time() - start_time))



