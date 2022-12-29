import re
from lib.helpers import log, get_strings_by_lines
from lib.config import TEST_MODE

TEST_INPUT = '10R5L5R10L4R5L5L'
REAL_INPUT = '42L16R50R47L35L8L9L30L12R41L5R42L31R30L36R37L8R16R12L43L27R15R18L18L38R39R2L22R17L34R12L32L50R37L9R22L36R4L35R29L26R15L34L4L32R1R12L30R38R30L40L20L47L46R29L21R48L23L34R41L18R36R47R16L31R8L20L24L29R26L2R23L46L48L33R46R47L15R39L38L15L3R36L39L40L5L30R27R42L12L3R42L1R28R42L50R8R15R39L29L38R10L37R49L25L45R3L44R29L16R30L48L29L22L42R44L36R12R38R44R29L18L37R39L47L4L49L18R32R34L45L15R11R28L21R35L20L40L8L2R16L21L30R9R21L44L33R40L50R15L38R49L40L13L3L5L16L23L26L27L12R41L40R33L15L28L43R16R4R9R7L16R48R4R46L5R29R7R35R17L30L32R37L19L49R45R4L43R28R1L23L33L11R31R30R30R47R25R9R16L43L40L8L9L12R47R32R33R36L8L2L26R29R5R32R11R45R14L31R30L10L16R27R26R10R2R50R37L9L12L13R38R27R21L30L21R37R5L44L1L33R43R5R31R30R11L38L9L35L21R37R7R50L26R18L32R21R45R22R29L40R36L27R15R27R38R27R12R14R23L6L33L4R4L38R17L38R44L33L38L43R14L11L47L18R2R40R26L30R10L5L28L14L23L46L29L1L35L24R33L14R33R29L37R6L49L33R6L37R4L7L33L29R12L28R24L1R20R36L8L34L17L20R41R1R34R3L38R20R35R21L7R34L44L9R39L30R22L36L45L4R49R39R21L22L29R5L5L40L17L40R40R5L45R37R42R42R15L38L17L4R30R5R16R42R12L22R24R12L45R49R49L37R10R16L27L9R19R13R42R46L9L37R47L11L23R19R25L29R28L36L13R24R25L20R12L44L11L42R47L8L20L35R10L49R22L33L25R46L29L19R40R15L24L33R29R48L39R30L25L8L26L26L10L12R50L10L32R6R19R15L48L40L40L33R19L20L9R44R15R22R18L19R26R7L43L38L39L37R11L13R34R36R6R42R8R32R36R17R28R48L20L50R38R43L18L31L49R15L41R31L6R38L33L4L38R49R6L11L16L31L19R18R1R4R16R46L13R23L46L45L11L40L18L21L38L33R22R16L47L10L48R32R16R5L2R21R22R33R32L18L41L40R46R2L29R24L24R14R42L44L24R32R5R16R5L29R40R32L30L19L47R39L48R35R26L47R40L9R47R43R50L1R47R10L43R39L37L24L7R33L38R37R10R39L13L3R4R29R25R10R43R35L40L41R36R31L11L18R14R41R23R32L40R14L45L22L42L38R43R11L43L16R48L1L6R2R2L5L18R21L42R38L10R48L4R32R38L33R16R33L23L29L43R19R41R15L11L1L43R33R49L43R22R20L18L30R18L43R41R6L40L50R6R48R16L27L4L32R27R4R10R13R41L47R30R44L19L28R38R35R5L26R46R10R19L38R40R9R50R43R7R36L29L20R5L16L37L24L46L6L49L2L40L39L18L9R46L42R48L8L47R10R9R48L26R40L23L42L25R30R17R33R4R40R46R23L15R2L47R40L3R18L14L29R9R19L2R12R19R20R2R27L17R5R22R30R10R1L42R48L26R15R18R43R44R23L6L24R35L45L3L8R43L48R50L8R8L19L12R45R29L5L13R20L15R3L33L39L38L30R2R37R31R48R18L13L36R47L37L16L29R38R27R27L27L21R16R50R12R9R36L6L4R48R39L41R5L11L47R22L20L12L26L43R19L34R1R19R44L48R8R32L36R47R8L22L18L48L32R9L42R14R32L35L36R48R42R36L4R42R44L19R1R35L17R48R23R49L27L13L5R5L14L24R35R6L20R2L50L31R16L28R39L36R44R6L1R28L38L22R13R12R46L34L39L44R49R48R8R26L9R17R6L38L26L50L31R18L42L46R15L26R43L8L41L30R33R33R46L37R44L35R1L1R1L15L43L16L33L22L15L32L43R43R30R49R2L26R46R18L2R39R1R28L2L42R42L2L21L41R41L1L3R37R6R21L29R8L26R46L36R22L14L23L12L12L9L42R17R41R26L3L27L25L11L6L32L1R41L11R40R47R35L45R15R38L1L1R28R12R17L43L14R17L17R4L42L46R43L46R41R32L12R22R4L25L23R14L5L43R22L40R4R50R36R24L26R27R15L34R44R1R43R43R7R7L10L4R27L12R29R5L48L26L20R26L9L13L32L48R34L29R33R22L35R42R41R19R37L16R24L33R5L10R14R28L5L46R42L11L16L44R5R27L21L38R36R33R45R10L40R35L37R3L37L37L6R27R41L45L21R1L2L5R15L33R26L14L10L29R32L24L7L9L3R49L32R37R23L10R42L33L16L18L13L34R23R17R46L45L29L18L6R34R29L34L10L27L27L47R27L37R28L10R14R48L19L11R24R24L38L6R23R13R19L11L34L19L23R12L5R26L22R36L16R47L23R24R29R40L43R15R9L2L45L35R32R27L41L45R17L17R17L9L29L22R26L19R47R4L2L23L37R40L3L28R29R9L24L14R50R43L18L19R15L27L46L47L31L50L44L29R14R8R17R12R8R16R35R11R41R11L2L43L35L15L14R10R44R25R45L42L29L27L14R10R30R26L5L23R46R31L43L44R29R22L24L34L14R36R15L16R20R31R4L14R45L24L22R50R10L10L36L35R11R12L29R33R4R18R16R34L44R33R10L5L23R48R19R18L25L23L36R27L1R28R49R43L24L22L40R5L26R22L8R49L48R18R21L43L43L43R26R21R46L21R8L48L5R24R16R27L16R50L41R13R9L7R24R35R23L7R14L16R39L7R22R34R36R3R48L22R22R29L22L27L8L18L30L30L42R42R47R12R49R8L5R5L47L45R7R36L31L39R23L9R18L5L38L49R4R6R22R17R4L34R40R48R23L37L6L43L37R10L30R39L22L11L30L30L24L31L30L34L26L17R39R23L31L24L30R1L23L9R21R40R27R42L24L48R34L15L17R39R11R30R27L28L38L14R26L20L41R20L48L33R41R26L1L34L43L20L12L38L32R8L17L23R46L24R13R29R1R13L33R21R8R36R35R7R24L38L39L27L49L4R28R31L49L45L3R6R17L43R21L8L10L46R17R43R45L12R25R18L41L28L46L38L4R46R22R25L26L11R48L1L10R39R41R13R48L10R40R45R35L45R24R30L29L14L12R9R12L33R13L21R23L22L32L6R34L27L42L31R8L24L23L34L27L37R27R4L20R2L22R17R29L1L25L30R11R6L44R8L14R11L32L28L34L4R17L29R24L20R46R12R14R43R46R11L35R23L12R43L46L35R48L36L25R41R46L33R43R41L32L16L1L25R17R42R44L34R6R37L49R29L21L47L45R39L46L26R2L49L49R7R36R18R39L49L45R45L10R27R13R3L10L17L14R34R22R17L49L34L24R39R37R26L28L24R2R30R40R17R46L27R11L9L20L18L41L5L31R3R45R28R6L32L34L46L4L13L29R50R15R14R26L36R48R12L13R10R29R31R47L49R9L18R50L1L2L46R33L14R21R33L44L18R9L34L39L29L17L49R6R1R41R7R12R45R13R41L24L50L35R21R5R25R2L42L24R42L31R48L4L34R48L15R43L40R30L7R24R47L42L7R44L12L30L24R5R39R26L17L46L14R15L23R4L48L8R37L27L29L24R11L37L18R38L35R8R7R36R22L35R8R18L49R41R46R24R11L47L50L15L38L38L11R39R44L36L2L40L47R39R42R11R35L9R13R36L46R36R22R42R19L20L31R7L21R11L37L6R28R3L26R12L14L47R22L8L24R47R42L29L9R36L46R41L12L2R40L32R34L15R13R21R22L44R48L26L2L47R49R6R33R28R12L39R43L25R33R10R9L14L50R5L10R9L10R46R18L25L17R9R5R4L27R25L2R14L7L48L17L50R3L28R36R47L38L13R49L9R43R5L22L22L50L7R4R5R39R21L24R6L8L42L28L18L41L13R21R20R3L6L7L20R10R33R10R49L18R2L35L16R24R4L9R17R39L44R41L16L17R18R10R35R31R25L43L29R32R4R21L38R5L16L15R11L26R38L14R41R14R4R47R1R5R31R38L7L23L25L8L48R10R46L50L27L24L43R32L28L13R26R40L41L10L14R38R45L10L26L35L17L12R31R48L25R5R26L20R38R28R46L39R36R37L44R4R48L30R24R3L4R23R41R29R29L1L47L36L41R47R20L31R35L10L12R13L37L38R29L31L23L12L47L26L31L49L3R23R48R41L38L31L27L44R26R38R17L18R38R4R9R39L18R3L12R20L1L23L16R30R16L6R44L45R26R2R50L21R15R21R14R4R18R21L1R14L18L13L40R47R3L11R50L50L42L10R32L30L8R35R33L44R50R43R2L1R14L31L32R11R22L5L27L41L43L27L29R17R21R7R12R14R38L45R21L21R48L16R6R30R28R6R16L19L45L17R45R12L20L18L13L23L35R17L39L33L29R32R35L25L28R50L7R46L14L28L20R43R47R32R9R50R47L33R31R25L'

RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)

CUBE_DIM = 5 if TEST_MODE else 50
CUBE_LOCATION = {
    1: (CUBE_DIM * 2, 0),
    2: (CUBE_DIM, 0),
    3: (CUBE_DIM, CUBE_DIM),
    4: (CUBE_DIM, CUBE_DIM * 2),
    5: (0, CUBE_DIM * 2),
    6: (0, CUBE_DIM * 3),
}
CUBE_WRAP_FNS = {
    1: {
        # UP -> 6 going UP
        UP: lambda x, y: (
            (x - CUBE_LOCATION[1][0],
                CUBE_LOCATION[6][1] + CUBE_DIM - 1),
            UP
        ),
        # RIGHT -> 4 going LEFT
        RIGHT: lambda x, y: (
            (CUBE_LOCATION[4][0] + CUBE_DIM - 1,
                CUBE_LOCATION[4][1] + CUBE_DIM - 1 - y),
            LEFT
        ),
        # DOWN -> 3 going LEFT
        DOWN: lambda x, y: (
            (CUBE_LOCATION[3][0] + CUBE_DIM - 1,
                # PROBLEM
                CUBE_LOCATION[3][1] + (x - CUBE_LOCATION[1][0])),
            LEFT
        ),
    },
    2: {
        # UP -> 6 going RIGHT
        UP: lambda x, y: (
            (0,
                CUBE_LOCATION[6][1] + (x - CUBE_LOCATION[2][0])),
            RIGHT
        ),
        # LEFT -> 5 going RIGHT
        LEFT: lambda x, y: (
            (0,
                CUBE_LOCATION[5][1] + CUBE_DIM - 1 - y),
            RIGHT
        ),
    },
    3: {
        # LEFT -> 5 going DOWN
        LEFT: lambda x, y: (
            (y - CUBE_LOCATION[3][1],
                CUBE_LOCATION[5][1]),
            DOWN
        ),
        # RIGHT -> 1 going UP
        # PROBLEM
        RIGHT: lambda x, y: (
            (CUBE_LOCATION[1][0] + (y - CUBE_LOCATION[3][1]),
                CUBE_LOCATION[1][1] + CUBE_DIM - 1),
            UP
        ),
    },
    4: {
        # RIGHT -> 1 going LEFT
        RIGHT: lambda x, y: (
            (CUBE_LOCATION[1][0] + CUBE_DIM - 1,
                CUBE_LOCATION[4][1] + CUBE_DIM - 1 - y),
            LEFT
        ),
        # DOWN -> 6 going LEFT
        DOWN: lambda x, y: (
            (CUBE_LOCATION[6][0] + CUBE_DIM - 1,
                CUBE_LOCATION[6][1] + CUBE_DIM - (CUBE_LOCATION[4][0] + CUBE_DIM - x)),
            LEFT
        ),
    },
    5: {
        # UP -> 3 going RIGHT
        UP: lambda x, y: (
            (CUBE_LOCATION[3][0],
                CUBE_LOCATION[3][1] + x),
            RIGHT
        ),
        # LEFT -> 2 going RIGHT
        LEFT: lambda x, y: (
            (CUBE_LOCATION[2][0],
                CUBE_LOCATION[5][1] + CUBE_DIM - 1 - y),
            RIGHT
        ),
    },
    6: {
        # LEFT -> 2 going DOWN
        LEFT: lambda x, y: (
            (CUBE_LOCATION[2][0] + (y - CUBE_LOCATION[6][1]),
                0),
            DOWN
        ),
        # DOWN -> 1 going DOWN
        DOWN: lambda x, y: (
            (CUBE_LOCATION[1][0] + x,
                0),
            DOWN
        ),
        # RIGHT -> 4 going UP
        RIGHT: lambda x, y: (
            (CUBE_LOCATION[4][0] + (y - CUBE_LOCATION[6][1]),
                CUBE_LOCATION[4][1] + CUBE_DIM - 1),
            UP
        ),
    },
}


