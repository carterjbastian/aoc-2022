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
    for row in reversed(grid[1:]):
        print('|' + ''.join(['#' if c else '.' for c in row]) + '|')
    print('+-------+')


def move_rock(rock, bottom_left, direction):
    # TODO: Implement this, retruning updated bottom_left + is_blocked
    pass


def part_1():
    instr = get_strings_by_lines('17.txt')[0]
    log(len(instr))
    log(instr[-1])

    max_height = 0
    grid = [[1 for _ in range(7)]]  # The ground is the initial grid

    iterations = 2022
    block_len = len(blocks)
    wind_len = len(instr)
    print_grid(grid)
    for idx in range(1):
        rock = blocks[idx % len(blocks)]
        rock_height = len(rock)  # Vertical dimensions of the rock
        rock_width = len(rock[0])  # Horizontal dimensions of the rock

        # Add empty rows to the top of the grid until the length of the grid is max_height + 4
        while len(grid) < max_height + 4:
            grid += [[0 for _ in range(7)]]

        print_grid(grid)
        bottom_left = (2, max_height + 4)  # X, Y coordinates of the shape

        while True:
            #   To add a shape, add 3 empty rows to the top of the grid
            #   Then add our next shape on top of that
            #   Move the shape left or right if possible
            #   Then shift it down 1 if possible. If not, break
            break
