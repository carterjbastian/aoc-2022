from lib.helpers import log, get_strings_by_lines

def move(direction, knots):
    if direction == "R":
        log("Going Right")

        # Move the Head
        knots[0] = (knots[0][0] + 1, knots[0][1])

        # Move the Tails
        for idx in range(1, len(knots)):
            H = knots[idx - 1]
            T = knots[idx]
            # If we're now more than 1 x-unit > Tail, Pull it to our Y level
            if H[0] - T[0] > 1:
                knots[idx] = (H[0] - 1, H[1]) # Pull to our Y Level

    elif direction == "L":
        log("Going Left")
        # Move the Head
        knots[0] = (knots[0][0] + -1, knots[0][1])

        # Move the Tails
        for idx in range(1, len(knots)):
            H = knots[idx - 1]
            T = knots[idx]
            # If we're now more than 1 x-unit < Tail, Pull it to our Y level
            if T[0] - H[0] > 1:
                knots[idx] = (H[0] + 1, H[1]) # Pull to our Y Level

    elif direction == "U":
        log("Going Up")
        # Move the Head
        knots[0] = (knots[0][0], knots[0][1] + 1)

        # Move the Tails
        for idx in range(1, len(knots)):
            H = knots[idx - 1]
            T = knots[idx]

            # If we're now more than 1 y-unit > Tail, Pull it to our X level
            if H[1] - T[1] > 1:
                knots[idx] = (H[0], H[1] - 1) # Pull to our X Level
    else:
        log("Going Down")
        # Move the Head
        knots[0] = (knots[0][0], knots[0][1] - 1)

        # Move the Tails
        for idx in range(1, len(knots)):
            H = knots[idx - 1]
            T = knots[idx]
            # If we're now more than 1 y-unit < Tail, Pull it to our X level
            if T[1] - H[1] > 1:
                knots[idx] = (H[0], H[1] + 1) # Pull to our X Level

    return knots


def part_1():
    rows = get_strings_by_lines('9.txt')

    H = (0, 0)
    T = (0, 0)
    visited = set([(0, 0)])
    for row in rows:
        d, count = row.split(' ')
        for _ in range(int(count)):
            [H, T] = move(d, [H, T])
            # Mark square as visited
            visited.add(T)

    log(visited)
    
    return len(visited)
