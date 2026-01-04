from utils.console import readline
from modules.basic import add, sub, mul, div
from modules.number import is_prime, lcm, gcd

def main() -> None:
    """Runs the main loop."""
    options = (
        "add",
        "subtract",
        "multiply",
        "divide",
        "lcm",
        "gcd",
        "is prime",
        "quit",
    )
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
        if user_option.lower() in symbol.keys():
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
        else:
            match user_option.lower():
                case "lcm" | "gcd":
                    count = readline("How much number you like to add?", cast=int).unwrap("Failed to readline.")
                    arr = []
                    for _ in range(count):
                        arr.append(readline("Enter the number:", cast=int).unwrap("Failed to read line."))
                    res = lcm(*arr) if user_option.lower() == "lcm" else gcd(*arr)
                    print(f"{user_option.upper()} of {arr}: {res}")
                case "is prime":
                    num = readline("Enter a number:", cast=int).unwrap("Failed to readline.")
                    if is_prime(num):
                        print(f"{num} is a prime number.")
                    else:
                        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()
