import math
from lib.helpers import log, get_strings_by_lines
from lib.config import TEST_MODE


# manhattan_distance – caluclate the manhattan distance between two points
# as (x, y) tuples
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


points = {}
sensors = {}


# Print grid of points
def print_grid(grid, min_x, min_y, max_x, max_y):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in grid:
                print(grid[(x, y)], end='')
            else:
                print('.', end='')
        print()


def get_points_and_sensors():
    lines = get_strings_by_lines('15.txt')

    # parse each line into points keeping track of the min and max x and y
    max_x, max_y = - math.inf, - math.inf
    min_x, min_y = math.inf, math.inf
    for line in lines:
        line = line[10:]
        sensorStr, beaconStr = line.split(': closest beacon is at ')

        # Parse the sensor and track if sets any new records
        sensorX, sensorY = [int(x[2:]) for x in sensorStr.split(', ')]

        # Parse the beacon and track if it sets new records
        beaconX, beaconY = [int(x[2:]) for x in beaconStr.split(', ')]
        # Add points to the grid
        points[(beaconX, beaconY)] = 'B'
        points[(sensorX, sensorY)] = 'S'

        # Add sensor to the map
        sensors[(sensorX, sensorY)] = manhattan_distance(
            (sensorX, sensorY), (beaconX, beaconY))

    log(points)
    log(sensors)

    return points, sensors


def part_1():
    points, sensors = get_points_and_sensors()

    # Find min and max values
    all_xs = [x for x, _ in points.keys()]
    all_ys = [y for _, y in points.keys()]
    min_x, max_x = min(all_xs), max(all_xs)
    min_y, max_y = min(all_ys), max(all_ys)

    log(f"min_x: {min_x}, max_x: {max_x}")
    log(f"min_y: {min_y}, max_y: {max_y}")
    if TEST_MODE:
        print_grid(points, min_x, min_y, max_x, max_y)
        check_row = 10
    else:
        check_row = 2000000

    # find the max manhattan distance
    max_dist = max([d for d in sensors.values()])

    taken_count = 0
    for x in range(min_x - max_dist, max_x + max_dist + 1):
        if (x, check_row) not in points:
            for sensor, dist in sensors.items():
                if manhattan_distance((x, check_row), sensor) <= dist:
                    taken_count += 1
                    break
            else:
                continue  # only executed if the inner loop did NOT break
            continue  # only executed if the inner loop DID break

    return taken_count


def part_2():
    points, sensors = get_points_and_sensors()

    max_x = 20 if TEST_MODE else 4000000
    max_y = max_x

    log(f"{len(sensors)} sensors")
    options = []
    # Find the potential points
    for sensor, dist in sensors.items():
        # Triangle Method
        sx, sy = sensor
        log(f"Sensor: {sensor}, dist: {dist}")

        for d in range(0, dist + 1):
            dx = d
            dy = dist - d
            low_x, high_x = sx - dx - 1, sx + dx + 1
            low_y, high_y = sy - dy, sy + dy

            options += (
                [(x, y) for x, y in
                 [(low_x, low_y), (low_x, high_y),
                  (high_x, low_y), (high_x, high_y)]
                    if 0 <= x <= max_x and 0 <= y <= max_y
                 ])

    log(len(options))

    idx = 0
    for (x, y) in options:
        idx += 1
        if idx % 1000 == 0:
            log(f"Checking {idx} of {len(options)}")
        for sensor, dist in sensors.items():
            if manhattan_distance((x, y), sensor) <= dist:
                break
        else:
            return (x * 4000000) + y  # Executed if we didn't brek
        continue  # executed if we did break
