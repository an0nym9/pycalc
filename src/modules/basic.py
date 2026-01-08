from utils.console import clear_screen, readline, show_menu
from utils.history import add_history

def add(a: float, b: float, /) -> float:
    """Find the sum of two numbers."""
    return a + b

def sub(a: float, b: float, /) -> float:
    """Find the difference of two numbers."""
    return a - b

def mul(a: float, b: float, /) -> float:
    """Find the product of two numbers."""
    return a * b

def div(a: float, b: float, /) -> float:
    """Find the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def run_basic():
    """Runs the main loop."""
    options = {
        "addition": ('+', add),
        "subtraction": ('-', sub),
        "multiplication": ('*', mul),
        "division": ('/', div),
    }
    while (
        clear_screen(),
        show_menu("Basic", (option_keys := tuple(options.keys())) + ("exit",), capitalize_options=True),
        user_option := readline("Enter your option (number):", cast=int).unwrap(),
    )[-1] != len(options) + 1:
        if not (1 <= user_option <= len(options)):
            continue
        num1 = readline("Enter the first number:", cast=float).unwrap()
        num2 = readline("Enter the second number:", cast=float).unwrap()
        option = options[option_keys[user_option-1]]
        res = f"{num1} {option[0]} {num2} = {option[1](num1, num2)}"
        add_history(res)
