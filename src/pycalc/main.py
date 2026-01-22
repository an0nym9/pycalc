import ast
import sys

from pycalc.utils.console import clear_screen, readline, show_menu, animateText
from pycalc.utils.guards import handle_exception
# from pycalc.utils.history import create_history, show_history
from pycalc.basic import run_basic
from pycalc.number import run_number
from pycalc.algebra import run_algebra
from pycalc.parser import eval_expr
from pycalc.probability import run_probability

@handle_exception
def main() -> None:
    """Runs the main loop."""
    options = ("basic", "number", "algebra", "probability",)
    while (
        clear_screen(),
        show_menu("Pycalc", options + ("exit",), capitalize_options=True).unwrap(),
        user_option := readline("Enter your option (number):", cast=int).unwrap(),
    )[-1] != len(options) + 1:
        if not (1 <= user_option <= len(options)):
            print("Unknown option, try again.")
            continue
        match options[user_option-1]:
            case "basic":
                run_basic()
            case "number":
                run_number()
            case "algebra":
                run_algebra()
            case "probability":
                run_probability()
            # case "history":
            #     show_history()
        readline("Press enter to continue...", enter_only=True).unwrap()
    animateText("Exited successfully...")

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) >= 1:
        if args[0] == "-tui":
            main().unwrap()
        elif args[0] == "-quick":
            while clear_screen() or (expr := readline(">>>").unwrap().strip()) != "exit":
                tree = ast.parse(expr, mode="eval")
                res = eval_expr(tree.body)
                print(f" > {res}")
                readline("Press enter to continue...", enter_only=True).unwrap()
        elif args[0] in ("-V", "-version",):
            print("Pycalc version 0.0.5")
        else:
            print(f"Unknown argument, {args[0]}.")
    else:
        print(f"Expecting at least one argument, got {len(args)}.")
