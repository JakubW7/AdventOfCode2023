# Get seed input in a list
f = open("Day5/seeds.txt", "r")
seeds= f.read()
seeds = seeds.split(" ")
f.close
# Rework list of seeds into list of pairs
seeds = list(zip(seeds[::2], seeds[1::2]))
# Create seed ranges
seed_range_list = []
for seed_start, seed_pos in seeds:
    seed_range_list.append(range(int(seed_start), int(seed_start) + int(seed_pos)))

# Get maps input in a list and clean it
f = open("Day5/maps.txt", "r")
maps = f.read()
f.close()
maps = maps.split(":")
map_list= []
for i in maps[1:-1]:
    single_map = i.split("\n")[1:-2]
    submap = []
    for j in single_map:
        submap.append(j.split(" "))
    map_list.append(submap)
lastmap = []
for i in maps[-1].split("\n")[1:]:
    lastmap.append(i.split(" "))
map_list.append(lastmap)  

seed_range_list_backup = []
# For every map translate all seed ranges 
for single_map in map_list:
    for seed_range in seed_range_list:
        for map_line in single_map:
            map_range = range(int(map_line[1]), int(map_line[1]) + int(map_line[2]))
            # Find intersection of seed_range and map_range
            irange = range(max(seed_range[0], map_range[0]), min(seed_range[-1] + 1 ,map_range[-1] + 1))
            try: 
                # Test if range is correct
                irange[0]
            except:
                continue
            else:
                # If seed range is wider than map range create new seed ranges 
                if seed_range[0] < map_range[0]:
                    seed_range_list.append(range(seed_range[0], map_range[0]))
                if seed_range[-1] > map_range[-1]:
                    seed_range_list.append(range(map_range[-1] + 1, seed_range[-1] + 1))
                # Translate seed ranges which intersect with map map range 
                seed_range = range(int(map_line[0]) + irange[0] - int(map_line[1]), int(map_line[0]) + irange[-1] - int(map_line[1]) + 1)
                break
        seed_range_list_backup.append(seed_range)
    seed_range_list = seed_range_list_backup
    seed_range_list_backup = []

# Get lowest location
locations = []
for i in seed_range_list:
    locations.append(i[0])
print(min(locations))
    
        