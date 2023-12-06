from functools import reduce
def parse_line(line):
  vals = line.split(" ")
  vals = list(map(int,filter(None,vals[1:])))
  return vals

def parse_line_2(line):
  vals = line.split(" ")
  vals = ''.join(list(filter(None,vals[1:])))
  return int(vals)

def calculate_distance(hold_for,max_time):
  time_passed = hold_for
  speed = hold_for
  return speed*(max_time-time_passed)


f = open("input.txt", "r")
lines = f.read().splitlines()
#part 1
vals = [parse_line(line) for line in lines]
times, record_distances = vals[0],vals[1]
print(times,record_distances)
result = []
for i in range(0,len(times)):
  current_times = list(map(lambda x: calculate_distance(x,times[i]),range(times[i])))
  winning_times_count = len(list(filter(lambda x: x > record_distances[i],current_times)))
  result.append(winning_times_count)
print(reduce(lambda x,y: x*y,result))

#part 2
vals = [parse_line_2(line) for line in lines]
current_times = list(map(lambda x: calculate_distance(x,vals[0]), range(vals[0])))
winning_times_count = len(list(filter(lambda x: x >vals[1], current_times)))
print(winning_times_count)