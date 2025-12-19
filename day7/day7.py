import sys
import numpy as np
  

# dp style:
# if no split, num splits is whatever the num of splits is for the subtree
# if split, num splits is 1 + count_splits (L subtree) + count_splits (R subtree)
# smallest case - S is last row. return + 0


def process_file(filename):
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
        input_arr = [list(line) for line in input_lines]
        input_matrix = np.array(input_arr)
        return input_matrix

def count_splits(input_matrix, memo, row, col):
        # base case
        if row == len(input_matrix) - 1:
            return 0
        
        # out of bounds
        if col < 0 or col >= len(input_matrix[0]):
            return 0
        
        # if we've already seen this beam, continue
        if (row, col) in memo:
            return 0
             
        # split beam
        if input_matrix[row+1][col] == "^":
            split_val =  1 + count_splits(input_matrix, memo, row + 1, col - 1) + count_splits(input_matrix, memo, row + 1, col + 1)
            memo[(row, col)] = split_val
            return split_val
        # not split beam
        else:
            split_val = count_splits(input_matrix, memo, row + 1, col)
            memo[(row, col)] = split_val
            return split_val
        

def count_splits_p2(input_matrix, memo, row, col):
    # base case. if you're at the end, that's a path
    if row == len(input_matrix) - 1:
        return 1
    
    # out of bounds
    if col < 0 or col >= len(input_matrix[0]):
        return 0
    
    # if we've already seen this beam
    if (row, col) in memo:
        return memo[(row, col)]
            
    # split beam
    if input_matrix[row+1][col] == "^":
        split_val =  count_splits_p2(input_matrix, memo, row + 1, col - 1) + count_splits_p2(input_matrix, memo, row + 1, col + 1)
        memo[(row, col)] = split_val
        return split_val
    # not split beam
    else:
        split_val = count_splits_p2(input_matrix, memo, row + 1, col)
        memo[(row, col)] = split_val
        return split_val
    
def main():
    input = process_file(sys.argv[1])
    memo = {}
    print(count_splits_p2(input, memo, 0, list(input[0]).index("S")))

main()