def parse_inputs():
    INSTR_PATTER = re.compile(r"(\d+)([RL])")
    input = TEST_INPUT if TEST_MODE else REAL_INPUT

    moves = [(int(m[0]), m[1]) for m in INSTR_PATTER.findall(input)]

    grid = get_strings_by_lines('22.txt')

    max_len = max(len(r) for r in grid)
    # Make the grid evenly sized
    for i in range(len(grid)):
        while len(grid[i]) < max_len:
            grid[i] += " "
    min_len = min(len(r) for r in grid)
    col_grid = []

    for col in range(max_len):
        col_grid += [""]
        for row in range(len(grid)):
            if col < len(grid[row]):
                col_grid[col] += grid[row][col]
            else:
                col_grid[col] += " "

    max_col_len = max(len(c) for c in col_grid)
    min_col_len = min(len(c) for c in col_grid)

    log(f"Max len: {max_len}")
    log(f"Min len: {min_len}")
    log(f"Max col len: {max_col_len}")
    log(f"Min col len: {min_col_len}")

    return moves, grid, col_grid


CLOCKWISE_TURN = {
    (0, -1): (1, 0),  # Moving up -> moving right
    (1, 0): (0, 1),  # Moving right -> moving down
    (0, 1): (-1, 0),  # Moving down -> moving left
    (-1, 0): (0, -1),  # Moving left -> moving up
}

