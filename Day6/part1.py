# Get input
f = open("Day6/input.txt", "r")
input = []
for x in f:
    x = x.split(":")[1][:].split(" ")
    while "" in x:
        x.remove("")
    x = [*map(int, x)]
    input.append(x)
f.close
time = input[0]
distance_race = input[1]

# For every race caluclate every possibility of holding the button
score = 1
for i in range(len(time)):
    possible_wins = 0
    for hold in range(time[i]):
        distance_boat = hold * (time[i] - hold)
        if distance_boat > distance_race[i]:
            possible_wins += 1
    score = score * possible_wins
print(score)