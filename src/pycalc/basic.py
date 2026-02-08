from pycalc.utils.console import readline, show_menu
from pycalc.utils.guards import handle_exception, enhance_params
from pycalc.utils.history import add_history

@handle_exception
@enhance_params
def sum(*args: tuple[float, ...],) -> float | ValueError:
    """Find the sum of two numbers."""
    if not args:
        raise ValueError("No numbers provided.")
    num = args[0]
    if len(args) != 1:
        for i in range(1, len(args)):
            num += args[i]
    return num

@handle_exception
@enhance_params
def difference(*args: tuple[float, ...],) -> float | ValueError:
    """Find the difference of two numbers."""
    if not args:
        raise ValueError("No numbers provided.")
    num = args[0]
    if len(args) != 1:
        for i in range(1, len(args)):
            num -= args[i]
    return num

@handle_exception
@enhance_params
def product(*args: tuple[float, ...],) -> float | ValueError:
    """Find the product of two numbers."""
    if not args:
        raise ValueError("No numbers provided.")
    num = args[0]
    if len(args) != 1:
        for i in range(1, len(args)):
            num *= args[i]
    return num

@handle_exception
@enhance_params
def qoutient(
    *args: tuple[float, ...],
    ignore_zero: bool = False
) -> float | ValueError  | ZeroDivisionError:
    """Find the quotient of two numbers."""
    if not args:
        raise ValueError("No numbers provided.")
    num = args[0]
    if num != 0 and len(args) != 1:
        for i in range(1, len(args)):
            if not ignore_zero and args[i] == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            num /= args[i if i != 0 else 1]
    return num

def run_basic():
    """Runs the main loop."""
    options = {
        "sum": ('+', sum),
        "difference": ('-', difference),
        "product": ('*', product),
        "quotient": ('/', qoutient),
    }
    while (user_option := show_menu(
            "Basic",
            tuple(options.keys()) +  ("exit",),
            capitalize_options=True,
        ).unwrap()) != "exit":
        if user_option not in options.keys():
            print("Unknown option, try again.")
            continue
        nums = []
        length = readline("How many number would you like:", cast=int).unwrap()
        while length > 0:
            nums.append(readline("Enter a number:", cast=float).unwrap())
            length -= 1
        option = options[user_option]
        res = option[1](*nums).unwrap()
        print(f">> {res}")
        add_history(str(res))
        readline("Press enter to continue...", enter_only=True).unwrap()