COUNTERCLOCKWISE_TURN = {
    (0, -1): (-1, 0),  # Moving up -> moving left
    (-1, 0): (0, 1),  # Moving left -> moving down
    (0, 1): (1, 0),  # Moving down -> moving right
    (1, 0): (0, -1),  # Moving right -> moving up
}

INF = 1000000000000  # yikes


def is_oob(nX, nY, grid, max_x, max_y):
    return (
        nX < 0 or nY < 0 or nX >= max_x or nY >= max_y
        or grid[nY][nX] == ' '
    )


def part_two_wrap(cX, cY, dX, dY, grid, max_x, max_y):
    nX, nY = cX + dX, cY + dY

    if not is_oob(nX, nY, grid, max_x, max_y):
        return nX, nY, dX, dY

    # Which cube are we in?
    found_face = 0
    for face, (x, y) in CUBE_LOCATION.items():
        if x <= cX < x + CUBE_DIM and y <= cY < y + CUBE_DIM:
            found_face = face
            break

    #log(f"Out of bounds in cube {found_face} moving {dX}, {dY}")
    newPos, newDir = CUBE_WRAP_FNS[found_face][(dX, dY)](cX, cY)

    # Figure out which cube
    return newPos[0], newPos[1], newDir[0], newDir[1]


def part_one_wrap(nX, nY, dX, dY, grid, col_grid, max_row_len, max_col_len):
    # Wrap Logic!
    # We are out of bounds horizontally if nX < 0 or nX >= len(grid[nY])
    if nX < 0:
        # Wrap around to the right
        log("\t wrapping around to the right")
        rightDot = grid[nY].rfind('.')
        rightWall = grid[nY].rfind('#')
        nX = max(rightDot if rightDot >= 0 else -1 * INF,
                 rightWall if rightWall >= 0 else -1 * INF)
    elif nY < 0:
        # Wrap around to the bottom
        log("\t wrapping around to the bottom")
        nY = max(col_grid[nX].rfind('.'), col_grid[nX].rfind('#'))
    elif nY >= max_col_len:
        # Wrap around to the top
        log("\t wrapping around to the top")
        topDot = col_grid[nX].find('.')
        topWall = col_grid[nX].find('#')
        nY = min(topDot if topDot >= 0 else INF,
                 topWall if topWall >= 0 else INF)
    elif nX >= max_row_len:
        # Wrap around to the left
        log("\t wrapping around to the left")
        leftDot = grid[nY].find('.')
        leftWall = grid[nY].find('#')
        nX = min(leftDot if leftDot >= 0 else INF,
                 leftWall if leftWall >= 0 else INF)
    elif grid[nY][nX] == ' ':
        if dX == -1:
            # Wrap around to the right
            log("\t wrapping around to the right 2")
            rightDot = grid[nY].rfind('.')
            rightWall = grid[nY].rfind('#')
            nX = max(rightDot if rightDot >= 0 else -1 * INF,
                     rightWall if rightWall >= 0 else -1 * INF)
        elif dX == 1:
            # Wrap around to left
            log("\t wrapping around to the left 2")
            leftDot = grid[nY].find('.')
            leftWall = grid[nY].find('#')
            nX = min(leftDot if leftDot >= 0 else INF,
                     leftWall if leftWall >= 0 else INF)
        elif dY == -1:
            # Wrap around to the bottom
            log("\t wrapping around to the bottom 2")
            nY = max(col_grid[nX].rfind('.'), col_grid[nX].rfind('#'))
        elif dY == 1:
            # Wrap around to the top
            log("\t wrapping around to the top 2")
            topDot = col_grid[nX].find('.')
            topWall = col_grid[nX].find('#')
            nY = min(topDot if topDot >= 0 else INF,
                     topWall if topWall >= 0 else INF)

    return nX, nY


