import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors


from lib.helpers import log, get_strings_by_lines


def get_surface_area(arr, max_val):
    surface_area = 0
    # Go in X horizontal for every Z and Y layer, looking for changes
    for z in range(0, max_val + 1):
        for y in range(0, max_val + 1):
            for x in range(1, max_val + 1):
                if arr[z][y][x] ^ arr[z][y][x - 1]:
                    surface_area += 1

    # Go in Y horizontal for every Z and X layer, looking for changes
    for z in range(0, max_val + 1):
        for x in range(0, max_val + 1):
            for y in range(1, max_val + 1):
                if arr[z][y][x] ^ arr[z][y - 1][x]:
                    surface_area += 1

    # Go in Z horizontal for every Y and X layer, looking for changes
    for y in range(0, max_val + 1):
        for x in range(0, max_val + 1):
            for z in range(1, max_val + 1):
                if arr[z][y][x] ^ arr[z - 1][y][x]:
                    surface_area += 1

    return surface_area


def part_1():
    cubes = [s.split(',') for s in get_strings_by_lines('18.txt')]
    log(cubes)

    # Find min and max
    xs = []
    ys = []
    zs = []

    for cube in cubes:
        x, y, z = [int(x) + 1 for x in cube]
        xs += [x]
        ys += [y]
        zs += [z]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    min_z, max_z = min(zs), max(zs)
    min_val = min(min_x, min_y, min_z) - 1
    max_val = max(max_x, max_y, max_z) + 1

    log(f"X Range: {min_x}, {max_x}")
    log(f"Y Range: {min_y}, {max_y}")
    log(f"Z Range: {min_z}, {max_z}")

    log(f"Min: {min_val}, Max: {max_val}")

    # Create a 3D array
    arr = []
    for z in range(0, max_val + 1):
        arr += [[]]
        for y in range(0, max_val + 1):
            arr[z] += [[]]
            for x in range(0, max_val + 1):
                arr[z][y] += [False]

    for cube in cubes:
        x, y, z = [int(x) + 1 for x in cube]
        arr[z][y][x] = True

    return get_surface_area(arr, max_val)


def part_2():
    cubes = [s.split(',') for s in get_strings_by_lines('18.txt')]

    # Find min and max
    xs = []
    ys = []
    zs = []

    for cube in cubes:
        x, y, z = [int(x) + 1 for x in cube]
        xs += [x]
        ys += [y]
        zs += [z]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    min_z, max_z = min(zs), max(zs)
    min_val = min(min_x, min_y, min_z) - 1
    max_val = max(max_x, max_y, max_z) + 2

    log(f"X Range: {min_x}, {max_x}")
    log(f"Y Range: {min_y}, {max_y}")
    log(f"Z Range: {min_z}, {max_z}")

    log(f"Min: {min_val}, Max: {max_val}")

    # Create a 3D array
    arr = []
    filled_arr = []
    for z in range(0, max_val + 1):
        arr += [[]]
        filled_arr += [[]]
        for y in range(0, max_val + 1):
            arr[z] += [[]]
            filled_arr[z] += [[]]
            for x in range(0, max_val + 1):
                arr[z][y] += [False]
                filled_arr[z][y] += [False]

    for cube in cubes:
        x, y, z = [int(x) + 1 for x in cube]
        arr[z][y][x] = True

    # Fill in the X Plane
    for z in range(0, max_val + 1):
        for y in range(0, max_val + 1):
            # Get first and last index of True in this row
            first_x, last_x = -1, -1
            for x in range(0, max_val + 1):
                if arr[z][y][x]:
                    first_x = x
                    break
            for x in range(max_val, -1, -1):
                if arr[z][y][x]:
                    last_x = x
                    break

            # Fill in the gaps
            if first_x != -1 and last_x != -1:
                for x in range(first_x, last_x + 1):
                    filled_arr[z][y][x] = True

    # Fill in the Y Plane
    for z in range(0, max_val + 1):
        for x in range(0, max_val + 1):
            # Get first and last index of True in this row
            first_y, last_y = -1, -1
            for y in range(0, max_val + 1):
                if arr[z][y][x]:
                    first_y = y
                    break
            for y in range(max_val, -1, -1):
                if arr[z][y][x]:
                    last_y = y
                    break

            # Fill in the gaps
            if first_y != -1 and last_y != -1:
                for y in range(first_y, last_y + 1):
                    filled_arr[z][y][x] = True

    # Fill in the Z Plane
    for y in range(0, max_val + 1):
        for x in range(0, max_val + 1):
            # Get first and last index of True in this row
            first_z, last_z = -1, -1
            for z in range(0, max_val + 1):
                if arr[z][y][x]:
                    first_z = z
                    break
            for z in range(max_val, -1, -1):
                if arr[z][y][x]:
                    last_z = z
                    break

            # Fill in the gaps
            if first_z != -1 and last_z != -1:
                for z in range(first_z, last_z + 1):
                    filled_arr[z][y][x] = True

    # Carve out the Y plane
    for z in range(0, max_val + 1):
        for x in range(0, max_val + 1):
            for y in range(0, max_val + 1):
                if not arr[z][y][x]:
                    filled_arr[z][y][x] = False
                else:
                    break
            for y in range(max_val, -1, -1):
                if not arr[z][y][x]:
                    filled_arr[z][y][x] = False
                else:
                    break

    # Carve out the Z plane
    for y in range(0, max_val + 1):
        for x in range(0, max_val + 1):
            for z in range(0, max_val + 1):
                if not arr[z][y][x]:
                    filled_arr[z][y][x] = False
                else:
                    break
            for z in range(max_val, -1, -1):
                if not arr[z][y][x]:
                    filled_arr[z][y][x] = False
                else:
                    break

    # Carve out the X plane
    for z in range(0, max_val + 1):
        for y in range(0, max_val + 1):
            for x in range(0, max_val + 1):
                if not arr[z][y][x]:
                    filled_arr[z][y][x] = False
                else:
                    break
            for x in range(max_val, -1, -1):
                if not arr[z][y][x]:
                    filled_arr[z][y][x] = False
                else:
                    break

    return get_surface_area(filled_arr, max_val)


def visualize_poorly(arr):
    # Convert the array to a NumPy array for easier manipulation
    array = np.array(arr)

    # Create a figure and a 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X, Y, Z = np.indices(array.shape)

    X = X.reshape(-1)
    Y = Y.reshape(-1)
    Z = Z.reshape(-1)

    # Plot the boolean values as a surface plot
    ax.scatter(X, Y, Z, c=array, marker="s", cmap="binary",
               edgecolor='face', alpha=.5, depthshade=True)
    plt.show()
