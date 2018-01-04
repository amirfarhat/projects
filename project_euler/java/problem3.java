/*
Largest prime factor
Problem 3

The prime factors of 13195 
are 5, 7, 13 and 29.

What is the largest prime 
factor of the number 600851475143 ?

SOLUTION: 6857
*/

public class problem3 {
	public static void main(String[] args) {
		int divisor = 2;
		int max_divisor = 0;
		// int num = 13195; // test
		Long num = 600851475143L;
		while (num != 1) {
			while (num % divisor == 0) { 
				if (divisor > max_divisor) {
					max_divisor = divisor;
				num /= divisor;
				}
			}
			divisor++; 
		}
		System.out.println(max_divisor);
	}
}