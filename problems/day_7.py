from collections import deque
from lib.helpers import log, get_strings_by_lines


class Tree(object):
    def __init__(self, name, fsize=0):
        self.name = name
        self.size = fsize

        self.children = {}
        self.parent = None

    def __repr__(self):
        indent = "  "
        s = '- ' + self.name + f" ({self.size})" + "\n"
        for child_name, child_object in self.children.items():
            s += indent + child_object.__repr__().replace("\n", "\n" + indent)
        return s

# Recursive DFS to compute sizes at each node


def get_size(node):
    if node.size == 0:
        if len(node.children) > 0:
            node.size = sum([get_size(child)
                            for child in node.children.values()])
        else:
            node.size = 0
    return node.size


def parse_tree():
    rules = get_strings_by_lines('7.txt')
    root = Tree('/')
    cur = root
    for rule in rules[1:]:
        # Commands to change Directory
        log(f"Rule: {rule}")
        if rule.startswith("$ "):
            pieces = rule[2:].split(" ")
            log(f"pieces: {pieces}")
            cmd = pieces[0]
            if cmd == "cd":
                arg = pieces[1]
                log(f"moving into {arg}")
                if arg == "/":
                    cur = root
                elif arg == "..":
                    cur = cur.parent
                else:
                    if arg not in cur.children:
                        cur.children[arg] = Tree(arg)
                        cur.children[arg].parent = cur
                    cur = cur.children[arg]
            elif cmd == "ls":
                # We can ignore the ls command
                log("Printing")
        elif rule.startswith("dir"):
            dirName = rule.split(" ")[1]
            # We may ls a dict multiple times
            if dirName not in cur.children:
                cur.children[dirName] = Tree(dirName)
                cur.children[dirName].parent = cur
        else:
            size, fname = rule.split(" ")
            # Add a leaf!
            cur.children[fname] = Tree(fname, int(size))
            cur.children[fname].parent = cur
            cur.children[fname].children = {}

    get_size(root)
    return root


CAP = 100000


def part_1():
    root = parse_tree()
    log(root)

    queue = deque([root])
    total = 0
    while len(queue) > 0:
        cur = queue.pop()
        if cur.size <= CAP:
            total += cur.size
        # Add subdirectories to the BFS Queue
        queue.extend([node for node in cur.children.values()
                     if len(node.children) > 0])

    return total


AVAILABLE = 70000000
REQUIRED = 30000000


def part_2():
    root = parse_tree()
    log(root)

    current_space = AVAILABLE - root.size
    log(root.size)
    log(current_space)

    target = REQUIRED - current_space
    log(target)

    closest = root

    queue = deque([root])
    while len(queue) > 0:
        cur = queue.pop()
        if cur.size >= target and cur.size - target < closest.size - target:
            log(f"Replacing Best with: {cur.name} ({cur.size})")
            closest = cur
        queue.extend([node for node in cur.children.values()
                     if len(node.children) > 0])

    return closest.size
