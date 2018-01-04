"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do not exceed four million, 
find the sum of the even-valued terms.
-------------------------------------------------

STATUS: COMPLETE
ANSWER: 4613732
RUNTIME: 0.1s
COMPLEXITY: O(n)
OPERATION COUNT: 4*(10**6)
"""

def fib(n): # assuming O(1)
    """
    Returns the nth fibonacci number
    """
    phi1 = (5 ** 0.5 + 1) / 2
    phi2 = (-5 ** 0.5 + 1) / 2
    fib_n = (((5**0.5)**-1) * (phi1 ** (n+1))) - (((5**0.5)**-1) * (phi2 ** (n+1)))
    return int(fib_n )

total = 0
n = 1
fib_n = fib(n)
while fib_n <= 4 * (10 ** 6):
    if fib_n % 2 == 0:
        # print(fib_n)
        total += fib_n
    n += 1
    fib_n = fib(n)
print(total)

