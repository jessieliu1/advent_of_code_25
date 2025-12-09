import sys

def is_fresh(ingredient, ranges):
    for r in ranges:
        low, high = r.split('-')
        if int(ingredient) >= int(low) and int(ingredient) <= int(high):
            return True
    return False
            
def fresh_count(filename):
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
        ranges = []
        ingredients = []
        print(input_lines)
        for line in input_lines:
            if "-" in line:
                ranges.append(line)
            elif line != "":
                ingredients.append(line)

        fresh_count = 0
        print(ingredients)
        print(ranges)
        for i in ingredients:
            if is_fresh(i, ranges): 
                fresh_count += 1
        return fresh_count
    
def merge_intervals(ranges):
    ranges = sorted(ranges)
    merged = []
    merged.append(ranges[0])

    for i in range(1, len(ranges)):
        prev = merged[-1]
        curr = ranges[i]

        if curr[0] <= prev[1]:
            merged[-1] = (prev[0], max(prev[1], curr[1]))
        else:
            merged.append(curr)

    return merged

    
def fresh_count_p2(filename):
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
        ranges = []
        ingredients = []
        for line in input_lines:
            if "-" in line:
                rng = line.split("-")
                ranges.append((int(rng[0]), int(rng[1])))
            if line == "":
                break
        print(ranges)

        merged_ranges = merge_intervals(ranges)
        fresh_count = 0
        for r in merged_ranges:
            fresh_count += r[1] - r[0] + 1
        return fresh_count

def main():
    # print(fresh_count(sys.argv[1]))
    print(fresh_count_p2(sys.argv[1]))

main()
