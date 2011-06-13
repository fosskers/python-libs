# file:    strhelp.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   A module that helps with string processing.

class NonStringError(TypeError):
    '''An Error for arguments given that are not strings.'''

def check_type(func):
    def inner(item):
        if not isinstance(item, str):
            raise NonStringError('Non-string passed as an argument.')
        return func(item)
    return inner
    
@check_type
def reverse_words(items):
    '''Reverses the order of words in a string formatted
    like a sentence, or at least part of one.
    '''
    words = items.split()
    words.reverse()
    return ' '.join(words)

@check_type
def reverse_chars(line):
    '''Reverses the chars in a string.'''
    line = list(line)
    line.reverse()
    return ''.join(line)
