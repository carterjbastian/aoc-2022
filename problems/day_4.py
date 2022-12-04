from lib.helpers import log, get_strings_by_lines

def part_1():
    input_arr = get_strings_by_lines('4.txt')

    cur_sum = 0
    for pair in input_arr:
        log(pair)
        p1, p2 = pair.split(',')
        l1, h1 = [int(v) for v in p1.split('-')]
        l2, h2 = [int(v) for v in p2.split('-')]

        if (l1 <= l2 and h1 >= h2) or (l2 <= l1 and h2 >= h1):
            cur_sum += 1

    return cur_sum

def part_2():
    input_arr = get_strings_by_lines('4.txt')

    cur_sum = 0
    for pair in input_arr:
        log(pair)
        p1, p2 = pair.split(',')
        l1, h1 = [int(v) for v in p1.split('-')]
        l2, h2 = [int(v) for v in p2.split('-')]

        if (l1 <= h2 and l1 >= l2) or (h1 >= l2 and h1 <= h2) or (l2 <= h1 and l2 >= l1) or (h2 >= l1 and h2 <= h1):
            cur_sum += 1

    return cur_sum
