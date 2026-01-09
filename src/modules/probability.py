from utils.console import readline, show_menu
from utils.guards import handle_exception, enhance_params
from utils.history import add_history

@handle_exception
@enhance_params
def factorial(n: int, /, *, stop: int = 1) -> int:
    """Find the factorial of 'n'."""
    if n in (0, 1):
        return 1
    res = n
    for i in range(res-1, stop - 1, -1):
        res *= i
    return res

@handle_exception
@enhance_params
def permutations(a: int, b: int, /) -> int:
    """Find the permutations."""
    return factorial(a) / factorial(a - b)

@handle_exception
@enhance_params
def combinations(a: int, b: int, /) -> int:
    """Find the combinations."""
    return factorial(a) / (factorial(b) * factorial(a - b))

def run_probability() -> None:
    """Runs the main loop."""
    options = ("factorial", "permutations", "combinations",)
    while (
        show_menu("Probability", options + ("exit",), capitalize_options=True),
        user_option := readline("Enter your selected option (number):", cast=int).unwrap()
    )[-1] != len(options) + 1:
        if not (1 <= user_option <= len(options)):
            print("Unknown option, try again.")
            continue
        match (option := options[user_option-1]):
            case "factorial":
                num = readline("Enter the number:", cast=int).unwrap()
                if num < 0:
                    print("Cant factorial a negative number.")
                    continue
                res = f"Factorial of {num} is {factorial(num)}"
                add_history(res)
            case "permutations" | "combinations":
                num1 = readline("Enter the first number:", cast=int).unwrap()
                num2 = readline("Enter the second number:", cast=int).unwrap()
                if num2 > num1:
                    print("A non-permisble value")
                    continue
                if option == "permutations":
                    res = f"Permutations of {num1} and {num2}: {permutations(num1, num2)}"
                else:
                    res = f"Combinations of {num1} and {num2}: {combinations(num1, num2)}"
                add_history(res)
        readline("Press enter to continue...", enter_only=True).unwrap()