def move_once(grid, col_grid, pos, dir, move, cubed=False):
    global INF
    cX, cY = pos
    dX, dY = dir
    moveCount, turnDir = move

    max_row_len = max(len(r) for r in grid)
    max_col_len = max(len(c) for c in col_grid)

    for _ in range(moveCount):

        if cubed:
            dX, dY = dir
            nX, nY, ndX, ndY = part_two_wrap(
                cX, cY, dX, dY, grid, max_row_len, max_col_len)
            # log(f"Moving from {cX}, {cY} to {nX}, {nY}")
            if grid[nY][nX] == '#':
                log(f"Hit a wall! Falling back to {cX}, {cY}")
                nX, nY = cX, cY
                break
            else:
                dir = (ndX, ndY)
        else:
            nX, nY = cX + dX, cY + dY
            nX, nY = part_one_wrap(nX, nY, dX, dY, grid,
                                   col_grid, max_row_len, max_col_len)

            # If we've hit a wall, fall back!
            if grid[nY][nX] == '#':
                nX, nY = cX, cY
                break

        cX, cY = nX, nY

    # Not matter what, turn
    #log(f"Current Dir: {dir}")
    new_dir = CLOCKWISE_TURN[dir] if turnDir == 'R' else COUNTERCLOCKWISE_TURN[dir]

    return (cX, cY), new_dir


def part_1():
    moves, grid, col_grid = parse_inputs()

    log("\n\nRows:")
    for r in grid:
        log(r)

    log("\n\nColumns:")
    for c in col_grid:
        log(c)

    # Init to first '.' in first row
    pos = grid[0].index('.'), 0
    dir = (1, 0)  # Start moving right

    for move in moves:
        log(f"Starting at {pos} moving {dir} for {move}")
        pos, dir = move_once(grid, col_grid, pos, dir, move)
    log(f"Ended at {pos} moving {dir}")

    facing_score = {
        (1, 0): 0,  # Right
        (0, 1): 1,  # Down
        (-1, 0): 2,  # Left
        (0, -1): 3,  # Up
    }
    facing = facing_score[CLOCKWISE_TURN[dir]]
    return ((pos[1] + 1) * 1000) + ((pos[0] + 1) * 4) + facing


