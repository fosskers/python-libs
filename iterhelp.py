# file:    iterhelp.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   A library that provides some handy iterators.

class char_range():
    '''Given a starting and ending char, yields all chars in between.'''
    def __init__(self, start, stop):
        self.start = ord(start)
        self.stop  = ord(stop)

    def __iter__(self):
        return map(chr, range(self.start, self.stop + 1))
