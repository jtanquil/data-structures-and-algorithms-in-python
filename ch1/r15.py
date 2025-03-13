# R-1.4 Write a short Python function that takes a positive integer n and returns 
# the sum of the squares of all the positive integers smaller than n.
# R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying 
# on Python’s comprehension syntax and the built-in sum function.

def sum_squares(n):
  return sum([i ** 2 for i in range(n)])

if __name__ == "__main__":
  print(sum_squares(3))     # 5
  print(sum_squares(5))     # 30