import pytest
from pycalc.finance import interest

@pytest.mark.parametrize("kwargs,error_msg,is_error,expected_value", [
    # Happy cases
    (
        {
            "I": None,
            "P": 850.0,
            "r": 0.05,
            "t": 2.0,
            "compound": False,
            "n": 1,
            "FV": False,
        },
        "",
        False,
        85.0,
    ),
    (
        {
            "I": None,
            "P": 128.0,
            "r": 0.05,
            "t": 1.0,
            "compound": True,
            "n": 6,
            "FV": True,
        },
        "",
        False,
        134.53,
    ),
])
def test_interest(
    kwargs: dict,
    error_msg: str,
    is_error: bool,
    expected_value: any
) -> None:
    result = interest(**kwargs)
    if not is_error:
        assert result.is_ok()
        assert round(result.ok(), 2) == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg
