# Features

Here is a detailed explanation of each feature **Pycalc** currently supports.

> [!NOTE]
> The output below comes from the actual functions in the program.

---

### Basic Arithmetic

Pycalc allows basic arithmetic operations such as addition, subtraction, multiplication, and division. You can also perform these operations on multiple numbers at once. For example:

```python
# Calculating the product of 23, 34, 87, and 45
nums = (23, 34, 87, 45)
result = product(*nums).unwrap()
print(result)  # 3061530
```

---

### Prime / Semi-Prime Checker

Pycalc can check whether a number is prime or semi-prime. For example:

```python
num = 23
if is_prime(num).unwrap():
    print(f"{num} is a prime number.")  # 23 is prime
elif is_semi_prime(num).unwrap():
    print(f"{num} is a semi-prime number.")
else:
    print(f"{num} is neither a prime nor a semi-prime number.")
```

---

### Generate Prime / Semi-Prime Sequence

You can generate sequences of prime or semi-prime numbers within a specified range. For example:

```python
min_r = 1
max_r = 10
print(f"Primes: {gen_primes(min_r, max_r).unwrap()}")        # {2, 3, 5, 7}
print(f"Semi-primes: {gen_semi_primes(min_r, max_r).unwrap()}")  # {4, 6, 9, 10}
```

---

### Fraction to Decimal

Convert fractions to decimals. Pycalc calculates this by combining the whole number and fraction, then dividing by the denominator. Example:

```python
whole_number = 1
numerator = 10
denominator = 12
print(f"Decimal: {fraction_to_decimal(whole_number, numerator, denominator).unwrap()}")  # 1.8333...
```

---

### Decimal to Fraction

Convert decimals back into fractions. Useful for very large decimals. Example:

```python
f = 1.6532
print(f"Fraction: {decimal_to_fraction(f).unwrap()}")  # 1 1633/2500
```

---

### Factor

Factor a whole number into its prime factors. Polynomial factoring is not yet supported. Example:

```python
num = 32
print(f"Factors of {num}: {factor(num).unwrap()}")  # {2: 5} equivalent to 2*2*2*2*2
```

---

### Least Common Multiple (LCM)

Calculate the LCM of multiple numbers. Larger numbers may take longer to compute. Example:

```python
nums = (12, 43, 6, 8, 21)
print(f"LCM of {nums}: {lcm(*nums).unwrap()}")  # 7224
```

---

### Greatest Common Divisor (GCD)

Calculate the GCD of multiple numbers. Example:

```python
nums = (12, 4, 8, 2)
print(f"GCD of {nums}: {gcd(*nums).unwrap()}")  # 2
```

---

### Get Remainder

Get the remainder of division. Example:

```python
num1 = 52
num2 = 321
print(f"Remainder: {remain(num1, num2).unwrap()}")  # 52
```

---

### Proper Fraction

Convert an improper fraction to a proper fraction. Example:

```python
whole_number = 1
numerator = 324
denominator = 61
print(f"Proper Fraction: {proper_fraction(whole_number, numerator, denominator).unwrap()}")
```

---

### Get Numerator / Denominator

Retrieve the numerator or denominator from a fraction. Example:

```python
whole_number = 0
numerator = 31
denominator = 43
fraction = Fraction(whole_number, numerator, denominator)
print(f"Numerator: {fraction.get_numerator()}")    # 31
print(f"Denominator: {fraction.get_denominator()}")  # 43
```

---

### Factorial

Calculate the factorial of a number. Currently, only single whole numbers are supported. Example:

```python
n = 5
print(f"Factorial of {n}: {factorial(n).unwrap()}")  # 120
```

---

### Permutations

Calculate permutations when order matters. Example:

```python
n = 12
r = 3
print(f"Permutations: {permutations(n, r).unwrap()}")  # 1320
```

---

### Combinations

Calculate combinations when order does not matter. Example:

```python
n = 34
r = 12
print(f"Combinations: {combinations(n, r).unwrap()}")  # 225792840
```
