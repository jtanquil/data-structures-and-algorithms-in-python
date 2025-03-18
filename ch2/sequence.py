from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
  """Our own version of collections.Sequence abstract base class"""

  @abstractmethod
  def __len__(self):
    """Return the length of the sequence."""

  @abstractmethod
  def __getitem__(self, j):
    """Return the element at index j of the sequence."""

  def __contains__(self, val):
    """Return True if val found in the sequence, False otherwise."""
    for j in range(len(self)):
      if self[j] == val:
        return True
    return False
  
  def index(self, val):
    """Return leftmost index at which val is found (or raise ValueError)."""
    for j in range(len(self)):
      if self[j] == val:
        return j
    raise ValueError('value not in sequence')
  
  def count(self, val):
    """Return the number of elements equal to given value."""
    k = 0
    for j in range(len(self)):
      if self[j] == val:
        k += 1
    return k
  
  # R-2.22. The collections.Sequence abstract base class does not provide 
  # support for comparing two sequences to each other. Modify our Sequence 
  # class from Code Fragment 2.14 to include a definition for the __eq__ 
  # method, so that expression seq1 == seq2 will return True precisely when 
  # the two sequences are element by element equivalent.
  def __eq__(self, other):
    if (len(self) != len(other)):
      return False
    else:
      for i in range(len(self)):
        if self[i] != other[i]:
          return False
      return True

  # R-2.23. In similar spirit to the previous problem, augment the Sequence 
  # class with method __lt__, to support lexicographic comparison seq1 < seq2.
  def __lt__(self, other):
    min_length = min(len(self), len(other))

    for i in range(min_length):
      if self[i] < other[i]:
        return True
      elif self[i] > other[i]:
        return False
      
    return len(self) < len(other)
  
class TestList(Sequence):
  def __init__(self):
    self._elements = []

  def __len__(self):
    return len(self._elements)
  
  def __getitem__(self, j):
    return self._elements[j]
  
  def __setitem__(self, j, val):
    self._elements[j] = val

  def append(self, val):
    self._elements.append(val)
    
if __name__ == "__main__":
  a = TestList()
  b = TestList()
  
  for i in range(3):
    a.append(i + 1)

  b.append(1)
  b.append(2)
  b.append(4)

  print(a == b) # [1, 2, 3] != [1, 2, 4]
  print(a < b)  # [1, 2, 3] < [1, 2, 4]

  a[2] = 4
  a.append(5)

  print(a < b)  # [1, 2, 4, 5] > [1, 2, 4]