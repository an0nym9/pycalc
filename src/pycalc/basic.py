from pycalc.utils.console import clear_screen, readline, show_menu
from pycalc.utils.guards import handle_exception, enhance_params
# from pycalc.utils.history import add_history

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
    while (
        clear_screen(),
        show_menu("Basic", (option_keys := tuple(options.keys())) + ("exit",), capitalize_options=True),
        user_option := readline("Enter your option (number):", cast=int).unwrap(),
    )[-1] != len(options) + 1:
        if not (1 <= user_option <= len(options)):
            print("Unknown option, try again.")
            continue
        nums = []
        length = readline("How many number would you like:", cast=int).unwrap()
        while length > 0:
            nums.append(readline("Enter a number:", cast=float).unwrap())
            length -= 1
        option = options[option_keys[user_option-1]]
        res = option[1](*nums).unwrap()
        print(f">> {res}")
        # add_history({
        #     "Category": "Basic",
        #     "Type": option_keys[user_option-1].capitalize(),
        #     "Args": nums,
        #     "Result": res,
        # })
        readline("Press enter to continue...", enter_only=True).unwrap()
