# file:    listhelp.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   A module that helps with list processing.

from decorum import *

class picker():
    '''An iterator that yields random elements from a given list
    until all the elements have been given.
    '''
    def __init__(self, items, lim=None):
        self.items = list(items)
        if not lim or lim > len(self.items):
            lim = len(self.items)
        self.lim = lim

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        from random import Random
        r = Random()
        for x in range(self.lim):
            pos = r.randint(0, len(self.items) - 1)
            yield self.items[pos]
            self.items.remove(self.items[pos])
    
def concat(items):
    '''Concats all the items of the list together as a string.
    Made: 03/04/2011  Mod: 05/31/2011 to kick ass.
    '''
    return ''.join(map(_concat, items))

def _concat(items):
    '''The work.'''
    if type(items) is str:
        return items
    elif hasattr(items, '__iter__'):
        return concat(items)
    return str(items)

def rotate(items, places=1):
    '''Rotates elements in a list.'''
    size = len(items)
    return items[-(size-places):] + items[:-(size-places)]

def scramble(items):
    '''Scrambles a given list. Will never return the same list.
    What are the chances of this blowing the stack, given a certain word
    length? That is to say, what are the chances that picker will generate
    an identicle list, say, 1000 times in a row?
    '''
    if len(items) in (0, 1):
        return list(items)
    result = [x for x in picker(items)]
    if result == list(items):
        result = scramble(items)
    return result

def frequencies(items):
    '''Produces a dictionary of keys equal to the items in 'items',
    and values that indicate how many times that item appeared.
    '''
    freqs = {}
    for item in items:
        if item in freqs:
            freqs[item] += 1
        else:
            freqs[item] = 1
    return freqs

# BINARY SEARCH, SORT TESTS, AND ORDERED INSERTION
def is_sorted(items):
    '''Determines if a list is sorted.'''
    if len(items) in (0, 1):
        return True
    for x in range(0, len(items) - 1):
        if items[x] > items[x + 1]:
            return False
    return True

def is_sorted2(items):
    '''Determines if a list is sorted, in a functional style. Slower.'''
    if len(items) in (0, 1):
        return True
    pairs = zip(items, items[1:])
    return all(map(lambda tup: False if tup[0] > tup[1] else True, pairs))

def bin_search(items, num):
    '''A binary search algorithm.'''
    size  = len(items)
    lower = 0
    upper = size - 1
    loc   = -1  # Assume failure.
    if size == 0:
        return -1
    while lower <= upper:
        mid = (lower + upper) // 2
        if items[mid] < num:  # Throw away lower part.                       
            lower = mid+1
        elif items[mid] == num:  # Found.                                
            loc = mid
            break
        else:  # Throw away upper part.                                     
            upper = mid-1
    return loc

def ordered_insert(items, num):
    '''Inserts the given argument in order into the list.'''
    size = len(items)
    if size == 0:
        items.append(num)
    else:  # Locate proper insert location.
        loc = mod_bin_search(items, num)
        if loc == size:
            items.append(num)
        else:
            items.insert(loc, num)

def mod_bin_search(items, num):
    '''Used by ordered_insert(), it determines where
    a value should be placed within a sorted list. 
    '''
    size = len(items)
    lower = 0
    upper = size - 1
    if num <= items[lower]:
        return 0
    elif num >= items[upper]:
        return size
    while lower <= upper:
        mid = (lower + upper) // 2
        if num == items[mid]: 
            loc = mid
            break
        elif num > items[mid] and num < items[mid + 1]: 
            # Goes to the right of mid.
            loc = mid+1
            break
        elif num < items[mid] and num > items[mid - 1]:
            # Goes to the left of mid.
            loc = mid
            break
        elif num > items[mid + 1]:
            lower = mid + 1
        else: #num < self[mid - 1]:
            upper = mid - 1
    return loc

        

