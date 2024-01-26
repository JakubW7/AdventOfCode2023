# Get input
f = open("Day9/input.txt","r")
input = []
for x in f:
    x = [*map(int, x.split())]
    input.append(x)
f.close

sum = 0
for line in input:
    history = [line]
    # Run while last sequnce are not all zeros
    while all([x == 0 for x in history[-1]]) != True:
        difference = []
        # Append next level of history
        for i in range(0, len(history[-1]) - 1):
            difference.append(history[-1][i + 1] - history[-1][i])
        history.append(difference)
    # Make predictions about previous values
    for i in range(len(history) - 3, -1, -1):
        history[i].append(history[i][0] - history[i+1][-1])
    sum += history[0][-1]
    
print(sum)