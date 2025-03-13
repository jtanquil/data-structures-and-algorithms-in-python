# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def has_no_repeats(data):
  unique_values = {}

  for value in data:
    if value not in unique_values:
      unique_values[value] = 1
    else:
      return False
    
  return True

if __name__ == "__main__":
  a = [1, 2, 3]
  b = [1, 2, 1]

  print(has_no_repeats(a))    # True
  print(has_no_repeats(b))    # False