from lib.helpers import log, get_strings_by_lines

# import sys;print(sys.version)
REGISTERS = {
    "X": 1,
}

add_in_2 = 0
add_next = 0
clock = 1
total = 0


def cycle(init_cmd, args):
    global total
    global clock
    global add_next
    global add_in_2
    global REGISTERS

    instrs = [init_cmd]
    while len(instrs):
        # Pop left
        cmd = instrs[0]
        instrs = instrs[1:]
        log(REGISTERS)

        REGISTERS["X"] += add_next

        # Part 1
        if clock in [20, 60, 100, 140, 180, 220]:
            log(f"Clock {clock}: Adding {clock} * {REGISTERS['X']}")
            total += (clock * REGISTERS["X"])

        # Part 2
        position = (clock - 1) % 40
        if REGISTERS["X"] - 1 <= position and REGISTERS["X"] + 1 >= position:
            print("# ", end="")
        else:
            print(". ", end="")
        if position == 39:
            print("")  # newline

        next_up = 0
        if cmd == "noop":
            log("")
        elif cmd == "addx":
            val = int(args[0])
            next_up = val
            # Add a noop to finish instruction
            instrs += ["noop"]
        else:
            log("Other")

        # Move upcoming additions
        add_next = add_in_2
        add_in_2 = next_up
        clock += 1


def part_1():
    rows = get_strings_by_lines('10.txt')

    for instr in rows:
        log(f"Cycle {clock}: {instr}")

        vals = instr.split(' ')
        cycle(vals[0], vals[-1:])

    return total
