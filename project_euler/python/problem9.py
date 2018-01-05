"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three 
natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean 
triplet for which a + b + c = 1000.
Find the product abc.

STATUS: COMPLETE
SOLUTION: 31875000
"""
for a in range(1, 1001):
	for b in range(a+1, 1001):
		c = (a**2 + b**2) ** 0.5 # construct right triangke
		if a + b + c == 1000: # found the triple
			print(a,b,c, a*b*c)
