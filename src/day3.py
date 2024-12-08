import re

TEST_1_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TEST_1_ANSWER = 161
TEST_2_INPUT = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
TEST_2_ANSWER = 48


RE_FIND_MULTS = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)", re.DOTALL)
RE_ENABLED_BLOCKS = re.compile(r"(?:^|do\(\)).*?(?:don't\(\)|$)", re.DOTALL)


def part_1(data):
    return sum(int(a) * int(b) for a, b in RE_FIND_MULTS.findall(data))


def part_2(data):
    parts = []
    for block in RE_ENABLED_BLOCKS.findall(data):
        print(block)
        parts.append(part_1(block))
    print(len(RE_ENABLED_BLOCKS.findall(data)))
    print(parts)
    print(sum(parts))
    return sum(map(part_1, RE_ENABLED_BLOCKS.findall(data)))
