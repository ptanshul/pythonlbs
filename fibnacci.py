def fibonacci_generator():
  """Generates an infinite sequence of Fibonacci numbers."""
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Using the generator
fib_gen = fibonacci_generator()

# Print the first 10 Fibonacci numbers
for _ in range(10):
  print(next(fib_gen))