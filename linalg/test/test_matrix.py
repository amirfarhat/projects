import unittest
import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(DIR, "../"))

from matrix import Matrix

def load_test_matrices():
	"""
	Returns a list of form [list, list] which 
	correspond to the a list of lists and a list
	of matrices to represent those matrices in
	matrices.txt
	"""
	return_value = [[],[]]
	# open and load matrices.txt
	# print('Opening the matrices.txt test file')
	test_matrices_file = open("matrices.txt")
	raw_text = test_matrices_file.read()
	print('Processing matrices...')
	test_matrices_file.close()
	# split to raw matrices to be processed
	raw_matrices = raw_text.split("\n\n")
	for mat in raw_matrices:
		raw_rows = mat.split("\n")
		array = []
		for row in raw_rows: # convert string rows into arrays of ints
			string_row = row.split(' ')
			array.append([int(x) for x in string_row])
		return_value[0].append(array)
		return_value[1].append(Matrix.get_from_list(array))
	print('Matrices ready for testing')
	return return_value

matrices_cache = load_test_matrices()

class TestMatrix(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		unittest.TestCase.__init__(self, *args, **kwargs)
		matrices = matrices_cache
		self.test_lists = matrices[0]
		self.test_matrices = matrices[1]

	def test_count_getters(self):
		"""
		Tests if get_col_count and get_row_count return
		the expected values to be returned
		"""
		for direction in ['h', 'v']:
			for matrix in self.test_matrices:
				i = 0
				while True:
					try:
						if direction == 'h':
							a = matrix[0, i]
						elif direction == 'v':
							a = matrix[i,0]
						i += 1
					except IndexError:
						break
				if direction == 'h':
					self.assertTrue(i == matrix.get_col_count())
				elif direction == 'v':
					self.assertTrue(i == matrix.get_row_count())

	def test_setitem(self):
		"""
		"""
		raise NotImplementedError

	def test_getitem(self):
		"""
		"""
		raise NotImplementedError

	def test_iter(self):
		"""
		Tests the functionality of __iter__ by
		verfiying the presence and positions of
		elements in the matrix
		"""
		k = len(self.test_matrices) - 1
		for i in range(len(self.test_matrices)):
			test_mat = self.test_matrices[i]
			list_repr = self.test_lists[i]
			expected_iter = []
			for elt in list_repr:
				if type(elt) == int:
					expected_iter.append(elt)
				elif type(elt) == list:
					expected_iter.extend(elt)
			# print(list(expected_iter), list(test_mat))
			self.assertTrue(list(expected_iter) == list(test_mat))
			# print(list(expected_iter), list(self.test_matrices[k-i]))
			self.assertFalse(list(expected_iter) == list(self.test_matrices[k-i]))

	def test_eq(self):
		"""
		Tests that the equality operation = 
		works for any two matrices by doing
		an element-wise check without __iter__
		"""
		raise NotImplementedError

	def test_ne(self):
		"""
		Tests that the equality operation = 
		works for any two matrices by doing
		an element-wise check without __iter__
		"""
		raise NotImplementedError



if __name__ == '__main__':
	unittest.main()