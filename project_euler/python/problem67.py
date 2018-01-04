"""
Maximum path sum II
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
-------------------------------
ANS: 7273
STATUS: COMPLETE
RUNTIME: 1.7s
COMPLEXITY: IDFK
"""

def triangle_sum(triangle):
	"""
	Returns the maximum total down 
	the height of a triangle of numbers
	"""
	if len(triangle) == 1:
		return triangle[0][0]

	# recursive case
	for number_index in range(len(triangle[-2])): # penultimate row
		below_left = triangle[-1][number_index] # element below and to the left
		below_right = triangle[-1][number_index + 1] # element below and to the right
		triangle[-2][number_index] += max(below_left, below_right)

	return triangle_sum(triangle[:-1]) # triangle without the last row


f = open('triangle.txt')
triangle = []
for line in f.read().split('\n')[:-1]:
	row = []
	for num in line.split(' '):
		# print(num)
		row.append(int(num))
	triangle.append(row)
# print(triangle)
print(triangle_sum(triangle))