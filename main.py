#!/bin/bash python3
import argparse
import lib.config
import importlib

parser = argparse.ArgumentParser(prog="advent_of_code_2020")

# Positional Arguments (Day and Part)
parser.add_argument("day", type=int, help="Which advent day?")
parser.add_argument("part", type=int, help="Which part of this day to run?")

# Optional Arguments (Test mode and Debug mode)
parser.add_argument(
    "-t", "--test", help="Run with test inputs", action="store_true")
parser.add_argument(
    "-d", "--debug", help="Run with logging", action="store_true")

# Parse arguments
args = parser.parse_args()

# Set global state
lib.config.DEBUG_MODE = args.debug
lib.config.TEST_MODE = args.test
lib.config.DAY_NUMBER = args.day

# Import helper functions
from lib.helpers import log, get_strings_by_lines

if __name__ == "__main__":
    # import the library dynamically
    lib_name = f"problems.day_{args.day}"
    solver = importlib.import_module(lib_name)

    # Choose day 1 or day 2
    if args.test:
        if args.part != 2:
            log('\nTesting part 1...')
            computed = solver.part_1()
            all_answers = get_strings_by_lines('answers-part-1.txt')
            answer = all_answers[args.day - 1]
            if str(computed) == answer:
                print(f"Part 1: PASSED ({computed})")
            else:
                print("Part 1: FAILED")
                print(f"\tcomputed: {computed}")
                print(f"\tintended: {answer}")
        if args.part != 1:
            log('\nTesting part 2...')
            computed = solver.part_2()
            all_answers = get_strings_by_lines('answers-part-2.txt')
            answer = all_answers[args.day - 1]
            if str(computed) == answer:
                print(f"Part 2: PASSED ({computed})")
            else:
                print("Part 2: FAILED")
                print(f"\tcomputed: {computed}")
                print(f"\tintended: {answer}")
    else:
        if args.part != 2:
            log('\nstarting part 1...')
            print(solver.part_1())
        if args.part != 1:
            log('\nstarting part 2...')
            print(solver.part_2())
