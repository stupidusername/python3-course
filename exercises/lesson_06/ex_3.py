# Requirement:
# Create a generator gen_seq() that creates the infinite geometric series:
#   1, 1/2, 1/4, 1/8...
# Write a function first_n(n) that sums the first n values.
# Write a function until_small(epsilon) that sums the sequence until the
# additional term is less than some small value epsilon.

# Implemented on Python 3.

def gen_seq():
    n = 1
    while True:
        yield 1 / n
        n *= 2


def first_n(n):
    g = gen_seq()
    return sum(next(g) for _ in range(n))


def get_until_small(epsilon):
    g = gen_seq()
    while True:
        v = next(g)
        if v <= epsilon:
            break
        yield v


def until_small(epsilon):
    return sum(get_until_small(epsilon))
