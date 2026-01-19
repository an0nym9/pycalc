import pytest
from pycalc.probability import factorial, permutations, combinations # type: ignore

@pytest.mark.parametrize("num,error_msg,is_error,expected_value", [
    # Happy cases
    (0, "", False, 1),
    (7, "", False, 5040),

    # Error cases
    (None, "No number provided.", True, None),
])
def test_factorial(num, error_msg, is_error, expected_value):
    result = factorial(num)
    if not is_error:
        assert result.is_ok()
        assert result.unwrap() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg


@pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
    # Happy cases
    ((5, 3), "", False, 60),
    ((7, 0), "", False, 1),

    # Error cases
    ((12, None), "Missing a number.", True, None),
    ((None, 4), "Missing a number.", True, None),
])
def test_permutations(args, error_msg, is_error, expected_value):
    result = permutations(*args)
    if not is_error:
        assert result.is_ok()
        assert result.unwrap() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
    # Happy cases
    ((5, 3), "", False, 10),
    ((7, 0), "", False, 1),

    # Error cases
    ((8, None), "Missing a number.", True, None),
    ((None, 2), "Missing a number.", True, None),
])
def test_combinations(args, error_msg, is_error, expected_value):
    result = combinations(*args)
    if not is_error:
        assert result.is_ok()
        assert result.unwrap() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg
