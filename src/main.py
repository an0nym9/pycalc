from utils.console import clear_screen, readline
from modules.basic import add, sub, mul, div
from modules.number import is_prime, lcm, gcd, remain
from modules.probability import factorial, permutations

def main() -> None:
    """Runs the main loop."""
    options = {
        "basic": {
            "Addition": add,
            "Subtraction": sub,
            "Multiplication": mul,
            "Division": div,
        },
        "number": {
            "Is Prime": is_prime,
            "Least Common Multiple": lcm,
            "Greatest Common Divisitor": gcd,
            "Find Remainder": remain,
        },
        "probability": {
            "Factorial": factorial,
            "Permutations": permutations,
        },
    }
    option_keys = tuple(options.keys())
    while (
        clear_screen(),
        print("= PYCALC =\n"),
        [print(f"{i}. {option.capitalize()}") for i, option in enumerate(option_keys + ("quit",), start=1)],
        main_option := readline("\nEnter your selected option (number):", cast=int).unwrap("Something happened..."),
    )[-1] != len(option_keys) + 1:
        if not (1 <= main_option <= len(option_keys) + 1):
            print(f"Unknown option '{main_option}', try again.")
            continue
        selected_option = options[option_keys[main_option-1]]
        selected_option_keys = tuple(selected_option.keys())
        while (
            clear_screen(),
            print(f"= {option_keys[main_option-1].upper()} =\n"),
            [print(f"{i}. {option.capitalize()}") for i, option in enumerate(selected_option_keys + ("go back",), start=1)],
            user_option := readline("\nEnter your selected option (number):", cast=int).unwrap("Something happened..."),
        )[-1] != len(selected_option_keys) + 1:
            if not (1 <= user_option <= len(selected_option_keys) + 1):
                print(f"Unknown option '{user_option}', try again.")
                continue
            match option_keys[main_option-1], selected_option_keys[user_option-1]:
                case "basic", _:
                    num1 = readline("Enter the first number:", cast=float).unwrap("Something happend...")
                    num2 = readline("Enter the second number:", cast=float).unwrap("Something happend...")
                    res = selected_option[selected_option_keys[user_option-1]](num1, num2).unwrap("Something happend..")
                    print(f"Result: {res:.2f}")
                case "number", "Is Prime":
                    num = readline("Enter the number:", cast=int).unwrap("Something happened...")
                    if is_prime(num):
                        print(f"{num} is a prime number.")
                    else:
                        print(f"{num} is not a prime number.")
                case "number", "Least Common Multiple" | "Greatest Common Divisitor":
                    count = readline("How many number would you like to add?", cast=int).unwrap("Something happend...")
                    nums = []
                    [nums.append(readline("Enter the number:", cast=int).unwrap("Something happend...")) for _ in range(count)]
                    if selected_option_keys[user_option-1] == "Least Common Multiple":
                        print(f"LCM: {lcm(*nums)}")
                    else:
                        print(f"GCD: {gcd(*nums)}")
                case "number", "Find Remainder":
                    num1 = readline("Enter the first number:", cast=float).unwrap("Something happend...")
                    num2 = readline("Enter the second number:", cast=float).unwrap("Something happend...")
                    print(f"Remainder of {num1} / {num2} is {remain(num1, num2)}")
                case "probability", "Factorial":
                    num = readline("Enter the number:", cast=int).unwrap("Something happend...")
                    print(f"Factorial of {num} is {factorial(num)}")
                case "probability", "Permutations":
                    num1 = readline("Enter the first number:", cast=int).unwrap("Something happend...")
                    num2 = readline("Enter the second number:", cast=int).unwrap("Something happend...")
                    print(f"Permutations: {permutations(num1, num2)}")
            readline("Press enter to continue...", enter_only=True)
        print("Returning to main menu...")
    print("Successfully Exited...")

if __name__ == "__main__":
    main()
