# P-1.35 The birthday paradox says that the probability that two people in a 
# room will have the same birthday is more than half, provided n, the number 
# of people in the room, is more than 23. This property is not really a paradox,
# but many people find it surprising. Design a Python program that can test this 
# paradox by a series of experiments on randomly generated birthdays, which test 
# this paradox for n = 5,10,15,20,...,100.

from random import randint

DAYS_IN_YEAR = 365
SAMPLE_SIZE = 100

def generate_birthdays(n):
  return [randint(1, DAYS_IN_YEAR) for i in range(n)]

def birthday_paradox(n, m):
  matching_birthdays = 0
  birthdays = [generate_birthdays(n) for i in range(m)]

  for birthday in birthdays:
    unique_birthdays = {}

    for ele in birthday:
      if ele in unique_birthdays:
        matching_birthdays += 1
        break;
      else:
        unique_birthdays[ele] = 1

  return matching_birthdays / m

if __name__ == "__main__":
  for i in range(5, 105, 5):
    print(i, birthday_paradox(i, SAMPLE_SIZE))