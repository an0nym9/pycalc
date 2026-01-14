from pycalc.utils.console import clear_screen, readline, show_menu
from pycalc.utils.guards import handle_exception, enhance_params
from pycalc.utils.history import add_history

@handle_exception
@enhance_params
def factorial(n: int, /) -> int:
    """Find the factorial of 'n'."""
    if n in (0, 1):
        return 1
    res = n
    for i in range(res-1, 1, -1):
        res *= i
    return res

@handle_exception
@enhance_params
def permutations(a: int, b: int, /) -> int:
    """Find the permutations."""
    return factorial(a).unwrap() / factorial(a - b).unwrap()

@handle_exception
@enhance_params
def combinations(a: int, b: int, /) -> int:
    """Find the combinations."""
    return factorial(a).unwrap() / (factorial(b).unwrap() * factorial(a - b).unwrap())

@handle_exception
def run_probability() -> None:
    """Runs the main loop."""
    options = ("factorial", "permutations", "combinations",)
    while (
        clear_screen(),
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
                result = factorial(num).unwrap()
                add_history({
                    "Category": "Probability",
                    "Type": option.capitalize(),
                    "Arg": num,
                    "Result": result,
                })
            case "permutations" | "combinations":
                num1 = readline("Enter the first number:", cast=int).unwrap()
                num2 = readline("Enter the second number:", cast=int).unwrap()
                if num2 > num1:
                    print("A non-permisble value")
                    continue
                result = permutations(num1, num2).unwrap() if option == "permutations" else combinations(num1, num2).unwrap()
                add_history({
                    "Category": "Probability",
                    "Type": option.capitalize(),
                    "Args": [num1, num2],
                    "Result": result,
                })
        print(f">> {result}")
        readline("Press enter to continue...", enter_only=True).unwrap()
