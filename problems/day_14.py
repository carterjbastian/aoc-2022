from lib.helpers import log, get_strings_by_lines

SAND_INIT = (500, 0)

def get_grid():
    strs = get_strings_by_lines('14.txt')

    filled = set()
    max_depth = 0
    for line in strs:
        points = [tuple(t.split(',')) for t in line.split(" -> ")]
        # Fill in the rocks
        for idx in range(len(points) - 1):
            x1, y1 = int(points[idx][0]), int(points[idx][1])
            x2, y2 = int(points[idx + 1][0]), int(points[idx + 1][1])

            # figure out max depth
            if y1 > max_depth:
                log(f"setting max depth {y1}")
                max_depth = y1

            if y2 > max_depth:
                log(f"setting max depth {y2}")
                max_depth = y2

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    filled.add((x1, y))
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    filled.add((x, y1))
    return filled, max_depth

def part_1():
    filled, max_depth = get_grid()

    total = 0
    while True:
        x, y = SAND_INIT
        while True:
            # Check if we're falling off the cliff
            if y == max_depth:
                log(filled)
                log(len(filled))
                log(max_depth)
                return total

            # Calculate next place to go
            down = (x, y + 1)
            down_left = (x - 1, y + 1)
            down_right = (x + 1, y + 1)

            if down not in filled:
                log('Going down')
                x, y = down
            elif down_left not in filled:
                log('Going down left')
                x, y = down_left
            elif down_right not in filled:
                log('Going down right')
                x, y = down_right
            else:
                # Place the sand
                log(f"Resting at {x, y}")
                filled.add((x,y))
                total += 1
                break

def part_2():
    filled, max_depth = get_grid()

    total = 0
    while True:
        x, y = SAND_INIT
        while True:
            if y == max_depth + 1:
                # We've hit the bottom - add a rock
                filled.add((x, y))
                total += 1
                break

            # Calculate next place to go
            down = (x, y + 1)
            down_left = (x - 1, y + 1)
            down_right = (x + 1, y + 1)

            if down not in filled:
                log('Going down')
                x, y = down
            elif down_left not in filled:
                log('Going down left')
                x, y = down_left
            elif down_right not in filled:
                log('Going down right')
                x, y = down_right
            else:
                # Have we hit the end?
                if x == 500 and y == 0:
                    log(f"Hit the stop")
                    return total + 1

                # Place the sand
                log(f"Resting at {x, y}")
                filled.add((x,y))
                total += 1
                break
