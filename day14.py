def get_rocks(lines):
  rocks = []
  cube_rocks = []
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if lines[i][j] == "O":
        rocks.append((i,j))
      elif lines[i][j] == "#":
        cube_rocks.append((i,j))
  return rocks,cube_rocks
def roll_north(rocks,cube_rocks,rows=0):
  new_rocks = [rock for rock in rocks]
  for i in range(len(rocks)):
    new_rock = (rocks[i][0]-1,rocks[i][1])
    if new_rock[0] >= 0 and (new_rock not in rocks) and (new_rock not in cube_rocks):
      new_rocks[i] = new_rock
  return new_rocks, new_rocks != rocks 

def roll_south(rocks,cube_rocks,rows):
  new_rocks = [rock for rock in rocks]
  for i in range(len(rocks)):
    new_rock = (rocks[i][0]+1,rocks[i][1])
    if new_rock[0] < rows and (new_rock not in rocks) and (new_rock not in cube_rocks):
      new_rocks[i] = new_rock
  return new_rocks, new_rocks != rocks
def roll_west(rocks,cube_rocks,rows=0):
  new_rocks = [rock for rock in rocks]
  for i in range(len(rocks)):
    new_rock = (rocks[i][0],rocks[i][1]-1)
    if new_rock[1] >= 0 and (new_rock not in rocks) and (new_rock not in cube_rocks):
      new_rocks[i] = new_rock
  return new_rocks, new_rocks != rocks
def roll_east(rocks,cube_rocks,rows):
  new_rocks = [rock for rock in rocks]
  for i in range(len(rocks)):
    new_rock = (rocks[i][0],rocks[i][1]+1)
    if new_rock[1] < rows and (new_rock not in rocks) and (new_rock not in cube_rocks):
      new_rocks[i] = new_rock
  return new_rocks, new_rocks != rocks
def cycle(rocks,cube_rocks, rows):

  new_rocks = rocks
  directions=[roll_north,roll_west,roll_south,roll_east]
  for direction in directions:
    not_same =True 
    while not_same:
      new_rocks, not_same = direction(new_rocks,cube_rocks,rows)
    rocks = new_rocks
  return rocks
      
f = open("test.txt", "r")
lines = f.read().splitlines()
rocks, cube_rocks = get_rocks(lines)
# not_same =True 
# new_rocks = rocks
# while not_same:
#   new_rocks, not_same = roll_north(new_rocks,cube_rocks)

# new_rocks.sort(key=lambda rock:rock[0])
# rows = len(lines)
# result = 0
# for rock in new_rocks:
#   result += rows - rock[0]

# print(result)
rows = len(lines)
num_of_cycles =1000000000 

for i in range(num_of_cycles):
  rocks = cycle(rocks,cube_rocks,rows)

result = 0
for rock in rocks:
  result += rows - rock[0]
