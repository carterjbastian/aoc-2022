import time
from collections import defaultdict
from lib.helpers import log, get_strings_by_lines
import os


directions = [
    [(-1, -1), (1, -1), (0, -1)],  # North
    [(-1, 1), (1, 1), (0, 1)],  # South
    [(-1, -1), (-1, 1), (-1, 0)],  # West
    [(1, -1), (1, 1), (1, 0)],  # East
]

all_eight = [(-1, -1), (1, -1), (0, -1), (-1, 1),
             (1, 1), (0, 1), (-1, 0), (1, 0)]


def get_dimensions(grid):
    min_x = min([x for x, y in grid])
    max_x = max([x for x, y in grid])
    min_y = min([y for x, y in grid])
    max_y = max([y for x, y in grid])
    return min_x, max_x, min_y, max_y


def print_grid(grid):
    min_x, max_x, min_y, max_y = get_dimensions(grid)
    count = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in grid:
                print('#', end='')
            else:
                count += 1
                print('.', end='')
        print()
    return count


def iterate(grid, start_idx):
    moves = defaultdict(list)
    next_grid = set()
    moved_count = 0

    # For each position, find the next position
    for x, y in grid:
        if not any([(x + dx, y + dy) in grid for dx, dy in all_eight]):
            # If there are no neighbors, stay
            next_grid |= {(x, y)}
            continue

        for dir_idx in range(4):
            dir = directions[(start_idx + dir_idx) % 4]
            # Check each spot in the direction
            for dx, dy in dir:
                if (x + dx, y + dy) in grid:
                    break
            else:
                # If the loop didn't break, we found a move to do!
                moves[(x + dx, y + dy)].append((x, y))
                break
        else:
            # If the loop didn't break, we didn't find a move. Stay
            next_grid |= {(x, y)}

    for (x, y), move_list in moves.items():
        if len(move_list) == 1:
            # If there's only one, move there
            moved_count += 1
            next_grid |= {(x, y)}
        else:
            next_grid |= set(move_list)  # If there are multiple, stay

    return next_grid, moved_count


def part_1():
    lines = get_strings_by_lines('23.txt')

    grid = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                grid.add((x, y))

    print('\033[2J')
    c = print_grid(grid)

    i = 0
    for _ in range(10):
        # Wait for 2 seconds
        time.sleep(1)

        # Clear the screen
        print('\033[2J')

        grid, moved_count = iterate(grid, i)
        i = (i + 1) % 4
        c = print_grid(grid)

    return c


def part_2():
    lines = get_strings_by_lines('23.txt')

    grid = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                grid.add((x, y))

    print('\033[2J')
    c = print_grid(grid)

    i = 0
    round = 0
    moved_count = 1
    while moved_count != 0:
        # Wait for 2 seconds
        time.sleep(.1)

        # Clear the screen
        os.system('clear')

        grid, moved_count = iterate(grid, i)
        i = (i + 1) % 4
        c = print_grid(grid)
        round += 1

    return round
