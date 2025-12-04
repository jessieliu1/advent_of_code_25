import sys
import math 

def compute_password_pt1(filename):
    zero_count = 0
    current_val = 50
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
        for line in input_lines:
            dir = line[:1]
            clicks = int(line[1:])
            if (dir == "L"):
                current_val = (current_val - clicks) % 100
            else:
                current_val = (current_val + clicks) % 100
            if current_val == 0:
                zero_count += 1
    return zero_count
    
def compute_password_pt2(filename):
    zero_count = 0
    current_val = 50
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
        for line in input_lines:
            dir = line[:1]
            clicks = int(line[1:])
            pass_zero_count = 0
            if (dir == "L"):
                pass_zero_count = abs(math.floor((current_val - clicks) / 100))
                current_val = (current_val - clicks) % 100
                if current_val == 0:
                    pass_zero_count += 1
            else:
                pass_zero_count = abs(math.floor((current_val + clicks) / 100))
                current_val = (current_val + clicks) % 100

            zero_count += pass_zero_count
    return zero_count
    

def main():
    print(compute_password_pt1(sys.argv[1]))
    print(compute_password_pt2(sys.argv[1]))

main()
