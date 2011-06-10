# Help with system tasks.

import sys

def get_args(num=1):
    '''Checks args on the command line and returns them if valid.
    TODO: Make it accept REGEXs to test for args of a certain format?
    '''
    if len(sys.argv) != num + 1:  # +1 for the filename of the script.
        print('Bad args ->', sys.argv[1:])
        return
    return sys.argv[1:1+num]
