# Get seed input in a list
f = open("Day5/testseeds.txt", "r")
seeds= f.read()
seeds = seeds.split(" ")
f.close

# Get maps input in a list and clean it
f = open("Day5/testmaps.txt", "r")
maps = f.read()
f.close()
maps = maps.split(":")
map_list= []
for i in maps[1 : -1]:
    map = i.split("\n")[1 : -2]
    submap = []
    for j in map:
        submap.append(j.split(" "))
    map_list.append(submap)
lastmap = []
for i in maps[-1].split("\n")[1:]:
    lastmap.append(i.split(" "))
map_list.append(lastmap)    

# For every seed check if it's in the range given by map 
locations = []
for seed in seeds:
    seed = int(seed)
    for map in map_list:
        for map_line in map:
            if seed in range(int(map_line[1]), int(map_line[1]) + int(map_line[2])):
                seed = int(map_line[0]) + seed - int(map_line[1])
                break
    locations.append(seed)
print(min(locations))
    
        