import pytest
from pycalc.calculus import arithmetic_sequence, arithmetic_series, arithmetic_difference

@pytest.mark.parametrize("kwargs,error_msg,is_error,expected_value", [
    # Happy cases
    ({"tn":None,"ti":6,"d":4,"n":5}, "", False, 22),
    ({"tn": None, "ti": 3, "d": 5, "n": 4}, "", False, 18),

    # Error Cases
    ({"tn": None, "ti": None, "d": 7, "n": None}, "Need only one unknown value.", True, None),
])
def test_arithmetic_sequence(
    kwargs: dict,
    error_msg: str,
    is_error: bool,
    expected_value: any
) -> None:
    result = arithmetic_sequence(**kwargs)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("kwargs,error_msg,is_error,expected_value", [
    # Happy cases
    ({"sn": None, "n": 4, "ti": 2, "tn": 14, "d": None}, "", False, 32),
    ({"sn": None, "n": 5, "ti": 1, "tn": 10, "d": None}, "", False, 27.5),

    # Error Cases
    ({"sn": None, "n": 5, "ti": None, "tn": 10, "d": None}, "Need only 2 unknown value to solve.", True, None),
])
def test_arithmetic_series(
    kwargs: dict,
    error_msg: str,
    is_error: bool,
    expected_value: any
) -> None:
    result = arithmetic_series(**kwargs)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("kwargs,error_msg,is_error,expected_value", [
    # Happy Cases
    ({"tn1": 10, "tn2": 4}, "", False, 6),
    ({"tn1": 7, "tn2": 12}, "", False, -5),

    # Error Cases
    ({"tn1": None, "tn2": 6}, "Not enough data to find the difference.", True, None),
])
def test_arithmetic_difference(
    kwargs: dict,
    error_msg: str,
    is_error: bool,
    expected_value: any
) -> None:
    result = arithmetic_difference(**kwargs)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

