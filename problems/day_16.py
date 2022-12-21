import heapq
from lib.helpers import log, get_strings_by_lines


pressures = {}
paths = {}

# Keep these two lists with only the nodes that have pressure
index_of = {}
ordered_list = []


def get_nodes():
    global pressures, paths, index_of, ordered_list
    lines = [l[6:] for l in get_strings_by_lines('16.txt')]

    for idx, line in enumerate(lines):
        valve = line[0:2]
        _, rest = line.split('rate=')
        rateStr, tStr = rest.split('; ')
        rate = int(rateStr)
        tunnels = [s[-2:] for s in tStr.split(', ')]

        pressures[valve] = rate
        paths[valve] = [t for t in tunnels]
        if rate > 0:
            ordered_list += [valve]
            index_of[valve] = len(ordered_list) - 1


# Find the minimum distance from start node to every other node with pressure
def dijkstra(start):
    global paths
    distances = {start: 0}
    visited = set()
    queue = [(0, start)]

    while queue:
        distance, node = heapq.heappop(queue)
        visited.add(node)

        for neighbor in paths[node]:
            if neighbor in visited:
                continue
            new_distance = distance + 1
            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances


CACHE = {}


def dynamic_solve(cur_node, opened, tick):
    global CACHE, pressures, paths, min_distances
    key = (cur_node, opened, tick)
    # log(f"Checking {cur_node} with {opened} at {so_far} with {tick} left")

    # Check Cache for the answer
    if key in CACHE:
        # log("Cache Hit: " + key + " " + str(CACHE[key]))
        return CACHE[key]

    best_remaining = 0
    if tick > 0:  # Base Case
        # Try going down each of the tunnels
        for tunnel in ordered_list:
            mask = 1 << index_of[tunnel]
            dist = min_distances[cur_node][tunnel]
            if (not (opened & mask)) and (tick - (dist + 1) >= 0):
                # Go there and open it
                possibility = (
                    dynamic_solve(tunnel, opened | mask, tick - (dist + 1)) +
                    pressures[tunnel] * (tick - (dist + 1)))
                if possibility > best_remaining:
                    best_remaining = possibility
    elif tick < 0:
        log(f"Error: tick is {tick}")
        return 0

    # Cache answer
    CACHE[key] = best_remaining
    return best_remaining


min_distances = {}


def part_1():
    global pressures, paths, index_of, ordered_list, min_distances, CACHE
    get_nodes()
    min_distances["AA"] = dijkstra("AA")
    for node in ordered_list:
        min_distances[node] = dijkstra(node)

    # Keep track of all possible places we could go
    return dynamic_solve("AA", 0, 30)


def part_2():
    global pressures, paths, index_of, ordered_list, min_distances, CACHE
    get_nodes()

    min_distances["AA"] = dijkstra("AA")
    for node in ordered_list:
        min_distances[node] = dijkstra(node)

    max_bits = 1 << len(ordered_list)
    max_return = 0
    for i in range(max_bits):
        forged_1 = i
        forged_2 = (max_bits - 1) ^ forged_1  # XOR to get inverse bitmask

        if i % 1000 == 0:
            log(f"Checking {i} of {max_bits}")

        # Partition sets by pretending we've already opened some nodes
        section_1 = dynamic_solve("AA", forged_1, 26)
        section_2 = dynamic_solve("AA", forged_2, 26)

        if section_1 + section_2 > max_return:
            max_return = section_1 + section_2
            log(f"New Max: {max_return} with {forged_1} and {forged_2}")

    return max_return
