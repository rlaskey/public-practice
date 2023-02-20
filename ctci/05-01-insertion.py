def all_ones(digit: int) -> int:
    count = 0
    while digit > 0:
        count += 1
        digit >>= 1
    return (1 << count) - 1


def insert(dest: int, source: int, i: int, j: int) -> int:
    if i > j or i < 0 or j >= 32:
        return 0

    # 11100000
    left = (all_ones(dest) << (j + 1)) if j < 31 else 0
    # 00000011
    right = (1 << i) - 1
    # 11100011
    mask = left | right

    return (dest & mask) | (source << i)


def test_all_ones():
    assert all_ones(0b11101) == 0b11111
    assert all_ones(0b10001) == 0b11111
    assert all_ones(0b101) == 0b111
    assert all_ones(0b0) == 0b0
    assert all_ones(0b1) == 0b1


def test_it():
    assert insert(0b0, 0b0, -1, 0) == 0
    assert insert(0b0, 0b0, 1, 0) == 0
    assert insert(0b0, 0b0, 1, 33) == 0
    assert insert(0b0, 0b0, 1, 32) == 0

    assert insert(0b1, 0b0, 1, 31) == 0b1

    assert insert(0b10000000000, 0b10011, 2, 6) == 0b10001001100
    assert insert(0b10000000, 0b10011, 2, 6) == 0b11001100
