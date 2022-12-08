from lib.helpers import log, get_strings_by_lines

def parse_grid():
    rows = get_strings_by_lines('8.txt')
    grid = [list() for i in range(len(rows))]
    for idx, row in enumerate(rows):
        for c in row:
            grid[idx].append((int(c), False))

    return grid

def part_1():
    grid = parse_grid()

    # Horizontal
    for col in range(len(grid[0])):
        tallest_up = -1
        tallest_down = -1
        for idx in range(len(grid)):
            # Top Down
            val, seen = grid[idx][col]
            if val > tallest_up:
                grid[idx][col] = (val, True)
                tallest_up = val
            
            # Bottom Up
            val, seen = grid[(-1 * idx) - 1][col]
            if val > tallest_down:
                grid[(-1 * idx) - 1][col] = (val, True)
                tallest_down = val

    # Vertical
    for row in range(len(grid)):
        tallest_left = -1
        tallest_right = -1
        for idx in range(len(grid[0])):
            # Top Down
            val, seen = grid[row][idx]
            if val > tallest_left:
                grid[row][idx] = (val, True)
                tallest_left = val
            
            # Bottom Up
            val, seen = grid[row][(-1 * idx) - 1]
            if val > tallest_right:
                grid[row][(-1 * idx) - 1] = (val, True)
                tallest_right = val

    # Count Em
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            total += (1 if grid[y][x][1] else 0)

    return total

def part_2():
    grid = parse_grid()

    max_score = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            # find the score left
            left_score = 0
            for i in range(x - 1, -1, -1):
                left_score += 1
                if grid[y][x][0] <= grid[y][i][0]:
                    break

            # find the score right
            right_score = 0
            for i in range(x + 1, len(grid[0])):
                right_score += 1
                if grid[y][x][0] <= grid[y][i][0]:
                    break

            # find the score up
            up_score = 0
            for j in range(y - 1, -1, -1):
                up_score += 1
                if grid[y][x][0] <= grid[j][x][0]:
                    break

            # find the score down
            down_score = 0
            for j in range(y + 1, len(grid)):
                down_score += 1
                if grid[y][x][0] <= grid[j][x][0]:
                    break

            # Multiply together
            score = left_score * right_score * up_score * down_score
            # Debug info to print
            grid[y][x] = (grid[y][x][0], grid[y][x][1], score, [left_score, right_score, up_score, down_score])
            if score > max_score:
                max_score = score

    for r in grid:
        log(r)

    return max_score
