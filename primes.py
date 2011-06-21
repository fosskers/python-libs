# file:    primes.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   A module that performs various calculations
#          relating to prime numbers.
# updated: 06/21/2011 

# Big primes: 104729, 1299709, 7368787

# TODO: Make an iterator version of prime_factors()?

from math      import sqrt   as _sqrt, ceil as _ceil
from functools import reduce as _reduce
from itertools import takewhile, count
from funchelp  import take, head, last
from numworks  import sdiv
from fractions import gcd

class primes():
    '''An iterator that produces all the prime numbers.'''
    def __iter__(self):
        yield 2
        prime = 3
        while True:
            yield prime
            prime = _next_prime(prime)

def is_prime(num):
    '''Tests if a given number is prime. Written procedurally.'''
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
    '''Tests if a given number is prime. Written with a map.'''
    if num == 2:
        return True
    elif num % 2 == 0 or num <= 1:
        return False
    root = _ceil(_sqrt(num))
    return all(map(lambda div: False if num % div == 0 else True, 
                   range(3, root+1, 2)))

def is_prime3(num):
    '''Tests if a given number is prime. Written with reduce.'''
    if num == 2:
        return True
    elif num % 2 == 0 or num <= 1:
        return False
    root = _ceil(_sqrt(num))
    return _reduce(lambda acc, d: False if not acc or num % d == 0 else True,
                   range(3, root+1, 2), True)
    
def next_prime(num):
    '''Given any number, determines the first prime number greater than it.'''
    if num < 2:
        return 2
    elif num == 2:
        return 3
    elif num % 2 == 0:  # Even number. Perform magic.
        num -= 1
    return _next_prime(num)

def _next_prime(odd):
    '''Optimized version. Assumes its arg is odd and positive.'''
    return head(filter(is_prime, count(odd + 2, 2)))

def nth_prime(n):
    '''Calculates the nth prime, as indicated by the caller.'''
    return last(take(n, primes()))

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
    f_a = factors.append
    lim = 10  # After ten failures, checks if n has reduced to a prime.
    for prime in primes():
        if n % prime == 0:
            f_a(prime)
            n = sdiv(n, prime)  # Reduce n as far as possible.
            lim = 10  # Reset the fail limit.
            if n == 1:  # We're done!
                break
        elif lim == 0 and is_prime(n):
            f_a(n)
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
    '''Euler's totient function. Yields the number of coprimes of n.'''
    if n == 1:
        return 1
    factors = prime_factors(n)
    return int(n * _reduce(lambda acc, f: acc * (1 - (1 / f)), factors, 1))

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
