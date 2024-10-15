

# Generator function
def squares1(n):
  """Generates squares from 0 to n-1."""
  for i in range(n):
    yield i 



num_list1 = squares1(5)  # [0, 1, 4, 9, 16]
print(num_list1)