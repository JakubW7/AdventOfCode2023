import re
from word2number import w2n

f = open("input.txt", "r")
count = 0

# Initilaze list with digits spelled out and in numerical form
string_lst = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Find all occurences using regex and add to count
for x in f:
    match = re.findall(r"(?=("+'|'.join(string_lst)+r"))", x)
    count += w2n.word_to_num(match[0]) * 10
    count += w2n.word_to_num(match[-1])
print(count)
f.close()