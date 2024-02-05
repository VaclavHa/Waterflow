import argparse
import copy
import sys

INPUT = [
    [5, 5, 5, 3, 3, 3, 2, 4],
    [5, 2, 5, 1, 1, 1, 2, 4],
    [5, 2, 6, 6, 1, 3, 2, 4],
    [5, 1, 2, 6, 3, 1, 2, 4],
    [5, 1, 1, 3, 3, 4, 4, 4],
    [5, 1, 2, 3, 1, 5, 2, 4],
    [5, 2, 1, 4, 5, 6, 2, 4],
    [4, 2, 1, 3, 2, 2, 1, 4],
    [4, 4, 4, 3, 3, 3, 1, 4]
]

DIRECTION_OPERATION = {
    "TOP": (0, -1),
    "TOP_LEFT": (-1, -1),
    "TOP_RIGHT": (1, -1),
    "BOTTOM": (0, 1),
    "BOTTOM_LEFT": (-1, 1),
    "BOTTOM_RIGHT": (1, 1),
}


def print_matrix(matrix):
    delimiter = ""
    for i in range(len(matrix)):
        delimiter += "==="

    print(delimiter)
    for r in matrix:
        row = "|"
        for c in r:
            row += f" {str(c)} "
        print(f"{row}|")
    print(delimiter)


def step(steps: list, result_steps: list, result_matrix: list):
    # store current step and pop from step history
    current = steps.pop()
    x = current["x"]
    y = current["y"]
    value = current["value"]

    # cycle all available operations and generate new states
    for name, direction in DIRECTION_OPERATION.items():
        # calculate next state destination
        next_x = x + direction[0]
        next_y = y + direction[1]

        # underflow check
        if next_y < 0 or next_x < 0:
            continue
        # overflow check
        if next_y >= len(INPUT) or next_x >= len(INPUT[next_y]):
            continue
        # value check, higher values cannot access, zero values dont evaluate again
        if result_matrix[next_y][next_x] > value or result_matrix[next_y][next_x] == 0:
            continue

        next_step = {"x": next_x, "y": next_y, "direction": name, "value": result_matrix[next_y][next_x]}
        steps.append(next_step)
        result_steps.append(next_step)
        result_matrix[next_y][next_x] = 0

    # end condition, no new states generated
    if len(steps) == 0:
        return

    # continue recursively
    step(steps, result_steps, result_matrix)


def run(x: int, y: int):
    if y >= len(INPUT) - 1:
        print("Y out of bounds", y)
        return False
    if x >= len(INPUT[y]):
        print("X out of bounds", x)
        return False

    steps = [
        {"x": x, "y": y, "direction": "START", "value": INPUT[y][x]}
    ]
    result_steps = copy.deepcopy(steps)
    result_matrix = copy.deepcopy(INPUT)

    # start running
    step(steps, result_steps, result_matrix)
    # assign first state value
    result_matrix[y][x] = 0

    print_matrix(INPUT)
    print_matrix(result_matrix)
    for s in result_steps:
        print(s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Waterfall", description="Insert position in the matrix to find water path.")
    parser.add_argument("-x", action="store", dest="x", default=0, type=int, help="X position in the matrix, columns")
    parser.add_argument("-y", action="store", dest="y", default=0, type=int, help="Y position in the matrix, rows")
    args = parser.parse_args(sys.argv[1:])
    run(args.x, args.y)
