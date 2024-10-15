def squares(n):
  """Returns a list of squares from 0 to n-1."""
  result = []
  for i in range(n):
    result.append(i * i)
  return result

# Generator function
def squares1(n):
  """Generates squares from 0 to n-1."""
  for i in range(n):
    yield i * i

# Using the functions
num_list = squares(5)  # [0, 1, 4, 9, 16]
print(num_list)

num_list1 = squares1(5)  # [0, 1, 4, 9, 16]
print(num_list1)