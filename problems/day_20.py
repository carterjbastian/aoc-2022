from lib.helpers import log, get_ints_by_lines
from lib.config import DEBUG_MODE


# Class of a Doubly Linked List Node (DLL Node)
class Node:
    def __init__(self, val):
        self.val = val

        self.next = None
        self.prev = None

        self.visited = False

    def __repr__(self):
        return str(self.prev.val) + ' -> ' + str(self.val) + ' -> ' + str(self.next.val)


# Function to mov a Node backward or forward x spots in the list
def move_node(node, x):
    if x == 0:
        return node.next

    # Connect the two surrounding nodes and node out
    prev, next = node.prev, node.next
    prev.next = next
    next.prev = prev

    if x > 0:
        # Current node moves forward to where we want to insert
        cur = node
        for _ in range(x):
            cur = cur.next

        # Cur now has the node we want to be after
        node.prev = cur
        node.next = cur.next

        cur.next.prev = node
        cur.next = node
    else:
        # Current node moves back to where we want to insert
        cur = node
        for _ in range((-x)):
            cur = cur.prev

        # Cur now has the node we want to be before
        node.prev = cur.prev
        node.next = cur

        cur.prev.next = node
        cur.prev = node

    return next


# Print the DLL
def print_dll(start, count):
    if DEBUG_MODE:
        print('[', end='')
        node = start
        for _ in range(count):
            print(node.val, end=', ')
            node = node.next

        print(']')


def part_1():
    ints = get_ints_by_lines('20.txt')

    # Make a DLL for each
    count = len(ints)
    log(count)

    first = Node(ints[0])
    last = first
    for val in ints[1:]:
        cur = Node(val)
        cur.prev = last
        last.next = cur

        last = cur

    # Connect the first and last nodes
    first.prev = last
    last.next = first

    print_dll(first, count)

    # Loop through a few times
    cur = first
    for _ in range(count):
        # Loop forward until we find one that hasn't been visited
        while cur.visited:
            cur = cur.next

        # Move the current node to the place it should be
        cur.visited = True
        # Count since it'd just go around otherwise
        cur = move_node(cur, cur.val % (count - 1) if cur.val >
                        0 else -(abs(cur.val) % (count - 1)))

        print_dll(cur, count)

    # Find 0
    log("Done with setting up")
    while cur.val != 0:
        cur = cur.next

    # Count forward 3000 times
    total = 0
    for idx in range(3000 + 1):
        if idx % 1000 == 0 and idx > 0:
            print(cur.val)
            total += cur.val

        cur = cur.next
    return total


def part_2():
    ints = [i * 811589153 for i in get_ints_by_lines('20.txt')]

    # Make a DLL for each
    count = len(ints)
    log(count)

    first = Node(ints[0])
    last = first
    for val in ints[1:]:
        cur = Node(val)
        cur.prev = last
        last.next = cur

        last = cur

    # Connect the first and last nodes
    first.prev = last
    last.next = first

    print_dll(first, count)

    # Mix 10 times
    cur = first

    node_list = []
    for _ in range(count):
        node_list += [cur]
        cur = cur.next

    for idx in range(10):
        log('Mixing ' + str(idx))
        for cur in node_list:
            # Move the current node to the place it should be
            cur.visited = True
            cur = move_node(cur, cur.val % (count - 1) if cur.val >
                            0 else -(abs(cur.val) % (count - 1)))

        print_dll(cur, count)

        # Reset all the visited values to False
        log("Before Resetting")
        log(cur)
        for _ in range(count):
            cur.visited = False
            cur = cur.next

        log("After Resetting")
        log(cur)
    # Find 0
    log("Done with setting up")
    while cur.val != 0:
        cur = cur.next

    # Count forward 3000 times
    total = 0
    for idx in range(3000 + 1):
        if idx % 1000 == 0 and idx > 0:
            print(cur.val)
            total += cur.val

        cur = cur.next

    return total
