from pycalc.utils.console import clear_screen, readline, show_menu, animateText
from pycalc.utils.guards import handle_exception
from pycalc.utils.history import create_history, show_history
from pycalc.basic import run_basic
from pycalc.number import run_number
from pycalc.probability import run_probability

@handle_exception
def main() -> None:
    """Runs the main loop."""
    options = ("basic", "number", "probability", "history",)
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
            case "probability":
                run_probability()
            case "history":
                show_history()
        readline("Press enter to continue...", enter_only=True).unwrap()
    animateText("Exited successfully...")

if __name__ == "__main__":
    create_history()
    main().unwrap()