def unit_test():
    moves, grid, col_grid = parse_inputs()
    # FACE 1:
    # UP: (11, 0) + (0, -1) => (1, 19) + (0, -1)
    nx, ny, dx, dy = part_two_wrap(
        11, 0, 0, -1, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 1 Going Up: (11, 0) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(1, 19) going (0, -1)")

    # RIGHT: (14, 1) + (1, 0) => (9, 13) + (-1, 0)
    nx, ny, dx, dy = part_two_wrap(
        14, 1, 1, 0, grid, len(grid[0]), len(col_grid[0]))
    log(f"Face 1 Going Right: (14, 1) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(9, 13) going (-1, 0))")

    # DOWN: (11,4) + (0, 1) => (9, 6) + (-1, 0)
    nx, ny, dx, dy = part_two_wrap(
        11, 4, 0, 1, grid, len(grid[0]), len(col_grid[0]))
    log(f"Face 1 Going Down: (11, 4) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(9, 6) going (-1, 0))")

    # FACE 2:
    # UP: (6, 0) + (0, -1) =? (0, 16) + (1, 0)
    nx, ny, dx, dy = part_two_wrap(
        6, 0, 0, -1, grid, len(grid[0]), len(col_grid[0]))
    log(f"Face 2 Going Up: (6, 0) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(0, 16) going (1, 0)")

    # LEFT: (5, 1) + (-1, 0) => (0, 13) + (1, 0)
    nx, ny, dx, dy = part_two_wrap(
        5, 1, -1, 0, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 2 Going Left: (5, 1) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(0, 13) going (1, 0)")

    # FACE 3:
    # LEFT: (5, 6) + (-1, 0) => (1, 10) + (0, 1)
    nx, ny, dx, dy = part_two_wrap(
        5, 6, -1, 0, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 3 Going Left: (5, 6) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(1, 10) going (0, 1)")

    # RIGHT: (9, 6) + (1, 0) => (11, 4) + (0, -1)
    nx, ny, dx, dy = part_two_wrap(
        9, 6, 1, 0, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 3 Going right: (9, 6) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(11, 4) going (0, -1)")

    # FACE 4:
    # RIGHT: (9, 11) + (1, 0) => (14 , 3) + (-1, 0)
    nx, ny, dx, dy = part_two_wrap(
        9, 11, 1, 0, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 4 Going right: (9, 11) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(14, 3) going (-1, 0)")

    # DOWN: (6, 14) + (0, 1) => (4, 16) + (-1, 0)
    nx, ny, dx, dy = part_two_wrap(
        6, 14, 0, 1, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 4 Going DOWN: (6, 14) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(4, 16) going (-1, 0)")

    # FACE 5:
    # UP: (1, 10) + (0, -1) => (5, 6) + (1, 0)
    nx, ny, dx, dy = part_two_wrap(
        1, 10, 0, -1, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 5 Going UP: (1, 10) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(5, 6) going (1, 0)")

    # LEFT: (0, 11) + (-1, 0) => (5, 3) + (1, 0)
    nx, ny, dx, dy = part_two_wrap(
        0, 11, -1, 0, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 5 Going LEFT: (0, 11) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(5, 3) going (1, 0)")

    # FACE 6:
    # LEFT: (0, 16) + (-1, 0) => (6, 0) + (0, 1)
    nx, ny, dx, dy = part_two_wrap(
        0, 16, -1, 0, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 6 Going LEFT: (0, 11) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(6, 0) going (0, 1)")

    # RIGHT: (4, 18) + (1, 0) + => (8, 14) + (0, -1)
    nx, ny, dx, dy = part_two_wrap(
        4, 18, 1, 0, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 6 Going RIGHT: (4, 18) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(8, 14) going (0, -1)")

    # DOWN: (1, 19) + (0, 1) => (11, 0) + (0, 1)
    nx, ny, dx, dy = part_two_wrap(
        1, 19, 0, 1, grid, len(grid[0]), len(col_grid[0]))
    log(
        f"Face 6 Going DOWN: (1, 19) -> \n\t({nx}, {ny}) going ({dx}, {dy}), expecting... \n\t(11, 0) going (0, 1)")


def part_2():
    moves, grid, col_grid = parse_inputs()
    # Testing
    if TEST_MODE:
        unit_test()
        return 100

    log("\n\nRows:")
    for r in grid:
        log(r)

    log("\n\nColumns:")
    for c in col_grid:
        log(c)

    # Init to first '.' in first row
    pos = grid[0].index('.'), 0
    dir = (1, 0)  # Start moving right

    for move in moves:
        log(f"Starting at {pos} moving {dir} for {move}")
        pos, dir = move_once(grid, col_grid, pos, dir, move, cubed=True)
    log(f"Ended at {pos} moving {dir}")

    facing_score = {
        (1, 0): 0,  # Right
        (0, 1): 1,  # Down
        (-1, 0): 2,  # Left
        (0, -1): 3,  # Up
    }
    facing = facing_score[CLOCKWISE_TURN[dir]]
    return ((pos[1] + 1) * 1000) + ((pos[0] + 1) * 4) + facing
