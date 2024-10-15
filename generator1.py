def even_numbers(n):
  for i in range(n):
      yield i

# Using the generator
for number in even_numbers(10):
  print(number)