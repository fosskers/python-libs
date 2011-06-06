# file:    pghelp.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   Libraries for helping out pygame creation.

# COLOURS
def random_colour():
    '''Generates a random colour.'''
    from random import Random
    r = Random()
    return (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
