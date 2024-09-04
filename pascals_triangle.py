
# Solve with Recursion concept fuction calling itself instead of loopings.

"""
TRIANGLE = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
]

formula: Pascal(n, k)=(n) =  n!
                      (k)   ----
                            k!(n-k)!

row 5:
[1, 5, 10, 10, 5, 1]
"""
def rows(row_count):
    result = []
    for i in range(1, row_count):
       result.append(rows(factorial(i)))
    return result
       

def factorial(number):
  if number <= 1:  # base case
    return 1

  return number * factorial(number - 1) # recursive case

rows(5)