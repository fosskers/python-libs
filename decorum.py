# file:    decorum.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   A library containing various useful decorators.

from time import time as _time

# TIMER FUNCTIONS
def time_it(func):
    '''Times a function.'''
    def inner(*args):
        start = _time()
        result = func(*args)
        end = _time()
        print('Did {} in {} s'.format(func.__name__, end - start))
        return result
    return inner
    
def time_to_n(func, low=0):
    '''Runs a single-arg function with values 0 to n.
    The argument passed to the function becomes the upper limit,
    and the function is actually also run with all values lower than that.
    '''
    def inner(n):
        start = _time()
        for x in range(low, n):
            func(x)
        end = _time()
        print('Ran {} to {} in {} s'.format(func.__name__, n, end - start))
    return inner

def time_to_n_list(func):
    '''Times a function using progressively larger list sizes.'''
    def inner(n):
        start = _time()
        for x in range(n):
            func(list(range(x)))
        end = _time()
        print('Ran {} to {} in {} s'.format(func.__name__, n, end - start))
    return inner
