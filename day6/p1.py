from common import parse_file, parse_int_lst


def get_time_dis(filename):
    lines = parse_file(filename)
    times = lines[0].split(":")[1].strip().split()
    distance = lines[1].split(":")[1].strip().split()
    return parse_int_lst(times), parse_int_lst(distance)

def get_time_dis2(filename):
    lines = parse_file(filename)
    times = lines[0].split(":")[1].strip().split()
    distance = lines[1].split(":")[1].strip().split()
    time_str, distance_str = "", ""

    for t in times:
        time_str += t
    for d in distance:
        distance_str += d
    return int(time_str), int(distance_str)

def func(time, dis):
    count = 0
    for t in range(time + 1):
        dx = t * (time - t)
        if dx > dis:
            count += 1
    return count

def p1(times, distances):
    ans = 1
    for i in range(len(times)):
        ans *= func(times[i], distances[i])
    return ans

def p2(time, distance):
    return func(time, distance)

if __name__ == '__main__':
    time, dis = get_time_dis2("input.txt")
    print(p2(time, dis))

    # print(p1(times, dis))