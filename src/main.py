from utils.console import clear_screen, readline, show_menu
from modules.basic import add, sub, mul, div
from modules.number import is_prime, gen_primes, lcm, gcd, remain, factor
from modules.probability import factorial, permutations, combinations

def main() -> None:
    """Runs the main loop."""
    options = {
        "Basic": {
            "Addition": add,
            "Subtraction": sub,
            "Multiplication": mul,
            "Division": div,
        },
        "Number": {
            "Is Prime": is_prime,
            "Generate Prime Sequence": gen_primes,
            "Least Common Multiple": lcm,
            "Greatest Common Divisitor": gcd,
            "Find Remainder": remain,
            "Factor": factor,
        },
        "Probability": {
            "Factorial": factorial,
            "Permutations": permutations,
            "Combinations": combinations,
        },
    }
    option_keys = tuple(options.keys())
    while (
        clear_screen(),
        show_menu("PYCALC", option_keys + ("Exit",)),
        main_option := readline("\nEnter your selected option (number):", cast=int).unwrap("Something happened..."),
    )[-1] != len(option_keys) + 1:
        if not (1 <= main_option <= len(option_keys)):
            print(f"Unknown option '{main_option}', try again.")
            continue
        selected_option = options[option_keys[main_option-1]]
        selected_option_keys = tuple(selected_option.keys())
        while (
            clear_screen(),
            show_menu(option_keys[main_option-1], selected_option_keys + ("Go Back",)),
            user_option := readline("\nEnter your selected option (number):", cast=int).unwrap("Something happened..."),
        )[-1] != len(selected_option_keys) + 1:
            if not (1 <= user_option <= len(selected_option_keys) + 1):
                print(f"Unknown option '{user_option}', try again.")
                continue
            match option_keys[main_option-1], selected_option_keys[user_option-1]:
                case "Basic", _:
                    num1 = readline("Enter the first number:", cast=float).unwrap("Something happend...")
                    num2 = readline("Enter the second number:", cast=float).unwrap("Something happend...")
                    res = selected_option[selected_option_keys[user_option-1]](num1, num2).unwrap("Something happend..")
                    print(f"Result: {res:.2f}")
                case "Number", "Is Prime":
                    num = readline("Enter the number:", cast=int).unwrap("Something happened...")
                    if is_prime(num):
                        print(f"{num} is a prime number.")
                    else:
                        print(f"{num} is not a prime number.")
                case "Number", "Generate Prime Sequence":
                    num1 = readline("Enter the minimum:", cast=int).unwrap("Something happend...")
                    num2 = readline("Etner the maximum:", cast=int).unwrap("Something happend...")
                    print(f"Prime Numbers in that range: {gen_primes(num1, num2)}")
                case "Number", "Least Common Multiple" | "Greatest Common Divisitor":
                    count = readline("How many number would you like to add?", cast=int).unwrap("Something happend...")
                    nums = []
                    [nums.append(readline("Enter the number:", cast=int).unwrap("Something happend...")) for _ in range(count)]
                    if selected_option_keys[user_option-1] == "Least Common Multiple":
                        print(f"LCM: {lcm(*nums)}")
                    else:
                        print(f"GCD: {gcd(*nums)}")
                case "Number", "Find Remainder":
                    num1 = readline("Enter the first number:", cast=float).unwrap("Something happend...")
                    num2 = readline("Enter the second number:", cast=float).unwrap("Something happend...")
                    print(f"Remainder of {num1} / {num2} is {remain(num1, num2)}")
                case "Number", "Factor":
                    num = readline("Enter the number", cast=int).unwrap("Something happend...")
                    print(f"Prime Factorization of {num} is {factor(num)}")
                case "Probability", "Factorial":
                    num = readline("Enter the number:", cast=int).unwrap("Something happend...")
                    print(f"Factorial of {num} is {factorial(num)}")
                case "Probability", "Permutations" | "Combinations":
                    num1 = readline("Enter the first number:", cast=int).unwrap("Something happend...")
                    num2 = readline("Enter the second number:", cast=int).unwrap("Something happend...")
                    if selected_option_keys[user_option-1] == "Permutations":
                        print(f"Permutations: {permutations(num1, num2)}")
                    else:
                        print(f"Combinations: {combinations(num1, num2)}")
            readline("Press enter to continue...", enter_only=True)
        print("Returning to main menu...")
    print("Successfully Exited...")

if __name__ == "__main__":
    main()
