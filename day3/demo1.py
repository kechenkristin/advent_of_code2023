# pass the graph into a matrix
from common import parse_file

"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def parse_str(input_str):
    ret = []
    curr_num = ""

    for char in input_str:
        if char.isdigit():
            curr_num += char
        else:
            if curr_num:
                ret.extend([curr_num] * len(curr_num))
            curr_num = ""

            ret.append(char)

    if curr_num:
        ret.extend([curr_num] * len(curr_num))
    return ret


def build_matrix(lines):
    return [parse_str(line) for line in lines]


def find_num(lines):
    row, col = len(lines), len(lines[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
    symbols = ('#', '$', '%', '&', '*', '+', '-', '/', '=', '@')
    count = 0

    for x in range(row):
        for y in range(col):
            # print(lines[x][y])
            if lines[x][y] in symbols:
                for dx, dy in directions:
                    next_x, next_y = dx + x, dy + y
                    if next_x < 0 or next_x >= row or next_y < 0 or next_y >= col:
                        continue
                    if lines[next_x][next_y].isnumeric():
                        count += int(lines[next_x][next_y])
    return count


def sum_num(num_set):
    num_lst = list(num_set)
    return sum(int(num) for num in num_lst)


def solution(file_name):
    lines = parse_file(file_name)
    matrix = build_matrix(lines)
    num_set = find_num(matrix)
    return sum_num(num_set)


if __name__ == '__main__':
    lines = parse_file("input.txt")
    # print(lines)
    print("info for lines:", len(lines), len(lines[0]))

    matrix = build_matrix(lines)
    print(matrix)
    print("info for matrix:", len(matrix), len(matrix[0]))

    demo = find_num(matrix)
    print(demo)

    # sum_ = solution("input.txt")
    # print(sum_)

    # demo = parse_str("....456...89")
    # print(demo)