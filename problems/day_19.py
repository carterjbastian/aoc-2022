"""
Day_19.py. Another exponential search problem.

To Optimize, we're going to do recursive DFS modified by the following:
1. Reframe the search steps to be about robot building.
    In each step, next options are "which robot should I build next"
2. Always stop making robots after we've hit the max we need of them per-turn
3. Pruning: Calculate a constant time upper bound on the potential score of the path.
    If it's less than an actual score we've seen so far, don't consider that path.
"""
from lib.helpers import log, get_strings_by_lines
import math


def parse_blueprints():
    blueprints = []
    for line in get_strings_by_lines('19.txt'):
        costs = {}
        max_costs = {}
        _, oreStr, clayStr, obsStr, geoStr = line.split(' robot costs ')
        oreCost = int(oreStr.split(" ")[0])
        costs['ore'] = {
            'ore': oreCost,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
        }

        clayCost = int(clayStr.split(" ")[0])
        costs['clay'] = {
            'ore': clayCost,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
        }
        obsOre, obsClay = int(obsStr.split(" ")[0]), int(obsStr.split(" ")[3])
        costs['obsidian'] = {
            'ore': obsOre,
            'clay': obsClay,
            'obsidian': 0,
            'geode': 0
        }

        geoOre, geoObs = int(geoStr.split(" ")[0]), int(geoStr.split(" ")[3])
        costs['geode'] = {
            'ore': geoOre,
            'clay': 0,
            'obsidian': geoObs,
            'geode': 0
        }

        # When should we stop making robots?
        max_costs['ore'] = max([oreCost, clayCost, obsOre, geoOre])
        max_costs['clay'] = obsClay
        max_costs['obsidian'] = geoObs

        blueprints += [(costs, max_costs)]

    return blueprints


# Not thread-safe!
BEST_SO_FAR = 0


def get_max_obsidian(robots, ores, costs, max_costs, time_remaining):
    global BEST_SO_FAR
    # Base Case - time remaining = 0
    if time_remaining <= 0:
        return ores['geode']

    # Loop through each of the robots we could either make or try to make
    new_options = 0
    new_best = -1
    for material in ['ore', 'clay', 'obsidian', 'geode']:
        # skip early #1: Have we hit out max already?
        if material != 'geode' and robots[material] >= max_costs[material]:
            continue

        # Figure out how many turns we need to wait for ore, clay, or obsidian
        turns_to_wait = max([0] + [
            # We might not be able to get to a clay-requiring or obsidian robot
            math.inf
            if robots[dep] == 0
            else math.ceil((costs[material][dep] -
                            ores[dep]) / robots[dep])

            # In each actual dependency ore required for material
            for dep in ['ore', 'clay', 'obsidian'] if costs[material][dep] > 0
        ])

        # Do we have enough time to wait?
        if turns_to_wait >= time_remaining:
            continue

        # Else, simulate the turns - Add the new robots
        new_robots = robots.copy()
        new_robots[material] += 1

        # Simulate turns_to_wait + 1 turns, and subtract out the costs of the new robot
        new_ores = ores.copy()
        new_ores['ore'] += ((turns_to_wait + 1) *
                            robots['ore']) - costs[material]['ore']
        new_ores['clay'] += ((turns_to_wait + 1) *
                             robots['clay']) - costs[material]['clay']
        new_ores['obsidian'] += ((turns_to_wait + 1) *
                                 robots['obsidian']) - costs[material]['obsidian']
        new_ores['geode'] += ((turns_to_wait + 1) * robots['geode'])

        # Keep track of best actual 'geode' score early
        if new_ores['geode'] > BEST_SO_FAR:
            BEST_SO_FAR = new_ores['geode']
            log(f"New Best: {BEST_SO_FAR}")

        # TODO: Prune with upper-bound heuristic

        # Recurse on this option
        new_options += 1
        potential_quality = get_max_obsidian(
            new_robots, new_ores, costs, max_costs,
            time_remaining - (turns_to_wait + 1))

        if potential_quality > new_best:
            new_best = potential_quality

    # If we didn't find any new options, return the result of
    # waiting for the remainder for the time
    if new_options == 0:
        return ores['geode'] + (time_remaining * robots['geode'])
    else:
        return new_best


def part_1():
    global BEST_SO_FAR
    blueprints = parse_blueprints()
    log(blueprints)

    # Loop through each blueprint
    total_quality = 0
    for idx, (costs, max_costs) in enumerate(blueprints):
        BEST_SO_FAR = 0
        quality = get_max_obsidian(
            # Init robots and ores
            {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0},
            {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0},
            costs, max_costs, 24)
        log(f"Found Quality {quality} for {idx}")
        total_quality += ((idx + 1) * quality)
    return total_quality
