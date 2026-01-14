from pycalc.utils.console import clear_screen, show_menu, readline
from pycalc.utils.guards import handle_exception, enhance_params
from pycalc.utils.history import add_history

class Fraction:
    def __init__(
        self,
        whole_number: int,
        numerator: int,
        denominator: int,
        /,
    ) -> None | ValueError:
        """Initialize a Fraction object."""
        self.whole_number = whole_number
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        """Returns the fraction as a string."""
        return (
            f"{self.numerator} / {self.denominator}"
            if not self.whole_number else
            f"{self.whole_number} {f"{self.numerator} / {self.denominator}" if self.numerator != 0 else ''}"
        )

    def get_numerator(self) -> int:
        """Return the numerator of the fraction."""
        return self.numerator

    def get_denominator(self) -> int:
        """Returns the denominator of the fraction."""
        return self.denominator

@handle_exception
@enhance_params
def is_prime(n: int, /) -> bool:
    """Checks if the given number is prime."""
    if n < 2:
        return False
    for i in range(2, n+1, ):
        if n % i == 0 and n != i:
            return False
    return True

@handle_exception
@enhance_params
def gen_primes(min: int, max: int, /) -> set:
    """Generates a sequence of prime numbers."""
    if min > max:
        return set()
    primes = set()
    for num in range(min, max + 1):
        if is_prime(num):
            primes.add(num)
    return primes

@handle_exception
@enhance_params
def gen_semi_primes(min: int, max: int, /) -> set:
    """Generates a sequence of semi prime numbers."""
    if min > max:
        return set()
    semi_primes = set()
    for i in range(min, max+1):
        for j in range(i, max+1):
            num = i * j
            if num > max:
                break
            if is_prime(i) and is_prime(j):
                semi_primes.add(num)
    return semi_primes

@handle_exception
@enhance_params
def is_semi_prime(n: int, /) -> bool:
    """Checks if the given number is a semi prime number."""
    if n < 4:
        return False
    return n in gen_semi_primes(2, n).unwrap()

@handle_exception
@enhance_params
def fraction_to_decimal(
    whole_number: int,
    numerator: int,
    denominator: int,
    /,
) -> float | ValueError:
    """Convert into a decimal."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return (whole_number * denominator +  numerator) / denominator

@handle_exception
@enhance_params
def decimal_to_fraction(d: float, /) -> None:
    """Approximate to a fraction."""
    power = 10 ** len(str(d).split('.')[-1])
    num = d * power
    divisible = set()
    for n in range(2, int(num) + 1):
        if num % n == 0 and (10 ** power) % n == 0:
            divisible.add(n)
    whole_number = 0
    numerator = num / max(divisible) if divisible else num
    denominator = power / max (divisible) if divisible else power
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    if numerator > denominator:
        whole_number = numerator // denominator
        numerator = numerator % denominator
    return Fraction(*tuple(map(int, (whole_number, numerator, denominator))))

@handle_exception
@enhance_params
def factor(n: int, /) -> dict:
    """Factor the given number."""
    num = n
    factors = {}
    while num > 1:
        for i in range(2, n + 1):
            if is_prime(i) and num % i == 0:
                num /= i
                factors[i] = factors.get(i, 0) + 1
    return factors

@handle_exception
@enhance_params
def lcm(*args,) -> int:
    """Find the Least Common Multiple."""
    nums = list(args)
    while True:
        for i in range(len(nums)):
            if len(set(nums)) == 1:
                return nums[i]
            if nums[i] >= max(nums):
                continue
            nums[i] += args[i]

@handle_exception
@enhance_params
def gcd(*args,) -> int:
    """Find the Greatest Common Divisitor."""
    cd = [1,]
    for i in range(2, max(args)):
        for n in args:
            if n % i != 0:
                break
        else:
            cd.append(i)
    return max(cd)

@handle_exception
@enhance_params
def remain(a: int, b: int, /) -> int | ValueError:
    """Find the remainder of a / b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b

