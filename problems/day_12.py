from lib.helpers import log, get_strings_by_lines

# Very math super cool
INFINITY = 100000000000000000000000000

def make_grid():
    rows = get_strings_by_lines('12.txt')
    grid = [[] for _ in range(len(rows))]

    start = (-1, -1)
    end = (-1, -1)
    all_starts = []

    for j, row in enumerate(rows):
        for i, c in enumerate(row):
            height = ord(c) - 97
            if height < 0:
                if c == "S":
                    start = (i, j)
                    grid[j] += [0]
                    all_starts += [(i, j)]
                elif c == "E":
                    end = (i, j)
                    grid[j] += [25]
            else:
                if height == 0:
                    all_starts += [(i, j)]
                grid[j] += [height]

    return grid, start, end, all_starts


def shortest_path(grid, start, end):
    # Track visited -> Cost to get there + where from
    visited = {
        start: (0, None),
    }

    # Basically BFS
    to_check = [start]
    while len(to_check) > 0:
        (x, y) = to_check.pop(0)
        cur_height = grid[y][x]
        cur_cost = visited[(x, y)][0]

        # Look at all the possible moves
        for option in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            # Valid option?
            if option[0] < 0 or option[1] < 0 or option[0] >= len(grid[0]) or option[1] >= len(grid):
                continue

            # If we can't get to it from here, skip
            if grid[option[1]][option[0]] > cur_height + 1:
                continue

            # If we already have a faster way to get there, skip
            if option in visited and visited[option][0] <= cur_cost + 1:
                continue

            # Great, add it to the list
            visited[option] = (cur_cost + 1, (x, y))
            to_check += [option]

    if end in visited:
        return visited[end][0]
    else:
        return INFINITY

def part_1():
    grid, start, end, _ = make_grid()
    return shortest_path(grid, start, end)

def part_2():
    grid, _, end, all_starts = make_grid()
    log(all_starts)
    lowest = INFINITY # Infinity
    for start in all_starts:
        score = shortest_path(grid, start, end)
        if score < lowest:
            lowest = score

    return lowest
