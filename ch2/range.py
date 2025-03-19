class Range:
  def __init__(self, start, stop = None, step = 1):
    if step == 0:
      raise ValueError('step cannot be 0')
    
    # handles range(n) type calls
    if stop is None:
      start, stop = 0, start

    self._length = max(0, (stop - start + step - 1) // step)

    self._start = start
    self._step = step

  def __len__(self):
    return self._length
  
  def __getitem__(self, k):
    if k < 0:
      k += len(self)

    if not 0 <= k < self._length:
      raise IndexError('index out of range')
    
    return self._start + k * self._step
  
  # C-2.27 In Section 2.3.5, we note that our version of the Range class has 
  # implicit support for iteration, due to its explicit support of both len
  # and getitem . The class also receives implicit support of the Boolean
  # test, “k in r” for Range r. This test is evaluated based on a forward 
  # iteration through the range, as evidenced by the relative quickness of 
  # the test 2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
  # more efficient implementation of the contains method to determine
  # whether a particular value lies within a given range. The running time of
  # your method should be independent of the length of the range.
  def __contains__(self, value):
    # value is in the range if and only if value = start + k * step for
    # some 0 <= k < self._length; equivalently, (value - start) / step
    # is some integer k in this range
    steps = (value - self._start) / self._step

    return steps.is_integer() and (0 <= steps < self._length)
  
if __name__ == "__main__":
  start = 0
  stop = 10000000000000000
  r = Range(start, stop, 5)

  print(stop - 5 in r)
  print(stop - 6 in r)

  t = Range(start, -stop, -25)

  print(-stop + 25 in t)
  print(-stop + 51 in t)