# Get input
f = open("Day15/testinput.txt","r")
input = f.read().split(',')
f.close()

# Hash every value from input
total = 0
for code in input:
    code_val = 0
    for char in code:
        code_val += ord(char)
        code_val = code_val * 17
        code_val = code_val % 256
    total += code_val
print(total)
