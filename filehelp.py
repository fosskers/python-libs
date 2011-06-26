# file:    filehelp.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   A library of functions that aids in file processing.

from random import randrange as _randrange

def random_line(in_file):
    '''Given a file, returns a random line.'''
    pos = _randrange(0, in_file.seek(0, 2))  # Find a random position.
    in_file.seek(lseek(in_file, pos))  # Seek to the start of its line.
    return in_file.readline()

def lseek(in_file, pos, jump_dist=1):
    '''Returns the cursor position of the start of the line containing pos.
    If you know the average line length of the file, you can increase
    jump_dist to speed up the search. Default is one byte at a time.
    '''
    if pos < 1:
        return 0
    elif off_end(in_file, pos):
        pos = get_end(in_file)
    pos = jump_back(in_file, pos, jump_dist)  # Initial jump back.
    while True:
        if pos < 1:  # We've reached the start of the file.
            result = 0
            break
        sample = in_file.read(jump_dist)
        if '\n' in sample:  # We found the start of the next line back.
            result = in_file.tell()
            break
        else:
            pos = jump_back(in_file, pos, jump_dist)
    return result
                
def off_end(in_file, pos):
    '''Determines if the position given is off the end of the file.'''
    cursor = get_end(in_file)
    return True if pos > cursor else False

def get_end(in_file):
    '''Gets the cursor position of the last char of the file, before
    the EOF marker.
    '''
    return in_file.seek(0, 2) - 1

def jump_back(in_file, pos, jump_dist):
    '''Given a position and a distance to jump back by, moves the
    cursor there.
    '''
    pos -= jump_dist
    in_file.seek(pos)
    return pos
    
