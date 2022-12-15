from lib.helpers import log, get_strings_by_lines


def finder(length):
    signal = get_strings_by_lines('6.txt')[0]
    log(signal)

    for idx in range(length, len(signal)):
        if (len(set(signal[idx-length:idx])) == length):
            return idx
    return -1


def part_1():
    return finder(4)


def part_2():
    return finder(14)
