"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that 
are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
--------------------------------------------------------

STATUS: COMPLETE
ANSWER: 233168
RUNTIME: 0.1s
COMPLEXITY: O(n)
OPERATION COUNT: 1 + 1000 * 2 = 2001
"""

total = 0
for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print(total)

