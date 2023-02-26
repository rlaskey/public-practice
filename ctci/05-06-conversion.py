def bit_difference(a: int, b: int) -> int:
    result = 0
    xor = a ^ b
    while xor != 0:
        if xor & 1 == 1:
            result += 1
        xor >>= 1
    return result


def test_smallest():
    assert bit_difference(0b11101, 0b01111) == 2
    assert bit_difference(0b11111, 0b01111) == 1
    assert bit_difference(0b11101, 0b01101) == 1
    assert bit_difference(0b0111, 0b0111) == 0
    assert bit_difference(0b1111, 0b0111) == 1
