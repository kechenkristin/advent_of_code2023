import re

from common import parse_file


def parse_string(game_str):
    game_pattern = re.compile(r"Game\s+(\d+)")
    cubes_pattern = re.compile(r"(\d+)\s*(\w+)")  # E.g. "3 blue"
    game_part, samples_part = game_str.split(":")
    game_id = int(game_pattern.findall(game_part)[0])
    samples = samples_part.split(";")

    sample_cubes = []
    for sample in samples:
        cube_counts = {"red": 0, "green": 0, "blue": 0}
        matches = cubes_pattern.finditer(sample)
        for match in matches:
            cube_count, cube_colour = match.groups()
            cube_counts[cube_colour] = int(cube_count)
        sample_cubes.append(cube_counts)
    return {game_id: sample_cubes}


def parse_games(lines):
    return [parse_string(line) for line in lines]


def solve_p1(games):
    allowed_red = 12
    allowed_green = 13
    allowed_blue = 14
    count = 0
    for item in games:
        for game_id, colors in item.items():
            possible = True
            for color in colors:
                if color["red"] > allowed_red or color["blue"] > allowed_blue or color["green"] > allowed_green:
                    possible = False
            if possible:
                count += game_id
    return count


def solve_p2(games):
    count = 0
    for item in games:
        for colors in item.values():
            max_blue = max_green = max_red = 0
            for color in colors:
                max_blue = max(max_blue, color["blue"])
                max_green = max(max_green, color["green"])
                max_red = max(max_red, color["red"])
            count += max_red * max_blue * max_green
    return count


def solution(filename, question_id):
    lines = parse_file(filename)
    games = parse_games(lines)
    return solve_p1(games) if question_id == 1 else solve_p2(games)


if __name__ == '__main__':
    demo = solution("data.txt", 1)
    print(demo)
