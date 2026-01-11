from pycalc.probability import factorial, permutations, combinations # type: ignore

def test_factorial() -> None:
    assert factorial(5).unwrap() == 120

def test_permutations() -> None:
    assert permutations(4, 2).unwrap() == 12

def test_combinations() -> None:
    assert combinations(5, 3).unwrap() == 10
