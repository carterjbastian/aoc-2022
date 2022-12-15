from lib.helpers import log, get_strings_by_lines


def part_1():
    input_arr = get_strings_by_lines('3.txt')

    cur_sum = 0
    for rucksack in input_arr:
        divider = len(rucksack) // 2
        compartment1 = {ord(c) - 64 + 26 if c.isupper()
                        else ord(c) - 96 for c in rucksack[0:divider]}
        compartment2 = {ord(c) - 64 + 26 if c.isupper()
                        else ord(c) - 96 for c in rucksack[divider:]}
        both = compartment1 & compartment2
        log(len(both))
        cur_sum += both.pop()

    return cur_sum


def part_2():
    input_arr = get_strings_by_lines('3.txt')

    cur_sum = 0
    group = {}
    for idx, rucksack in enumerate(input_arr):
        compartment = {ord(c) - 64 + 26 if c.isupper()
                       else ord(c) - 96 for c in rucksack}

        if (idx + 1) % 3 == 0:
            # End of the group of 3. What's the badge?
            group &= compartment
            cur_sum += group.pop()
            group = {}
        elif len(group) == 0:
            # First compartment in the group - any could be it
            group = compartment
        else:
            # Another compartment - union the sets
            group &= compartment

    return cur_sum
