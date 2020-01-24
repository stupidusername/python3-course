# Requirement:
#
# Define a decorator @debug that prints the name, arguments and return value of
# a function.

# Implemented on Python 3.6

import functools


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        print(f'Running {func.__name__}:')

        print('\tPositional arguments:')
        for arg in args:
            print(f'\t\t{arg}')

        print('\tKeyword arguments:')
        for k, v in kwargs.items():
            print(f'\t\t{k}: {v}')

        value = func(*args, **kwargs)
        print(f'\tReturn value: {value}')

        return value
    return wrapper
