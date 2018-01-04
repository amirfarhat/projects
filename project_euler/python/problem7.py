"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
---------------------------------------------
STATUS: COMPLETE
ANSWER: 104743
"""

def is_prime(num):
    """
    Returns True if num is a prime number
    return False otherwise
    """
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0: 
            return False
    return True

primes = []
num = 2
while len(primes) < 10 ** 4 + 1:
    if is_prime(num):
        # print(num)
        primes.append(num)
    num += 1

print(len(primes))
print(primes[-1])

