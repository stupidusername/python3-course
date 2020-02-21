# Requirement:
# Define a generator that generates the elements of the Fibonacci sequence
# that are less than a given integer.

# Implemented on Python 3.

def gen_fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
