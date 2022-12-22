from lib.helpers import log, get_strings_by_lines

# 2D Blocks (in order)
blocks = [
    [
        [1, 1, 1, 1],
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1],
    ],
    [
        [1],
        [1],
        [1],
        [1],
    ],
    [
        [1, 1],
        [1, 1],
    ]
]


def print_grid(grid):
    print('\n\n+       +')
    for row in reversed(grid):
        print('|' + ''.join(['#' if c else '.' for c in row]) + '|')
    print('+-------+')


def move_rock(grid, rock, bottom_left, direction):
    height = len(rock)
    width = len(rock[0])
    cX, cY = bottom_left
    if direction == '<':
        nX, nY = cX - 1, cY
    elif direction == '>':
        nX, nY = cX + 1, cY
    else:  # Go Down
        nX, nY = cX, cY - 1

    # Is there a colision?
    for y in range(height):
        for x in range(width):
            # Check if there's a collision with the wall boundaries
            if not (0 <= nX + x < 7):
                return False, (cX, cY)
            if nY + y < 0:
                return False, (cX, cY)

            # Grid cols are in weird order
            if rock[height - y - 1][x] == 1 and grid[nY + y][nX + x] == 1:
                return False, (cX, cY)

    return True, (nX, nY)


def part_1(count=2022):
    instr = get_strings_by_lines('17.txt')[0]
    log(len(instr))
    log(instr[-1])

    max_height = 0
    grid = [[0 for _ in range(7)]]  # The ground is the initial grid

    block_len = len(blocks)
    wind_len = len(instr)
    wind_idx = 0
    print_grid(grid)
    for idx in range(count):
        rock = blocks[idx % block_len]
        rock_height = len(rock)  # Vertical dimensions of the rock
        rock_width = len(rock[0])  # Horizontal dimensions of the rock

        # Add empty rows to the top of the grid until the length of the grid has
        # Enough empty cushion for the whole shape to fit
        while len(grid) < max_height + 8:
            grid += [[0 for _ in range(7)]]

        bottom_left = (2, max_height + 3)  # X, Y coordinates of the shape

        # Add the rock
        while True:
            # Move with the wind
            log(f"Starting at {bottom_left}")
            log(f"Trying to move {instr[wind_idx]} ...")
            moved_wind, bottom_left = move_rock(
                grid, rock, bottom_left, instr[wind_idx])
            if (moved_wind):
                log(f"\tMoved with the wind!")
            else:
                log("\tNothing hapened")
            wind_idx = (wind_idx + 1) % wind_len  # Update the wind index

            #   Move Down
            moved_down, bottom_left = move_rock(grid, rock, bottom_left, 'v')
            if not moved_down:
                log(f"Landed at {bottom_left}!")

                cX, cY = bottom_left
                # Add the rock to the grid where it belongs
                for y in range(rock_height):
                    for x in range(rock_width):
                        # Grid cols are in weird order
                        if rock[rock_height - y - 1][x] == 1:
                            grid[cY + y][cX + x] = 1

                # Update Max Height!
                if (bottom_left[1] + rock_height) > max_height:
                    max_height = bottom_left[1] + rock_height
                break
            else:
                log(f"Moved down!")

        # Broke out of the while loop - rock has landed
        log(f"Done with iteration {idx} (max height: {max_height})")
        # print_grid(grid)

    return max_height


PART_2_COUNT = 1000000000000


def part_2():
    return part_1(PART_2_COUNT)
