# Get input
f = open("Day6/input.txt", "r")
input = []
for x in f:
    x = x.split(":")[1][:].split(" ")
    while "" in x:
        x.remove("")
    x = int(''.join(x))
    input.append(x)
f.close
time = input[0]
distance_race = input[1]

# Calculate distance for every possibility of holding the button
possible_wins = 0
for hold in range(time):
    distance_boat = hold * (time - hold)
    if distance_boat > distance_race:
        possible_wins += 1
        
print(possible_wins)