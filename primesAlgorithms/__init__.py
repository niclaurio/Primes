from functools import wraps


def validate_input(func):
    @wraps(func)  # to be called during tests
    def wrapper(n, *args, **kwargs):
        if not isinstance(n, (float, int)):
            raise TypeError("Expected n to be a float or int")

        if n < 2:
            return []

        return func(n, *args, **kwargs)

    return wrapper
