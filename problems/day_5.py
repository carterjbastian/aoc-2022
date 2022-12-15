from lib.helpers import log, get_strings_by_lines
from lib.config import TEST_MODE

TEST_STACKS = {
    "1": ["Z", "N"],
    "2": ["M", "C", "D"],
    "3": ["P"],
}

REAL_STACKS = {
    "1": ["H", "B", "V", "W", "N", "M", "L", "P"],
    "2": ["M", "Q", "H"],
    "3": ["N", "D", "B", "G", "F", "Q", "M", "L"],
    "4": ["Z", "T", "F", "Q", "M", "W", "G"],
    "5": ["M", "T", "H", "P"],
    "6": ["C", "B", "M", "J", "D", "H", "G", "T"],
    "7": ["M", "N", "B", "F", "V", "R"],
    "8": ["P", "L", "H", "M", "R", "G", "S"],
    "9": ["P", "D", "B", "C", "N"],
}

# I hate that you can conditionally declare variables in python. yuck.
if TEST_MODE:
    stacks = TEST_STACKS
else:
    stacks = REAL_STACKS


def simulate(part):
    input_arr = get_strings_by_lines('5.txt')

    log(stacks)

    for pair in input_arr:
        strAmt, rest = pair.strip("move ").split(" from ")
        amt = int(strAmt)
        start, end = rest.split(" to ")
        log(f"{amt}: {start} -> {end}")

        rev = stacks[start][-1 * amt:]
        stacks[start] = stacks[start][:-1 * amt]
        stacks[end] += reversed(rev) if part == 1 else rev
        log(stacks)

    return "".join([v[-1] for v in stacks.values()])


def part_1():
    return simulate(1)


def part_2():
    return simulate(2)
