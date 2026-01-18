import ast
import pytest
from pycalc.parser import eval_expr

@pytest.mark.parametrize("expr,error_msg,is_error,expected_value", [
    # Happy cases
    ("factorial(5) * 2 / 5", "", False, 48),
    ("sum(4, 6, 2, 5) * 2", "", False, 34),

    # Error Cases
])
def test_eval_expr(
    expr: str,
    error_msg: str,
    is_error: bool,
    expected_value: any
) -> None:
    result = eval_expr(ast.parse(expr, mode="eval").body)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg
