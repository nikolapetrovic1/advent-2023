import re

def parse_numbers(line):
    matches = re.finditer(r'\d+',line)
    numbers_and_coordinates = [
        (int(match.group()), match.start(), match.end()) for match in matches]
    return (numbers_and_coordinates)

def get_neighbors(matrix, row, col):
    # Get dimensions of the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Define relative positions for adjacent and diagonal cells
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        # Check if the new position is within the matrix boundaries
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            c = matrix[new_row][new_col]
            if ((not c.isdigit()) and c != "."):
                return True
    return False

def get_neighbors_2(matrix, row, col):
    # Get dimensions of the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Define relative positions for adjacent and diagonal cells
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        # Check if the new position is within the matrix boundaries
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            c = matrix[new_row][new_col]
            if c == '*':
                return (True,new_row,new_col)
    return (False,"","")



def check_number(matrix,number,row):
    start = number[1]
    end = number[2]
    for col in range(start,end):
        if get_neighbors(matrix,row,col):
            return number[0]

def check_number_2(matrix,number,row):
    start = number[1]
    end = number[2]
    for col in range(start,end):
        res = get_neighbors_2(matrix,row,col)
        if res[0]:
            return (number[0],(res[1],res[2]))



f = open("input.txt", "r")
lines = f.read().splitlines()
numbers = [parse_numbers(line) for line in lines]

#part 1
valid_numbers = []
for row, nums in enumerate(numbers):
    result = [check_number(lines,number,row) for number in nums]
    valid_numbers.append(result)
valid_numbers = [item for sublist in valid_numbers for item in sublist]
result = list(filter(lambda x: x != None, valid_numbers))
print(sum(result))

#part 2
valid_numbers = []
for row, nums in enumerate(numbers):
    result = [check_number_2(lines,number,row) for number in nums]
    valid_numbers.append(result)
valid_numbers = [item for sublist in valid_numbers for item in sublist]
valid_numbers = list(filter(lambda x: x!= None, valid_numbers))
coordinates = list(map(lambda x: x[1],valid_numbers))
coordinates = set(coordinates)
grouped = dict.fromkeys(coordinates,[])
result = []
for key in grouped.keys():
    vars = (list(filter(lambda x: x[1] == key,valid_numbers)))
    if len(vars) == 2:
        product = vars[0][0] * vars[1][0]
        result.append(product)
print(sum(result))
