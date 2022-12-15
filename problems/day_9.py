from lib.helpers import log, get_strings_by_lines


def move(direction, knots):
    # Move the Head
    if direction == "R":
        log("Going Right")
        knots[0] = (knots[0][0] + 1, knots[0][1])

    elif direction == "L":
        log("Going Left")
        knots[0] = (knots[0][0] - 1, knots[0][1])

    elif direction == "U":
        log("Going Up")
        knots[0] = (knots[0][0], knots[0][1] + 1)
    else:
        log("Going Down")
        knots[0] = (knots[0][0], knots[0][1] - 1)

    # Move the Tails
    for idx in range(1, len(knots)):
        H = knots[idx - 1]
        T = knots[idx]

        # Initialize to where its at now
        X = T[0]
        Y = T[1]

        # If we're now more than 1 y-unit > Tail, Pull it to our X level
        if H[1] - T[1] > 1:
            Y = H[1] - 1
            if X < H[0]:
                X += 1
            elif X > H[0]:
                X -= 1
        # If we're now more than 1 y-unit < Tail, Pull it to our X level
        elif T[1] - H[1] > 1:
            Y = H[1] + 1
            if X < H[0]:
                X += 1
            elif X > H[0]:
                X -= 1
        # If we're now more than 1 x-unit > Tail, Pull it to our Y level
        elif H[0] - T[0] > 1:
            X = H[0] - 1
            if Y < H[1]:
                Y += 1
            elif Y > H[1]:
                Y -= 1
        # If we're now more than 1 x-unit < Tail, Pull it to our Y level
        elif T[0] - H[0] > 1:
            X = H[0] + 1
            if Y < H[1]:
                Y += 1
            elif Y > H[1]:
                Y -= 1

        knots[idx] = (X, Y)

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
            log(H)
            log(T)

    return len(visited)


def part_2():
    rows = get_strings_by_lines('9.txt')

    rope = [(0, 0)] * 10
    visited = set([(0, 0)])
    for row in rows:
        d, count = row.split(' ')
        for _ in range(int(count)):
            rope = move(d, rope)
            # Mark square as visited
            visited.add(rope[-1])

    return len(visited)
