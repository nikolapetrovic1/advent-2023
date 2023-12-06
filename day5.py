
# destination range start, the source range start, and the range length.
def calculate_range(element,mappings,curr_iter):
  destionation_start = element[0]
  source_start = element[1]
  range_length = element[2]
  destination_range = list(range(destionation_start,destionation_start+range_length))
  source_range = list(range(source_start,source_start+range_length))
  for i in range(0,len(source_range)):
    mappings[curr_iter+1][source_range[i]] = destination_range[i]
  return mappings

def check_target_seeds(seed,mappings):
  for i in range(8):
    seed = mappings[i][seed]
  return seed

def seedInRange(seed,ranges):
  source_start = ranges[0]
  destination_start = ranges[1]
  range_length = ranges[2]
  source_end = source_start + range_length
  destination_end = destination_start + range_length
  if seed >= source_start and seed <=source_end:
    diff = seed - source_start
    destination_seed = destination_start + diff
    print(destination_seed)

def seed_path(seed,sections):
  seedInRange(seed,sections[0][1]) 


num_of_mappings=8
f = open("test.txt", "r")
lines = f.read().splitlines()
seeds = list(map(int,lines[0].split(" ")[1:]))
rest = lines[2:]
sections = [[] for _ in range(7)]
curr_section = 0
max_value = -1
for line in rest:
  if line == '':
    curr_section += 1
  elif line[0].isdigit():
    vals = list(map(int,line.split(" ")))
    max_value = max(max_value,max(vals))
    sections[curr_section].append(vals)

seed_path(seeds[0],sections)

# mappings = []
# for i in range(num_of_mappings):
#   mappings.append(list(range(0,max_value)))

# for i in range(0,7):
#   for section in sections[i]:
#     mappings = calculate_range(section,mappings,i)

# locations = list(map(lambda seed: check_target_seeds(seed,mappings),seeds))
# print(min(locations))