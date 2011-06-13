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

def time_it_n(func, n):
    '''Runs a function n times and times it.'''
    def inner(*args):
        start = _time()
        for x in range(n):
            result = func(*args)
        end = _time()
        print('Ran {} {} times in {} s'.format(func.__name__, n, end - start))
        return result
    return inner        
    
def time_it1000(func):
    '''Runs a given function 1000 times.'''
    return time_it_n(func, 1000)

def time_it10000(func):
    '''Runs a given function ten thousand times.'''
    return time_it_n(func, 10000)

def time_it100000(func):
    '''Runs a given function one hundred thousand times.'''
    return time_it_n(func, 100000)

def time_it1000000(func):
    '''Runs a given function one million times.'''
    return time_it_n(func, 1000000)
