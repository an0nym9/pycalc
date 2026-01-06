def factorial(n: int, /, *, stop: int = 1) -> int:
    """Find the factorial of 'n'."""
    res = n
    for i in range(res-1, stop - 1, -1):
        res *= i
    return res

def permutations(a: int, b: int, /) -> int:
    """Find the permutations."""
    return factorial(a) / factorial(a - b)

def combinations(a: int, b: int, /) -> int:
    """Find the combinations."""
    return factorial(a) / (factorial(b) * factorial(a - b))
