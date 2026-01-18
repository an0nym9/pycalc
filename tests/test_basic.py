import pytest
from pycalc.basic import sum, difference, product, qoutient # type: ignore

@pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
    # Happy cases
    ((25, 56, 4), "", False, 85),
    ((128, 5, 6), "", False, 139),

    # Error Cases
    ((), "No numbers provided.", True, None),
])
def test_sum(
    args: tuple,
    error_msg: str,
    is_error: bool,
    expected_value: any
) -> None:
    result = sum(*args)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
    # Happy cases
    ((14, 3, 6), "", False, 5),
    ((23, 15, 2), "", False, 6),

    # Error Cases
    ((), "No numbers provided.", True, None),
])
def test_difference(
    args: tuple,
    error_msg: str,
    is_error: bool,
    expected_value: any
) -> None:
    result = difference(*args)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
    # Happy cases
    ((2, 8, 4), "", False, 64),
    ((5, 3, 7), "", False, 105),

    # Error Cases
    ((), "No numbers provided.", True, None),
])
def test_product(
    args: tuple,
    error_msg: str,
    is_error: bool,
    expected_value: any
) -> None:
    result = product(*args)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
    # Happy cases
    ((12, 3, 2), "", False, 2),
    ((120, 5, 2), "", False, 12),

    # Error Cases
    ((), "No numbers provided.", True, None),
    ((1, 0, 2), "Cannot divide by zero.", True, None),
])
def test_qoutient(
    args: tuple,
    error_msg: str,
    is_error: bool,
    expected_value: any
) -> None:
    result = qoutient(*args)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg
