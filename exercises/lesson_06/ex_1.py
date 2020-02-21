# Requirement:
# Define a generetor that accepts a list of strings as only argument and
# iterates over their lengths.

# Implemented on Python 3.

def lengths(strings):
    for s in strings:
        yield len(s)
