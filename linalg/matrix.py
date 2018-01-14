
class Matrix:
	def __init__(self, row_count, col_count):
		# allow only non-negative whole 
		# numbers for the row and column sizes
		for count in [row_count, col_count]:
			assert count >= 0 and type(count) == int
		self.row_count = row_count
		self.col_count = col_count
		self.matrix = [[0 for _ in range(col_count)] for _ in range(row_count)]

	@classmethod
	def get_from_list(cls, array):
		"""
		Returns a matrix from the 1D / 2D array
		of ints
		"""
		row_count = len(array)
		col_count = len(array[0])
		M = cls(row_count, col_count)
		for i in range(row_count):
			for j in range(col_count):
				M[i,j] = array[i][j]
		return M

	def get_row_count(self):
		return self.row_count

	def get_col_count(self):
		return self.col_count

	def get_matrix(self):
		return self.matrix

	def __setitem__(self, key, value):
		self.matrix[key[0]][key[1]] = value

	def __getitem__(self, key):
		return self.matrix[key[0]][key[1]]

	def __eq__(self, other):
		# other must be a matrix to intuit equality 
		if type(other) != Matrix:
			raise TypeError('Given parameter is not a Matrix')
		# other must have the same dimensions as self
		if self.get_row_count() != other.get_row_count() or \
			   self.get_col_count() != other.get_col_count():
			   raise IndexError('Unequal dimensions')
		# other must have the same entires as self
		return list(self) == list(other)

	def __ne__(self, other):
		return not self == other

	def __iter__(self):
		for row in self.matrix:
			for num in row:
				yield num

	def __repr__(self):
		longest_length = len(str(max((str(x) for x in self), key = len)))
		s = "\n"
		for row in self.matrix:
			s += "| "
			for num in row:
				addition = (longest_length-len(str(num)))*" "+str(num)
				s += addition + " "
			s += "|" + "\n"
		return s

	def __str__(self):
		return self.__repr__()