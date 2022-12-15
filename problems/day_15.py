from lib.helpers import log, get_strings_by_lines


def part_1():
    lines = get_strings_by_lines('15.txt')
    for line in lines:
        log(line)

    return len(lines)
