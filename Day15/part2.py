# Get input
f = open("Day15/input.txt","r")
input = f.read().split(',')
f.close()

def hash(code):
    "Hash value accordingly to specification"
    code_val = 0
    for char in code:
        if char == "-" or char == "=": break
        code_val += ord(char)
        code_val = (code_val * 17) % 256
    return code_val

boxes = {}
for code in input:
    hash_val = hash(code)
    # Determine operation to perform
    if "-" in code:
        method = "-"
        sep_index = code.index("-")
    else:
        method = "="
        sep_index = code.index("=")
    code_list = [code[:sep_index], code[-1]]
    # Add lens
    if method == "=": 
        if hash_val not in boxes.keys():
            boxes[hash_val] = [code_list]
        else:
            flag = True 
            for i, lens in enumerate(boxes[hash_val]):
                if code_list[0] == lens[0]:
                    boxes[hash_val][i][1] = code_list[1]
                    flag = False
                    break
            if flag == True: boxes[hash_val].append(code_list)
    # Remove lens
    if method == "-" and hash_val in boxes.keys():
        for i, lens in enumerate(boxes[hash_val]):
            if code_list[0] == lens[0]: 
                boxes[hash_val].pop(i)
                break
total = 0
# Count lenses in the box
for box in boxes:
    for i, lens in enumerate(boxes[box]):
        total += (box + 1) * (i + 1) * int(boxes[box][i][1])

print(total)


    
