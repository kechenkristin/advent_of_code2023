from common import parse_file



def build_graph(filename):
    lines = parse_file(filename)
    row, col = len(lines), len(lines[0])

    # horizontal
    horizontal = []
    for i in range(row):
        flag = True
        for j in range(col):
            if lines[i][j] == '#':
                flag = False
        if flag:
            horizontal.append(i)

    # vertical
    vertical = []
    for i in range(row):
        flag = True
        for j in range(col):
            if lines[i][j] == '#':
                flag = False
        if flag:
            horizontal.append(i)
