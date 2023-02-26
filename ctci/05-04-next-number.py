def largest(input: int) -> int:
    count_zeros = 0
    count_ones = 0

    copy = input
    while ((copy & 1) == 0) and (copy != 0):
        count_zeros += 1
        copy >>= 1

    while (copy & 1) == 1:
        count_ones += 1
        copy >>= 1
    del copy

    # no solution, re: nothing we can change
    if (count_zeros + count_ones) in (31, 0):
        return -1

    # highest place that we flip
    first_non_leading_zero = count_zeros + count_ones

    # from: 0b1010011100
    # to:   0b1010111100
    input |= 1 << first_non_leading_zero

    # clear the bits below
    # from: 0b1010111100
    # to:   0b1010100000
    input &= ~((1 << first_non_leading_zero) - 1)

    # add back in the ones; one less, re: what we flipped
    # from: 0b1010100000
    # to:   0b1010100011
    input |= (1 << (count_ones - 1)) - 1

    return input


def smallest(input: int) -> int:
    count_zeros = 0
    count_ones = 0

    copy = input
    while (copy & 1) == 1:
        count_ones += 1
        copy >>= 1

    if copy == 0:
        return -1

    while ((copy & 1) == 0) and (copy != 0):
        count_zeros += 1
        copy >>= 1
    del copy

    # highest place that we flip
    first_non_leading_one = count_zeros + count_ones

    # clear bits out
    # from: 0b10000011
    # to:   0b00000000
    input &= ~0 << (first_non_leading_one + 1)

    # fill in the ones, high up as we can go
    # from: 0b00000000
    # to:   0b01110000
    input |= ((1 << (count_ones + 1)) - 1) << (count_zeros - 1)

    return input


def test_largest():
    assert largest(0b1010) == 0b1100
    assert largest(0b1001) == 0b1010
    assert largest(0b101) == 0b110
    assert largest(0b1010011100) == 0b1010100011


def test_smallest():
    assert smallest(0b10000011) == 0b1110000
