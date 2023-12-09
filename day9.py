def calculate_difference(vals1, vals2):
    return list(map(lambda x, y: x - y, vals1, vals2))


def calculate_last(results):
    results[0].append(0)
    for i in range(1, len(results)):
        new_val = results[i - 1][-1] + results[i][-1]
        results[i].append(new_val)
    return results[-1][-1]


def calculate_first(results):
    results[0].append(0)
    for i in range(1, len(results)):
        new_val = results[i][0] - results[i - 1][0]
        results[i].insert(0, new_val)
    return result[-1][0]


f = open("input.txt", "r")
lines = f.read().splitlines()
lines = [list(map(int, line.split())) for line in lines]
part_1 = []
part_2 = []
for vals in lines:
    result = [vals]
    while not all(val == 0 for val in vals):
        vals = calculate_difference(vals[1:], vals[:-1])
        result.append(vals)
    result.reverse()
    next_val1 = calculate_last(result)
    next_val2 = calculate_first(result)
    part_1.append(next_val1)
    part_2.append(next_val2)

print(sum(part_1))
print(sum(part_2))
