/*
Largest palindrome product
Problem 4

A palindromic number reads the 
same both ways. The largest palindrome 
made from the product of two 2-digit 
numbers is 9009 = 91 × 99.

Find the largest palindrome made from 
the product of two 3-digit numbers.

SOLUTION: 906609
*/

public class problem4 {

	public static boolean is_palindrome(int num) {
		// returns true if num is a palindrome
		// returns false otherwise
		String s_num = "" + num; // convert num to a string
		int k = s_num.length(); 
		int i = 0;
		while (i <= k-i) {
			if (s_num.charAt(i) != s_num.charAt(k-1-i)) return false;
			i++;
		}
		return true;
	}

	public static int max_palindrome_product(int digs) {
		// returns the largest palindrome which is
		// the product of two number with digs digits
		int max_pal = 0;
		for (int num1 = (int) Math.pow(10, digs-1); num1 < (int) Math.pow(10, digs); num1++) {
			for (int num2 = num1; num2 < (int) Math.pow(10, digs); num2++) {
				if (is_palindrome(num1 * num2) && num1 * num2 > max_pal) {
					max_pal = num1 * num2;
				}
			}
		}
		return max_pal;
	}

	public static void main(String[] args) {
		// TESTS 1
		// System.out.println(""+123+" palindromicity "+is_palindrome(123));
		// System.out.println(""+1231+" palindromicity "+is_palindrome(1231));
		// System.out.println(""+12321+" palindromicity "+is_palindrome(12321));
		// System.out.println(""+12312+" palindromicity "+is_palindrome(12312));
		// System.out.println(""+12399+" palindromicity "+is_palindrome(12399));
		// System.out.println(""+32123+" palindromicity "+is_palindrome(32123));
		// System.out.println(""+123+" palindromicity "+is_palindrome(123));
		// System.out.println(""+0+" palindromicity "+is_palindrome(0))
		System.out.println(max_palindrome_product(1));
		System.out.println(max_palindrome_product(2));
		System.out.println(max_palindrome_product(3));
	}
}