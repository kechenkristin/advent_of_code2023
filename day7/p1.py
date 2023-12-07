from collections import Counter

from common import parse_file


def strength(hand):
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    C = Counter(hand)

    if sorted(C.values()) == [5]:
        return (10, hand)
    elif sorted(C.values()) == [1, 4]:
        return (9, hand)
    elif sorted(C.values()) == [2, 3]:
        return (8, hand)
    elif sorted(C.values()) == [1, 1, 3]:
        return (7, hand)
    elif sorted(C.values()) == [1, 2, 2]:
        return (6, hand)
    elif sorted(C.values()) == [1, 1, 1, 2]:
        return (5, hand)
    else:
        return (4, hand)

def get_cards_values(filename):
    lines = parse_file(filename)
    cards = [line.split(" ")[0] for line in lines]
    vals = [int(line.split(" ")[1]) for line in lines]
    return list(zip(cards, vals))

def p1(filename):
    H = get_cards_values(filename)
    H = sorted(H, key=lambda hb: strength(hb[0]))
    ans = 0
    for i,(h,b) in enumerate(H):
        ans += (i+1)*int(b)
    return ans

if __name__ == '__main__':
    demo2 = p1("input.txt")
    print(demo2)