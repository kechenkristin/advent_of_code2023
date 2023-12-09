import numpy

from common import parse_int_lst, parse_file


def get_data(filename):
    lines = parse_file(filename)
    str_lst = [line.split(" ") for line in lines]
    return [parse_int_lst(s) for s in str_lst]


def build_sub_lst(lst):
    return numpy.diff(lst)


def zero_lst(lst):
    return all(v == 0 for v in lst)


def find_next(lst):
    if zero_lst(lst):
        return 0
    else:
        sub_lst = build_sub_lst(lst)
        return lst[-1] + find_next(sub_lst)


def find_prev(lst):
    if zero_lst(lst):
        return 0
    else:
        sub_lst = build_sub_lst(lst)
        return lst[0] - find_prev(sub_lst)


def find_sum(lsts, p1):
    return sum([find_next(lst) for lst in lsts]) if p1 else sum([find_prev(lst) for lst in lsts])


def solution(filename, p1):
    lsts = get_data(filename)
    return find_sum(lsts, p1)


if __name__ == '__main__':
    demo = get_data("test.txt")
    print(demo)
    # demo2 = build_sub_lst(demo)
    # print(demo2)
    #
    # demo3 = zero_lst(demo[0])
    # print(demo3)
    # demo4 = find_prev(demo[2])
    # print(demo4)
    demo5 = solution("input.txt", p1=False)
    print(demo5)
