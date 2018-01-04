"""
Powerful digit counts
Problem 63

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
---------------------------------

ANS: 49
STATUS: COMPLETED
RUNTIME: 2.0s
COMPLEXITY: IDFK

"""

def num_digs(x):
	"""
	Returns the number of digits that
	the integer x contains

	>>> num_digs(0) == num_digs(5) == 1
	True
	>>> num_digs(666666)
	6
	"""
	return len(str(x))

def n_dig_nth_power(n):
	"""
	Returns the set number of integers k 
	such that k^n has exactly n digits
	"""
	c = 0
	while num_digs(c**n) < n:
		c += 1
	counter = 0
	while num_digs(c**n) == n:
		counter += 1
		c += 1
	return counter

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	upper = 100
	print(sum(n_dig_nth_power(i) for i in range(1, upper+1)) - 1)
	print('done')