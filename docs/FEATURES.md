# Features

Here is a more detailed explanation of each feature **Pycalc** currently supports.

> [!NOTE]
> The output below comes from the actual functions in the program.

### Basic Arithmetic

Pycalc allows you to do basic arithmetic like addition, subtraction, multiplication, and division. It also allows you to add multiple numbers for each not just two. For example:

```python
# Calculating the product of 23, 43, 87, and 45
nums = (23, 34, 87, 45,)
result = product(*nums).unwrap()
print(result) # 2881440
```

### Prime / Semi Prime Checker

Pycalc supports prime and semi prime numbers, with this feature you can check wether a number is prime or semi prime. Here is an example.

```python
num = 23
if is_prime(num).unwrap():
    print(f"{num} is a prime number.") # it will print this since 23 is a prime number
elif is_semi_prime(num).unwrap():
    print(f"{num} is a semi prime number.")
else:
    print(f"{num} is neither a prime nor a semi prime number.")
```

### Generate Prime / Semi Prime Sequence

Pycalc not only support whether a number is prime or semi prime, it also is able to generate a sequence of prime or semi prime numbers with a given min and max range. Here is an example.

```python
min_r = 1
max_r = 10
print(f"Primes: {gen_primes(min_r, max_r).unwrap()}") # {2, 3, 5, 7, 9}
print(f"Semi-primes: {gen_semi_primes(min_r, max_r).unwrap()}") # {4, 6, 9, 10}
```
### Fraction to Decimal

Pycalc also supports Fraction to Decimal conversion, this is not too complicated since we only need to multiply the whole number by the denominator and add it to the numerator and divide it to the denominator. Here is an example:

```python
whole_number = 1
numerator = 10
denominator = 12
print(f"Decimal: {fraction_to_decimal(whole_number, numerator, denominator).unwrap()}") # 1.8333...
```

### Decimal to Fraction

Pycalc also supports decimal to fraction conversions. Last time it was fraction to decimal now vice versa. This allows the user to convert decimals back to fractions which is useful when the decimal is very large but it may take a while depending on the size of the decimal. Here is an example:

```python
f = 1.6532
print(f"Fraction: {decimal_to_fraction(f).unwrap()}") # 1 1633 / 2500
```

### Factor

This function allows you to factor a whole number into smaller pieces, sadly it doesn't support polynomial functions but it may be added in future updates. Here is an example:

```python
num = 32
print(f"Factor 32: {factor(num).unwrap()}") # {2: 5} is equivalent to 2 * 2 * 2 * 2 * 2
```

### Least Common Multitple

This feature allows you to find the least common multiple easier, it also allows you to calculate the LCM of multiple numbers at once, though larger number or numbers added may take a while depending on the size. Here is an example:

```python
nums = (12, 43, 6, 8, 21,)
print(f"LCM of {nums}: {lcm(*nums).unwrap()}") # 7224
```

### Greatest Common Divisitor

Pycalc is also capable of calculating the greatest common divisitor not just two but multiple numbers but, too large numbers or number count may take a while. Here is an example:

```python
nums = (12, 4, 8, 2,)
print(f"GCD of {nums}: {gcd(*nums).unwrap()}) # 2
```

### Get Remainder

Pycalc also supports remainders. Though this can be done by n % m, it is also be useful for some cases. Here is an example:

```python
num1 = 52
num2 = 321
print(f"Remainder: {remain(num1, num2).unwrap()}") # 52
```

### Proper Fraction

Unlike the decimal to fraction conversions, this turns a fraction into proper fraction, this can be useful when your checking if a fraction is proper or not. Here is an example:

```python
whole_number = 1
numerator = 324
denominator = 61
print(f"Proper Fraction: {proper_fraction(whole_number, numerator, denominator).unwrap()}")
```

### Get Numerator / Denominator

This simple feature allows you to get the numerator or denominator from a fraction. Here is an example:

```python
whole_number = 0
numerator = 31
denominator = 43
fraction = Fraction(whole_number, numerator, denominator)
print(f"Numerator: {fraction.get_numerator()}") # 31
print(f"Denominator: {fraction.get_denominator()}") # 43
```

### Factorial

This feature allows you to find the factorial of any number, though this version only support single whole numbers not expressions, future updates may implement this feature. Here is an example:

```python
n = 5
print(f"Factorial of {n}: {factorial(n).unwrap()}") # 120
```

### Permutations

This allows you to calculate the permutations when order matters. Here is an example:

```python
n = 12
r = 3
print(f"Permutations: {permutations(n, r).unwrap()}") # 1320
```

### Combinations

This allows you to calculate the combinations when order doesn't matter. Here is an example:

```python
n = 34
r = 12
print(f"Combinations: {combinations(n, r).unwrap()}") # 225792840
```
