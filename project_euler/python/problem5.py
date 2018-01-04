"""
Smallest multiple
Problem 5

2520 is the smallest number that 
can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?

-------------------------------------------------------
STATUS: ONGOING

-------------------------------------------------------
1 = 1
2 = 2
3 = 3
4 = 2 ** 2
5 = 5
6 = 2 * 3
7 = 7
8 = 2 ** 3
9 = 3 ** 2
10 = 2 * 5

1*2*3*4*5*6*7*8*9*10 = 
1 * (2**(1+2+1+3+1)) * (3**(1+1+2)) * (5**(1+1)) * 7

has 
"""

def divides_one_through_twenty(num):
    for div in range(1, 21):
        if num % div != 0:
            return False
    return True

num = 2
while not divides_one_through_twenty(num):
    # print(num)
    num += 2

print(num)

