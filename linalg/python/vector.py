from functools import reduce

class Vector:
	"""
	Immutable data type to represent a column vector. 
	Requires at least one component, and the items a vector is
	made of may be any of int or float

	AF(components) = the vector with component v_i = components[i]

	RI(components) = true iff len(components) > 1
							   and components[i] an int or float for all i
	"""
	def __init__(self, elts):
		"""
		Constructs a new Vector from the items in elts

		- elts: tuple, list, or other iterable of vector components
		"""
		# self.components = list(elts)
		self.components = tuple(elts)
		self.check_rep()

	def check_rep(self):
		"""
		Asserts the representation invariant, see ADT spec
		"""
		assert isinstance(self.components, tuple)
		assert len(self.components) > 1

	def __iter__(self):
		"""
		Returns a generator of the objects inside this vector, 
		i.e. return a generator of its components
		"""
		yield from self.components

	def norm(self):
		"""
		Returns the Euclidean norm of self, i.e.
		the length of the vector in n-dimensional space
		for self an n-dimensional vector
		"""
		add = lambda a, b : a + b
		square = lambda x : x ** 2
		return reduce(add, map(square, self.components), 0) ** 0.5

	def _linear_combine(self, other, combine_func):
		"""
		Returns the result of combining the elements of self and other
		through the function combine_func as another Vector

		other: equidimensional Vector to self
		combine_func:
		"""
		assert isinstance(other, Vector)
		n = len(self.components)
		assert len(other.components) == n
		return Vector([combine_func(s_i, o_i) for s_i, o_i in zip(self, other)])

	def __add__(self, other):
		"""
		Returns the new Vector resultant from summing self and other

		other: equidimensional Vector to self
		"""
		addition = lambda a, b : a + b
		return self._linear_combine(other, addition)

	def __sub__(self, other):
		"""
		Returns the new Vector resultant from subtracting self and other

		other: equidimensional Vector to self
		"""
		subtraction = lambda a, b : a - b
		return self._linear_combine(other, subtraction)

	def dot(self, other):
		"""
		Returns the new Vector resultant from taking the 
		dot product of self and other

		other: equidimensional Vector to self
		"""
		mul = lambda a, b :  a * b
		products = self._linear_combine(other, mul)
		return sum(products.components)

	def __eq__(self, other):
		"""
		Returns True if self and other are equal Vectors componentwise
		and False otherwise

		other: valid Vector object
		"""
		assert isinstance(other, Vector)
		return all(s_i == o_i for s_i, o_i in zip(self.components, other.components))

	def __ne__(self, other):
		"""
		Returns False if self and other are equal Vectors componentwise
		and True otherwise

		other: valid Vector object
		"""
		return not self == other

	def __str__(self):
		"""
		Produce and return a human-readable representation of this vector
		"""
		s, separator = "<", ","
		for component in self:
			s += str(component) + separator
		return s[:-len(separator)] + ">" # take up until the last extra comma and space

	def __repr__(self):
		"""
		Returns a string such that evaluating that string in python
		produces a Vector with the same components as self
		"""
		return "{}({})".format('Vector', str(self.components))

