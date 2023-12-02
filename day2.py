from functools import reduce
def parse_game(game):
    rounds = game.split(",")
    rounds = [round.strip().split(" ") for round in rounds]
    return rounds
def parse_line(line):
    vals = line.split(":")
    games = vals[1].split(";")
    id = vals[0].split(" ")[-1]
    games = [parse_game(game) for game in games]
    return [id,games]

def part_1(games,color_dict):
    for game in games[1]:
        for round in game:
            for key in color_dict.keys():
                if round[1] == key:
                    if int(round[0]) > color_dict[key]:
                        return False
    return True

def part_2(games):
    color_dict = {
        "blue": -1, 
        "red": -1, 
        "green": -1
    }
    for game in games[1]:
        for round in game:
            curr = color_dict[round[1]]
            color_dict[round[1]] = max(int(round[0]),curr)

    return reduce(lambda x,y: x*y, color_dict.values())




color_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}
f = open("input.txt", "r")
lines = f.read().splitlines()
games = [parse_line(line) for line in lines]
result = list(map(lambda x: int(x[0]), 
                 filter(lambda game: part_1(game,color_dict),games)))
print(sum(result))
dicts = [part_2(game) for game in games]
print(sum(dicts))

