# C-1.14 Write a short Python function that takes a sequence of integer values 
# and determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def has_odd_product(data):
  for i in range(len(data)):
    for j in range(i + 1, len(data)):
      if (data[i] * data[j]) % 2 == 1:
        return True
      
  return False

if __name__ == "__main__":
  a = [1, 2, 3]
  b = [2, 3, 4]

  print(has_odd_product(a))     # True
  print(has_odd_product(b))     # False