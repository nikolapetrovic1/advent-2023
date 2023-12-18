f = open("test.txt", "r")
vals = f.read().splitlines()[0].split(",")
result = []
for val in vals:
  total = 0
  for letter in val:
    total += ord(letter)
    total *= 17
    total %= 256
  result.append(total)
print(sum(result))
part_2 = {}
for val in vals:
  total = 0
  for i in range(len(val)):
    if val[i] == "=":
      if total in part_2.keys():
        part_2[total][val[:i]] = val[i+1:]
      else:
        part_2[total] = {}
        part_2[total][val[:i]] = val[i+1:]
      break
    if val[i] == "-":
      print(val[:i])
      if total in part_2.keys():
        if val[:i] in part_2.keys():
          del part_2[total][val[:i]]
      break
    total += ord(val[i])
    total *= 17
    total %= 256
print(part_2)