# R-1.2 Write a short Python function, is_even(k), that takes an integer value 
# and returns True if k is even, and False otherwise. However, your function 
# cannot use the multiplication, modulo or division operators.

def is_even(k):
  return not k & 0b1    # True if and only if the 1 bit of k is 1

if __name__ == "__main__":
  print(is_even(0))     # True
  print(is_even(3))     # False
  print(is_even(-4))    # True
  print(is_even(6))     # True