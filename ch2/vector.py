class Vector:
  """Represent a vector in a multidimensional space."""

  # R-2.15 The Vector class of Section 2.3.3 provides a constructor that takes
  # an integer d, and produces a d-dimensional vector with all coordinates equal
  # to 0. Another convenient form for creating a new vector would be to send the
  # constructor a parameter that is some iterable type representing a sequence
  # of numbers, and to create a vector with dimension equal to the length of
  # that sequence and coordinates equal to the sequence values. For example,
  # Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates 
  # <4, 7, 5>. Modify the constructor so that either of these forms is
  # acceptable; that is, if a single integer is sent, it produces a vector of 
  # that dimension with all zeros, but if a sequence of numbers is provided, it
  # produces a vector with coordinates based on that sequence.
  def __init__(self, d):
    """If d is a sequence of numbers, create a vector from the sequence.
    Otherwise, assume d is a positive integer and create a d-dimensional
    vector of zeroes."""
    if (isinstance(d, int) and d > 0):
      self._coords = [0] * d
    elif (isinstance(d, list)):
      for j in range(len(d)):
        if (not (isinstance(d[j], int) or isinstance(d[j], float))):
          raise ValueError("d must be a positive integer or list of numbers")
      
      self._coords = d[:]
    else:
      raise ValueError("d must be a positive integer or list of numbers")
  
  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return the jth coordinate of the vector."""
    return self._coords[j]
  
  def __setitem__(self, j, val):
    """Set the jth coordinate of vector to the given value."""
    self._coords[j] = val

  def __add__(self, other):
    """Return the sum of two vectors."""

    if len(self) != len(other):            # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))             # start with vector of zeroes

    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result
  
  # R-2.11. In Section 2.3.3, we note that our Vector class supports a syntax
  # such as v = u + [5, 3, 10, -2, 1], in which the sum of a vector and list
  # returns a new vector. However, the syntax v = [5, 3, 10, -2, 1] + u is
  # illegal. Explain how the Vector class definition can be revised so that 
  # this syntax generates a new vector.
  
  # This syntax is currently illegal since the left operand, a list, does not
  # have a method __add__ defined that works on itself and a Vector class on
  # the right; similarly, the right operand, a Vector, does not have an 
  # __radd__ method that works on itself on the right a list on the left.
  # This can be fixed by adding such an __radd__ method to Vector:
  def __radd__(self, other):
    """Return the sum of two vectors."""
    return self + other # since componentwise addition is commutative
  
  # R-2.12. Implement the __mul__ method for the Vector class of Section 2.3.3.,
  # so that the expression v * 3 returns a new vector with coordinates that are
  # 3 times the respective coordinates of v.
  
  # R-2.13. Implement the __mul__ method for the Vector class of Section 2.3.3.,
  # so that the expression u * v returns a scalar that represents the dot product
  # of the vectors, that is, u_1 * v_1 + u_2 * v_2 + ... + u_d * v_d.
  def __mul__(self, other):
    """If other is a Vector, return the dot product self * other.
    Otherwise, assume it's a number and return a copy of self
    with the components scaled by a factor of other."""

    if (isinstance(other, Vector)):
      dot_product = 0

      if len(self) != len(other):
        raise ValueError("dimensions must agree")
      
      for i in range(len(self)):
        dot_product += self[i] * other[i]

      return dot_product
    else:
      scaled_vector = Vector(len(self))

      for i in range(len(scaled_vector)):
        scaled_vector[i] = other * self[i]

      return scaled_vector

  # R-2.13. Exercise R-2.12 asks for an implementation of __mul__ for the 
  # Vector class of Section 2.3.3, to provide support for the syntax v * 3.
  # Implement the __rmul__ method, to provide additional support for the 
  # syntax 3 * v.
  def __rmul__(self, scalar):
    """Returns a copy of the vector multiplied by a scalar factor."""
    return self * scalar # since scalar multiplication and dot product are commutative

  # R-2.10. Implement the __neg__ method for the Vector class of Section 2.3.3.,
  # so that tthe expression -v returns a new vector instance whose coordinates 
  # are all the negated values of the respective coordinates of v.
  def __neg__(self):
    """Returns a copy of the vector with the coordinates negated"""
    return self * -1
  
  # R-2.9. Implement the __sub__ method for the Vector class of Section 2.3.3.,
  # so that the expression u-v returns a new vector instance representing the
  # difference between two vectors.
  def __sub__(self, other):
    """Returns the difference of two vectors."""
    return self + (other * -1)
  
  def __eq__(self, other):
    """Return True if vector has the same coordinates as other"""
    return self._coords == other._coords
  
  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other               # rely on existing __eq__ definition
  
  def __str__(self):
    """Produce string representation of vector."""
    return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
  
if __name__ == "__main__":
  v = Vector(5)
  u = Vector([1, 2, 3, 4, 5])

  for i in range(len(v)):
    v[i] = i
    u[i] = 2 * i
  
  print(v)
  print(u)
  print(u + v)
  print(v * 3)
  print(4 * v)
  print(-v)
  print(v - u)
  print(v + [1, 2, 3, 4, 5])
  print([1, 2, 3, 4, 5] + v)
  print(u * v)