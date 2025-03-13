# P-1.29 Write a Python program that outputs all possible strings formed by
# using the characters c , a , t , d , o , and g exactly once.

def get_permutations(data):
  if len(data) == 0:
    return [[]]
  else:
    permutations = []

    for value in data:
      others = [ele for ele in data if ele != value]
      permutations += [[value] + remainder for remainder in get_permutations(others)]

    return permutations
  
def get_string_permutations(str):
  return [''.join(ele) for ele in get_permutations(str)]
  
if __name__ == "__main__":
  permutations = get_string_permutations("catdog")
  print(permutations)
  print(len(permutations))