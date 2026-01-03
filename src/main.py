from utils.console import readline
from modules.basic import add, sub, mul, div

def main() -> None:
    """Runs the main loop."""
    options = ("add", "subtract", "multiply", "divide", "quit",)
    symbol = {
        "add": "+",
        "subtract": "-",
        "multiply": "*",
        "divide": "/",
    }
    while (
        [print(f"{i}. {option.capitalize()}") for i, option in enumerate(options, start=1)],
        user_option := input("\nSelect your option from above: ").strip(),
    )[-1].lower() not in ("quit", "exit",):
        if user_option.lower() not in options:
            print(f"Unknown option '{user_option}', try again.")
            continue
        num1 = readline("Enter the first number:", cast=float).unwrap("Failed to readline.")
        num2 = readline("Enter the second number:", cast=float).unwrap("Failed to readline.")
        match user_option.lower():
            case "add":
                res = add(num1, num2).unwrap_or(None)
            case "subtract":
                res = sub(num1, num2).unwrap_or(None)
            case "multiply":
                res = mul(num1, num2).unwrap_or(None)
            case "divide":
                res = div(num1, num2).unwrap_or(None)
        print(f"Results: {num1} {symbol.get(user_option.lower())} {num2} = {res}")

if __name__ == "__main__":
    main()