nlen = 0
sum = 0
stars = {}
# Get input into list of lines
f = open('Day3/input.txt', 'r')
engine = []
for x in f:
    engine.append(x)
f.close()

# Check whole input for numbers 
for i in range(len(engine)):
    for j in range(len(engine[i])):
        # Skip chars if longer valid number was found
        if nlen > 1:
            nlen -= 1
            continue
        if engine[i][j].isnumeric():
            # Get number length for looking up symbols
            j2 = j
            nlen = 0
            while engine[i][j2].isnumeric():
                j2 += 1
                nlen += 1
            # Look for * and get it's location
            cordy = max(i - 1, 0) - 1
            for k in engine[max(i - 1, 0) : min(i + 2, len(engine))]:
                cordx = max(j - 1, 0) - 1
                cordy += 1 
                for m in k[max(j - 1, 0) : min(j + 2 + (nlen -1), len(engine[0]))]:
                    cordx += 1
                    if m == '*':
                        # If number valid save it
                        number = ''
                        for n in range(nlen):
                            number = number + engine[i][j]
                            j += 1
                        # If * was already encounterd add gear ratio to sum, else save it's location
                        if (cordy, cordx) in stars:
                            sum += int(number) * stars[(cordy, cordx)]
                        else:
                            stars[(cordy, cordx)] = int(number)
                        break
                else:
                    continue
                break
print(sum)
