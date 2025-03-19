class Progression:
  def __init__(self, start = 0):
    self._current = start

  def _advance(self):
    """Updates self._current to the next value.
    
    By default, advances through the sequence 0, 1, 2, ...

    Should be overridden by subclasses to modify the progression.
    """
    self._current += 1

  def __next__(self):
    """Returns the next element, or raises StopIteration error."""
    # ends the progression
    if self._current is None:
      raise StopIteration()
    else:
      answer = self._current   # current value to be returned
      self._advance()          # advance to prepare for next call to __next__
      return answer            # return answer
  
  def __iter__(self):
    """By convention, an iterator must return itself as an iterator."""
    return self
  
  def print_progression(self, n):
    """Prints the next n values of the progression."""
    print(' '.join(str(next(self)) for j in range(n)))

# C-2.31 Write a Python class that extends the Progression class so that each 
# value in the progression is the absolute value of the difference between the
# previous two values. You should include a constructor that accepts a pair of
# numbers as the first two values, using 2 and 200 as the defaults.

class AbsoluteValueProgression(Progression):
  def __init__(self, start = 2, after = 200):
    super().__init__(start)
    self._after = after

  def _advance(self):
    """The sequence is defined by the progression 
    a_0, a_1, a_i = |a_{i - 1} - a_{i - 2}|
    
    so advancing this sequence involves setting self._current = after
    and self._after = |self._current - self._after|.
    """
    self._current, self._after = self._after, abs(self._current - self._after)

# C-2.32 Write a Python class that extends the Progression class so that each 
# value in the progression is the square root of the previous value. (Note that
# you can no longer represent each value with an integer.) Your constructor 
# should accept an optional parameter specifying the start value, using 65,536
# as a default.

class SquareRootProgression(Progression):
  def __init__(self, start = 65536):
    super().__init__(start)

  def _advance(self):
    self._current = self._current ** 0.5

if __name__ == "__main__":
  a = AbsoluteValueProgression(5, -7)

  a.print_progression(100)

  b = SquareRootProgression(1e308)

  b.print_progression(10)