from lib.helpers import log, get_all_strings_by_lines

def part_1():
    input_arr = get_all_strings_by_lines('1.txt')
    log(input_arr)

    cur_max = 0
    cur_sum = 0
    for val in input_arr:
        # End of group
        if val == "":
            if cur_sum > cur_max:
                cur_max = cur_sum
            # Update elf index and reset sum
            cur_sum = 0
        else:
            cur_sum += int(val)

    return cur_max

def part_2():
    input_arr = get_all_strings_by_lines('1.txt')

    totals = []

    cur_sum = 0
    for val in input_arr:
        # End of group
        if val == "":
            totals += [cur_sum]
            cur_sum = 0
        else:
            cur_sum += int(val)
    # Don't forget the last one.
    totals += [cur_sum]
    log(totals)

    return sum(sorted(totals)[-3:])
