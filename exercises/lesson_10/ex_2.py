# Requirement:
# Write a decorator @validate_types that takes an optional argument called
# valid_type (that can be a type or a tuple of types) and validates that all
# the arguments passed to the function being decorated are instances of
# that/those type(s). If one argument is not an instance of a valid type a
# TypeError exception must be raised. If valid_type is not specified then the
# decorator must validate that none of the arguments passed to the decorated
# function are None.

# Implemented on Python 3.6.

import functools


def validate_types(_func=None, *, valid_type=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            def validate(arg):

                msg = (
                    f'{repr(arg)} is not a valid'
                    f'argument for {func.__name__}()'
                )

                if valid_type:
                    if not isinstance(arg, valid_type):
                        raise TypeError(msg)
                else:
                    if arg is None:
                        raise TypeError(msg)

            [validate(arg) for arg in args]
            [validate(v) for v in kwargs.values()]

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)



@validate_types(valid_type=str)
def test(a):
    pass

test(1)
