from functools import cache

import numpy as np

TEST_1_INPUT = TEST_2_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""
TEST_1_ANSWER = 11
TEST_2_ANSWER = 31


def parse(data):
    return np.array([list(map(int, line.split())) for line in data.splitlines()])


def part_1(data):
    data = parse(data)
    data.sort(axis=0)
    return np.abs(np.diff(data, axis=1)).sum()


def part_2(data):
    data = parse(data)

    @cache
    def count(num):
        return np.count_nonzero(data[:, 1] == num)

    return sum(i * count(i) for i in data[:, 0])
