import sys

def is_invalid_twice(id):
    string_val = str(id)
    # odd length strings must be valid
    if len(string_val) % 2 != 0:
        return False
    
    substr = string_val[:int(len(string_val) / 2)]
    substr += substr
    if string_val == substr:
        return True

    return False

def is_invalid_n(id):
    string_val = str(id)

    # check for repeated patterns
    for pattern_length in range(1, int(len(string_val) / 2) +1):
        # string length must be divisible by pattern length
        if len(string_val) % pattern_length != 0:
            continue

        pattern_candidate = string_val[:pattern_length]
        if string_val == construct_candidate_string(pattern_candidate, len(string_val)):
            return True

    return False

def construct_candidate_string(pattern_candidate, str_length):
    candidate = ''
    for i in range(int(str_length / len(pattern_candidate))):
        candidate += pattern_candidate
    return candidate
    
def check_ranges_pt1(filename):
    invalid_id_sum = 0
    with open(filename, 'r') as file:
        ranges = file.readline().split(',')
        for id_range in ranges:
           start = int(id_range.split('-')[0])
           end = int(id_range.split('-')[1])
           for i in range(start, end + 1):
               if is_invalid_twice(i):
                   invalid_id_sum += i
    return invalid_id_sum
    
def check_ranges_pt2(filename):
    invalid_id_sum = 0
    with open(filename, 'r') as file:
        ranges = file.readline().split(',')
        for id_range in ranges:
           start = int(id_range.split('-')[0])
           end = int(id_range.split('-')[1])
           for i in range(start, end + 1):
               if is_invalid_n(i):
                   invalid_id_sum += i
    return invalid_id_sum
    

def main():
    print(check_ranges_pt1(sys.argv[1]))
    print(check_ranges_pt2(sys.argv[1]))

main()
