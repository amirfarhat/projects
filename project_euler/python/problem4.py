"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. 
The largest palindrome made from the product 
of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
---------------------------------------------------------------------

STATUS: COMPLETE
ANSWER: 906609
RUNTIME: 1.0s
COMPLEXITY: O(n * len(max_number))
OPERATION COUNT: 4*(10**6)
"""

def is_palindrome(num): # O(len(num)), C(5*len(num))
    return str(num) == str(num)[::-1]

# SOLUTION
three_dig_nums = [n for n in range(100, 1000)] # 900 numbers
pals = []
for index1 in range(len(three_dig_nums)): # O()
    for index2 in range(index1, len(three_dig_nums)):
        num1 = three_dig_nums[index1]
        num2  = three_dig_nums[index2]
        if is_palindrome(num1 * num2):
            pals.append(num1 * num2)
print(max(pals))
