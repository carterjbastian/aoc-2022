from lib.helpers import log, get_strings_by_lines


def part_1():
    signal = get_strings_by_lines('6.txt')[0]
    log(signal)

    for idx in range(4, len(signal)):
        if (len(set(signal[idx-4:idx])) == 4):
            return idx

    return -1

def part_2():
    signal = get_strings_by_lines('6.txt')[0]
    log(signal)

    for idx in range(14, len(signal)):
        if (len(set(signal[idx-14:idx])) == 14):
            return idx

    return -1
