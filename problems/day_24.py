from collections import defaultdict, deque
from lib.helpers import log, get_strings_by_lines

direction_fn = {
    '^': lambda x, y: (x, y - 1),
    'v': lambda x, y: (x, y + 1),
    '<': lambda x, y: (x - 1, y),
    '>': lambda x, y: (x + 1, y),
}


def out_of_bounds(x, y, grid):  # Check if the position is out of bounds
    return x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid)


def parse_inputs():
    grid = []  # Triple nested list

    lines = get_strings_by_lines('24.txt')

    height = len(lines[1:-1])
    width = len(lines[0][1:-1])
    for y, line in enumerate(lines[1:-1]):
        grid += [defaultdict(list)]
        for x, char in enumerate(line[1:-1]):
            if char != '.':
                grid[y][x] += [char]

    return grid, height, width


def print_grid(grid, height, width):
    for y in range(height):
        for x in range(width):
            if len(grid[y][x]) > 1:
                print(len(grid[y][x]), end='')
            elif len(grid[y][x]) == 1:
                print(grid[y][x][0], end='')
            else:
                print('.', end='')
        print()
    print()


def iter_grid(grid, height, width):
    next_grid = [defaultdict(list) for _ in range(height)]

    for y in range(height):
        for x in range(width):
            blizzards = grid[y][x]
            for direction in blizzards:
                nX, nY = direction_fn[direction](x, y)
                # Wrapping logic for blizzards
                if nX < 0:
                    nX = width - 1
                if nY < -0:
                    nY = height - 1
                if nX >= width:
                    nX = 0
                if nY >= height:
                    nY = 0
                next_grid[nY][nX] += [direction]

    return next_grid


def next_options(next_grid, cx, cy):
    opts = []
    # Look up, down, left, and right, and still
    for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]:
        if out_of_bounds(cx + dx, cy + dy, next_grid):
            continue
        if len(next_grid[cy + dy][cx + dx]) > 0:
            continue
        else:
            opts += [(cx + dx, cy + dy)]

    return opts


def part_1():
    grid, height, width = parse_inputs()

    # Basic BFS
    init = (0, -1)

    print_grid(grid, height, width)
    log("Iterating /n")
    next_grid = iter_grid(grid, height, width)
    print_grid(next_grid, height, width)
