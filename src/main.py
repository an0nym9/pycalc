from utils.console import clear_screen, readline, show_menu, animateText
from utils.history import create_history, show_history
from modules.basic import run_basic
from modules.number import run_number
from modules.probability import run_probability

def main() -> None:
    """Runs the main loop."""
    options = ("basic", "number", "probability", "history",)
    while (
        clear_screen(),
        show_menu("Pycalc", options + ("exit",), capitalize_options=True),
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
    main()
