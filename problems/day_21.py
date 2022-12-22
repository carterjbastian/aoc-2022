from lib.helpers import log, get_strings_by_lines


def add(x, y): return x + y
def subtract(x, y): return x - y
def divide(x, y): return x // y
def multiply(x, y): return x * y


INVERSE_FN = {
    add: subtract,
    subtract: add,
    divide: multiply,
    multiply: divide,
}


def get_monkeys():
    lines = get_strings_by_lines('21.txt')

    monkeys = []
    known = {}
    unknown = {}
    for l in lines:
        monkey_name, remainder = l.split(': ')
        monkeys += [monkey_name]

        plus_split = remainder.split(' + ')
        if len(plus_split) == 2:
            unknown[monkey_name] = (plus_split[0], plus_split[1], add)
            continue

        div_split = remainder.split(' / ')
        if len(div_split) == 2:
            unknown[monkey_name] = (div_split[0], div_split[1], divide)
            continue

        sub_split = remainder.split(' - ')
        if len(sub_split) == 2:
            unknown[monkey_name] = (sub_split[0], sub_split[1], subtract)
            continue

        mul_split = remainder.split(' * ')
        if len(mul_split) == 2:
            unknown[monkey_name] = (mul_split[0], mul_split[1], multiply)
            continue

        # It's not a divider, it's a number
        known[monkey_name] = int(remainder)

    return known, unknown


def part_1():
    known, unknown = get_monkeys()

    iteration = 1
    while 'root' not in known:
        log(f'Iteration {iteration}')
        iteration += 1
        # Which monkeys can we solve now
        next_up = [
            (monkey, val)
            for monkey, val in unknown.items()
            if val[0] in known and val[1] in known
        ]
        log(f'Next up: {len(next_up)}')

        for (monkey, (dep1, dep2, fn)) in next_up:
            known[monkey] = fn(known[dep1], known[dep2])
            del unknown[monkey]

    return known['root']


def part_2():
    known, unknown = get_monkeys()

    del known['humn']

    iteration = 1
    while 'root' not in known:
        log(f'Iteration {iteration}')
        iteration += 1
        # Which monkeys can we solve now
        next_up = [
            (monkey, val)
            for monkey, val in unknown.items()
            if val[0] in known and val[1] in known
        ]
        log(f'Next up: {len(next_up)}')
        if (len(next_up) == 0):
            log(f'Unknown left: {len(unknown.keys())}')
            break

        for (monkey, (dep1, dep2, fn)) in next_up:
            known[monkey] = fn(known[dep1], known[dep2])
            del unknown[monkey]

    two_left = []
    one_left = []
    for (u, (dep1, dep2, fn)) in unknown.items():
        if dep1 in known or dep2 in known:
            one_left += [(u)]
        else:
            two_left += [(u)]

    solve_for_val = None
    solve_for_monkey = None
    # Solve the root problem
    (dep1, dep2, fn) = unknown['root']
    if (dep1 in known):
        solve_for_val = known[dep1]
        solve_for_monkey = dep2
    else:
        solve_for_val = known[dep2]
        solve_for_monkey = dep1

    next_up = solve_for_monkey
    next_val = solve_for_val
    while next_up != 'humn':
        (dep1, dep2, fn) = unknown[next_up]
        if (dep1 in known):
            # Arg order is weird
            if fn == divide:
                next_val = fn(known[dep1], next_val)
            elif fn == subtract:
                next_val = fn(known[dep1], next_val)
            else:
                next_val = INVERSE_FN[fn](next_val, known[dep1])
            next_up = dep2
        else:
            next_val = INVERSE_FN[fn](next_val, known[dep2])
            next_up = dep1

    log(unknown)
    log(one_left)
    log(two_left)

    log(solve_for_val)
    log(solve_for_monkey)

    log(next_val)
    log(next_up)

    # then solve each other one one at a time

    return next_val
