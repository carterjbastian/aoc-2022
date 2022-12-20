from lib.helpers import log, get_strings_by_lines


class Node(object):
    def __init__(self, name):
        self.name = name
        self.pressure = 0

        self.tunnels = {}
        self.parent = None

    def __repr__(self):
        return self.name


def get_nodes():
    lines = [l[6:] for l in get_strings_by_lines('16.txt')]

    nodes = {}
    idx = 0
    for line in lines:
        valve = line[0:2]
        _, rest = line.split('rate=')
        rateStr, tStr = rest.split('; ')
        rate = int(rateStr)
        tunnels = [s[-2:] for s in tStr.split(', ')]

        if valve not in nodes:
            nodes[valve] = Node(valve)
        nodes[valve].pressure = rate

        # Add new valves as children
        for t in tunnels:
            if t not in nodes:
                nodes[t] = Node(t)
            nodes[valve].tunnels[t] = nodes[t]

        if idx == 0:
            first = nodes[valve]
        idx += 1

    return nodes, first


class Runner():
    def __init__(self, next_node, visited, opened, so_far):
        self.next_node = next_node
        self.visited = visited
        self.opened = opened
        self.so_far = so_far

    def __str__(self):
        return (
            self.next_node.name + str(self.visited) +
            str(self.opened) + str(self.so_far)
        )

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return str(self) == str(other)


def part_1():
    nodes, start = get_nodes()
    for _, node in nodes.items():
        log(node)

    # Keep track of all possible places we could go
    next_iter = set([Runner(start, set(), set(), 0)])
    log([str(i) for i in next_iter])

    known_options = set()
    # tick 30 times
    for idx in range(30):
        log(f"idx: {idx}: {len(next_iter)} options")
        cur_iter = next_iter

        next_iter = set()

        for cur in cur_iter:
            # Get values for this iteration
            # log(cur)
            node = cur.next_node
            visited = cur.visited
            opened = cur.opened
            so_far = cur.so_far

            # Calculate pressure to add this iteration
            next_pressure = sum([n.pressure for n in opened])
            # log(f"so_far = {so_far} + {next_pressure} = {so_far + next_pressure}")
            so_far += next_pressure

            # Add this node to visited set
            visited.add(node)

            options_added = 0
            # One option may be to open and stay here
            if node not in opened and node.pressure > 0:
                options_added += 1
                next_iter.add(Runner(node, visited.copy(),
                                     opened.copy() | {node}, so_far))

            # For each tunnel, we can go to the next node
            for tunnel in node.tunnels.values():
                if idx >= 15 and so_far < 300:
                    continue
                if idx >= 25 and so_far < 900:
                    continue
                next_iter.add(
                    Runner(tunnel, visited.copy(), opened.copy(), so_far)
                )

    # Find the max pressure
    log(len(next_iter))
    totals = max([n.so_far for n in next_iter], [
                 known.so_far for known in known_options])
    return max(totals)
