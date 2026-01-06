def is_prime(n: int, /) -> bool:
    """Checks if the given number is prime."""
    if n < 2:
        return False
    for i in range(2, n+1, ):
        if n % i == 0 and n != i:
            return False
    return True

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
