from utils.guards import handle_exception

@handle_exception
def add(a: float, b: float, /) -> float:
    """Find the sum of two numbers."""
    return a + b

@handle_exception
def sub(a: float, b: float, /) -> float:
    """Find the difference of two numbers."""
    return a - b

@handle_exception
def mul(a: float, b: float, /) -> float:
    """Find the product of two numbers."""
    return a * b

@handle_exception
def div(a: float, b: float, /) -> float:
    """Find the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
