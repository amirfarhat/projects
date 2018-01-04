/*
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that 
are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

SOLUTION: 233168
*/

class problem1 {
	public static void main(String[] args) {
		int counter = 0;
		// check all integers i in [1,999]
		for (int i = 0; i < 1000; i++) {
			// if i is divisible by 3 or 5
			if (i % 3 == 0 || i % 5 == 0) {
				counter += i; // add to the running sum
			} 
		}
		System.out.println(counter); // print the result
	}
}