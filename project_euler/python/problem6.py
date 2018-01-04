"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^52 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
-------------------------------------------------------
STATUS: COMPLETED
ANSWER: 25164150
RUNTIME: 0.4s
COMPLEXITY: O(n)
-------------------------------------------------------
"""

def sum_squares(a,b):
    """
    Returns the sum of the square of all 
    numbers between a and b inclusive
    """
    return sum([x**2 for x in range(a,b+1)])

def square_sum(a,b):
    """
    Returns the the square of the
    sum of all the numbers from a 
    to b inclusive
    """
    return (sum([x for x in range(a,b+1)])) ** 2


start = 1
end = 100
print(square_sum(start, end) - sum_squares(start, end))