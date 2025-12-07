import sys

def get_accessble_rolls(input_lines):
    forklift_accessible = 0
    accessible_indices = []

    for row in range(len(input_lines)):
        print(input_lines[row])
        for col in range(len(input_lines[0])):
            if input_lines[row][col]== "@":
                adjacent_roll_count = 0

                # check the eight adjacent positions
                for adj_row in range(max(0, row-1), min(len(input_lines), row + 2)):
                    for adj_col in range(max(0, col-1), min(len(input_lines[0]), col+2)):
                        if (adj_row, adj_col) == (row, col):
                            continue
                        if input_lines[adj_row][adj_col] == "@":
                            adjacent_roll_count += 1

                if (adjacent_roll_count < 4):
                    accessible_indices.append((row, col))
                    forklift_accessible += 1
    print('\n')
    
    output = []
    for row in range(len(input_lines)):
        row_output = ""
        for col in range(len(input_lines[0])):
            if (row, col) in accessible_indices:
                row_output += "x"
            else:
                row_output += input_lines[row][col]
        print(row_output)
        output.append(row_output)
    return (forklift_accessible, output)
            
def paper_rolls_pt1(filename):
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
        return get_accessble_rolls(input_lines)[0]
        
def paper_rolls_pt2(filename):
    accessible_sum = 0
    with open(filename, 'r') as file:
        state = [line.strip() for line in file]
        
        rolls, state = get_accessble_rolls(state)
        while rolls:
            accessible_sum += rolls
            rolls, state = get_accessble_rolls(state)

    return accessible_sum

def main():
    # print(paper_rolls_pt1(sys.argv[1]))
    print(paper_rolls_pt2(sys.argv[1]))

main()
