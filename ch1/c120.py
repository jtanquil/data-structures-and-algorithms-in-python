# C-1.20 Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible order
# occurs with equal probability. The random module includes a more basic function
# randint(a, b) that returns a uniformly random integer from a to b (including 
# both endpoints). Using only the randint function, implement your own version 
# of the shuffle function.

from random import randint

def shuffle(data):
  shuffled_indices = {}

  for i in range(len(data)):
    while True:
      shuffled_index = randint(0, len(data) - 1)

      if (i not in shuffled_indices and 
          shuffled_index not in shuffled_indices.values()):
        shuffled_indices[i] = shuffled_index
        break
  
  for i in range(len(data)):
    data[i], data[shuffled_indices[i]] = data[shuffled_indices[i]], data[i]

if __name__ == "__main__":
  for i in range(10):
    a = [1, 2, 3, 4, 5]
    shuffle(a)
    print(a)