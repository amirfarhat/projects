"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
-----------------------------------------

STATUS: COMPLETE
ANSWER: 6857
"""

def prime_factors(n):
	"""
	Attempts to return a list of factors for
	an integer n by exploiting the Fundamental
	Theorem of Arithmetic (Unique Factorization Theorem)
	"""
	facs = set()
	div = 2
	while n > 1:
		while n % div == 0: 
			n /= div
			facs.add(div)
		div += 1
	return facs

if __name__ == '__main__':
	# num = 13195
	num = 600851475143
	# print(prime_factors(num))
	print(max(prime_factors(num)))

