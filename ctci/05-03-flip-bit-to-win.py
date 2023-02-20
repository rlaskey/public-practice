def most_ones(input: int) -> int:
    result = 1
    current_len = 0
    previous_len = 0
    while input > 0:
        if (input & 1) == 1:
            current_len += 1
        else:
            # two 0s in a row => reset
            previous_len = 0 if (input & 2) == 0 else current_len
            current_len = 0
        result = max(result, previous_len + current_len + 1)
        input >>= 1
    return result


def test_it():
    assert most_ones(1775) == 8
