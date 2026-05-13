def is_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return False
    # Check for divisibility from 2 up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Usage
num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
