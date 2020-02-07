# Requirement:
# Write a function that accepts any number of strings as positional arguments
# and a keyword argument (sep) that is also a string.
# If the function is called liked this
# super_print(“String”, “Long String”, sep=”|-.+:”)
# It should print:
#   |-.+:|-.+:|
#   String
#   |-.+:|-.+:|
#   Long String
#   |-.+:|-.+:|

# Implemented on Python 3.

def super_print(*strings, sep):

    # get the longest string
    longest = max(strings, key=len)

    # get the lenght of the separator
    sep_len = len(longest)

    # build the separator
    q, r = divmod(sep_len, len(sep))
    built_sep = sep * q + sep [:r]

    # print the decorated text
    for string in strings:
        print(built_sep)
        print(string)
    else:
        print(built_sep)
