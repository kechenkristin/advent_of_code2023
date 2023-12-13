from common import parse_file

def get_grids(filename):
    pass


def get_split_index(grid):
    # 3
    cache = ""

    for i in range(len(grid)):
        if grid[i] == cache:
            return i - 1
        cache = grid[i]
    return -999


def get_matrix(filename):
    return parse_file(filename)


def trans_matrix(matrix):
    return list(zip(*matrix))

def if_match(grid, i):
    index1, index2 = i, i + 1
    while index1 >= 0 and index2 <= len(grid) - 1:
        if grid[index1] != grid[index2]:
            return False
        index1 -= 1
        index2 += 1
    return True

def single_matrix(filename):
    matrix = get_matrix(filename)
    split_index = get_split_index(matrix)
    match = if_match(matrix, split_index)
    if match:
        return (split_index + 1) * 100
    else:
        return get_split_index(trans_matrix(matrix)) + 1


if __name__ == '__main__':
    index = get_split_index(get_matrix("test2.txt"))
    print(index)  # 3

    matrix = trans_matrix(get_matrix("test1.txt"))
    print(matrix)

    index2 = get_split_index(matrix)
    print(index2)  # 4

    demo1 = if_match(get_matrix("test1.txt"), 2)
    print(demo1)    # False

    demo2 = if_match(matrix, index2)
    print(demo2) #t

    demo3 = if_match(get_matrix("test2.txt"), 3)
    print(demo3) #t

    print(single_matrix("test1.txt"))
    print(single_matrix("test2.txt"))
