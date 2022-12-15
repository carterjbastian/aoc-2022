from lib.helpers import log, get_input

monkeys = []


class Monkey():
    def __init__(self, initList, testDivBy, operation, throwTrue, throwFalse, ):
        self.queue = initList
        self.testDivBy = testDivBy
        self.operation = operation
        self.throwTrue = throwTrue
        self.throwFalse = throwFalse

        self.count = 0

    def inspection(self, inspect=True):
        global monkeys
        for item in self.queue:
            self.count += 1  # Item Counter

            # Operation and division
            item = self.operation(item)
            if inspect:
                item //= 3
            else:
                item = item % common_multiple

            # Throw it
            if item % self.testDivBy == 0:
                monkeys[self.throwTrue].queue += [item]
            else:
                monkeys[self.throwFalse].queue += [item]

        # Queue is now empty
        self.queue = []

    def __repr__(self):
        return f"{self.queue}"


def create_lambda(funcStr):
    # I hate python scopes
    operand = funcStr.split(" ")[1]
    def func(x): return x
    if "*" == funcStr[0]:
        return lambda x: x * (x if operand == "old" else int(operand))
    else:
        return lambda x: x + (x if operand == "old" else int(operand))


common_multiple = 1


def make_monkeys():
    global monkeys
    global common_multiple
    groups = get_input('11.txt').split("\n\n")

    # Make our monkey friends
    for group in groups:
        notes = group.split("\n")

        # Parse Queue
        queueStr = notes[1].split("items: ")[1]
        queue = [int(x) for x in queueStr.split(", ")]

        # Parse update
        funcStr = notes[2].split("new = old ")[1]
        func = create_lambda(funcStr)

        # Parse test & results who to throw what to
        testDivBy = int(notes[3].split("divisible by ")[1])
        common_multiple *= testDivBy
        throwTrue = int(notes[4].split("throw to monkey ")[1])
        throwFalse = int(notes[5].split("throw to monkey ")[1])

        # Make the monkey
        monkeys += [Monkey(queue, testDivBy, func, throwTrue, throwFalse)]


def part_1():
    global monkeys
    make_monkeys()

    for _ in range(20):
        for monkey in monkeys:
            monkey.inspection()

    counts = sorted([m.count for m in monkeys])
    return counts[-2] * counts[-1]


def part_2():
    global monkeys
    make_monkeys()
    log(common_multiple)

    for idx in range(10000):
        log(f"IDX: {idx}")
        for monkey in monkeys:
            monkey.inspection(False)
        log(monkeys)

    counts = sorted([m.count for m in monkeys])
    return counts[-2] * counts[-1]
