import math
from collections import defaultdict
from lib.helpers import log, get_strings_by_lines
import heapq

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
    for (dx, dy) in [(0, 0), (0, -1), (-1, 0), (0, 1), (1, 0)]:
        if out_of_bounds(cx + dx, cy + dy, next_grid):
            continue
        if len(next_grid[cy + dy][cx + dx]) > 0:
            continue
        else:
            opts += [(cx + dx, cy + dy)]

    return opts


def part_1():
    grid, height, width = parse_inputs()

    grid_caches = {}

    # Basic DFS with a queue
    init = (0, -1)
    target = (width - 1, height - 1)

    # Need a custom class for the heap
    class PriorityEntry(object):
        def __init__(self, pos, cost):
            self.pos = pos
            self.cost = cost
            # Minimize Manhattan distance
            self.priority = ((width - pos[0]) + (height - pos[1]))

        def __lt__(self, other):
            return self.priority < other.priority

    best_seen = 341
    pqueue = []
    seen = set()

    # Pre-load the blizzard cache
    last_bliz = grid
    wait = 0
    while len(pqueue) < 1000 and wait < 341:
        if len(last_bliz[0][0]) == 0:
            pqueue += [PriorityEntry(init, wait)]
            seen |= {(init[0], init[1], wait)}
            log(f"Adding wait of {wait}")
        grid_caches[wait] = last_bliz
        wait += 1
        last_bliz = iter_grid(last_bliz, height, width)

    # While there is a queue
    closest = math.inf
    while len(pqueue) > 0:
        if max([s.priority for s in pqueue]) < closest:
            closest = max([s.priority for s in pqueue])
            log(f"New Closest: {closest}")
        # Pop the first item
        entry = heapq.heappop(pqueue)
        cx, cy = entry.pos
        cost = entry.cost

        # If we've seen this before, skip it
        if cost >= best_seen:
            continue

        # If we've reached the target, update the best seen
        if (cx, cy) == target:
            best_seen = cost
            log(f"Setting Best Seen: {best_seen}")
            continue

        # Get the next grid (with caching)
        next_grid = grid_caches.get(
            cost + 1, iter_grid(grid_caches[cost], height, width))
        grid_caches[cost + 1] = next_grid

        # Get the next options
        opts = next_options(next_grid, cx, cy)

        # Add the next valid options to the queue
        for (nx, ny) in opts:
            if (nx, ny) == target:
                best_seen = cost + 1
                log(f"Setting Best Seen: {best_seen}")
                continue
            if cost + 1 > best_seen:
                continue
            if (nx, ny, cost + 1) not in seen:
                seen |= {(nx, ny, cost + 1)}
                heapq.heappush(pqueue, PriorityEntry((nx, ny), cost + 1))

    return best_seen + 1
