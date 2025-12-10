import sys
import numpy as np
  
def cephalopod_math_p1(filename):
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
        operations = input_lines[-1].split()
        sums = list(map(int, input_lines[0].split()))
        for i in range(1, len(input_lines) - 1):
            values = list(map(int, input_lines[i].split()))
            for j in range(len(values)):
                if operations[j] == "*":
                    sums[j] *= values[j]
                if operations[j] == "+":
                    sums[j] += values[j]
        return sum(sums)

def cephalopod_math_p2(filename):
    total = None
    with open(filename, 'r') as file:
        input_lines = [list(line.strip("\n")) for line in file]
        operations = ''.join(input_lines[-1]).split()
        operations.reverse()

        input_lines = input_lines[:-1]
        input_matrix = np.array(input_lines)
        input_matrix = np.rot90(input_matrix)

        operation_index = 0

        total = 0
        val = None
        for row in input_matrix:
            num = "".join(list(row)).strip()
            if num == "":
                total += val
                operation_index += 1
                val = None
                continue

            if val is None:
                val = int(num)
            else:
                if operations[operation_index] == "*":
                    val *= int(num)
                if operations[operation_index] == "+":
                    val += int(num)
        total += val
        return total
    
def main():
    print(cephalopod_math_p2(sys.argv[1]))

main()
