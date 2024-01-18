# Get input and translate it into list of lists, change figures to numbers, append bid at the and of every hand with offset to keep sorting intact
figures_dict = {"A" : 14, "K" : 13, "Q" : 12, "J" : 11, "T" : 10}
bids = []
hands = []
f = open("Day7/input.txt", "r")
for x in f:
    hand = []
    x = x.split(" ")
    for y in x[0]:
        if y in figures_dict:
            y = figures_dict[y]
        else:
            y = int(y)
        hand.append(y)
    hand.append(int(x[1]) + 100)
    hands.append(hand)
f.close()

types = [[],[],[],[],[],[],[]]

for hand in hands:
    frequency = []
    for i in hand[:-1]:
        frequency.append(hand.count(i))
    # Appending five of a kind
    if max(frequency) == 5:
        types[0].append(hand)
    # Appending four of a kind
    elif max(frequency) == 4:
        types[1].append(hand)
    # Appending full house
    elif max(frequency) == 3 and min(frequency) == 2:
        types[2].append(hand)
    # Appending three of a kind
    elif max(frequency) == 3:
        types[3].append(hand)
    # Appending two pairs
    elif frequency.count(2) == 4:
        types[4].append(hand)
    # Appending pair
    elif max(frequency) == 2:
        types[5].append(hand)
    # Appending high card
    else:
        types[6].append(hand)

# Sort hands and add them to score
winnings = 0
rank = 1
for type in types[::-1]:
    type.sort()
    for hand in type:
        winnings += rank * (hand[-1] - 100)
        rank += 1
print(winnings)

