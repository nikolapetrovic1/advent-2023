def parse_line(line):
  vals = line.split(":")
  card = int(vals[0].split(" ")[-1])
  nums = vals[1].split("|")
  winning_nums = set(map(int, filter(None,nums[0].strip().split(" "))))
  your_nums = set(map(int, filter(None,nums[1].strip().split(" "))))
  intersection = (list(winning_nums & your_nums))
  return card,intersection

def parse_line_1(line):
  card,intersection = parse_line(line)
  if intersection:
    result = 1
    for i in range(0,len(intersection)-1):
      result *= 2 
    return result 

def parse_line_2(line):
  card,intersection = parse_line(line)
  return (card,len(intersection))

def add_winnings(dict,multiplier_dict,idx):
  multiplier = multiplier_dict[idx]
  matching = dict[idx]
  for i in range(idx+1,idx+1+matching):
    multiplier_dict[i] += multiplier
  return multiplier_dict

f = open("input.txt", "r")
lines = f.read().splitlines()
#part 1
results = list(filter(None,[parse_line_1(line) for line in lines]))
print(sum(results))

#part 2
results = list([parse_line_2(line) for line in lines])
num_of_cards = results[-1][0]
dict = {}
multiplier_dict = {}
for res in results:
  dict[res[0]] = res[1]
  multiplier_dict[res[0]] = 1

for i in range(1,num_of_cards + 1):
  multiplier_dict = add_winnings(dict,multiplier_dict,i)

print(sum(multiplier_dict.values()))