@handle_exception
def run_fraction_tools() -> None:
    """Runs fraction tools section."""
    options = ("proper fraction", "get numerator", "get denominator",)
    while (
         clear_screen(),
         show_menu("Factorial Tools", options + ("exit",), capitalize_options=True),
         user_option := readline("Enter your option (number):", cast=int).unwrap(),
    )[-1] != len(options) + 1:
        if not (1 <= user_option <= len(options)):
            print("Unknown option, try again.")
            continue
        whole_number = readline("Enter the whole number:", cast=int).unwrap()
        numerator = readline("Enter the numerator:", cast=int).unwrap()
        denominator = readline("Enter the denominator:", cast=int).unwrap()
        if denominator == 0:
            print("Denominator cannot be zero, try again.")
            continue
        match (option := options[user_option-1]):
            case "proper fraction":
                if numerator < denominator:
                    print(f"{f"{whole_number} " if whole_number > 0 else ''}{numerator} / {denominator}")
                    continue
                new_whole_number = (numerator // denominator) + whole_number
                new_numerator = numerator % denominator
                result = f"{new_whole_number if new_whole_number != 0 else ''} {f"{new_numerator} / {denominator}" if new_numerator != 0 else ''}"
            case "get numerator" | "get denominator":
                fraction = Fraction(whole_number, numerator, denominator)
                result = fraction.get_numerator() if option == "get numerator" else fraction.get_denominator()
        add_history({
            "Category": "Number - Fraction Tools",
            "Type": option.capitalize(),
            "Args": {
                "Whole Number": whole_number,
                "Numerator": numerator,
                "Denominator": denominator,
            },
            "Results": result,
        })
        print(f">> {result}")
        readline("Press enter to continue...", enter_only=True).unwrap()

def run_number():
    """Runs the main loop."""
    options = (
        "check prime", "check semi prime",
        "generate prime sequence", "generate semi prime sequence",
        "fraction to decimal", "decimal to fraction",
        "factor", "least common multiple",
        "greatest common divisitor", "get remainder",
        "fraction tools",
    )
    while (
         clear_screen(),
         show_menu("Number", options + ("exit",), capitalize_options=True),
         user_option := readline("Enter your option (number):", cast=int).unwrap(),
    )[-1] != len(options) + 1:
        if not (1 <= user_option <= len(options)):
            print("Unknown option, try again.")
            continue
        match (option := options[user_option-1]):
            case "check prime" | "check semi prime":
                num = readline("Enter the number:", cast=int).unwrap()
                if num < 0:
                    print("Cannot be negative.")
                    continue
                result = is_prime(num).unwrap() if option == "check prime" else is_semi_prime(num).unwrap()
                add_history({
                    "Category": "Number",
                    "Type": option.capitalize(),
                    "Arg": num,
                    "Result": result,
                })
            case "generate prime sequence" | "generate semi prime sequence":
                minimum = readline("Enter the minimum:", cast=int).unwrap()
                maximum = readline("Enter the maximum:", cast=int).unwrap()
                if maximum < minimum:
                    print("Maximum cannot be smaller than minimum.")
                    continue
                result = gen_primes(minimum, maximum).unwrap() if option == "generate prime sequence" else gen_semi_primes(minimum, maximum).unwrap()
                add_history({
                    "Category": "Number",
                    "Type": option.capitalize(),
                    "Args": {
                        "Minimum": minimum,
                        "Maximum": maximum,
                    },
                    "Result": list(result),
                })
            case "fractiont to decimal":
                num1 = readline("Enter the whole number:", cast=int).unwrap()
                num2 = readline("Enter the numerator:", cast=int).unwrap()
                num3 = readline("Enter the denominator:", cast=int).unwrap()
                if num2 == 0:
                    print("Denominator cannot be zero.")
                    continue
                result = fraction_to_decimal(num1, num2).unwrap()
                add_history({
                    "Category": "Number",
                    "Type": option.capitalize(),
                    "Args": {
                        "Whole Number": num1,
                        "Numerator": num2,
                        "Denominator": num3,
                    },
                    "Result": result,
                })
            case "decimal to fraction":
                num = readline("Enter a decimal:", cast=float).unwrap()
                result = decimal_to_fraction(num).unwrap()
                add_history({
                    "Category": "Number",
                    "Type": option.capitalize(),
                    "Args": num,
                    "Result": str(result),
                })
            case "factor":
                num = readline("Enter the number:", cast=int).unwrap()
                if num < 0:
                    print("Dont support negative numbers.")
                    continue
                result = factor(num).unwrap()
                add_history({
                    "Category": "Number",
                    "Type": option.capitalize(),
                    "Arg": num,
                    "Result": result,
                })
            case "least common multiple" | "greatest common divisitor":
                length = readline("How many number would you like to add?", cast=int).unwrap()
                if length < 0:
                    print("Cannot be negative.")
                    continue
                nums = set()
                for num in range(length):
                    nums.add(readline("Enter the number:", cast=int).unwrap())
                result = lcm(*nums).unwrap() if option == "least common multiple" else gcd(*nums).unwrap()
                add_history({
                    "Category": "Number",
                    "Type": option.capitalize(),
                    "Args": nums,
                    "Result": list(result),
                })
            case "get remainder":
                num1 = readline("Enter the first number:", cast=int).unwrap()
                num2 = readline("Enter the second number:", cast=int).unwrap()
                result = remain(num1, num2).unwrap()
                add_history({
                    "Category": "Number",
                    "Type": option.capitalize(),
                    "Args": [num1, num2],
                    "Results": result,
                })
            case "fraction tools":
                run_fraction_tools()
        print(f">> {result}")
        readline("Press enter to continue...", enter_only=True).unwrap()
