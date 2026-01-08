from utils.console import clear_screen, show_menu, readline
from utils.history import add_history

def is_prime(n: int, /) -> bool:
    """Checks if the given number is prime."""
    if n < 2:
        return False
    for i in range(2, n+1, ):
        if n % i == 0 and n != i:
            return False
    return True

def gen_primes(min: int, max: int, /) -> set:
    """Generates a sequence of prime numbers."""
    if min > max:
        return set()
    primes = set()
    for num in range(min, max + 1):
        if is_prime(num):
            primes.add(num)
    return primes

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

def is_semi_prime(n: int, /) -> bool:
    if n < 4:
        return False
    return n in gen_semi_primes(2, n)

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

def remain(a: int, b: int, /) -> int:
    """Find the remainder of a / b."""
    return a % b

def run_number():
    """Runs the main loop."""
    options = (
        "check prime", "check semi prime",
        "generate prime sequence", "generate semi prime sequence",
        "factor", "least common multiple",
        "greatest common divisitor", "get remainder",
    )
    while (
         clear_screen(),
         show_menu("Number", options + ("exit",), capitalize_options=True),
         user_option := readline("Enter your option (number):", cast=int).unwrap(),
    )[-1] != len(options) + 1:
        if not (1 <= user_option <= len(options)):
            continue
        match (option := options[user_option-1]):
            case "check prime" | "check semi prime":
                num = readline("Enter the number:", cast=int).unwrap()
                if num < 0:
                    print("Cannot be negative.")
                    continue
                if option == "check prime":
                    res = f"{num} is {"a" if is_prime(num) else "not a"} prime number."
                else:
                    res = f"{num} is {"a" if is_semi_prime(num) else "not a"} semi prime number."
                add_history(res)
            case "generate prime sequence" | "generate semi prime sequence":
                minimum = readline("Enter the minimum:", cast=int).unwrap()
                maximum = readline("Enter the maximum:", cast=int).unwrap()
                if maximum < minimum:
                    print("Maximum cannot be smaller than minimum.")
                    continue
                if option == "generate prime sequence":
                    res = f"Prime numbers within that range: {gen_primes(minimum, maximum)}"
                else:
                    res = f"Semi prime numbers within that range: {gen_semi_primes(minimum, maximum)}"
                add_history(res)
            case "factor":
                num = readline("Enter the number:", cast=int).unwrap()
                if num < 0:
                    print("Dont support negative numbers.")
                    continue
                res = f"Factors of {num} are {factor(num)}"
                add_history(res)
            case "least common multiple" | "greatest common divisitor":
                length = readline("How many number would you like to add?", cast=int).unwrap()
                if length < 0:
                    print("Cannot be negative.")
                    continue
                nums = set()
                for num in range(length):
                    nums.add(readline("Enter the number:", cast=int).unwrap())
                if option == "least common multiple":
                    res = f"LCM: {lcm(*nums)}"
                else:
                    res = f"GCD: {gcd(*nums)}"
                add_history(res)
