BAD_RESULT = "ERROR"


def doubling_printer(input: float) -> str:
    if input >= 1 or input <= 0:
        return BAD_RESULT

    result = "."
    while input > 0:
        if len(result) >= 32:
            return BAD_RESULT
        r = input * 2
        if r >= 1:
            result += "1"
            input = r - 1
        else:
            result += "0"
            input = r
    return result


def halving_printer(input: float) -> str:
    if input >= 1 or input <= 0:
        return BAD_RESULT

    result = "."
    fraction = 0.5
    while input > 0:
        if len(result) >= 32:
            return BAD_RESULT

        if input >= fraction:
            result += "1"
            input -= fraction
        else:
            result += "0"

        fraction /= 2

    return result


def test_doubling():
    assert doubling_printer(-1) == BAD_RESULT
    assert doubling_printer(1.01) == BAD_RESULT

    assert doubling_printer(0.125) == ".001"
    assert doubling_printer(0.25) == ".01"
    assert doubling_printer(0.5) == ".1"
    assert doubling_printer(0.75) == ".11"
    assert doubling_printer(0.875) == ".111"
    assert doubling_printer(0.88) == BAD_RESULT


def test_halving():
    assert halving_printer(0.125) == ".001"
    assert halving_printer(0.25) == ".01"
    assert halving_printer(0.5) == ".1"
    assert halving_printer(0.75) == ".11"
    assert halving_printer(0.875) == ".111"
    assert halving_printer(0.88) == BAD_RESULT
