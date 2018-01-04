"""
Smallest multiple
Problem 5

2520 is the smallest number that 
can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?

-------------------------------------------------------
STATUS: COMPLETE
ANSWER: 232792560
-------------------------------------------------------
"""

def prime_factors(num):
	"""
	Returns a dictionary of the prime factors
	of the number num where keys are prime factors
	and values are their respective multiplicities
	"""
	facs = dict()
	div = 2
	while num != 1:
		while num % div == 0: # still divisible
			num /= div # decompose
			if div not in facs:
				facs[div] = 1
			else:
				facs[div] += 1
		div += 1
	return facs

def compactify_prime_factors(divisor_list):
	"""
	Returns a factors dictionary new_facs which has
	the prime factors of divisor_list, but has the 
	maximum multiplicity of each prime factor
	"""
	new_facs = dict()
	for divisor in divisor_list:
		facs = prime_factors(divisor)
		for factor in facs:
			if factor not in new_facs:
				new_facs[factor] = 1
			else:
				new_facs[factor] = max(new_facs[factor], facs[factor])
	return new_facs

def construct_num_from_dict(factors):
	"""
	Takes in a factors dictionary with form same as
	output from prime_factors, and returns the number
	made from those factors and their multiplicities
	"""
	result = 1
	for factor in factors:
		multiplicity = factors[factor]
		result *= factor ** multiplicity
	return result

if __name__ == '__main__':
	divisor_list = [x for x in range(1, 21)]
	compact_primes = compactify_prime_factors(divisor_list)
	print(construct_num_from_dict(compact_primes))