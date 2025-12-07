import sys

def find_max_joltage_2(line):
    largest_num = -1
    largest_num_index = -1
    for i in range(0, len(line) - 1):
        if int(line[i]) > largest_num:
            largest_num = int(line[i])
            largest_num_index = i
    second_digit = -1
    for j in range(largest_num_index+1, len(line)):
        if int(line[j]) > second_digit:
            second_digit = int(line[j])
    return int(str(largest_num) + str(second_digit))

def find_max_joltage_12(line):
    joltage = ""
    index_limit = -1
    for x in range(11, -1, -1):
        largest_num = -1
        new_limit = -1
        for i in range(index_limit + 1, len(line) - x):
            if int(line[i]) > largest_num:
                largest_num = int(line[i])
                new_limit = i
        joltage += str(largest_num)
        index_limit = new_limit
    return int(joltage)

def joltage_pt1(filename):
    sum = 0
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
        for line in input_lines:
            joltage = find_max_joltage_2(line)
            sum += joltage
    return sum
            
def joltage_pt2(filename):
    sum = 0
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
        for line in input_lines:
            joltage = find_max_joltage_12(line)
            sum += joltage
    return sum

def main():
    print(joltage_pt1(sys.argv[1]))
    print(joltage_pt2(sys.argv[1]))

main()
