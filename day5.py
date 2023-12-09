# destination range start, the source range start, and the range length.
def calculate_range(element, mappings, curr_iter):
    destionation_start = element[0]
    source_start = element[1]
    range_length = element[2]
    destination_range = list(
        range(destionation_start, destionation_start + range_length)
    )
    source_range = list(range(source_start, source_start + range_length))
    for i in range(0, len(source_range)):
        mappings[curr_iter + 1][source_range[i]] = destination_range[i]
    return mappings


def check_target_seeds(seed, mappings):
    for i in range(8):
        seed = mappings[i][seed]
    return seed


def seedInRange(seed, ranges):
    source_start = ranges[0]
    destination_start = ranges[1]
    range_length = ranges[2]
    destination_end = destination_start + range_length
    changed = False
    if seed >= destination_start and seed <= destination_end:
        diff = seed - destination_start
        seed = source_start + diff
        changed = True
    return seed, changed


def seed_path(seed, sections):
    changed = False
    for section in sections:
        if changed:
            return seed
        seed, changed = seedInRange(seed, section)
    return seed


def pairwise(iterable):
    a = iter(iterable)
    return list(zip(a, a))


num_of_mappings = 8
f = open("input.txt", "r")
lines = f.read().splitlines()
seeds = list(map(int, lines[0].split(" ")[1:]))
rest = lines[2:]
sections = [[] for _ in range(7)]
curr_section = 0
max_value = -1
for line in rest:
    if line == "":
        curr_section += 1
    elif line[0].isdigit():
        vals = list(map(int, line.split(" ")))
        max_value = max(max_value, max(vals))
        sections[curr_section].append(vals)

# for section in sections:
#     for i in range(len(seeds)):
#         seeds[i] = seed_path(seeds[i], section)


result = []

seed_pairs = []
for i in range(0, len(seeds), 2):
    seed_pairs.append((seeds[i], seeds[i] + seeds[i + 1]))
for section in sections:
    new = []
    while seed_pairs:
        s, e = seed_pairs.pop()
        for a, b, c in section:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seed_pairs.append((s, os))
                if e > oe:
                    seed_pairs.append((oe, e))
                break
        else:
            new.append((s, e))
    seed_pairs = new
# for pair in seed_pairs:
#     for i in range(pair[0], pair[0] + pair[1]):
#         seeds2.append(i)
# for section in sections:
#     for pair in seed_pairs:
#         for i in range(pair[0], pair[0] + pair[1]):
#             new_location = seed_path(i, section)
#             min_seed = min(min_seed, new_location)

print(min(seed_pairs)[0])
# print(min(seeds2))
