import functools
import re
from collections import defaultdict

TEST_1_INPUT = TEST_2_INPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
TEST_1_ANSWER = 143
TEST_2_ANSWER = 123


def parse(data):
    """Parse input into two required parts.

    Args:
        data (str): input from AoC

    Returns:
        dict, list: the rules dict which lists all values which should come before any given lookup,
                    and the list of page updates
    """
    rules, updates = data.strip().split("\n\n")
    values_which_come_before = defaultdict(set)
    for before, after in re.findall(r"(\d+)\|(\d+)", rules):
        values_which_come_before[int(after)].add(int(before))
    updates = [list(map(int, row.split(","))) for row in updates.split("\n")]
    return values_which_come_before, updates


def is_ordered(update, values_which_come_before):
    return not any(values_which_come_before[current].intersection(update[i + 1 :]) for i, current in enumerate(update))


def get_mid(update):
    return update[len(update) // 2]


def part_1(data):
    values_which_come_before, updates = parse(data)
    return sum(get_mid(update) for update in updates if is_ordered(update, values_which_come_before))


def get_key(values_which_come_before):
    def cmp(first, second):
        if first in values_which_come_before[second]:
            return -1
        if second in values_which_come_before[first]:
            return 1
        return 0

    return functools.cmp_to_key(cmp)


def part_2(data):
    values_which_come_before, updates = parse(data)
    return sum(
        get_mid(sorted(update, key=get_key(values_which_come_before)))
        for update in updates
        if not is_ordered(update, values_which_come_before)
    )
