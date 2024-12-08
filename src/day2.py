import numpy as np

TEST_1_INPUT = TEST_2_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
TEST_1_ANSWER = 2
TEST_2_ANSWER = 4


def part_1(data):
    safe_tot = 0
    for row in data.splitlines():
        data = np.array(list(map(int, row.strip().split())))
        deltas = np.diff(data)
        safe = (np.all(deltas < 0) | np.all(deltas > 0)) & np.all(np.abs(deltas) <= 3)
        if safe:
            safe_tot += 1
    return safe_tot


def part_2(data):
    safe_tot = 0
    for row in data.splitlines():
        data = np.array(list(map(int, row.strip().split())))
        for i, _ in enumerate(data):
            # TODO: do not copy data, just slice
            deltas = np.diff(np.delete(data, i, 0))
            safe = (np.all(deltas < 0) | np.all(deltas > 0)) & np.all(np.abs(deltas) <= 3)
            if safe:
                break
        else:
            continue
        safe_tot += 1
    return safe_tot
