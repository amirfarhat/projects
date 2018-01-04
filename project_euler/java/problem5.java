/*
Smallest multiple
Problem 5

2520 is the smallest number that 
can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?

SOLUTION: 232792560
*/

import java.util.*;

public class problem5 {

	public static HashMap<Integer, Integer> get_prime_factors(int num) {
		// returns a hashmap multiplicities by mapping prime 
		// factor keys to their respective multiplicities in num
		HashMap<Integer, Integer> multiplicities = new HashMap<Integer, Integer>();
		int divisor = 2;
		while (num != 1) {
			while (num % divisor == 0) {
				// we update the multiplicity of this divisor
				if (!multiplicities.containsKey(divisor)) {
				// if previously unseen, record this divisor
					multiplicities.put(divisor, 1);
				}
				else {
				// otherwise, increment the multiplicity of this divisor by 1
					multiplicities.put(divisor, multiplicities.get(divisor) + 1);
				}
				num /= divisor;
			}
			divisor++;
		}
		return multiplicities;
	}

	public static HashMap<Integer, Integer> get_minimal_factors(ArrayList<Integer> divisors) {
		// returns the smallest positive integer such that
		// it is divisible by each divisor in the divisors list
		HashMap<Integer, Integer> minimal_factors = new HashMap<Integer, Integer>();
		for (int div : divisors) {
			HashMap<Integer, Integer> div_factors = get_prime_factors(div);
			for (int factor : div_factors.keySet()) {
				if (!minimal_factors.containsKey(factor)) {
					// factor multiplicity in div_factors
					int factor_multiplicity = div_factors.get(factor);
					minimal_factors.put(factor, factor_multiplicity);
				}
				else {
					// factor multiplicity in div_factors
					int div_fact_mult = div_factors.get(factor); 
					// factor multiplicity in minimal_factors
					int min_fact_mult = minimal_factors.get(factor); 
					// recored the largest of the two
					minimal_factors.put(factor, Math.max(div_fact_mult, min_fact_mult));
				}
			}
		}
		return minimal_factors;
	}

	public static void main(String[] args) {
		// TESTS
		// ArrayList<Integer> divisors = new ArrayList<Integer>();
		// for (int i = 1; i <= 10; i++) divisors.add(i);
		// //// get_prime_factors 
		// // for (int div : divisors) {
		// // 	System.out.println(""+div+" , "+get_prime_factors(div));
		// // }
		//// get_minimal_factors
		// System.out.println(get_minimal_factors(divisors));
		// ----------------------------------------------------------
		ArrayList<Integer> divisors = new ArrayList<Integer>();
		for (int i = 1; i <= 20; i++) divisors.add(i);
		HashMap<Integer, Integer> minimal_factors = get_minimal_factors(divisors);
		int smallest_number = 1;
		for (int factor : minimal_factors.keySet()) {
			smallest_number *= Math.pow(factor, minimal_factors.get(factor));
		}
		System.out.println(smallest_number);

	}
}