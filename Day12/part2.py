from functools import cache

@cache   
def get_valid_spring_record_combinations(spring_state, damaged_spring_record):
    """Recursively get number of valid possible spring combination"""
    if not damaged_spring_record:
        if "#" in spring_state: return 0
        else: return 1

    if not spring_state: return 0

    total_combinations = 0

    if spring_state[0] in [".", "?"]:
        total_combinations += get_valid_spring_record_combinations(
            spring_state[1:], damaged_spring_record
        )

    if spring_state[0] in ["#", "?"]:
        if is_valid_condition(spring_state, damaged_spring_record):
            total_combinations += get_valid_spring_record_combinations(
                spring_state[damaged_spring_record[0] + 1 :], damaged_spring_record[1:]
            )

    return total_combinations

def is_valid_condition(spring_state, damaged_spring_record):
    """Check if given spring state is valid given spring records"""
    return (
        damaged_spring_record[0] <= len(spring_state)
        and "."
        not in spring_state[: damaged_spring_record[0]]
        and (
            damaged_spring_record[0] == len(spring_state)
            or spring_state[damaged_spring_record[0]] != "#"
        )
    )

# Get input
f = open("Day12/input.txt","r")
input = [x.strip("\n") for x in f]
f.close

sum_total = 0

# For every spring state and record get possible valid combinations
for line in input:
    spring_state, record = line.split()
    # Unfold springs and records
    spring_state = "?".join([spring_state] * 5)
    record = tuple(map(int, record.split(",") * 5))
    sum_total += get_valid_spring_record_combinations(spring_state, record)

print(sum_total)




