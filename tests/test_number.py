import pytest

from pycalc.number import ( # type: ignore
    is_prime,
    is_semi_prime,
    gen_primes,
    gen_semi_primes,
    fraction_to_decimal,
    decimal_to_fraction,
    factor,
    lcm,
    gcd,
    remain,
)

@pytest.mark.parametrize("num,error_msg,is_error,expected_value", [
    # Happy cases
    (2, "", False, True),
    (19, "", False, True),

    # Error cases
    (None, "No number provided.", True, None),
])
def test_is_prime(num, error_msg, is_error, expected_value):
    result = is_prime(num)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("num,error_msg,is_error,expected_value", [
    # Happy cases
    (4, "", False, True),
    (6, "", False, True),

    # Error cases
    (None, "No number provided.", True, None),
])
def test_is_semi_prime(num, error_msg, is_error, expected_value):
    result = is_semi_prime(num)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
    # Happy cases
    ((1, 10), "", False, {2, 3, 5, 7}),
    ((10, 20), "", False, {11, 13, 17, 19}),

    # Error cases
    ((1, None), "Missing a range.", True, None),
    ((None, 100), "Missing a range.", True, None),
])
def test_gen_primes(args, error_msg, is_error, expected_value):
    result = gen_primes(*args)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
    # Happy cases
    ((1, 10), "", False, {4, 6, 9, 10}),
    ((20, 30), "", False, {21, 22, 25, 26}),

    # Error cases
    ((1, None), "Missing a range.", True, None),
    ((None, 12), "Missing a range.", True, None),
])
def test_gen_semi_primes(args, error_msg, is_error, expected_value):
    result = gen_semi_primes(*args)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

@pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
    # Happy cases
    ((2, 3, 4), "", False, 2.75),
    ((10, 0, 1), "", False, 10.0),

    # Error cases
    ((), "Missing a number.", True, None),
    ((1, 0, 0), "Denominator cannot be zero.", True, None),
])
def test_fraction_to_decimal(args, error_msg, is_error, expected_value):
    result = fraction_to_decimal(*args)
    if not is_error:
        assert result.is_ok()
        assert result.ok() == expected_value
    else:
        assert result.is_err()
        assert str(result.err()) == error_msg

# @pytest.mark.parametrize("num,error_msg,is_error,expected_value", [
#     # Happy cases
#     (0.6, "", False, "3 / 5"),
#     (5.0, "", False, "5 / 1"),

#     # Error cases
#     (None, "Input cannot be None.", True, None),
# ])
# def test_decimal_to_fraction(num, error_msg, is_error, expected_value):
#     result = decimal_to_fraction(num)
#     if not is_error:
#         assert result.is_ok()
#         assert str(result.ok()) == expected_value
#     else:
#         assert result.is_err()
#         assert str(result.err()) == error_msg

# @pytest.mark.parametrize("num,error_msg,is_error,expected_value", [
#     # Happy cases
#     (45, "", False, {3: 2, 5: 1}),
#     (60, "", False, {2: 2, 3: 1, 5: 1}),
#     (13, "", False, {13: 1}),
#     (1, "", False, {}),
# ])
# def test_factor(num, error_msg, is_error, expected_value):
#     result = factor(num)
#     if not is_error:
#         assert result.is_ok()
#         assert result.ok() == expected_value
#     else:
#         assert result.is_err()
#         assert str(result.err()) == error_msg

# @pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
#     # Happy cases
#     ((4, 6, 8), "", False, 24),
#     ((5, 10, 15), "", False, 30),
#     ((7, 3), "", False, 21),
# ])
# def test_lcm(args, error_msg, is_error, expected_value):
#     result = lcm(*args)
#     if not is_error:
#         assert result.is_ok()
#         assert result.ok() == expected_value
#     else:
#         assert result.is_err()
#         assert str(result.err()) == error_msg

# @pytest.mark.parametrize("args,error_msg,is_error,expected_value", [
#     # Happy cases
#     ((24, 36, 60), "", False, 12),
#     ((17, 13), "", False, 1),
#     ((8, 32, 24), "", False, 8),
# ])
# def test_gcd(args, error_msg, is_error, expected_value):
#     result = gcd(*args)
#     if not is_error:
#         assert result.is_ok()
#         assert result.unwrap() == expected_value
#     else:
#         assert result.is_err()
#         assert str(result.err()) == error_msg
# @pytest.mark.parametrize("num,error_msg,is_error,expected_value", [
#     # Happy cases
#     (0.6, "", False, "3 / 5"),
#     (5.0, "", False, "5 / 1"),
#     (1.25, "", False, "1 1 / 4"),

#     # Error cases
#     (None, "Input cannot be None.", True, None),
# ])
# def test_decimal_to_fraction(num, error_msg, is_error, expected_value):
#     result = decimal_to_fraction(num)
#     if not is_error:
#         assert result.is_ok()
#         assert str(result.ok()) == expected_value
#     else:
#         assert result.is_err()
#         assert str(result.err()) == error_msg