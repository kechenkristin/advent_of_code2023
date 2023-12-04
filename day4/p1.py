import re
from functools import reduce

from common import parse_file

def solution(file_name, id):
    lines = parse_file(file_name)
    return get_points(lines) if id == 1 else get_copy(lines)

def get_points(lines):
    result = 0
    for line in lines:
        cards = extract_card_values(line)
        have = extract_second_card_values(line)

        win = [card for card in have if card in cards]

        if win:
            result += 2 ** (len(win) - 1)
    return result

def get_copy(lines):
    multiplier = [1 for _ in lines]
    totalSrc = 0

    for i, line in enumerate(lines):
        cards = extract_card_values(line)
        have = extract_second_card_values(line)
        win = [card for card in have if card in cards]
        mymult = multiplier[i]
        for j in range(i + 1, min(i + len(win), len(lines))):
            multiplier[j] += mymult
        totalSrc += mymult

    return totalSrc

def extract_card_values(input_str):
    str_ = input_str.split(':')[1].split("|")[0].strip().split()
    return [int(s) for s in str_]


def extract_second_card_values(input_str):
    str_ = input_str.split("|")
    return [int(s) for s in str_[1].strip().split()]


if __name__ == '__main__':
    # lines = parse_file("testinput1.txt")
    # print(extract_card_values(lines[0]))
    #
    # print(solution("input1.txt", 2))

    ll = [x for x in open("input1.txt").read().strip().split('\n')]
    p1 = 0
    multiplier = [1 for i in ll]
    p2 = 0
    for i,l in enumerate(ll):
        winning = set([int(x) for x in l.split(":")[1].split("|")[0].strip().split()])
        have = [int(x) for x in l.split("|")[1].strip().split()]
        have = [x for x in have if x in winning]
        if len(have):
            p1 += 2**(len(have)-1)
        mymult = multiplier[i]
        for j in range(i+1,min(i+len(have)+1,len(ll))):
            multiplier[j]+=mymult
        p2 += mymult
    print(p1, p2)
