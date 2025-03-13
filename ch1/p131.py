# P-1.31 Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.

DENOMINATIONS = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

def make_change(amount_charged, amount_given):
  change_amount = amount_given - amount_charged
  change_given = {}

  for denomination in DENOMINATIONS:
    if denomination < change_amount:
      change_given[denomination] = 0

      while change_amount >= denomination:
        change_amount -= denomination
        print(change_amount)
        change_given[denomination] += 1

  return change_given

if __name__ == "__main__":
  print(make_change(77433, 100000))