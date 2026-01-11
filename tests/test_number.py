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

def test_is_prime() -> None:
    assert is_prime(2)

def test_is_semi_prime() -> None:
    assert is_semi_prime(4)

def test_gen_primes() -> None:
    assert gen_primes(1, 10).unwrap() == {2, 3, 5, 7}

def test_gen_semi_primes() -> None:
    assert gen_semi_primes(1, 10).unwrap() == {4, 6, 9, 10}

def test_fraction_to_decimal() -> None:
    assert fraction_to_decimal(2, 3, 4).unwrap() == 2.75

def test_decimal_to_fraction() -> None:
    assert str(decimal_to_fraction(0.6).unwrap()) == "3 / 5"

def test_factor() -> None:
    assert factor(45).unwrap() == {3: 2, 5: 1}

def test_lcm() -> None:
    assert lcm(4, 6, 8).unwrap() == 24

def test_gcd() -> None:
    assert gcd(24, 36, 60).unwrap() == 12

def test_remain() -> None:
    assert remain(17, 5).unwrap() == 2