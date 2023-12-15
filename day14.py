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
def roll_north(rocks,cube_rocks):
  new_rocks = [rock for rock in rocks]
  for i in range(len(rocks)):
    new_rock = (rocks[i][0]-1,rocks[i][1])
    if new_rock[0] >= 0 and (new_rock not in rocks) and (new_rock not in cube_rocks):
      new_rocks[i] = new_rock
  return new_rocks, new_rocks != rocks 

      
f = open("input.txt", "r")
lines = f.read().splitlines()
rocks, cube_rocks = get_rocks(lines)
not_same =True 
new_rocks = rocks
while not_same:
  new_rocks, not_same = roll_north(new_rocks,cube_rocks)

new_rocks.sort(key=lambda rock:rock[0])
rows = len(lines)
result = 0
for rock in new_rocks:
  result += rows - rock[0]

print(result)