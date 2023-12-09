from functools import reduce
from math import lcm


def parse_node(node, location_dict):
    vals = node.split("=")
    position = vals[0].strip()
    neighbors = vals[1].strip()[1:-1].split(",")
    neighbors = [neighbor.strip() for neighbor in neighbors]
    location_dict[position] = neighbors
    return location_dict


def get_neighbor(neighbors, instruction):
    if instruction == "L":
        return neighbors[0]
    return neighbors[1]


def get_starting_nodes(location_dict):
    return list(filter(lambda x: x[-1] == "A", location_dict.keys()))


def check_end(current_nodes):
    for node in current_nodes:
        if node[-1] != "Z":
            return False
    return True


def get_next_node(position, location_dict):
    neighbors = location_dict[position]
    current_instruction = instructions[instruction_index]
    return get_neighbor(neighbors, current_instruction)


f = open("input.txt", "r")
lines = f.read().splitlines()
location_dict = {}

instructions = lines[0]
nodes = lines[2:]
location_dict = [parse_node(node, location_dict) for node in nodes][0]
current_location = "AAA"
instruction_index = 0
steps = 0

while current_location != "ZZZ":
    neighbors = location_dict[current_location]
    current_instruction = instructions[instruction_index]
    current_location = get_neighbor(neighbors, current_instruction)
    instruction_index += 1
    instruction_index = instruction_index % len(instructions)
    steps += 1
print(steps)


# part 2
current_positions = get_starting_nodes(location_dict)
instruction_index = 0
steps = 0

result = []
for i, position in enumerate(current_positions):
    steps = 0
    while current_positions[i][-1] != "Z":
        current_positions[i] = get_next_node(current_positions[i], location_dict)
        steps += 1
        instruction_index += 1
        instruction_index = instruction_index % len(instructions)
    result.append(steps)

print(lcm(*result))
