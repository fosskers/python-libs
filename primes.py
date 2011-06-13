# file:    primes.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   A module that performs various calculations
#          relating to prime numbers.
# updated: 06/07/2011 

# Big primes: 104729, 1299709, 7368787

# TODO: Make phi() less ugly.

from math      import sqrt as _sqrt, ceil as _ceil
from itertools import takewhile, count
from funchelp  import take, head, tail
from numworks  import sdiv
from fractions import gcd

from decorum import *

class primes():
    '''All the prime numbers.'''
    def __iter__(self):
        prime = 2
        while True:
            yield prime
            prime = next_prime(prime)

def is_prime(num):
    '''Tests if a given number is prime.'''
    if num == 2:
        return True
    elif num % 2 == 0 or num <= 1:
        return False
    count = 3
    root = _sqrt(num)
    while count <= root:
        if num % count == 0:  # If anything divides evenly, it isn't prime.
            return False
        count += 2
    return True

def is_prime2(num):
    '''Tests if a given number is prime.
    Seems to be faster for higher numbers.
    '''
    if num == 2:
        return True
    elif num % 2 == 0 or num <= 1:
        return False
    root = _ceil(_sqrt(num))
    return all(map(lambda div: False if num % div == 0 else True, 
                   range(3, root+1, 2)))
    
def next_prime(num):
    """Given any number, determines the first number greater
    than it that is prime.
    """
    if num < 2:
        return 2
    elif num == 2:
        return 3
    elif num % 2 == 0:  # Even number. Perform magic.
        num -= 1
    return head(filter(is_prime, count(num + 2, 2)))

@time_it
def nth_prime(n):
    '''Calculates the nth prime, as indicated by the caller.'''
    return tail(take(n, primes()))

def primes_upto(lim):
    '''Gets all the primes up to a certain limit.'''
    return list(takewhile(lambda p: p < lim, primes()))

def n_primes(n):
    '''Returns 'n' primes.'''
    return list(take(n, primes()))

def prime_factors(n):
    '''Calculates the unique prime factors of a number.'''
    if n < 2:
        return []
    factors = []
    lim = 10  # After ten failures, checks if n has reduced to a prime.
    for prime in primes():
        if n % prime == 0:
            factors.append(prime)
            n = sdiv(n, prime)  # Reduce n as far as possible.
            lim = 10  # Reset the fail limit.
            if n == 1:  # We're done!
                break
        elif lim == 0 and is_prime(n):
            factors.append(n)
            break
        else:  # A certain prime failed to divide.
            lim -= 1
    return factors

def is_relative_prime(n, m):
    """Determines if two numbers are relatively prime,
    that is, if they have no common factors other than 1.
    """
    if gcd(n, m) == 1:
        return True
    return False

def relative_primes(num):
    '''Returns a list of relative primes, relative to the given number.
    This is quite faster than using gcd.
    '''
    if num == 1 or is_prime(num):
        return list(range(1, num))  # num == 1 returns [].
    result = range(1, num)
    for factor in prime_factors(num):
        result = filter(lambda n, factor=factor: n % factor != 0, result)
    return list(result)

# PROJECT EULER FUNCTIONS
def phi(n):
    """This is Euler's Function."""
    if n == 1:
        result = 1
    else:
        factors = prime_factors(n, True)
        result = n
        for each in factors:
            result *= (1 - (1 / float(each)))
        temp = int(result) #this takes care of rounding issues
        if result - temp > 0.5:
            result = temp + 1
        else:
            result = temp
    return result

def consec_prime_sum(num):
    """Given a prime number, determines what sequence
    of consecutive prime numbers add up to it.
    """
    if not is_prime(num): #filter for non-prime numbers
        result = []
    else:
        primes = primes_upto(num+1)
        adder = 0
        subber = 0
        result = []
        #calculate the result
        while True:
            total = sum(result)
            if total < num:  # Add another term.
                result.append(primes[adder])
                adder += 1
            elif total > num:  # Remove the first term in the list.
                subber += 1
                del result[0]
            elif total == num:  # Success.
                break
    return result
