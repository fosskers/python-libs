# numworks.py
# author:  Colin Woodbury
# contact: colingw@gmail.com
# about:   A module that aids in certain mathematical calculations. 

from functools import reduce as _reduce
from listhelp import rotate as _rotate
from math import floor as _floor

# COMMON OPERATIONS
def factorial(num, limit=1):
    '''Can impose a limit to stop the multiplication part-way through.
    This represents x!/y! (factorial division) when y is less than x.
    '''
    result = 1
    while num > limit:
        result *= num
        num -= 1
    return result

def gcd(n, m):
    '''Determines the greatest common divisor of two numbers.'''
    upper = n
    lower = m
    remainder = n % m
    while remainder != 0:
        upper = lower
        lower = remainder
        remainder = upper % lower
    return lower

def is_whole(num):
    """Determines if a number is whole, in other words, an integer.
    Can be used to determine if the sqrt of something is whole.
    """
    if num == _floor(num):
        return True
    return False

# NUMBERS AS LISTS
def itol(num):
    """Converts a given int to a list,
    with each digit as a single element in the list.
    Last modified: 2/17/2011"""
    digits = []
    if num == 0:
        digits.append(0)
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()
    return digits

def ltoi(digits):
    '''Written with reduce. Written 06/04/2011'''
    return _reduce(lambda acc, n: acc * 10 + n, digits)

def int_concat(nums):
    """Concatinates a list of ints.
    Written 03/04/2011  Mod 06/04/2011
    """
    merged = ''.join(map(str, nums))
    return int(merged)

def rotate(num, places=1):
    '''Rotates an int to the left.'''
    return ltoi(_rotate(itol(num), places))

def reverse(num):
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
    in_ord = zip(digits, digits[1:])
    return False not in map(func, in_ord)

def is_bouncy(num):
    '''A number is bouncy if it is neither increasing nor decreasing.'''
    if not is_increasing(num) and not is_decreasing(num):
        return True  # Bouncy!                           
    return False

# MISC.
def is_permutation(n, m):
    '''Permutation test, written using a sort. Written 06/05/2011'''
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
