/*
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares 
of the first ten natural numbers and the square of 
the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of 
the first ONE HUNDRED natural numbers and the square of the sum.

SOLUTION: 2.516415E7 = 25164150
*/

/* 
Closed Form for square of sum
1 + 2 + ... + N = N*(N+1)/2, so
(1 + ... + N)**2 = (N*(N+1))**2 / 4

Closed Form for sum of squares
1**2 + ... + N**2 = N*(N+1)*(2*N+1)/6
*/

public class problem6 {
	public static void main(String[] args) {
		int N = 100;
		double sum_of_squares = N*(N+1)*(2*N+1)/6;
		double square_of_sum = Math.pow(N*(N+1), 2) / 4;
		System.out.println(square_of_sum - sum_of_squares);
	}
}