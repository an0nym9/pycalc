from pycalc.utils.console import readline, show_menu
from pycalc.utils.guards import handle_exception, enhance_params
from pycalc.utils.history import add_history

@handle_exception
@enhance_params
def factorial(n: int | None = None, /) -> int | ValueError:
    """Find the factorial of 'n'."""
    if n is None:
        raise ValueError("No number provided.")
    if n in (0, 1):
        return 1
    res = n
    for i in range(res-1, 1, -1):
        res *= i
    return res

@handle_exception
@enhance_params
def permutations(
    a: int | None = None,
    b: int | None = None,
    /,
) -> int | ValueError:
    """Find the permutations."""
    if any(n is None for n in (a, b,)):
        raise ValueError("Missing a number.")
    return factorial(a).unwrap() / factorial(a - b).unwrap()

@handle_exception
@enhance_params
def combinations(
    a: int | None = None,
    b: int | None = None,
    /,
) -> int | ValueError:
    """Find the combinations."""
    if any(n is None for n in (a, b,)):
        raise ValueError("Missing a number.")
    return factorial(a).unwrap() / (factorial(b).unwrap() * factorial(a - b).unwrap())

@handle_exception
def run_probability() -> None:
    """Runs the main loop."""
    options = ("factorial", "permutations", "combinations",)
    while (user_option := show_menu(
            "Probability",
            options + ("exit",),
            capitalize_options=True,
        ).unwrap()) != "exit":
        if user_option not in options:
            print("Unknown option, try again.")
            continue
        match user_option:
            case "factorial":
                num = readline("Enter the number:", cast=int).unwrap()
                if num < 0:
                    print("Cant factorial a negative number.")
                    continue
                result = factorial(num).unwrap()
            case "permutations" | "combinations":
                num1 = readline("Enter the first number:", cast=int).unwrap()
                num2 = readline("Enter the second number:", cast=int).unwrap()
                if num2 > num1:
                    print("A non-permisble value")
                    continue
                result = permutations(num1, num2).unwrap() if user_option == "permutations" else combinations(num1, num2).unwrap()
        add_history(str(result))
        print(f">> {result}")
        readline("Press enter to continue...", enter_only=True).unwrap()
