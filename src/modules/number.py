def is_prime(n: int) -> bool:
    """Checks if the given number is prime."""
    if n <= 2:
        return False
    for i in range(2, n+1):
        if i % 2 == 0:
            continue
        if i >= n:
            return True
    return False

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
        div = True
        for n in args:
            if n % i != 0:
                div = False
                break
        if div:
            cd.append(i)
    return max(cd)
