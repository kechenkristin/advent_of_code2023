def parse_file(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def parse_int_lst(str_lst):
    return [int(x) for x in str_lst]
