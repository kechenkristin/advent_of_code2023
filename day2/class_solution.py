import re


def parse_file(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

class CubeSample:
    """ A sample contains a number of red, blue, and green cubes """
    def __init__(self, red=0, blue=0, green=0):
        self.red = red
        self.blue = blue
        self.green = green

class Game:
    """ A game has an ID, and a random number of samples """
    def __init__(self, id, samples):
        self.id = id
        self.samples = samples

def parse_input(data) -> list[Game]:
    game_pattern = re.compile(r"Game\s+(\d+)")
    cubes_pattern = re.compile(r"(\d+)\s*(\w+)") # E.g. "3 blue"

    games = []
    for line in data:
        game_part, samples_part = line.split(":")
        game_id = int(game_pattern.findall(game_part)[0])
        samples = samples_part.split(";")

        cube_samples = []
        for sample in samples:
            matches = cubes_pattern.finditer(sample)
            cube_counts = {"red": 0, "green": 0, "blue": 0} # reset cube counts for each sample
            for match in matches:
                cube_count, cube_colour = match.groups()
                cube_counts[cube_colour] = int(cube_count)

            cube_samples.append(CubeSample(cube_counts["red"], cube_counts["blue"], cube_counts["green"]))

        games.append(Game(game_id, cube_samples))

    return games


def parse_input2(data) -> list[Game]:
    game_pattern = re.compile(r"Game\s+(\d+)")
    cubes_pattern = re.compile(r"(\d+)\s*(\w+)") # E.g. "3 blue"

    games = []
    for line in data:
        game_part, samples_part = line.split(":")
        game_id = int(game_pattern.findall(game_part)[0])
        samples = samples_part.split(";")

        cube_samples = []
        for sample in samples:
            matches = cubes_pattern.finditer(sample)
            cube_counts = {"red": 0, "green": 0, "blue": 0} # reset cube counts for each sample
            for match in matches:
                cube_count, cube_colour = match.groups()
                if int(cube_count) > cube_counts[cube_colour]:
                    cube_counts[cube_colour] = int(cube_count)

            cube_samples.append(CubeSample(cube_counts["red"], cube_counts["blue"], cube_counts["green"]))

        games.append(Game(game_id, cube_samples))

    return games

def solve_part1(games: list[Game]):
    """ Return the sum of the IDs for games that are possible. """

    allowed_red = 12
    allowed_green = 13
    allowed_blue = 14

    possible_games = []
    for game in games:
        possible = True
        for game_sample in game.samples:
            if (game_sample.red > allowed_red
                    or game_sample.green > allowed_green
                    or game_sample.blue > allowed_blue):
                possible = False

        if possible:
            possible_games.append(game.id)
    print(possible_games)
    return sum(game for game in possible_games)


def solve_part2(games: list[Game]):
    """ Return the sum of the powers of all the games """
    game_powers = []
    for game in games:
        max_blue = max_green = max_red = 0
        for game_sample in game.samples:
            max_blue = max(max_blue, game_sample.blue)
            max_green = max(max_green, game_sample.green)
            max_red = max(max_red, game_sample.red)

        # We're told that power = product of r, g, b
        game_powers.append(max_blue*max_green*max_red)

    return sum(game_powers)

if __name__ == '__main__':
    # data = parse_file("data.txt")
    # games = parse_input(data)
    # demo = solve_part1(games)
    # print(demo)


    data = parse_file("data.txt")
    games = parse_input2(data)
    demo = solve_part2(games)
    print(demo)
