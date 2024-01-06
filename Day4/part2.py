sum = 0
# Get input into list 
cards = []
f = open('Day4/input.txt', 'r')
for x in f:
    cards.append(x)
f.close()

# Create list for storing multiples of cards
mult = []
for i in range(len(cards)):
    mult.append(1)

for i in range(len(cards)):
    # Clean lines
    line = cards[i].split(":")[1]
    winnum = line.split("|")[0].split(" ")
    yournum = line.split("|")[1].strip("\n").split(" ")
    while "" in winnum:
        winnum.remove("")
    while "" in yournum:
        yournum.remove("")
    # Check your numbers for winning numbers
    wins = 0
    for n in winnum:
        if n in yournum:
            wins += 1
    # Count multiples of same cards
    multcount = mult[i]
    while multcount > 0:
        multwins = wins
        j = i + 1
        # Add multiples of same cards
        while multwins > 0:
            mult[j] += 1
            multwins -= 1
            j += 1
        multcount -= 1
# Count all cards
for i in mult:
    sum += i
print(sum)

