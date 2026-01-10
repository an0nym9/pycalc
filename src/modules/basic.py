from utils.console import clear_screen, readline, show_menu
from utils.guards import handle_exception, enhance_params
from utils.history import add_history

@handle_exception
@enhance_params
def sum(*args: tuple[int, ...],) -> int | float:
    """Find the sum of two numbers."""
    num = args[0]
    if len(args) != 1:
        for i in range(1, len(args)):
            num += args[i]
    return num

@handle_exception
@enhance_params
def difference(*args: tuple[int, ...],) -> int | float:
    """Find the difference of two numbers."""
    num = args[0]
    if len(args) != 1:
        for i in range(1, len(args)):
            num -= args[i]
    return num

@handle_exception
@enhance_params
def product(*args: tuple[int, ...],) -> int | float:
    """Find the product of two numbers."""
    num = args[0]
    if len(args) != 1:
        for i in range(1, len(args)):
            num *= args[i]
    return

@handle_exception
@enhance_params
def qoutient(*args: tuple[int, ...],) -> float | ValueError:
    """Find the quotient of two numbers."""
    if args[-1] == 0:
        raise ValueError("Cannot divide by zero.")
    num = args[0]
    if len(args) != 1:
        for i in range(1, len(args)):
            num /= args[i]
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
        length = readline("How much number would you like:", cast=int).unwrap()
        while length > 0:
            nums.append(readline("Enter a number:", cast=float).unwrap())
            length -= 1
        option = options[option_keys[user_option-1]]
        res = f"Results: {option[1](*nums)}"
        add_history(res)
        readline("Press enter to continue...", enter_only=True).unwrap()
