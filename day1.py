#part 1
def parse_nums(line):
    return [c for c in line if c.isdigit()]

#part 2
def parse_nums_1(line):
    start = parse_from_start(line)
    end = parse_from_end(line)
    return int(start + end)

def check_in_dict(line,idx=0):
    window_size = 3
    while window_size < 6:
        if line[idx:idx+window_size] in dict.keys():
            return str(dict[line[idx:idx+window_size]])
        else:
            window_size += 1

def check_kind(line,c,idx):
    if c.isdigit():
        return c
    v = check_in_dict(line,idx)
    if v is not None:
        return v

    
def parse_from_start(line):
    for idx,c in enumerate(line):
        res = check_kind(line,c,idx)
        if res:
            return res
        
def parse_from_end(line):
    for idx,c in reversed(list(enumerate(line))):
        res = check_kind(line,c,idx-2)
        if res:
            return res

dict = {
    "one" : 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
f = open("input.txt", "r")
lines = f.read().splitlines()
vals = [parse_nums_1(line) for line in lines]
print(sum(vals))
