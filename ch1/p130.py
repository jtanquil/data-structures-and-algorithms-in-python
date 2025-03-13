# P-1.30 Write a Python program that can take a positive integer greater than 2 
# as input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

def logfloor(number, base):
  n = 0
  product = base

  while (number >= product):
    product *= base
    n += 1

  return n

if __name__ == "__main__":
  print(logfloor(100, 2))       # 6
  print(logfloor(1024, 2))      # 10
  print(logfloor(127, 2))       # 6