import pytest
from pycalc.probability import factorial, permutations, combinations # type: ignore

# @pytest.mark.parametrize("num,error_msg,is_error,expected_value", [
#     # Happy cases
#     (0, "", False, 1),
#     (7, "", False, 5040),

#     # Error cases
#     (-1, "Parameter 'n' is expected to be of type int, got int.", True, None),
#     (None, "Parameter 'n' is expected to be of type int, got NoneType.", True, None),
# ])
# def test_factorial(num, error_msg, is_error, expected_value):
#     result = factorial(num)
#     if not is_error:
#         assert result.is_ok()
#         assert result.unwrap() == expected_value
#     else:
#         assert result.is_err()
#         assert str(result.err()) == error_msg


# @pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
#     # Happy cases
#     ((5, 3), "", False, 60),  # P(5,3) = 5*4*3 = 60
#     ((7, 0), "", False, 1),   # P(7,0) = 1

#     # Error cases
#     ((5, 6), "Cannot compute factorial of negative number.", True, None),
#     ((None, 3), "Parameter 'a' is expected to be of type int, got NoneType.", True, None),
# ])
# def test_permutations(args, error_msg, is_error, expected_value):
#     result = permutations(*args)
#     if not is_error:
#         assert result.is_ok()
#         assert result.unwrap() == expected_value
#     else:
#         assert result.is_err()
#         assert str(result.err()) == error_msg

# @pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
#     # Happy cases
#     ((5, 3), "", False, 10),  # C(5,3) = 10
#     ((7, 0), "", False, 1),   # C(7,0) = 1

#     # Error cases
#     ((5, 6), "Cannot compute factorial of negative number.", True, None),
#     ((None, 3), "Parameter 'a' is expected to be of type int, got NoneType.", True, None),
# ])
# def test_combinations(args, error_msg, is_error, expected_value):
#     result = combinations(*args)
#     if not is_error:
#         assert result.is_ok()
#         assert result.unwrap() == expected_value
#     else:
#         assert result.is_err()
#         assert str(result.err()) == error_msg
