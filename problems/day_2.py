from lib.helpers import log, get_strings_by_lines

symbol_map = {
    # rocks
    "A": 1,
    "X": 1,
    # papers
    "B": 2,
    "Y": 2,
    # scizzors
    "C": 3,
    "Z": 3,
}

def part_1():
    input_arr = get_strings_by_lines('2.txt')

    cur_sum = 0
    for val in input_arr:
        them = symbol_map[val[0]]
        me = symbol_map[val[2]]

        if them == me:
            # Draw
            cur_sum += me + 3
        elif (them % 3) + 1 == me:
            # Win - modular arithmetic just works sometimes don't ask questions
            cur_sum += me + 6
        else:
            # Loss
            cur_sum += me

    return cur_sum

def part_2():
    input_arr = get_strings_by_lines('2.txt')

    cur_sum = 0
    for val in input_arr:
        them = symbol_map[val[0]]
        match_result = val[2]

        if match_result == "X":
            # We need a loss
            me = (them + 3 - 1) % 3
            me += (3 if me == 0 else 0)
            cur_sum += me if me > 0 else 3
        elif match_result == "Y":
            # We need a Draw
            me = them
            cur_sum += them + 3
        else:
            # We need a win
            me = (them + 1) % 3
            me += (3 if me == 0 else 0)
            cur_sum += me + 6

    return cur_sum
