from lib.helpers import log, get_strings_by_lines


class Node(object):
    def __init__(self, name):
        self.name = name
        self.pressure = 0

        self.tunnels = {}
        self.parent = None

    def __repr__(self):
        return self.name
#    def __repr__(self):
#        indent = "  "
#        s = '- ' + self.name + f" ({self.pressure})" + "\n"
#        for child_name, child_object in self.tunnels.items():
#            s += f"{indent}: {child_name}\n"
#        return s


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


def part_1():
    nodes, start = get_nodes()
    for _, node in nodes.items():
        log(node)

    # Keep track of all possible places we could go
    next_iter = [{
        'next_node': start,
        'visited': set(),
        'opened': set(),
        'so_far': 0
    }]

    known_options = []
    # tick 30 times
    for idx in range(30):
        log(f"idx: {idx}: {len(next_iter)} options")
        if len(next_iter) > 700000:
            # keep the top half 2M only
            sorted_list = sorted(next_iter, key=lambda x: x['so_far'])
            cur_iter = sorted_list[-700000:]
        else:
            cur_iter = next_iter

        next_iter = []

        for cur in cur_iter:
            # Get values for this iteration
            # log(cur)
            node = cur['next_node']
            visited = cur['visited']
            opened = cur['opened']
            so_far = cur['so_far']

            # Calculate pressure to add this iteration
            next_pressure = sum([n.pressure for n in opened])
            # log(f"so_far = {so_far} + {next_pressure} = {so_far + next_pressure}")
            so_far += next_pressure

            # Add this node to visited set
            visited.add(node)

            options_added = 0
            # One option may be to open and stay here
            if node not in opened:
                options_added += 1
                next_iter.append({
                    'next_node': node,
                    'visited': visited.copy(),
                    'opened': opened.copy() | {node},
                    'so_far': so_far
                })

            # For each tunnel, we can go to the next node
            should_stay = True
            for tunnel in node.tunnels.values():
                all_children_visited = all(
                    [c in visited for c in tunnel.tunnels.values()])
                should_stay = should_stay and tunnel in visited and all_children_visited
                options_added += 1
                next_iter.append({
                    'next_node': tunnel,
                    'visited': visited.copy(),
                    'opened': opened.copy(),
                    'so_far': so_far
                })

            # Branch is a dead end – just stay here
            if options_added == 0:
                known_options.append({
                    'next_node': node,
                    'visited': visited.copy(),
                    'opened': opened.copy(),
                    'so_far': so_far + ((29 - idx) * next_pressure)
                })

    # Find the max pressure
    log(len(next_iter))
    totals = max([n['so_far'] for n in next_iter], [
                 known['so_far'] for known in known_options])
    return max(totals)
