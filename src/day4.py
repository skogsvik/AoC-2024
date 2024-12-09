import numpy as np

TEST_1_INPUT = TEST_2_INPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
TEST_1_ANSWER = 18
TEST_2_ANSWER = 9

LOOKUP = dict(zip("XMAS", XMAS := np.arange(4), strict=True))
X, M, A, S = XMAS


def parse(data):
    return np.array([[LOOKUP[c] for c in row] for row in data.splitlines()])


def find_char(data, char):
    return np.nonzero(data == char)


def find_word_1d(array: np.ndarray, start: int, match: np.ndarray):
    """Find subarrays starting at `start` either forward or backward.

    Args:
        array (np.ndarray): 1D array to search
        start (int): Starting index
        match (np.ndarray): array to look for

    Returns:
        int: count of the number of times the match exists, either 0, 1, or 2 times
    """
    n = match.size
    return np.array_equal(array[start : start + n], match) + np.array_equal(array[start::-1][:n], match)


def get_diagonal(data, row, col):
    return data.diagonal(col - row), min(col, row)


def count_xmas(row, col, data):
    diagonal, diag_idx = get_diagonal(data, row, col)
    # Flip array to get anti-diagonal
    anti_diagonal, flipped_diag_idx = get_diagonal(np.fliplr(data), row, data.shape[1] - 1 - col)
    return (
        find_word_1d(data[row], col, XMAS)
        + find_word_1d(data[:, col], row, XMAS)
        + find_word_1d(diagonal, diag_idx, XMAS)
        + find_word_1d(anti_diagonal, flipped_diag_idx, XMAS)
    )


def part_1(data):
    data = parse(data)
    xs_rows, xs_columns = find_char(data, X)
    return sum(count_xmas(r, c, data) for r, c in zip(xs_rows, xs_columns, strict=True))


R_CROSS = np.array([-1, 1, -1, 1])
C_CROSS = np.array([-1, 1, 1, -1])
VALID_CROSSES = np.array(
    [
        [M, S, M, S],
        [S, M, M, S],
        [M, S, S, M],
        [S, M, S, M],
    ]
)


def count_x_mas(row, col, data):
    cross = data[row + R_CROSS, col + C_CROSS]
    valid = cross == VALID_CROSSES
    return valid.all(axis=1).any()


def part_2(data):
    data = parse(data)
    as_rows, as_columns = find_char(data, A)

    # Remove edges
    rows, cols = data.shape
    top_or_bottom = (as_rows == 0) | (as_rows == rows - 1)
    left_or_right = (as_columns == 0) | (as_columns == cols - 1)
    not_edge = ~(top_or_bottom | left_or_right)
    as_rows, as_columns = as_rows[not_edge], as_columns[not_edge]

    return sum(count_x_mas(r, c, data) for r, c in zip(as_rows, as_columns, strict=True))
