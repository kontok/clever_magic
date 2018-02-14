from collections import namedtuple


def return_namedtuple (*name):
    def decorator (func):
        def wrapper (*args, **kwargs):
            if isinstance(name, tuple):
                x = func(*args, **kwargs)
                nazvanie = namedtuple('znachenie', name)
                result = nazvanie(*x)
            return result
        return wrapper
    return decorator



@return_namedtuple('one', 'two')
def func():
    return 1, 2

r = func()



@return_namedtuple('one', 'two', 'three')
def func():
    return 1, 2, 3


