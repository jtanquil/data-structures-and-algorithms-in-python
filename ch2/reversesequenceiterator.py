# C-2.26. The SequenceIterator class of Section 2.3.4 provides what is known as 
# a forward iterator. Implement a class named ReversedSequenceIterator that
# serves as a reverse iterator for any Python sequence type. The first call to
# next should return the last element of the sequence, the second call to next
# should return the second-to-last element, and so forth.

class ReversedSequenceIterator:
  def __init__(self, sequence):
    self._sequence = sequence
    self._k = len(self._sequence)

  def __next__(self):
    self._k -= 1  # first call to __next__ will set self._k = len(self._sequence) - 1

    # will return elements until the first element of the sequence, then raise error
    if (self._k >= 0):
      return self._sequence[self._k]
    else:
      raise StopIteration()
    
  def __iter__(self):
    return self
  

if __name__ == "__main__":
  a = ReversedSequenceIterator([1, 2, 3, 4, 5])

  for i in range(5):
    print(next(a))

  next(a) # raises StopIteration