from lib.helpers import log, get_input
import json
import functools


def cmp(left, right):
    if type(left) is int and type(right) is int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    else:
        # Maybe coerce to list
        if type(left) is not list:
            left = [left]
        if type(right) is not list:
            right = [right]

        idx = 0
        while True:
            # Check if result comes from list len
            if idx == len(left):
                if idx < len(right):
                    return -1
                else:
                    return 0

            if idx == len(right):
                return 1

            # Compare this element of the list
            nextCmp = cmp(left[idx], right[idx])
            if nextCmp != 0:
                return nextCmp

            # Move to next item
            idx += 1


def part_1():
    strs = get_input('13.txt').split('\n\n')
    pairs = [(json.loads(s.split('\n')[0]), json.loads(s.split('\n')[1]))
             for s in strs]
    log(pairs)

    total = 0
    for idx, (left, right) in enumerate(pairs):
        log(f"Testing {idx + 1}: {left} vs {right}")
        res = cmp(left, right)
        log(f"result: {res}")

        if res == -1:
            total += idx + 1

    return total


def part_2():
    vals = [json.loads(l) for l in get_input('13.txt').split('\n') if l]
    vals += [[[2]], [[6]]]
    # Sort with our comparator
    sortedVals = sorted(vals, key=functools.cmp_to_key(cmp))
    total = 1
    for idx, val in enumerate(sortedVals):
        if cmp(val, [[2]]) == 0 or cmp(val, [[6]]) == 0:
            total *= (1 + idx)

    return total
