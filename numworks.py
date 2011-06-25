# numworks.py
# author:  Colin Woodbury
# contact: colingw@gmail.com
# about:   A module that aids in certain mathematical calculations.
# updated: 06/12/2011

from listhelp  import rotate as _rotate, frequencies as _freqs
from funchelp  import take   as _take,   last        as _last
from functools import reduce as _reduce
from math      import floor  as _floor
from fractions import gcd    as _gcd

def no_negatives(func):
    '''Does not allow negative numbers to be passed to a function.'''
    def inner(*args):
        for arg in args:
            if arg < 0:
                raise ValueError('Negative number given.')
        return func(*args)
    return inner

def non_empty(func):
    '''Does not allow an empty list to be passed to a function.'''
    def inner(arg):
        if len(arg) < 1:
            raise ValueError('Empty list given.')
        return func(arg)
    return inner

# COMMON OPERATIONS
@no_negatives
def factorial(num, limit=1):
    '''Can impose a limit to stop the multiplication part-way through.
    This represents x!/y! (factorial division) when y is less than x.
    '''
    return _reduce(lambda acc, n: acc * n, range(limit, num+1), 1)

def lcm(n, m):
    '''Calculates the lowest common multiple of two numbers.'''
    return n * m // _gcd(n, m)

def is_whole(num):
    '''Determines if a number is whole, in other words, an integer.
    Can be used to determine if the sqrt of something is whole.
    '''
    if num == _floor(num):
        return True
    return False

# PROBABILITY
@non_empty
def mean(items):
    '''Calculates the mean of a list of numbers.'''
    return sum(items) / len(items)

@non_empty
def median(items):
    '''Finds the median of a set of numbers.'''
    items.sort()  # No guarantee the arg list was sorted.
    size = len(items)
    mid = size // 2
    if size % 2 != 0:  # Odd number of args.
        return items[mid]
    # Even number of elements. Find mean of middle two.
    return mean((items[mid - 1], items[mid]))

@non_empty
def mode(items):
    '''Finds the mode of a set of numbers.
    BUG: Can't handle ties yet.
    '''
    items  = _freqs(items)
    record = 0
    count  = 0
    for key in items:
        if items[key] > count:
            count  = items[key]
            record = key
    return record

# FIBONACCI NUMBERS
class fibonacci():
    '''Generates all the numbers of the fibonacci sequence.'''
    def __iter__(self):
        a = 0
        b = 1
        yield 1
        while True:
            yield a + b
            a, b = b, a + b

@no_negatives
def nth_fib(n):
    '''Gets the nth fibonacci number.'''
    return _last(_take(n, fibonacci()))

# NUMBERS AS LISTS
@no_negatives
def itol(num):
    '''Converts a given int to a list, with each digit 
    as a single element in the list. Mod: 06/13/2011
    '''
    digits = []
    d_a = digits.append
    if num == 0:
        d_a(0)
    while num > 0:
        d_a(num % 10)
        num //= 10
    digits.reverse()
    return digits

@non_empty
def ltoi(digits):
    '''Written with reduce. Written 06/04/2011'''
    return _reduce(lambda acc, n: acc * 10 + n, digits)

@non_empty
def int_concat(nums):
    '''Concatinates a list of ints.
    Written 03/04/2011  Mod 06/04/2011
    '''
    merged = ''.join(map(str, nums))
    return int(merged)

def rotate(num, places=1):
    '''Rotates an int to the left.'''
    return ltoi(_rotate(itol(num), places))

def reverse_digits(num):
    '''Given an int, reverses it.'''
    digits = itol(num)
    digits.reverse()
    return ltoi(digits)

# PROJECT EULER ALGORITHMS
def combinatorics_magic(n, r):
    '''nCr = n!/(r!(n-r)!)
    Represents the amount of r digit numbers that can be
    generated from the numbers in an n digit number.
    '''
    return factorial(n, r) // factorial(n-r)

def is_increasing(num):
    '''Tests if a number is made up of increasing digits.'''
    return is_incdec(num, lambda tup: False if tup[0] > tup[1] else True)

def is_decreasing(num):
    '''Tests if a number is made up of decreasing digits.'''
    return is_incdec(num, lambda tup: False if tup[0] < tup[1] else True)

def is_incdec(num, func):
    '''Tests if a number is increasing or decreasing.'''
    digits = itol(num)
    if len(digits) < 2:
        return False
    in_order = zip(digits, digits[1:])
    return all(map(func, in_order))

def is_bouncy(num):
    '''A number is bouncy if it is neither increasing nor decreasing.'''
    if not is_increasing(num) and not is_decreasing(num):
        return True  # Bouncy!                           
    return False

# MISC.
def sdiv(n, m):
    '''Super division. Divides n by m as many times as possible.'''
    if n == 0 or m == 1:
        return n  # Returns 0 or n's original value.
    while n % m == 0:
        n //= m
    return n

def is_permutation(n, m):
    '''Permutation test, using a sort. Written 06/05/2011'''
    n = itol(n)  # Convert both to lists, first.
    m = itol(m)
    if n.sort() == m.sort():
        return True
    return False
        
def is_pandigital(num, bound=1):
    '''Determines if an int is pandigital. A number if pandigital
    if it contains 1 to n exactly once (by default).
    User can indicate a lower bound to fit the pandigital they want.
    '''
    if isinstance(num, int):
        num = itol(num)
    for digit in range(bound, len(num)+bound):
        if digit not in num:
            return False
    return True

def sum_of_digits(num):
    '''Adds all the digits of a given int together.'''
    digits = itol(abs(num))
    return sum(digits)

@no_negatives
def to_base2(num):
    '''Converts a base 10 number to base 2.'''
    result = 0
    exp = 0
    while num > 0:
        bit = num % 2
        result += bit * (10 ** exp)
        num /= 2
        exp += 1
    return result
